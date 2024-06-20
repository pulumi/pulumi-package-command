// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Command.Remote
{
    /// <summary>
    /// Copy an Asset or Archive to a remote host.
    /// </summary>
    [CommandResourceType("command:remote:CopyToRemote")]
    public partial class CopyToRemote : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The parameters with which to connect to the remote host.
        /// </summary>
        [Output("connection")]
        public Output<Outputs.Connection> Connection { get; private set; } = null!;

        /// <summary>
        /// The destination path on the remote host. The last element of the path will be created if it doesn't exist but it's an error when additional elements don't exist. When the remote path is an existing directory, the source file or directory will be copied into that directory. When the source is a file and the remote path is an existing file, that file will be overwritten. When the source is a directory and the remote path an existing file, the copy will fail.
        /// </summary>
        [Output("remotePath")]
        public Output<string> RemotePath { get; private set; } = null!;

        /// <summary>
        /// An [asset or an archive](https://www.pulumi.com/docs/concepts/assets-archives/) to upload as the source of the copy. It must be path-based, i.e., be a `FileAsset` or a `FileArchive`. The item will be copied as-is; archives like .tgz will not be unpacked. Directories are copied recursively, overwriting existing files.
        /// </summary>
        [Output("source")]
        public Output<AssetOrArchive> Source { get; private set; } = null!;

        /// <summary>
        /// Trigger replacements on changes to this input.
        /// </summary>
        [Output("triggers")]
        public Output<ImmutableArray<object>> Triggers { get; private set; } = null!;


        /// <summary>
        /// Create a CopyToRemote resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CopyToRemote(string name, CopyToRemoteArgs args, CustomResourceOptions? options = null)
            : base("command:remote:CopyToRemote", name, args ?? new CopyToRemoteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CopyToRemote(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("command:remote:CopyToRemote", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "connection",
                },
                ReplaceOnChanges =
                {
                    "triggers[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CopyToRemote resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CopyToRemote Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CopyToRemote(name, id, options);
        }
    }

    public sealed class CopyToRemoteArgs : global::Pulumi.ResourceArgs
    {
        [Input("connection", required: true)]
        private Input<Inputs.ConnectionArgs>? _connection;

        /// <summary>
        /// The parameters with which to connect to the remote host.
        /// </summary>
        public Input<Inputs.ConnectionArgs>? Connection
        {
            get => _connection;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _connection = Output.Tuple<Input<Inputs.ConnectionArgs>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The destination path on the remote host. The last element of the path will be created if it doesn't exist but it's an error when additional elements don't exist. When the remote path is an existing directory, the source file or directory will be copied into that directory. When the source is a file and the remote path is an existing file, that file will be overwritten. When the source is a directory and the remote path an existing file, the copy will fail.
        /// </summary>
        [Input("remotePath", required: true)]
        public Input<string> RemotePath { get; set; } = null!;

        /// <summary>
        /// An [asset or an archive](https://www.pulumi.com/docs/concepts/assets-archives/) to upload as the source of the copy. It must be path-based, i.e., be a `FileAsset` or a `FileArchive`. The item will be copied as-is; archives like .tgz will not be unpacked. Directories are copied recursively, overwriting existing files.
        /// </summary>
        [Input("source", required: true)]
        public Input<AssetOrArchive> Source { get; set; } = null!;

        [Input("triggers")]
        private InputList<object>? _triggers;

        /// <summary>
        /// Trigger replacements on changes to this input.
        /// </summary>
        public InputList<object> Triggers
        {
            get => _triggers ?? (_triggers = new InputList<object>());
            set => _triggers = value;
        }

        public CopyToRemoteArgs()
        {
        }
        public static new CopyToRemoteArgs Empty => new CopyToRemoteArgs();
    }
}