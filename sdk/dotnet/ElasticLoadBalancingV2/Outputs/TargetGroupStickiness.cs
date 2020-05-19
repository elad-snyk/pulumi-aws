// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ElasticLoadBalancingV2.Outputs
{

    [OutputType]
    public sealed class TargetGroupStickiness
    {
        /// <summary>
        /// The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
        /// </summary>
        public readonly int? CookieDuration;
        /// <summary>
        /// Indicates whether  health checks are enabled. Defaults to true.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// The type of sticky sessions. The only current possible value is `lb_cookie`.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private TargetGroupStickiness(
            int? cookieDuration,

            bool? enabled,

            string type)
        {
            CookieDuration = cookieDuration;
            Enabled = enabled;
            Type = type;
        }
    }
}