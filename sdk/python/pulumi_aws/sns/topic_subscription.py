# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['TopicSubscription']


class TopicSubscription(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 confirmation_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 delivery_policy: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 endpoint_auto_confirms: Optional[pulumi.Input[bool]] = None,
                 filter_policy: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 raw_message_delivery: Optional[pulumi.Input[bool]] = None,
                 redrive_policy: Optional[pulumi.Input[str]] = None,
                 subscription_role_arn: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to. This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for provider users will probably be SQS queues.

        > **NOTE:** If the SNS topic and SQS queue are in different AWS regions, the `sns.TopicSubscription` must use an AWS provider that is in the same region as the SNS topic. If the `sns.TopicSubscription` uses a provider with a different region than the SNS topic, this provider will fail to create the subscription.

        > **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires the provider to have access to BOTH accounts.

        > **NOTE:** If an SNS topic and SQS queue are in different AWS accounts but the same region, the `sns.TopicSubscription` must use the AWS provider for the account with the SQS queue. If `sns.TopicSubscription` uses a Provider with a different account than the SQS queue, this provider creates the subscription but does not keep state and tries to re-create the subscription at every `apply`.

        > **NOTE:** If an SNS topic and SQS queue are in different AWS accounts and different AWS regions, the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.

        > **NOTE:** You cannot unsubscribe to a subscription that is pending confirmation. If you use `email`, `email-json`, or `http`/`https` (without auto-confirmation enabled), until the subscription is confirmed (e.g., outside of this provider), AWS does not allow this provider to delete / unsubscribe the subscription. If you `destroy` an unconfirmed subscription, this provider will remove the subscription from its state but the subscription will still exist in AWS. However, if you delete an SNS topic, SNS [deletes all the subscriptions](https://docs.aws.amazon.com/sns/latest/dg/sns-delete-subscription-topic.html) associated with the topic. Also, you can import a subscription after confirmation and then have the capability to delete it.

        ## Import

        SNS Topic Subscriptions can be imported using the `subscription arn`, e.g.

        ```sh
         $ pulumi import aws:sns/topicSubscription:TopicSubscription user_updates_sqs_target arn:aws:sns:us-west-2:0123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] confirmation_timeout_in_minutes: Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols. Default is `1`.
        :param pulumi.Input[str] delivery_policy: JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        :param pulumi.Input[str] endpoint: Endpoint to send data to. The contents vary with the protocol. See details below.
        :param pulumi.Input[bool] endpoint_auto_confirms: Whether the endpoint is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) (e.g., PagerDuty). Default is `false`.
        :param pulumi.Input[str] filter_policy: JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        :param pulumi.Input[str] protocol: Protocol to use. Valid values are: `sqs`, `sms`, `lambda`, `firehose`, and `application`. Protocols `email`, `email-json`, `http` and `https` are also valid but partially supported. See details below.
        :param pulumi.Input[bool] raw_message_delivery: Whether to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property). Default is `false`.
        :param pulumi.Input[str] redrive_policy: JSON String with the redrive policy that will be used in the subscription. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html#how-messages-moved-into-dead-letter-queue) for more details.
        :param pulumi.Input[str] subscription_role_arn: ARN of the IAM role to publish to Kinesis Data Firehose delivery stream. Refer to [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html).
        :param pulumi.Input[str] topic: ARN of the SNS topic to subscribe to.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['confirmation_timeout_in_minutes'] = confirmation_timeout_in_minutes
            __props__['delivery_policy'] = delivery_policy
            if endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint'")
            __props__['endpoint'] = endpoint
            __props__['endpoint_auto_confirms'] = endpoint_auto_confirms
            __props__['filter_policy'] = filter_policy
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['raw_message_delivery'] = raw_message_delivery
            __props__['redrive_policy'] = redrive_policy
            __props__['subscription_role_arn'] = subscription_role_arn
            if topic is None and not opts.urn:
                raise TypeError("Missing required property 'topic'")
            __props__['topic'] = topic
            __props__['arn'] = None
            __props__['confirmation_was_authenticated'] = None
            __props__['owner_id'] = None
            __props__['pending_confirmation'] = None
        super(TopicSubscription, __self__).__init__(
            'aws:sns/topicSubscription:TopicSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            confirmation_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
            confirmation_was_authenticated: Optional[pulumi.Input[bool]] = None,
            delivery_policy: Optional[pulumi.Input[str]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            endpoint_auto_confirms: Optional[pulumi.Input[bool]] = None,
            filter_policy: Optional[pulumi.Input[str]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            pending_confirmation: Optional[pulumi.Input[bool]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            raw_message_delivery: Optional[pulumi.Input[bool]] = None,
            redrive_policy: Optional[pulumi.Input[str]] = None,
            subscription_role_arn: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None) -> 'TopicSubscription':
        """
        Get an existing TopicSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the subscription.
        :param pulumi.Input[int] confirmation_timeout_in_minutes: Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols. Default is `1`.
        :param pulumi.Input[bool] confirmation_was_authenticated: Whether the subscription confirmation request was authenticated.
        :param pulumi.Input[str] delivery_policy: JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        :param pulumi.Input[str] endpoint: Endpoint to send data to. The contents vary with the protocol. See details below.
        :param pulumi.Input[bool] endpoint_auto_confirms: Whether the endpoint is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) (e.g., PagerDuty). Default is `false`.
        :param pulumi.Input[str] filter_policy: JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        :param pulumi.Input[str] owner_id: AWS account ID of the subscription's owner.
        :param pulumi.Input[bool] pending_confirmation: Whether the subscription has not been confirmed.
        :param pulumi.Input[str] protocol: Protocol to use. Valid values are: `sqs`, `sms`, `lambda`, `firehose`, and `application`. Protocols `email`, `email-json`, `http` and `https` are also valid but partially supported. See details below.
        :param pulumi.Input[bool] raw_message_delivery: Whether to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property). Default is `false`.
        :param pulumi.Input[str] redrive_policy: JSON String with the redrive policy that will be used in the subscription. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html#how-messages-moved-into-dead-letter-queue) for more details.
        :param pulumi.Input[str] subscription_role_arn: ARN of the IAM role to publish to Kinesis Data Firehose delivery stream. Refer to [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html).
        :param pulumi.Input[str] topic: ARN of the SNS topic to subscribe to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["confirmation_timeout_in_minutes"] = confirmation_timeout_in_minutes
        __props__["confirmation_was_authenticated"] = confirmation_was_authenticated
        __props__["delivery_policy"] = delivery_policy
        __props__["endpoint"] = endpoint
        __props__["endpoint_auto_confirms"] = endpoint_auto_confirms
        __props__["filter_policy"] = filter_policy
        __props__["owner_id"] = owner_id
        __props__["pending_confirmation"] = pending_confirmation
        __props__["protocol"] = protocol
        __props__["raw_message_delivery"] = raw_message_delivery
        __props__["redrive_policy"] = redrive_policy
        __props__["subscription_role_arn"] = subscription_role_arn
        __props__["topic"] = topic
        return TopicSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the subscription.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="confirmationTimeoutInMinutes")
    def confirmation_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols. Default is `1`.
        """
        return pulumi.get(self, "confirmation_timeout_in_minutes")

    @property
    @pulumi.getter(name="confirmationWasAuthenticated")
    def confirmation_was_authenticated(self) -> pulumi.Output[bool]:
        """
        Whether the subscription confirmation request was authenticated.
        """
        return pulumi.get(self, "confirmation_was_authenticated")

    @property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> pulumi.Output[Optional[str]]:
        """
        JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        """
        return pulumi.get(self, "delivery_policy")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint to send data to. The contents vary with the protocol. See details below.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="endpointAutoConfirms")
    def endpoint_auto_confirms(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the endpoint is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) (e.g., PagerDuty). Default is `false`.
        """
        return pulumi.get(self, "endpoint_auto_confirms")

    @property
    @pulumi.getter(name="filterPolicy")
    def filter_policy(self) -> pulumi.Output[Optional[str]]:
        """
        JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        """
        return pulumi.get(self, "filter_policy")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        AWS account ID of the subscription's owner.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="pendingConfirmation")
    def pending_confirmation(self) -> pulumi.Output[bool]:
        """
        Whether the subscription has not been confirmed.
        """
        return pulumi.get(self, "pending_confirmation")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Protocol to use. Valid values are: `sqs`, `sms`, `lambda`, `firehose`, and `application`. Protocols `email`, `email-json`, `http` and `https` are also valid but partially supported. See details below.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="rawMessageDelivery")
    def raw_message_delivery(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property). Default is `false`.
        """
        return pulumi.get(self, "raw_message_delivery")

    @property
    @pulumi.getter(name="redrivePolicy")
    def redrive_policy(self) -> pulumi.Output[Optional[str]]:
        """
        JSON String with the redrive policy that will be used in the subscription. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html#how-messages-moved-into-dead-letter-queue) for more details.
        """
        return pulumi.get(self, "redrive_policy")

    @property
    @pulumi.getter(name="subscriptionRoleArn")
    def subscription_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        ARN of the IAM role to publish to Kinesis Data Firehose delivery stream. Refer to [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html).
        """
        return pulumi.get(self, "subscription_role_arn")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        ARN of the SNS topic to subscribe to.
        """
        return pulumi.get(self, "topic")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

