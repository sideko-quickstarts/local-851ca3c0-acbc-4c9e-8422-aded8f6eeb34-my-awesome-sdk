import io
import pytest

from local_api_21_py import AsyncClient, Client
from local_api_21_py.core import BinaryResponse
from local_api_21_py.environment import Environment


def test_sync_200_success_all_params():
    """Tests a POST request to the /sdk/config/sync endpoint.

    Operation: sync
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        api_key="API_KEY", api_key_1="API_KEY", environment=Environment.MOCK_SERVER
    )
    response = client.sdk.config.sync(
        config=io.BytesIO(b"123"), api_version="latest", openapi=io.BytesIO(b"123")
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_sync_200_success_all_params():
    """Tests a POST request to the /sdk/config/sync endpoint.

    Operation: sync
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        api_key="API_KEY", api_key_1="API_KEY", environment=Environment.MOCK_SERVER
    )
    response = await client.sdk.config.sync(
        config=io.BytesIO(b"123"), api_version="latest", openapi=io.BytesIO(b"123")
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_init_200_success_all_params():
    """Tests a POST request to the /sdk/config/init endpoint.

    Operation: init
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        api_key="API_KEY", api_key_1="API_KEY", environment=Environment.MOCK_SERVER
    )
    response = client.sdk.config.init(
        api_name="my-project", api_version="latest", default_module_structure="flat"
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_init_200_success_all_params():
    """Tests a POST request to the /sdk/config/init endpoint.

    Operation: init
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        api_key="API_KEY", api_key_1="API_KEY", environment=Environment.MOCK_SERVER
    )
    response = await client.sdk.config.init(
        api_name="my-project", api_version="latest", default_module_structure="flat"
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"
