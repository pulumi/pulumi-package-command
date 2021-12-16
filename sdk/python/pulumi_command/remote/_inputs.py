# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ConnectionArgs',
]

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[str],
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Instructions for how to connect to a remote endpoint.
        :param pulumi.Input[str] host: The address of the resource to connect to.
        :param pulumi.Input[str] password: The password we should use for the connection.
        :param pulumi.Input[float] port: The port to connect to.
        :param pulumi.Input[str] private_key: The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        pulumi.set(__self__, "host", host)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is None:
            port = 22
        if port is not None:
            pulumi.set(__self__, "port", port)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if user is None:
            user = 'root'
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        The address of the resource to connect to.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password we should use for the connection.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[float]]:
        """
        The port to connect to.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


