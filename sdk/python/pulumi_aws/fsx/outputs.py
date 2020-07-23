# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'WindowsFileSystemSelfManagedActiveDirectory',
]

@pulumi.output_type
class WindowsFileSystemSelfManagedActiveDirectory(dict):
    @property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> List[str]:
        """
        A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
        """
        ...

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
        """
        ...

    @property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[str]:
        """
        The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
        """
        ...

    @property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[str]:
        """
        The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
        """
        ...

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        """
        ...

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

