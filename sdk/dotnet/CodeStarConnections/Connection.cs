// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CodeStarConnections
{
    /// <summary>
    /// Provides a CodeStar Connection.
    /// 
    /// &gt; **NOTE:** The `aws.codestarconnections.Connection` resource is created in the state `PENDING`. Authentication with the connection provider must be completed in the AWS Console.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleConnection = new Aws.CodeStarConnections.Connection("exampleConnection", new Aws.CodeStarConnections.ConnectionArgs
    ///         {
    ///             ProviderType = "Bitbucket",
    ///         });
    ///         var examplePipeline = new Aws.CodePipeline.Pipeline("examplePipeline", new Aws.CodePipeline.PipelineArgs
    ///         {
    ///             RoleArn = aws_iam_role.Codepipeline_role.Arn,
    ///             ArtifactStore = ,
    ///             Stages = 
    ///             {
    ///                 new Aws.CodePipeline.Inputs.PipelineStageArgs
    ///                 {
    ///                     Name = "Source",
    ///                     Actions = 
    ///                     {
    ///                         new Aws.CodePipeline.Inputs.PipelineStageActionArgs
    ///                         {
    ///                             Name = "Source",
    ///                             Category = "Source",
    ///                             Owner = "AWS",
    ///                             Provider = "CodeStarSourceConnection",
    ///                             Version = "1",
    ///                             OutputArtifacts = 
    ///                             {
    ///                                 "source_output",
    ///                             },
    ///                             Configuration = 
    ///                             {
    ///                                 { "ConnectionArn", exampleConnection.Arn },
    ///                                 { "FullRepositoryId", "my-organization/test" },
    ///                                 { "BranchName", "main" },
    ///                             },
    ///                         },
    ///                     },
    ///                 },
    ///                 new Aws.CodePipeline.Inputs.PipelineStageArgs
    ///                 {
    ///                     Name = "Build",
    ///                     Actions = 
    ///                     {
    ///                         ,
    ///                     },
    ///                 },
    ///                 new Aws.CodePipeline.Inputs.PipelineStageArgs
    ///                 {
    ///                     Name = "Deploy",
    ///                     Actions = 
    ///                     {
    ///                         ,
    ///                     },
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// CodeStar connections can be imported using the ARN, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:codestarconnections/connection:Connection test-connection arn:aws:codestar-connections:us-west-1:0123456789:connection/79d4d357-a2ee-41e4-b350-2fe39ae59448
    /// ```
    /// </summary>
    [AwsResourceType("aws:codestarconnections/connection:Connection")]
    public partial class Connection : Pulumi.CustomResource
    {
        /// <summary>
        /// The codestar connection ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The codestar connection status. Possible values are `PENDING`, `AVAILABLE` and `ERROR`.
        /// </summary>
        [Output("connectionStatus")]
        public Output<string> ConnectionStatus { get; private set; } = null!;

        /// <summary>
        /// The name of the connection to be created. The name must be unique in the calling AWS account. Changing `name` will create a new resource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the external provider where your third-party code repository is configured. Valid values are `Bitbucket`, `GitHub`, or `GitHubEnterpriseServer`. Changing `provider_type` will create a new resource.
        /// </summary>
        [Output("providerType")]
        public Output<string> ProviderType { get; private set; } = null!;


        /// <summary>
        /// Create a Connection resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Connection(string name, ConnectionArgs args, CustomResourceOptions? options = null)
            : base("aws:codestarconnections/connection:Connection", name, args ?? new ConnectionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Connection(string name, Input<string> id, ConnectionState? state = null, CustomResourceOptions? options = null)
            : base("aws:codestarconnections/connection:Connection", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Connection resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Connection Get(string name, Input<string> id, ConnectionState? state = null, CustomResourceOptions? options = null)
        {
            return new Connection(name, id, state, options);
        }
    }

    public sealed class ConnectionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the connection to be created. The name must be unique in the calling AWS account. Changing `name` will create a new resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the external provider where your third-party code repository is configured. Valid values are `Bitbucket`, `GitHub`, or `GitHubEnterpriseServer`. Changing `provider_type` will create a new resource.
        /// </summary>
        [Input("providerType", required: true)]
        public Input<string> ProviderType { get; set; } = null!;

        public ConnectionArgs()
        {
        }
    }

    public sealed class ConnectionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The codestar connection ARN.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The codestar connection status. Possible values are `PENDING`, `AVAILABLE` and `ERROR`.
        /// </summary>
        [Input("connectionStatus")]
        public Input<string>? ConnectionStatus { get; set; }

        /// <summary>
        /// The name of the connection to be created. The name must be unique in the calling AWS account. Changing `name` will create a new resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the external provider where your third-party code repository is configured. Valid values are `Bitbucket`, `GitHub`, or `GitHubEnterpriseServer`. Changing `provider_type` will create a new resource.
        /// </summary>
        [Input("providerType")]
        public Input<string>? ProviderType { get; set; }

        public ConnectionState()
        {
        }
    }
}