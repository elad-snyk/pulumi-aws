// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualNodeSpecListenerTimeout
    {
        /// <summary>
        /// Timeouts for gRPC listeners.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutGrpc? Grpc;
        /// <summary>
        /// Timeouts for HTTP listeners.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutHttp? Http;
        /// <summary>
        /// Timeouts for HTTP2 listeners.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutHttp2? Http2;
        /// <summary>
        /// Timeouts for TCP listeners.
        /// </summary>
        public readonly Outputs.VirtualNodeSpecListenerTimeoutTcp? Tcp;

        [OutputConstructor]
        private VirtualNodeSpecListenerTimeout(
            Outputs.VirtualNodeSpecListenerTimeoutGrpc? grpc,

            Outputs.VirtualNodeSpecListenerTimeoutHttp? http,

            Outputs.VirtualNodeSpecListenerTimeoutHttp2? http2,

            Outputs.VirtualNodeSpecListenerTimeoutTcp? tcp)
        {
            Grpc = grpc;
            Http = http;
            Http2 = http2;
            Tcp = tcp;
        }
    }
}