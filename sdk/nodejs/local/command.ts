// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A local command to be executed.
 *
 * This command can be inserted into the life cycles of other resources using the `dependsOn` or `parent` resource options. A command is considered to have failed when it finished with a non-zero exit code. This will fail the CRUD step of the `Command` resource.
 *
 * ## Example Usage
 * ### Triggers
 *
 * This example defines several trigger values of various kinds. Changes to any of them will cause `cmd` to be re-run.
 *
 * ```typescript
 * import * as local from "@pulumi/command/local";
 * import * as random from "@pulumi/random";
 * import { asset } from "@pulumi/pulumi";
 * import * as path from "path";
 *
 * const str = "foo";
 * const fileAsset = new pulumi.asset.FileAsset("Pulumi.yaml");
 * const rand = new random.RandomString("rand", {length: 5});
 * const localFile = new local.Command("localFile", {
 *     create: "touch foo.txt",
 *     archivePaths: ["*.txt"],
 * });
 *
 * const cmd = new local.Command("pwd", {
 *     create: "echo create > op.txt",
 *     delete: "echo delete >> op.txt",
 *     triggers: [str, rand.result, fileAsset, localFile.archive],
 * });
 * ```
 */
export class Command extends pulumi.CustomResource {
    /**
     * Get an existing Command resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Command {
        return new Command(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'command:local:Command';

    /**
     * Returns true if the given object is an instance of Command.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Command {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Command.__pulumiType;
    }

    /**
     * If the previous command's stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     */
    public readonly addPreviousOutputInEnv!: pulumi.Output<boolean | undefined>;
    /**
     * An archive asset containing files found after running the command.
     */
    public /*out*/ readonly archive!: pulumi.Output<pulumi.asset.Archive | undefined>;
    /**
     * A list of path globs to return as a single archive asset after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    public readonly archivePaths!: pulumi.Output<string[] | undefined>;
    /**
     * A list of path globs to read after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    public readonly assetPaths!: pulumi.Output<string[] | undefined>;
    /**
     * A map of assets found after running the command.
     * The key is the relative path from the command dir
     */
    public /*out*/ readonly assets!: pulumi.Output<{[key: string]: pulumi.asset.Asset | pulumi.asset.Archive} | undefined>;
    /**
     * The command to run on create.
     */
    public readonly create!: pulumi.Output<string | undefined>;
    /**
     * The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     */
    public readonly delete!: pulumi.Output<string | undefined>;
    /**
     * The directory from which to run the command from. If `dir` does not exist, then
     * `Command` will fail.
     */
    public readonly dir!: pulumi.Output<string | undefined>;
    /**
     * Additional environment variables available to the command's process.
     */
    public readonly environment!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The program and arguments to run the command.
     * On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
     */
    public readonly interpreter!: pulumi.Output<string[] | undefined>;
    /**
     * If the command's stdout and stderr should be logged. This doesn't affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
     */
    public readonly logging!: pulumi.Output<enums.local.Logging | undefined>;
    /**
     * The standard error of the command's process
     */
    public /*out*/ readonly stderr!: pulumi.Output<string>;
    /**
     * Pass a string to the command's process as standard in
     */
    public readonly stdin!: pulumi.Output<string | undefined>;
    /**
     * The standard output of the command's process
     */
    public /*out*/ readonly stdout!: pulumi.Output<string>;
    /**
     * Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the "create" command will be re-run.
     * Please see the resource documentation for examples.
     */
    public readonly triggers!: pulumi.Output<any[] | undefined>;
    /**
     * The command to run on update, if empty, create will 
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
     * are set to the stdout and stderr properties of the Command resource from previous 
     * create or update steps.
     */
    public readonly update!: pulumi.Output<string | undefined>;

    /**
     * Create a Command resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CommandArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["addPreviousOutputInEnv"] = (args ? args.addPreviousOutputInEnv : undefined) ?? true;
            resourceInputs["archivePaths"] = args ? args.archivePaths : undefined;
            resourceInputs["assetPaths"] = args ? args.assetPaths : undefined;
            resourceInputs["create"] = args ? args.create : undefined;
            resourceInputs["delete"] = args ? args.delete : undefined;
            resourceInputs["dir"] = args ? args.dir : undefined;
            resourceInputs["environment"] = args ? args.environment : undefined;
            resourceInputs["interpreter"] = args ? args.interpreter : undefined;
            resourceInputs["logging"] = args ? args.logging : undefined;
            resourceInputs["stdin"] = args ? args.stdin : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
            resourceInputs["update"] = args ? args.update : undefined;
            resourceInputs["archive"] = undefined /*out*/;
            resourceInputs["assets"] = undefined /*out*/;
            resourceInputs["stderr"] = undefined /*out*/;
            resourceInputs["stdout"] = undefined /*out*/;
        } else {
            resourceInputs["addPreviousOutputInEnv"] = undefined /*out*/;
            resourceInputs["archive"] = undefined /*out*/;
            resourceInputs["archivePaths"] = undefined /*out*/;
            resourceInputs["assetPaths"] = undefined /*out*/;
            resourceInputs["assets"] = undefined /*out*/;
            resourceInputs["create"] = undefined /*out*/;
            resourceInputs["delete"] = undefined /*out*/;
            resourceInputs["dir"] = undefined /*out*/;
            resourceInputs["environment"] = undefined /*out*/;
            resourceInputs["interpreter"] = undefined /*out*/;
            resourceInputs["logging"] = undefined /*out*/;
            resourceInputs["stderr"] = undefined /*out*/;
            resourceInputs["stdin"] = undefined /*out*/;
            resourceInputs["stdout"] = undefined /*out*/;
            resourceInputs["triggers"] = undefined /*out*/;
            resourceInputs["update"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["triggers[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Command.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Command resource.
 */
export interface CommandArgs {
    /**
     * If the previous command's stdout and stderr (as generated by the prior create/update) is
     * injected into the environment of the next run as PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR.
     * Defaults to true.
     */
    addPreviousOutputInEnv?: pulumi.Input<boolean>;
    /**
     * A list of path globs to return as a single archive asset after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    archivePaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of path globs to read after the command completes.
     *
     * When specifying glob patterns the following rules apply:
     * - We only include files not directories for assets and archives.
     * - Path separators are `/` on all platforms - including Windows.
     * - Patterns starting with `!` are 'exclude' rules.
     * - Rules are evaluated in order, so exclude rules should be after inclusion rules.
     * - `*` matches anything except `/`
     * - `**` matches anything, _including_ `/`
     * - All returned paths are relative to the working directory (without leading `./`) e.g. `file.text` or `subfolder/file.txt`.
     * - For full details of the globbing syntax, see [github.com/gobwas/glob](https://github.com/gobwas/glob)
     *
     * #### Example
     *
     * Given the rules:
     * ```yaml
     * - "assets/**"
     * - "src/**.js"
     * - "!**secret.*"
     * ```
     *
     * When evaluating against this folder:
     *
     * ```yaml
     * - assets/
     *   - logos/
     *     - logo.svg
     * - src/
     *   - index.js
     *   - secret.js
     * ```
     *
     * The following paths will be returned:
     *
     * ```yaml
     * - assets/logos/logo.svg
     * - src/index.js
     * ```
     */
    assetPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The command to run on create.
     */
    create?: pulumi.Input<string>;
    /**
     * The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
     * and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
     * Command resource from previous create or update steps.
     */
    delete?: pulumi.Input<string>;
    /**
     * The directory from which to run the command from. If `dir` does not exist, then
     * `Command` will fail.
     */
    dir?: pulumi.Input<string>;
    /**
     * Additional environment variables available to the command's process.
     */
    environment?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The program and arguments to run the command.
     * On Linux and macOS, defaults to: `["/bin/sh", "-c"]`. On Windows, defaults to: `["cmd", "/C"]`
     */
    interpreter?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * If the command's stdout and stderr should be logged. This doesn't affect the capturing of
     * stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
     * outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
     */
    logging?: pulumi.Input<enums.local.Logging>;
    /**
     * Pass a string to the command's process as standard in
     */
    stdin?: pulumi.Input<string>;
    /**
     * Trigger a resource replacement on changes to any of these values. The
     * trigger values can be of any type. If a value is different in the current update compared to the
     * previous update, the resource will be replaced, i.e., the "create" command will be re-run.
     * Please see the resource documentation for examples.
     */
    triggers?: pulumi.Input<any[]>;
    /**
     * The command to run on update, if empty, create will 
     * run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
     * are set to the stdout and stderr properties of the Command resource from previous 
     * create or update steps.
     */
    update?: pulumi.Input<string>;
}
