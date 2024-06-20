// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.command.remote;

import com.pulumi.command.Utilities;
import com.pulumi.command.remote.CommandArgs;
import com.pulumi.command.remote.enums.Logging;
import com.pulumi.command.remote.outputs.Connection;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.Object;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * A command to run on a remote host. The connection is established via ssh.
 * 
 * ## Example Usage
 * ### Triggers
 * 
 * This example defines several trigger values of various kinds. Changes to any of them will cause `cmd` to be re-run.
 * 
 * <pre>
 * {@code
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         final var fileAssetVar = new FileAsset("Pulumi.yaml");
 * 
 *         var rand = new RandomString("rand", RandomStringArgs.builder()
 *             .length(5)
 *             .build());
 * 
 *         var localFile = new Command("localFile", CommandArgs.builder()
 *             .create("touch foo.txt")
 *             .archivePaths("*.txt")
 *             .build());
 * 
 *         var cmd = new Command("cmd", CommandArgs.builder()
 *             .connection(ConnectionArgs.builder()
 *                 .host("insert host here")
 *                 .build())
 *             .create("echo create > op.txt")
 *             .delete("echo delete >> op.txt")
 *             .triggers(            
 *                 rand.result(),
 *                 fileAssetVar,
 *                 localFile.archive())
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * 
 */
@ResourceType(type="command:remote:Command")
public class Command extends com.pulumi.resources.CustomResource {
    /**
     * If the previous command&#39;s stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     * 
     */
    @Export(name="addPreviousOutputInEnv", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> addPreviousOutputInEnv;

    /**
     * @return If the previous command&#39;s stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     * 
     */
    public Output<Optional<Boolean>> addPreviousOutputInEnv() {
        return Codegen.optional(this.addPreviousOutputInEnv);
    }
    /**
     * The parameters with which to connect to the remote host.
     * 
     */
    @Export(name="connection", refs={Connection.class}, tree="[0]")
    private Output<Connection> connection;

    /**
     * @return The parameters with which to connect to the remote host.
     * 
     */
    public Output<Connection> connection() {
        return this.connection;
    }
    /**
     * The command to run on create.
     * 
     */
    @Export(name="create", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> create;

    /**
     * @return The command to run on create.
     * 
     */
    public Output<Optional<String>> create() {
        return Codegen.optional(this.create);
    }
    /**
     * The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     * 
     */
    @Export(name="delete", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> delete;

    /**
     * @return The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     * 
     */
    public Output<Optional<String>> delete() {
        return Codegen.optional(this.delete);
    }
    /**
     * Additional environment variables available to the command&#39;s process.
     * Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
     * Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
     * with the variables in the form &#39;VAR=value command&#39;.
     * 
     */
    @Export(name="environment", refs={Map.class,String.class}, tree="[0,1,1]")
    private Output</* @Nullable */ Map<String,String>> environment;

    /**
     * @return Additional environment variables available to the command&#39;s process.
     * Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
     * Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
     * with the variables in the form &#39;VAR=value command&#39;.
     * 
     */
    public Output<Optional<Map<String,String>>> environment() {
        return Codegen.optional(this.environment);
    }
    /**
     * If the command&#39;s stdout and stderr should be logged. This doesn&#39;t affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via &#39;additionalSecretOutputs&#39;. Defaults to logging both stdout and stderr.
     * 
     */
    @Export(name="logging", refs={Logging.class}, tree="[0]")
    private Output</* @Nullable */ Logging> logging;

    /**
     * @return If the command&#39;s stdout and stderr should be logged. This doesn&#39;t affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via &#39;additionalSecretOutputs&#39;. Defaults to logging both stdout and stderr.
     * 
     */
    public Output<Optional<Logging>> logging() {
        return Codegen.optional(this.logging);
    }
    /**
     * The standard error of the command&#39;s process
     * 
     */
    @Export(name="stderr", refs={String.class}, tree="[0]")
    private Output<String> stderr;

    /**
     * @return The standard error of the command&#39;s process
     * 
     */
    public Output<String> stderr() {
        return this.stderr;
    }
    /**
     * Pass a string to the command&#39;s process as standard in
     * 
     */
    @Export(name="stdin", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> stdin;

    /**
     * @return Pass a string to the command&#39;s process as standard in
     * 
     */
    public Output<Optional<String>> stdin() {
        return Codegen.optional(this.stdin);
    }
    /**
     * The standard output of the command&#39;s process
     * 
     */
    @Export(name="stdout", refs={String.class}, tree="[0]")
    private Output<String> stdout;

    /**
     * @return The standard output of the command&#39;s process
     * 
     */
    public Output<String> stdout() {
        return this.stdout;
    }
    /**
     * Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the &#34;create&#34; command will be re-run.
     * Please see the resource documentation for examples.
     * 
     */
    @Export(name="triggers", refs={List.class,Object.class}, tree="[0,1]")
    private Output</* @Nullable */ List<Object>> triggers;

    /**
     * @return Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the &#34;create&#34; command will be re-run.
     * Please see the resource documentation for examples.
     * 
     */
    public Output<Optional<List<Object>>> triggers() {
        return Codegen.optional(this.triggers);
    }
    /**
     * The command to run on update, if empty, create will
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
     * are set to the stdout and stderr properties of the Command resource from previous
     * create or update steps.
     * 
     */
    @Export(name="update", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> update;

    /**
     * @return The command to run on update, if empty, create will
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR
     * are set to the stdout and stderr properties of the Command resource from previous
     * create or update steps.
     * 
     */
    public Output<Optional<String>> update() {
        return Codegen.optional(this.update);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Command(String name) {
        this(name, CommandArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Command(String name, CommandArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Command(String name, CommandArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("command:remote:Command", name, args == null ? CommandArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Command(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("command:remote:Command", name, null, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "connection"
            ))
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Command get(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Command(name, id, options);
    }
}
