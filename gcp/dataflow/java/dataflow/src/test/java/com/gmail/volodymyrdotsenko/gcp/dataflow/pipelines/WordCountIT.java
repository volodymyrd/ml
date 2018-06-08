package com.gmail.volodymyrdotsenko.gcp.dataflow.pipelines;

import org.apache.beam.sdk.io.FileSystems;
import org.apache.beam.sdk.io.fs.ResolveOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.testing.FileChecksumMatcher;
import org.apache.beam.sdk.testing.TestPipeline;
import org.apache.beam.sdk.testing.TestPipelineOptions;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.Date;

/**
 * Test {@link WordCount}
 */
public class WordCountIT {
    private static final String DEFAULT_INPUT =
            //"gs://apache-beam-samples/shakespeare/winterstale-personae";
            "src/test/resources/input.txt";
    private static final String DEFAULT_OUTPUT_CHECKSUM = "ebf895e7324e8a3edc72e7bcc96fa2ba7f690def";

    /**
     * Options for the WordCount Integration Test.
     * <p>
     * <p>Define expected output file checksum to verify WordCount pipeline result
     * with customized input.
     */
    public interface WordCountITOptions extends TestPipelineOptions, WordCount.WordCountOptions {
    }

    @BeforeClass
    public static void setUp() {
        PipelineOptionsFactory.register(TestPipelineOptions.class);
    }

    @Test
    public void testE2EWordCount() throws Exception {
        WordCountITOptions options = TestPipeline.testingPipelineOptions().as(WordCountITOptions.class);
        options.setTempRoot("/tmp/1");
        options.setInputFile(DEFAULT_INPUT);
        options.setOutput(FileSystems.matchNewResource(options.getTempRoot(), true)
                .resolve(String.format("WordCountIT-%tF-%<tH-%<tM-%<tS-%<tL", new Date()),
                        ResolveOptions.StandardResolveOptions.RESOLVE_DIRECTORY)
                .resolve("output", ResolveOptions.StandardResolveOptions.RESOLVE_DIRECTORY)
                .resolve("results", ResolveOptions.StandardResolveOptions.RESOLVE_FILE).toString());
        options.setOnSuccessMatcher(
                new FileChecksumMatcher(DEFAULT_OUTPUT_CHECKSUM, options.getOutput() + "*-of-*"));

        new WordCount(options).start();
    }

//    @Test
//    public void testStart() {
//        WordCountITOptions options = TestPipeline.testingPipelineOptions().as(WordCountITOptions.class);
//        String outputDirName = "src/test/resources";
//        String outputFilePrefix = "output";
//        File outputDir = new File(outputDirName);
//        new WordCount(PipelineOptionsFactory.create())
//                .start("src/test/resources/input.txt", outputDirName + "/" + outputFilePrefix);
//        assertNotNull(outputDir.listFiles());
//        int numberOfOutput = 0;
//        for (File output : outputDir.listFiles()) {
//            if (output.getName().startsWith(outputFilePrefix)) {
//                numberOfOutput++;
//                output.delete();
//            }
//        }
//
//        assertTrue(numberOfOutput > 0);
//    }
}