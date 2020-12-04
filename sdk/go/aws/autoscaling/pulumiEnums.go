// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html
type Metric pulumi.String

const (
	MetricGroupMinSize              = Metric("GroupMinSize")
	MetricGroupMaxSize              = Metric("GroupMaxSize")
	MetricGroupDesiredCapacity      = Metric("GroupDesiredCapacity")
	MetricGroupInServiceInstances   = Metric("GroupInServiceInstances")
	MetricGroupInServiceCapacity    = Metric("GroupInServiceCapacity")
	MetricGroupPendingInstances     = Metric("GroupPendingInstances")
	MetricGroupPendingCapacity      = Metric("GroupPendingCapacity")
	MetricGroupStandbyInstances     = Metric("GroupStandbyInstances")
	MetricGroupStandbyCapacity      = Metric("GroupStandbyCapacity")
	MetricGroupTerminatingInstances = Metric("GroupTerminatingInstances")
	MetricGroupTerminatingCapacity  = Metric("GroupTerminatingCapacity")
	MetricGroupTotalInstances       = Metric("GroupTotalInstances")
	MetricGroupTotalCapacity        = Metric("GroupTotalCapacity")
)

func (Metric) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e Metric) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e Metric) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e Metric) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e Metric) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html
type MetricsGranularity pulumi.String

const (
	MetricsGranularityOneMinute = MetricsGranularity("1Minute")
)

func (MetricsGranularity) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e MetricsGranularity) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e MetricsGranularity) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e MetricsGranularity) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e MetricsGranularity) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_NotificationConfiguration.html
type NotificationType pulumi.String

const (
	NotificationTypeInstanceLaunch         = NotificationType("autoscaling:EC2_INSTANCE_LAUNCH")
	NotificationTypeInstanceTerminate      = NotificationType("autoscaling:EC2_INSTANCE_TERMINATE")
	NotificationTypeInstanceLaunchError    = NotificationType("autoscaling:EC2_INSTANCE_LAUNCH_ERROR")
	NotificationTypeInstanceTerminateError = NotificationType("autoscaling:EC2_INSTANCE_TERMINATE_ERROR")
	NotificationTypeTestNotification       = NotificationType("autoscaling:TEST_NOTIFICATION")
)

func (NotificationType) ElementType() reflect.Type {
	return reflect.TypeOf((*pulumi.String)(nil)).Elem()
}

func (e NotificationType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e NotificationType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e NotificationType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e NotificationType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}