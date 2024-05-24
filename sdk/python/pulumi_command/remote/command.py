# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['CommandArgs', 'Command']

@pulumi.input_type
class CommandArgs:
    def __init__(__self__, *,
                 connection: pulumi.Input['ConnectionArgs'],
                 add_previous_output_in_env: Optional[pulumi.Input[bool]] = None,
                 create: Optional[pulumi.Input[str]] = None,
                 delete: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 logging: Optional[pulumi.Input['Logging']] = None,
                 stdin: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Command resource.
        :param pulumi.Input['ConnectionArgs'] connection: The parameters with which to connect to the remote host.
        :param pulumi.Input[str] create: The command to run on create.
        :param pulumi.Input[str] delete: The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
               and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
               Command resource from previous create or update steps.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: Additional environment variables available to the command's process.
               Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
               Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
               with the variables in the form 'VAR=value command'.
        :param pulumi.Input['Logging'] logging: If the command's stdout and stderr should be logged. This doesn't affect the capturing of
               stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
               outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
        :param pulumi.Input[str] stdin: Pass a string to the command's process as standard in
        :param pulumi.Input[Sequence[Any]] triggers: Trigger replacements on changes to this input.
        :param pulumi.Input[str] update: The command to run on update, if empty, create will 
               run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
               are set to the stdout and stderr properties of the Command resource from previous 
               create or update steps.
        """
        pulumi.set(__self__, "connection", connection)
        if add_previous_output_in_env is not None:
            pulumi.set(__self__, "add_previous_output_in_env", add_previous_output_in_env)
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)
        if stdin is not None:
            pulumi.set(__self__, "stdin", stdin)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Input['ConnectionArgs']:
        """
        The parameters with which to connect to the remote host.
        """
        return pulumi.get(self, "connection")

    @connection.setter
    def connection(self, value: pulumi.Input['ConnectionArgs']):
        pulumi.set(self, "connection", value)

    @property
    @pulumi.getter(name="addPreviousOutputInEnv")
    def add_previous_output_in_env(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "add_previous_output_in_env")

    @add_previous_output_in_env.setter
    def add_previous_output_in_env(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_previous_output_in_env", value)

    @property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[str]]:
        """
        The command to run on create.
        """
        return pulumi.get(self, "create")

    @create.setter
    def create(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[str]]:
        """
        The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
        and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
        Command resource from previous create or update steps.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Additional environment variables available to the command's process.
        Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
        Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
        with the variables in the form 'VAR=value command'.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['Logging']]:
        """
        If the command's stdout and stderr should be logged. This doesn't affect the capturing of
        stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
        outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
        """
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['Logging']]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter
    def stdin(self) -> Optional[pulumi.Input[str]]:
        """
        Pass a string to the command's process as standard in
        """
        return pulumi.get(self, "stdin")

    @stdin.setter
    def stdin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stdin", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        Trigger replacements on changes to this input.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "triggers", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[str]]:
        """
        The command to run on update, if empty, create will 
        run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
        are set to the stdout and stderr properties of the Command resource from previous 
        create or update steps.
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update", value)


class Command(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_previous_output_in_env: Optional[pulumi.Input[bool]] = None,
                 connection: Optional[pulumi.Input[pulumi.InputType['ConnectionArgs']]] = None,
                 create: Optional[pulumi.Input[str]] = None,
                 delete: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 logging: Optional[pulumi.Input['Logging']] = None,
                 stdin: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A command to run on a remote host.
        The connection is established via ssh.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ConnectionArgs']] connection: The parameters with which to connect to the remote host.
        :param pulumi.Input[str] create: The command to run on create.
        :param pulumi.Input[str] delete: The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
               and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
               Command resource from previous create or update steps.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: Additional environment variables available to the command's process.
               Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
               Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
               with the variables in the form 'VAR=value command'.
        :param pulumi.Input['Logging'] logging: If the command's stdout and stderr should be logged. This doesn't affect the capturing of
               stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
               outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
        :param pulumi.Input[str] stdin: Pass a string to the command's process as standard in
        :param pulumi.Input[Sequence[Any]] triggers: Trigger replacements on changes to this input.
        :param pulumi.Input[str] update: The command to run on update, if empty, create will 
               run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
               are set to the stdout and stderr properties of the Command resource from previous 
               create or update steps.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommandArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A command to run on a remote host.
        The connection is established via ssh.

        :param str resource_name: The name of the resource.
        :param CommandArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommandArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_previous_output_in_env: Optional[pulumi.Input[bool]] = None,
                 connection: Optional[pulumi.Input[pulumi.InputType['ConnectionArgs']]] = None,
                 create: Optional[pulumi.Input[str]] = None,
                 delete: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 logging: Optional[pulumi.Input['Logging']] = None,
                 stdin: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[Any]]] = None,
                 update: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommandArgs.__new__(CommandArgs)

            __props__.__dict__["add_previous_output_in_env"] = add_previous_output_in_env
            if connection is None and not opts.urn:
                raise TypeError("Missing required property 'connection'")
            __props__.__dict__["connection"] = None if connection is None else pulumi.Output.secret(connection)
            __props__.__dict__["create"] = create
            __props__.__dict__["delete"] = delete
            __props__.__dict__["environment"] = environment
            __props__.__dict__["logging"] = logging
            __props__.__dict__["stdin"] = stdin
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["update"] = update
            __props__.__dict__["stderr"] = None
            __props__.__dict__["stdout"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["connection"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["triggers[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Command, __self__).__init__(
            'command:remote:Command',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Command':
        """
        Get an existing Command resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CommandArgs.__new__(CommandArgs)

        __props__.__dict__["add_previous_output_in_env"] = None
        __props__.__dict__["connection"] = None
        __props__.__dict__["create"] = None
        __props__.__dict__["delete"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["logging"] = None
        __props__.__dict__["stderr"] = None
        __props__.__dict__["stdin"] = None
        __props__.__dict__["stdout"] = None
        __props__.__dict__["triggers"] = None
        __props__.__dict__["update"] = None
        return Command(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addPreviousOutputInEnv")
    def add_previous_output_in_env(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "add_previous_output_in_env")

    @property
    @pulumi.getter
    def connection(self) -> pulumi.Output['outputs.Connection']:
        """
        The parameters with which to connect to the remote host.
        """
        return pulumi.get(self, "connection")

    @property
    @pulumi.getter
    def create(self) -> pulumi.Output[Optional[str]]:
        """
        The command to run on create.
        """
        return pulumi.get(self, "create")

    @property
    @pulumi.getter
    def delete(self) -> pulumi.Output[Optional[str]]:
        """
        The command to run on delete. The environment variables PULUMI_COMMAND_STDOUT
        and PULUMI_COMMAND_STDERR are set to the stdout and stderr properties of the
        Command resource from previous create or update steps.
        """
        return pulumi.get(self, "delete")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Additional environment variables available to the command's process.
        Note that this only works if the SSH server is configured to accept these variables via AcceptEnv.
        Alternatively, if a Bash-like shell runs the command on the remote host, you could prefix the command itself
        with the variables in the form 'VAR=value command'.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional['Logging']]:
        """
        If the command's stdout and stderr should be logged. This doesn't affect the capturing of
        stdout and stderr as outputs. If there might be secrets in the output, you can disable logging here and mark the
        outputs as secret via 'additionalSecretOutputs'. Defaults to logging both stdout and stderr.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def stderr(self) -> pulumi.Output[str]:
        """
        The standard error of the command's process
        """
        return pulumi.get(self, "stderr")

    @property
    @pulumi.getter
    def stdin(self) -> pulumi.Output[Optional[str]]:
        """
        Pass a string to the command's process as standard in
        """
        return pulumi.get(self, "stdin")

    @property
    @pulumi.getter
    def stdout(self) -> pulumi.Output[str]:
        """
        The standard output of the command's process
        """
        return pulumi.get(self, "stdout")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Trigger replacements on changes to this input.
        """
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter
    def update(self) -> pulumi.Output[Optional[str]]:
        """
        The command to run on update, if empty, create will 
        run again. The environment variables PULUMI_COMMAND_STDOUT and PULUMI_COMMAND_STDERR 
        are set to the stdout and stderr properties of the Command resource from previous 
        create or update steps.
        """
        return pulumi.get(self, "update")

