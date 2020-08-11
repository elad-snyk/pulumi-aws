# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'CertificateDomainValidationOption',
    'CertificateOptions',
]

@pulumi.output_type
class CertificateDomainValidationOption(dict):
    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        A domain name for which the certificate should be issued
        """
        ...

    @property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[str]:
        """
        The name of the DNS record to create to validate the certificate
        """
        ...

    @property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[str]:
        """
        The type of DNS record to create
        """
        ...

    @property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[str]:
        """
        The value the DNS record needs to have
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CertificateOptions(dict):
    @property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[str]:
        """
        Specifies whether certificate details should be added to a certificate transparency log. Valid values are `ENABLED` or `DISABLED`. See https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency for more details.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

