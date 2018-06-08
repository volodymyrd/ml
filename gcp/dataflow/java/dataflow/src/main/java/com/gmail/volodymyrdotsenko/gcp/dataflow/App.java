package com.gmail.volodymyrdotsenko.gcp.dataflow;

import com.gmail.volodymyrdotsenko.gcp.dataflow.pipelines.MinimalWordCount;
import org.apache.beam.runners.dataflow.DataflowRunner;
import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
import org.apache.beam.sdk.options.PipelineOptions;
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

        if (args.length < 2) {
            System.out.println("You must specified at least 2 params: 'input' and 'output'");
            throw new IllegalArgumentException();
        }
        String input = args[0];
        String output = args[1];
        String runner = null;
        if (args.length == 3) {
            runner = args[2];
        }


        PipelineOptions options = PipelineOptionsFactory.create();

        if (runner != null && !runner.isEmpty()) {
            if (runner.equals("DataflowRunner")) {
                if (args.length < 5) {
                    System.out.println("You must specified at least 5 params: " +
                            "'input', 'output', 'runner', 'projectId', 'tempLocation'");
                    throw new IllegalArgumentException();
                }
                DataflowPipelineOptions dataflowOptions = options.as(DataflowPipelineOptions.class);
                dataflowOptions.setRunner(DataflowRunner.class);
                dataflowOptions.setProject(args[3]);
                dataflowOptions.setTempLocation(args[4]);
            }
        }

        new MinimalWordCount(options).start(input, output);
    }
}