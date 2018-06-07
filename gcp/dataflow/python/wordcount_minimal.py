"""A minimalist word-counting workflow that counts words in Shakespeare.
Concepts:
1. Reading data from text files
2. Specifying 'inline' transforms
3. Counting a PCollection
4. Writing data to Cloud Storage as text files

Run with command:
python wordcount_minimal.py --input YOUR_INPUT_FILE --output counts
"""
from __future__ import absolute_import

import argparse
import logging
import re

import six

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

PROJECT_ID = 'YOUR_PROJECT_ID'
BUCKET_PATH = 'gs://YOUR_OUTPUT_BUCKET/'
BUCKET_OUTPUT_DIR = 'YOUR_OUTPUT_DIR_IN_YOUR_BUCKET'
BUCKET_STAGING_DIR = 'YOUR_STAGING_DIR_IN_YOUR_BUCKET'
BUCKET_TEMP_DIR = 'YOUR_TEMP_DIR_IN_YOUR_BUCKET'
RUNNER = 'DirectRunner'
JOB_NAME = 'wordcount-job'


def run(argv=None):
    """Main entry point; defines and runs the wordcount pipeline."""
    print 'Start...'
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        dest='input',
                        default='gs://dataflow-samples/shakespeare/kinglear.txt',
                        help='Input file to process.')

    parser.add_argument('--output',
                        dest='output',
                        default=BUCKET_PATH + BUCKET_OUTPUT_DIR,
                        help='Output file to write results to.')

    known_args, pipeline_args = parser.parse_known_args(argv)

    print 'known_args:{}, pipeline_args:{}'.format(known_args, pipeline_args)

    pipeline_args.extend([
        '--runner=' + RUNNER,
        '--project=' + PROJECT_ID,
        '--staging_location=' + BUCKET_PATH + BUCKET_STAGING_DIR,
        '--temp_location=' + BUCKET_PATH + BUCKET_TEMP_DIR,
        '--job_name=' + JOB_NAME,
    ])
    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        # Read the text file[pattern] into a PCollection.
        lines = p | ReadFromText(known_args.input)

        # Count the occurrences of each word.
        counts = (
                lines
                | 'Split' >> (beam.FlatMap(lambda x: re.findall(r'[A-Za-z\']+', x))
                              .with_output_types(six.text_type))
                | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
                | 'GroupAndSum' >> beam.CombinePerKey(sum))

        # Format the counts into a PCollection of strings.
        def format_result(word_count):
            (word, count) = word_count
            return '%s: %s' % (word, count)

        output = counts | 'Format' >> beam.Map(format_result)

        # Write the output using a "Write" transform that has side effects.
        # pylint: disable=expression-not-assigned
        output | WriteToText(known_args.output)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
