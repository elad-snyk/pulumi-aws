// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh.Inputs
{

    public sealed class RouteSpecHttp2RouteMatchHeaderMatchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The value sent by the client must match the specified value exactly.
        /// </summary>
        [Input("exact")]
        public Input<string>? Exact { get; set; }

        /// <summary>
        /// The value sent by the client must begin with the specified characters.
        /// This parameter must always start with /, which by itself matches all requests to the virtual router service name.
        /// </summary>
        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        /// <summary>
        /// The object that specifies the range of numbers that the value sent by the client must be included in.
        /// </summary>
        [Input("range")]
        public Input<Inputs.RouteSpecHttp2RouteMatchHeaderMatchRangeArgs>? Range { get; set; }

        /// <summary>
        /// The value sent by the client must include the specified characters.
        /// </summary>
        [Input("regex")]
        public Input<string>? Regex { get; set; }

        /// <summary>
        /// The value sent by the client must end with the specified characters.
        /// </summary>
        [Input("suffix")]
        public Input<string>? Suffix { get; set; }

        public RouteSpecHttp2RouteMatchHeaderMatchArgs()
        {
        }
    }
}