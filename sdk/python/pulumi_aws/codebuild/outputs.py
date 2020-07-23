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
    'ProjectArtifacts',
    'ProjectCache',
    'ProjectEnvironment',
    'ProjectEnvironmentEnvironmentVariable',
    'ProjectEnvironmentRegistryCredential',
    'ProjectLogsConfig',
    'ProjectLogsConfigCloudwatchLogs',
    'ProjectLogsConfigS3Logs',
    'ProjectSecondaryArtifact',
    'ProjectSecondarySource',
    'ProjectSecondarySourceAuth',
    'ProjectSecondarySourceGitSubmodulesConfig',
    'ProjectSource',
    'ProjectSourceAuth',
    'ProjectSourceGitSubmodulesConfig',
    'ProjectVpcConfig',
    'WebhookFilterGroup',
    'WebhookFilterGroupFilter',
]

@pulumi.output_type
class ProjectArtifacts(dict):
    @property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> Optional[str]:
        """
        The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
        """
        ...

    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        """
        If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
        """
        ...

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[str]:
        """
        The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
        """
        ...

    @property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[bool]:
        """
        If set to true, a name specified in the build spec file overrides the artifact name.
        """
        ...

    @property
    @pulumi.getter
    def packaging(self) -> Optional[str]:
        """
        The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
        """
        ...

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        If `type` is set to `S3`, this is the path to the output artifact
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectCache(dict):
    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location where the AWS CodeBuild project stores cached resources. For type `S3` the value must be a valid S3 bucket name/prefix.
        """
        ...

    @property
    @pulumi.getter
    def modes(self) -> Optional[List[str]]:
        """
        Specifies settings that AWS CodeBuild uses to store and reuse build dependencies. Valid values:  `LOCAL_SOURCE_CACHE`, `LOCAL_DOCKER_LAYER_CACHE`, and `LOCAL_CUSTOM_CACHE`
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of storage that will be used for the AWS CodeBuild project cache. Valid values: `NO_CACHE`, `LOCAL`, and `S3`. Defaults to `NO_CACHE`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironment(dict):
    @property
    @pulumi.getter
    def certificate(self) -> Optional[str]:
        """
        The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.
        """
        ...

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> str:
        """
        Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.
        """
        ...

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[List['outputs.ProjectEnvironmentEnvironmentVariable']]:
        """
        A set of environment variables to make available to builds for this build project.
        """
        ...

    @property
    @pulumi.getter
    def image(self) -> str:
        """
        The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `nginx:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).
        """
        ...

    @property
    @pulumi.getter(name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> Optional[str]:
        """
        The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`
        """
        ...

    @property
    @pulumi.getter(name="privilegedMode")
    def privileged_mode(self) -> Optional[bool]:
        """
        If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter(name="registryCredential")
    def registry_credential(self) -> Optional['outputs.ProjectEnvironmentRegistryCredential']:
        """
        Information about credentials for access to a private Docker registry. Registry Credential config blocks are documented below.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of build environment to use for related builds. Available values are: `LINUX_CONTAINER`, `LINUX_GPU_CONTAINER`, `WINDOWS_CONTAINER` or `ARM_CONTAINER`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironmentEnvironmentVariable(dict):
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The environment variable's name or key.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of environment variable. Valid values: `PARAMETER_STORE`, `PLAINTEXT`.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The environment variable's value.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectEnvironmentRegistryCredential(dict):
    @property
    @pulumi.getter
    def credential(self) -> str:
        """
        The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
        """
        ...

    @property
    @pulumi.getter(name="credentialProvider")
    def credential_provider(self) -> str:
        """
        The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for AWS Secrets Manager.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfig(dict):
    @property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional['outputs.ProjectLogsConfigCloudwatchLogs']:
        """
        Configuration for the builds to store logs to CloudWatch
        """
        ...

    @property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional['outputs.ProjectLogsConfigS3Logs']:
        """
        Configuration for the builds to store logs to S3.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfigCloudwatchLogs(dict):
    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        """
        The group name of the logs in CloudWatch Logs.
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.
        """
        ...

    @property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[str]:
        """
        The stream name of the logs in CloudWatch Logs.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectLogsConfigS3Logs(dict):
    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        """
        If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket.
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Current status of logs in CloudWatch Logs for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `ENABLED`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondaryArtifact(dict):
    @property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> str:
        """
        The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.
        """
        ...

    @property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[bool]:
        """
        If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket. If `path` is not also specified, then `location` can also specify the path of the output artifact in the output bucket.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
        """
        ...

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[str]:
        """
        The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.
        """
        ...

    @property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[bool]:
        """
        If set to true, a name specified in the build spec file overrides the artifact name.
        """
        ...

    @property
    @pulumi.getter
    def packaging(self) -> Optional[str]:
        """
        The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`
        """
        ...

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        If `type` is set to `S3`, this is the path to the output artifact
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySource(dict):
    @property
    @pulumi.getter
    def auths(self) -> Optional[List['outputs.ProjectSecondarySourceAuth']]:
        """
        Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
        """
        ...

    @property
    @pulumi.getter
    def buildspec(self) -> Optional[str]:
        """
        The build spec declaration to use for this build project's related builds.
        """
        ...

    @property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[float]:
        """
        Truncate git history to this many commits.
        """
        ...

    @property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(self) -> Optional['outputs.ProjectSecondarySourceGitSubmodulesConfig']:
        """
        Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`, `GITHUB` or `GITHUB_ENTERPRISE`.
        """
        ...

    @property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[bool]:
        """
        Ignore SSL warnings when connecting to source control.
        """
        ...

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the source code from git or s3.
        """
        ...

    @property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[bool]:
        """
        Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when your source provider is `GITHUB`, `BITBUCKET`, or `GITHUB_ENTERPRISE`.
        """
        ...

    @property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> str:
        """
        The source identifier. Source data will be put inside a folder named as this parameter inside AWS CodeBuild source directory
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET` or `S3`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySourceAuth(dict):
    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        """
        The resource value that applies to the specified authorization type.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The authorization type to use. The only valid value is `OAUTH`
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSecondarySourceGitSubmodulesConfig(dict):
    @property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> bool:
        """
        If set to true, fetches Git submodules for the AWS CodeBuild build project.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSource(dict):
    @property
    @pulumi.getter
    def auths(self) -> Optional[List['outputs.ProjectSourceAuth']]:
        """
        Information about the authorization settings for AWS CodeBuild to access the source code to be built. Auth blocks are documented below.
        """
        ...

    @property
    @pulumi.getter
    def buildspec(self) -> Optional[str]:
        """
        The build spec declaration to use for this build project's related builds. This must be set when `type` is `NO_SOURCE`.
        """
        ...

    @property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[float]:
        """
        Truncate git history to this many commits.
        """
        ...

    @property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(self) -> Optional['outputs.ProjectSourceGitSubmodulesConfig']:
        """
        Information about the Git submodules configuration for an AWS CodeBuild build project. Git submodules config blocks are documented below. This option is only valid when the `type` is `CODECOMMIT`, `GITHUB` or `GITHUB_ENTERPRISE`.
        """
        ...

    @property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[bool]:
        """
        Ignore SSL warnings when connecting to source control.
        """
        ...

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the source code from git or s3.
        """
        ...

    @property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[bool]:
        """
        Set to `true` to report the status of a build's start and finish to your source provider. This option is only valid when the `type` is `BITBUCKET` or `GITHUB`.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of repository that contains the source code to be built. Valid values for this parameter are: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `GITHUB_ENTERPRISE`, `BITBUCKET`, `S3` or `NO_SOURCE`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSourceAuth(dict):
    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        """
        The resource value that applies to the specified authorization type.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The authorization type to use. The only valid value is `OAUTH`
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectSourceGitSubmodulesConfig(dict):
    @property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> bool:
        """
        If set to true, fetches Git submodules for the AWS CodeBuild build project.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProjectVpcConfig(dict):
    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> List[str]:
        """
        The security group IDs to assign to running builds.
        """
        ...

    @property
    @pulumi.getter
    def subnets(self) -> List[str]:
        """
        The subnet IDs within which to run builds.
        """
        ...

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The ID of the VPC within which to run builds.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WebhookFilterGroup(dict):
    @property
    @pulumi.getter
    def filters(self) -> Optional[List['outputs.WebhookFilterGroupFilter']]:
        """
        A webhook filter for the group. Filter blocks are documented below.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WebhookFilterGroupFilter(dict):
    @property
    @pulumi.getter(name="excludeMatchedPattern")
    def exclude_matched_pattern(self) -> Optional[bool]:
        """
        If set to `true`, the specified filter does *not* trigger a build. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter
    def pattern(self) -> str:
        """
        For a filter that uses `EVENT` type, a comma-separated string that specifies one event: `PUSH`, `PULL_REQUEST_CREATED`, `PULL_REQUEST_UPDATED`, `PULL_REQUEST_REOPENED`. `PULL_REQUEST_MERGED` works with GitHub & GitHub Enterprise only. For a filter that uses any of the other filter types, a regular expression.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The webhook filter group's type. Valid values for this parameter are: `EVENT`, `BASE_REF`, `HEAD_REF`, `ACTOR_ACCOUNT_ID`, `FILE_PATH`. At least one filter group must specify `EVENT` as its type.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

