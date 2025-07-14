import pydantic
import pytest

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_exchange_code_200_success_all_params():
    """Tests a GET request to the /auth/exchange_key endpoint.

    Operation: exchange_code
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.UserApiKey

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
    response = client.auth.exchange_code(code="string")
    try:
        pydantic.TypeAdapter(models.UserApiKey).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_exchange_code_200_success_all_params():
    """Tests a GET request to the /auth/exchange_key endpoint.

    Operation: exchange_code
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.UserApiKey

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
    response = await client.auth.exchange_code(code="string")
    try:
        pydantic.TypeAdapter(models.UserApiKey).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
