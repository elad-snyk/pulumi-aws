# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GatewaySmbActiveDirectorySettingsArgs',
    'NfsFileShareNfsFileShareDefaultsArgs',
]

@pulumi.input_type
class GatewaySmbActiveDirectorySettingsArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] domain_name: The name of the domain that you want the gateway to join.
        :param pulumi.Input[str] password: The password of the user who has permission to add the gateway to the Active Directory domain.
        :param pulumi.Input[str] username: The user name of user who has permission to add the gateway to the Active Directory domain.
        """
        pulumi.set(__self__, "domainName", domain_name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The name of the domain that you want the gateway to join.
        """
        ...

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the user who has permission to add the gateway to the Active Directory domain.
        """
        ...

    @password.setter
    def password(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The user name of user who has permission to add the gateway to the Active Directory domain.
        """
        ...

    @username.setter
    def username(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class NfsFileShareNfsFileShareDefaultsArgs:
    def __init__(__self__, *,
                 directory_mode: Optional[pulumi.Input[str]] = None,
                 file_mode: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[float]] = None,
                 owner_id: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] directory_mode: The Unix directory mode in the string form "nnnn". Defaults to `"0777"`.
        :param pulumi.Input[str] file_mode: The Unix file mode in the string form "nnnn". Defaults to `"0666"`.
        :param pulumi.Input[float] group_id: The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        :param pulumi.Input[float] owner_id: The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        pulumi.set(__self__, "directoryMode", directory_mode)
        pulumi.set(__self__, "fileMode", file_mode)
        pulumi.set(__self__, "groupId", group_id)
        pulumi.set(__self__, "ownerId", owner_id)

    @property
    @pulumi.getter(name="directoryMode")
    def directory_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The Unix directory mode in the string form "nnnn". Defaults to `"0777"`.
        """
        ...

    @directory_mode.setter
    def directory_mode(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="fileMode")
    def file_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The Unix file mode in the string form "nnnn". Defaults to `"0666"`.
        """
        ...

    @file_mode.setter
    def file_mode(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[float]]:
        """
        The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        ...

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[float]]:
        """
        The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
        """
        ...

    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[float]]):
        ...

