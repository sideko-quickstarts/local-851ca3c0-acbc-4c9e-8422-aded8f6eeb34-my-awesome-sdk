import typing

from local_api_21_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from local_api_21_py.types import models


class HealthClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthCheckResponse:
        """
        Health Check

        GET /_health

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Check if the service is up and running.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.health.check()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/_health",
            auth_names=["ApiKeyAuth", "CookieAuth"],
            cast_to=models.HealthCheckResponse,
            request_options=request_options or default_request_options(),
        )

    def ping(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthPingResponse:
        """
        Ping Check

        GET /_ping

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Check if the service is up and running.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.health.ping()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/_ping",
            cast_to=models.HealthPingResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncHealthClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def check(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthCheckResponse:
        """
        Health Check

        GET /_health

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Check if the service is up and running.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.health.check()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/_health",
            auth_names=["ApiKeyAuth", "CookieAuth"],
            cast_to=models.HealthCheckResponse,
            request_options=request_options or default_request_options(),
        )

    async def ping(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.HealthPingResponse:
        """
        Ping Check

        GET /_ping

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Check if the service is up and running.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.health.ping()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/_ping",
            cast_to=models.HealthPingResponse,
            request_options=request_options or default_request_options(),
        )
