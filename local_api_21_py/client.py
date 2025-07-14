import httpx
import typing

from local_api_21_py.core import AsyncBaseClient, AuthKey, SyncBaseClient
from local_api_21_py.environment import Environment, _get_base_url
from local_api_21_py.resources.api import ApiClient, AsyncApiClient
from local_api_21_py.resources.api_link import ApiLinkClient, AsyncApiLinkClient
from local_api_21_py.resources.asset import AssetClient, AsyncAssetClient
from local_api_21_py.resources.auth import AsyncAuthClient, AuthClient
from local_api_21_py.resources.cli import AsyncCliClient, CliClient
from local_api_21_py.resources.doc import AsyncDocClient, DocClient
from local_api_21_py.resources.health import AsyncHealthClient, HealthClient
from local_api_21_py.resources.lint import AsyncLintClient, LintClient
from local_api_21_py.resources.org import AsyncOrgClient, OrgClient
from local_api_21_py.resources.role import AsyncRoleClient, RoleClient
from local_api_21_py.resources.sdk import AsyncSdkClient, SdkClient
from local_api_21_py.resources.service_account import (
    AsyncServiceAccountClient,
    ServiceAccountClient,
)
from local_api_21_py.resources.user import AsyncUserClient, UserClient
from local_api_21_py.resources.webhook import AsyncWebhookClient, WebhookClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        api_key_1: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "ApiKeyAuth", AuthKey(name="x-sideko-key", location="header", val=api_key)
        )
        self._base_client.register_auth(
            "CookieAuth",
            AuthKey(name="SIDEKO_SESSION", location="cookie", val=api_key_1),
        )
        self.api = ApiClient(base_client=self._base_client)
        self.api_link = ApiLinkClient(base_client=self._base_client)
        self.doc = DocClient(base_client=self._base_client)
        self.asset = AssetClient(base_client=self._base_client)
        self.role = RoleClient(base_client=self._base_client)
        self.service_account = ServiceAccountClient(base_client=self._base_client)
        self.health = HealthClient(base_client=self._base_client)
        self.auth = AuthClient(base_client=self._base_client)
        self.cli = CliClient(base_client=self._base_client)
        self.org = OrgClient(base_client=self._base_client)
        self.sdk = SdkClient(base_client=self._base_client)
        self.user = UserClient(base_client=self._base_client)
        self.lint = LintClient(base_client=self._base_client)
        self.webhook = WebhookClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        api_key: typing.Optional[str] = None,
        api_key_1: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "ApiKeyAuth", AuthKey(name="x-sideko-key", location="header", val=api_key)
        )
        self._base_client.register_auth(
            "CookieAuth",
            AuthKey(name="SIDEKO_SESSION", location="cookie", val=api_key_1),
        )
        self.api = AsyncApiClient(base_client=self._base_client)
        self.api_link = AsyncApiLinkClient(base_client=self._base_client)
        self.doc = AsyncDocClient(base_client=self._base_client)
        self.asset = AsyncAssetClient(base_client=self._base_client)
        self.role = AsyncRoleClient(base_client=self._base_client)
        self.service_account = AsyncServiceAccountClient(base_client=self._base_client)
        self.health = AsyncHealthClient(base_client=self._base_client)
        self.auth = AsyncAuthClient(base_client=self._base_client)
        self.cli = AsyncCliClient(base_client=self._base_client)
        self.org = AsyncOrgClient(base_client=self._base_client)
        self.sdk = AsyncSdkClient(base_client=self._base_client)
        self.user = AsyncUserClient(base_client=self._base_client)
        self.lint = AsyncLintClient(base_client=self._base_client)
        self.webhook = AsyncWebhookClient(base_client=self._base_client)
