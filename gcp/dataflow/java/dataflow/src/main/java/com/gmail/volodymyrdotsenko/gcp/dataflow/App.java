package com.gmail.volodymyrdotsenko.gcp.dataflow;

import com.gmail.volodymyrdotsenko.gcp.dataflow.pipelines.WordCount;
import org.apache.beam.sdk.options.PipelineOptionsFactory;

import java.util.Arrays;

/**
 * Main app.
 * <p>
 * Run with gradle:
 * gradle run -PappArgs="['input.txt', 'output', 'DataflowRunner']"
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Start app with params: " + Arrays.toString(args));

        if (args.length < 1) {
            System.out.println("You must specified at least 1 param: 'output'");
            throw new IllegalArgumentException();
        }

        WordCount.WordCountOptions options = PipelineOptionsFactory.fromArgs(args).withValidation()
                .as(WordCount.WordCountOptions.class);

        new WordCount(options).start();
    }
}