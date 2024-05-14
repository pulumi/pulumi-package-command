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
    [CommandResourceType("command:remote:Copy")]
    public partial class Copy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The parameters with which to connect to the remote host.
        /// </summary>
        [Output("connection")]
        public Output<Outputs.Connection> Connection { get; private set; } = null!;

        /// <summary>
        /// An archive to upload as the source of the copy. It must be a path based archive. Only one of Asset or Archive can be set.
        /// </summary>
        [Output("localArchive")]
        public Output<Archive?> LocalArchive { get; private set; } = null!;

        /// <summary>
        /// An asset to upload as the source of the copy. It must be a path based asset. Only one of Asset or Archive can be set.
        /// </summary>
        [Output("localAsset")]
        public Output<AssetOrArchive?> LocalAsset { get; private set; } = null!;

        /// <summary>
        /// The destination path in the remote host.
        /// </summary>
        [Output("remotePath")]
        public Output<string> RemotePath { get; private set; } = null!;

        /// <summary>
        /// Trigger replacements on changes to this input.
        /// </summary>
        [Output("triggers")]
        public Output<ImmutableArray<object>> Triggers { get; private set; } = null!;


        /// <summary>
        /// Create a Copy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Copy(string name, CopyArgs args, CustomResourceOptions? options = null)
            : base("command:remote:Copy", name, args ?? new CopyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Copy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("command:remote:Copy", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Copy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Copy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Copy(name, id, options);
        }
    }

    public sealed class CopyArgs : global::Pulumi.ResourceArgs
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
        /// An archive to upload as the source of the copy. It must be a path based archive. Only one of Asset or Archive can be set.
        /// </summary>
        [Input("localArchive")]
        public Input<Archive>? LocalArchive { get; set; }

        /// <summary>
        /// An asset to upload as the source of the copy. It must be a path based asset. Only one of Asset or Archive can be set.
        /// </summary>
        [Input("localAsset")]
        public Input<AssetOrArchive>? LocalAsset { get; set; }

        /// <summary>
        /// The destination path in the remote host.
        /// </summary>
        [Input("remotePath", required: true)]
        public Input<string> RemotePath { get; set; } = null!;

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

        public CopyArgs()
        {
        }
        public static new CopyArgs Empty => new CopyArgs();
    }
}
