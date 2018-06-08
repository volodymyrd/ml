package com.gmail.volodymyrdotsenko.gcp.dataflow.pipelines;

import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.junit.Test;

import java.io.File;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

/**
 * Test {@link MinimalWordCount}
 */
public class MinimalWordCountTest {

    @Test
    public void testStart() {
        String outputDirName = "src/test/resources";
        String outputFilePrefix = "output";
        File outputDir = new File(outputDirName);
        new MinimalWordCount(PipelineOptionsFactory.create())
                .start("src/test/resources/input.txt", outputDirName + "/" + outputFilePrefix);
        assertNotNull(outputDir.listFiles());
        int numberOfOutput = 0;
        for (File output : outputDir.listFiles()) {
            if (output.getName().startsWith(outputFilePrefix)) {
                numberOfOutput++;
                output.delete();
            }
        }

        assertTrue(numberOfOutput > 0);
    }
}