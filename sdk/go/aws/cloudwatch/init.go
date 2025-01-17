// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "aws:cloudwatch/compositeAlarm:CompositeAlarm":
		r, err = NewCompositeAlarm(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/dashboard:Dashboard":
		r, err = NewDashboard(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/eventArchive:EventArchive":
		r, err = NewEventArchive(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/eventBus:EventBus":
		r, err = NewEventBus(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/eventPermission:EventPermission":
		r, err = NewEventPermission(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/eventRule:EventRule":
		r, err = NewEventRule(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/eventTarget:EventTarget":
		r, err = NewEventTarget(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logDestination:LogDestination":
		r, err = NewLogDestination(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logDestinationPolicy:LogDestinationPolicy":
		r, err = NewLogDestinationPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logGroup:LogGroup":
		r, err = NewLogGroup(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logMetricFilter:LogMetricFilter":
		r, err = NewLogMetricFilter(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logResourcePolicy:LogResourcePolicy":
		r, err = NewLogResourcePolicy(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logStream:LogStream":
		r, err = NewLogStream(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/logSubscriptionFilter:LogSubscriptionFilter":
		r, err = NewLogSubscriptionFilter(ctx, name, nil, pulumi.URN_(urn))
	case "aws:cloudwatch/metricAlarm:MetricAlarm":
		r, err = NewMetricAlarm(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := aws.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/compositeAlarm",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/dashboard",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/eventArchive",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/eventBus",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/eventPermission",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/eventRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/eventTarget",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logDestination",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logDestinationPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logMetricFilter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logResourcePolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logStream",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/logSubscriptionFilter",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"cloudwatch/metricAlarm",
		&module{version},
	)
}
