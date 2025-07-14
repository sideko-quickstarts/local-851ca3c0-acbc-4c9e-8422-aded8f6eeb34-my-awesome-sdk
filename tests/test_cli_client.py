import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_check_updates_200_success_all_params():
    """Tests a GET request to the /cli/updates/{cli_version} endpoint.

    Operation: check_updates
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.CliUpdate]

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
    response = client.cli.check_updates(cli_version="0.1.0")
    try:
        pydantic.TypeAdapter(typing.List[models.CliUpdate]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_check_updates_200_success_all_params():
    """Tests a GET request to the /cli/updates/{cli_version} endpoint.

    Operation: check_updates
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.CliUpdate]

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
    response = await client.cli.check_updates(cli_version="0.1.0")
    try:
        pydantic.TypeAdapter(typing.List[models.CliUpdate]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
