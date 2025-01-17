# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Bucket']


class Bucket(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 outpost_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage an S3 Control Bucket.

        > This functionality is for managing [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html). To manage S3 Buckets in an AWS Partition, see the `s3.Bucket` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3control.Bucket("example",
            bucket="example",
            outpost_id=data["aws_outposts_outpost"]["example"]["id"])
        ```

        ## Import

        S3 Control Buckets can be imported using Amazon Resource Name (ARN), e.g.

        ```sh
         $ pulumi import aws:s3control/bucket:Bucket example arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-12345678/bucket/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] outpost_id: Identifier of the Outpost to contain this bucket.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
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

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            if outpost_id is None and not opts.urn:
                raise TypeError("Missing required property 'outpost_id'")
            __props__['outpost_id'] = outpost_id
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['creation_date'] = None
            __props__['public_access_block_enabled'] = None
        super(Bucket, __self__).__init__(
            'aws:s3control/bucket:Bucket',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            creation_date: Optional[pulumi.Input[str]] = None,
            outpost_id: Optional[pulumi.Input[str]] = None,
            public_access_block_enabled: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Bucket':
        """
        Get an existing Bucket resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the bucket.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] creation_date: UTC creation date in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
        :param pulumi.Input[str] outpost_id: Identifier of the Outpost to contain this bucket.
        :param pulumi.Input[bool] public_access_block_enabled: Boolean whether Public Access Block is enabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["bucket"] = bucket
        __props__["creation_date"] = creation_date
        __props__["outpost_id"] = outpost_id
        __props__["public_access_block_enabled"] = public_access_block_enabled
        __props__["tags"] = tags
        return Bucket(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the bucket.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        UTC creation date in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> pulumi.Output[str]:
        """
        Identifier of the Outpost to contain this bucket.
        """
        return pulumi.get(self, "outpost_id")

    @property
    @pulumi.getter(name="publicAccessBlockEnabled")
    def public_access_block_enabled(self) -> pulumi.Output[bool]:
        """
        Boolean whether Public Access Block is enabled.
        """
        return pulumi.get(self, "public_access_block_enabled")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

