package com.gmail.volodymyrdotsenko.gcp.dataflow.pipelines;

import java.util.Arrays;

import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.transforms.Count;
import org.apache.beam.sdk.transforms.Filter;
import org.apache.beam.sdk.transforms.FlatMapElements;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.TypeDescriptors;

/**
 * An example that counts words in Shakespeare.
 * <p>
 * <p>This class, {@link MinimalWordCount}, is the first in a series of four successively more
 * detailed 'word count' examples. Here, for simplicity, we don't show any error-checking or
 * argument processing, and focus on construction of the pipeline, which chains together the
 * application of core transforms.
 * <p>
 * <p>Next, see the {@link WordCount} pipeline, then the {@link DebuggingWordCount}, and finally the
 * {@link WindowedWordCount} pipeline, for more detailed examples that introduce additional
 * concepts.
 * <p>
 * <p>Concepts:
 * <p>
 * <pre>
 *   1. Reading data from text files
 *   2. Specifying 'inline' transforms
 *   3. Counting items in a PCollection
 *   4. Writing data to text files
 * </pre>
 * <p>
 * <p>No arguments are required to run this pipeline. It will be executed with the DirectRunner. You
 * can see the results in the output files in your current working directory, with names like
 * "wordcounts-00001-of-00005. When running on a distributed service, you would use an appropriate
 * file service.
 */
public final class MinimalWordCount {
    private final PipelineOptions options;

    public MinimalWordCount(PipelineOptions options) {
        this.options = options;
    }

    public void start(String input, String output) {
        // Create the Pipeline object with the options we defined above
        Pipeline p = Pipeline.create(options);

        // Concept #1: Apply a root transform to the pipeline; in this case, TextIO.Read to read a set
        // of input text files. TextIO.Read returns a PCollection where each element is one line from
        // the input text (a set of Shakespeare's texts).

        // This example reads a public data set consisting of the complete works of Shakespeare.
        p.apply(TextIO.read().from(input))

                // Concept #2: Apply a FlatMapElements transform the PCollection of text lines.
                // This transform splits the lines in PCollection<String>, where each element is an
                // individual word in Shakespeare's collected texts.
                .apply(FlatMapElements
                        .into(TypeDescriptors.strings())
                        .via((String word) -> Arrays.asList(word.split("[^\\p{L}]+"))))
                // We use a Filter transform to avoid empty word
                .apply(Filter.by((String word) -> !word.isEmpty()))
                // Concept #3: Apply the Count transform to our PCollection of individual words. The Count
                // transform returns a new PCollection of key/value pairs, where each key represents a
                // unique word in the text. The associated value is the occurrence count for that word.
                .apply(Count.perElement())
                // Apply a MapElements transform that formats our PCollection of word counts into a
                // printable string, suitable for writing to an output file.
                .apply(MapElements
                        .into(TypeDescriptors.strings())
                        .via((KV<String, Long> wordCount) -> wordCount.getKey() + ": " + wordCount.getValue()))
                // Concept #4: Apply a write transform, TextIO.Write, at the end of the pipeline.
                // TextIO.Write writes the contents of a PCollection (in this case, our PCollection of
                // formatted strings) to a series of text files.
                //
                // By default, it will write to a set of files with names like wordcounts-00001-of-00005
                .apply(TextIO.write().to(output));

        p.run().waitUntilFinish();
    }
}
