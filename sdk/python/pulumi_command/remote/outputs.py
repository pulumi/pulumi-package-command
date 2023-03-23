# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'Connection',
]

@pulumi.output_type
class Connection(dict):
    """
    Instructions for how to connect to a remote endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "agentSocketPath":
            suggest = "agent_socket_path"
        elif key == "dialErrorLimit":
            suggest = "dial_error_limit"
        elif key == "privateKey":
            suggest = "private_key"
        elif key == "privateKeyPassword":
            suggest = "private_key_password"
        elif key == "proxyHost":
            suggest = "proxy_host"
        elif key == "proxyPassword":
            suggest = "proxy_password"
        elif key == "proxyPort":
            suggest = "proxy_port"
        elif key == "proxyPrivateKey":
            suggest = "proxy_private_key"
        elif key == "proxyUser":
            suggest = "proxy_user"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Connection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Connection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Connection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host: str,
                 agent_socket_path: Optional[str] = None,
                 dial_error_limit: Optional[int] = None,
                 password: Optional[str] = None,
                 port: Optional[float] = None,
                 private_key: Optional[str] = None,
                 private_key_password: Optional[str] = None,
                 proxy_host: Optional[str] = None,
                 proxy_password: Optional[str] = None,
                 proxy_port: Optional[int] = None,
                 proxy_private_key: Optional[str] = None,
                 proxy_user: Optional[str] = None,
                 user: Optional[str] = None):
        """
        Instructions for how to connect to a remote endpoint.
        :param str host: The address of the resource to connect to.
        :param str agent_socket_path: SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        :param int dial_error_limit: Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10
        :param str password: The password we should use for the connection.
        :param float port: The port to connect to.
        :param str private_key: The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        :param str private_key_password: The password to use in case the private key is encrypted.
        :param str proxy_host: The address of the bastion host to connect to.
        :param str proxy_password: The password we should use for the bastion host connection.
        :param str proxy_private_key: The contents of an SSH key to use for the bastion host to setup the connection. This takes preference over the password if provided.
        :param str proxy_user: The user that we should use for the bastion host connection.
        :param str user: The user that we should use for the connection.
        """
        pulumi.set(__self__, "host", host)
        if agent_socket_path is not None:
            pulumi.set(__self__, "agent_socket_path", agent_socket_path)
        if dial_error_limit is None:
            dial_error_limit = 10
        if dial_error_limit is not None:
            pulumi.set(__self__, "dial_error_limit", dial_error_limit)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is None:
            port = 22
        if port is not None:
            pulumi.set(__self__, "port", port)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if private_key_password is not None:
            pulumi.set(__self__, "private_key_password", private_key_password)
        if proxy_host is not None:
            pulumi.set(__self__, "proxy_host", proxy_host)
        if proxy_password is not None:
            pulumi.set(__self__, "proxy_password", proxy_password)
        if proxy_port is None:
            proxy_port = 22
        if proxy_port is not None:
            pulumi.set(__self__, "proxy_port", proxy_port)
        if proxy_private_key is not None:
            pulumi.set(__self__, "proxy_private_key", proxy_private_key)
        if proxy_user is not None:
            pulumi.set(__self__, "proxy_user", proxy_user)
        if user is None:
            user = 'root'
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The address of the resource to connect to.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="agentSocketPath")
    def agent_socket_path(self) -> Optional[str]:
        """
        SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
        """
        return pulumi.get(self, "agent_socket_path")

    @property
    @pulumi.getter(name="dialErrorLimit")
    def dial_error_limit(self) -> Optional[int]:
        """
        Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10
        """
        return pulumi.get(self, "dial_error_limit")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        The password we should use for the connection.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> Optional[float]:
        """
        The port to connect to.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[str]:
        """
        The contents of an SSH key to use for the connection. This takes preference over the password if provided.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="privateKeyPassword")
    def private_key_password(self) -> Optional[str]:
        """
        The password to use in case the private key is encrypted.
        """
        return pulumi.get(self, "private_key_password")

    @property
    @pulumi.getter(name="proxyHost")
    def proxy_host(self) -> Optional[str]:
        """
        The address of the bastion host to connect to.
        """
        return pulumi.get(self, "proxy_host")

    @property
    @pulumi.getter(name="proxyPassword")
    def proxy_password(self) -> Optional[str]:
        """
        The password we should use for the bastion host connection.
        """
        return pulumi.get(self, "proxy_password")

    @property
    @pulumi.getter(name="proxyPort")
    def proxy_port(self) -> Optional[int]:
        return pulumi.get(self, "proxy_port")

    @property
    @pulumi.getter(name="proxyPrivateKey")
    def proxy_private_key(self) -> Optional[str]:
        """
        The contents of an SSH key to use for the bastion host to setup the connection. This takes preference over the password if provided.
        """
        return pulumi.get(self, "proxy_private_key")

    @property
    @pulumi.getter(name="proxyUser")
    def proxy_user(self) -> Optional[str]:
        """
        The user that we should use for the bastion host connection.
        """
        return pulumi.get(self, "proxy_user")

    @property
    @pulumi.getter
    def user(self) -> Optional[str]:
        """
        The user that we should use for the connection.
        """
        return pulumi.get(self, "user")


