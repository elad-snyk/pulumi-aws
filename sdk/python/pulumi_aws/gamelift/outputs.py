# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'AliasRoutingStrategy',
    'BuildStorageLocation',
    'FleetEc2InboundPermission',
    'FleetResourceCreationLimitPolicy',
    'FleetRuntimeConfiguration',
    'FleetRuntimeConfigurationServerProcess',
    'GameSessionQueuePlayerLatencyPolicy',
]

@pulumi.output_type
class AliasRoutingStrategy(dict):
    @property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> Optional[str]:
        """
        ID of the Gamelift Fleet to point the alias to.
        """
        ...

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Message text to be used with the `TERMINAL` routing strategy.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of routing strategy. e.g. `SIMPLE` or `TERMINAL`
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class BuildStorageLocation(dict):
    @property
    @pulumi.getter
    def bucket(self) -> str:
        """
        Name of your S3 bucket.
        """
        ...

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Name of the zip file containing your build files.
        """
        ...

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        ARN of the access role that allows Amazon GameLift to access your S3 bucket.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FleetEc2InboundPermission(dict):
    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> float:
        """
        Starting value for a range of allowed port numbers.
        """
        ...

    @property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> str:
        """
        Range of allowed IP addresses expressed in CIDR notation. e.g. `000.000.000.000/[subnet mask]` or `0.0.0.0/[subnet mask]`.
        """
        ...

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Network communication protocol used by the fleet. e.g. `TCP` or `UDP`
        """
        ...

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> float:
        """
        Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than `from_port`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FleetResourceCreationLimitPolicy(dict):
    @property
    @pulumi.getter(name="newGameSessionsPerCreator")
    def new_game_sessions_per_creator(self) -> Optional[float]:
        """
        Maximum number of game sessions that an individual can create during the policy period.
        """
        ...

    @property
    @pulumi.getter(name="policyPeriodInMinutes")
    def policy_period_in_minutes(self) -> Optional[float]:
        """
        Time span used in evaluating the resource creation limit policy.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FleetRuntimeConfiguration(dict):
    @property
    @pulumi.getter(name="gameSessionActivationTimeoutSeconds")
    def game_session_activation_timeout_seconds(self) -> Optional[float]:
        """
        Maximum amount of time (in seconds) that a game session can remain in status `ACTIVATING`.
        """
        ...

    @property
    @pulumi.getter(name="maxConcurrentGameSessionActivations")
    def max_concurrent_game_session_activations(self) -> Optional[float]:
        """
        Maximum number of game sessions with status `ACTIVATING` to allow on an instance simultaneously.
        """
        ...

    @property
    @pulumi.getter(name="serverProcesses")
    def server_processes(self) -> Optional[List['outputs.FleetRuntimeConfigurationServerProcess']]:
        """
        Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FleetRuntimeConfigurationServerProcess(dict):
    @property
    @pulumi.getter(name="concurrentExecutions")
    def concurrent_executions(self) -> float:
        """
        Number of server processes using this configuration to run concurrently on an instance.
        """
        ...

    @property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> str:
        """
        Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances `C:\game`, and for Linux instances `/local/game`.
        """
        ...

    @property
    @pulumi.getter
    def parameters(self) -> Optional[str]:
        """
        Optional list of parameters to pass to the server executable on launch.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GameSessionQueuePlayerLatencyPolicy(dict):
    @property
    @pulumi.getter(name="maximumIndividualPlayerLatencyMilliseconds")
    def maximum_individual_player_latency_milliseconds(self) -> float:
        """
        Maximum latency value that is allowed for any player.
        """
        ...

    @property
    @pulumi.getter(name="policyDurationSeconds")
    def policy_duration_seconds(self) -> Optional[float]:
        """
        Length of time that the policy is enforced while placing a new game session. Absence of value for this attribute means that the policy is enforced until the queue times out.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

