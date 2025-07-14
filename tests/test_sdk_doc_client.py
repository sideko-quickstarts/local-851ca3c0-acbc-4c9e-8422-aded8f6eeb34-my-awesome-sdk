import pydantic
import pytest

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /sdk/{sdk_id}/doc endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SdkDocResponse

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
    response = client.sdk.doc.create(sdk_id="h1jasdf123", modules_filter=["user.admin"])
    try:
        pydantic.TypeAdapter(models.SdkDocResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /sdk/{sdk_id}/doc endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SdkDocResponse

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
    response = await client.sdk.doc.create(
        sdk_id="h1jasdf123", modules_filter=["user.admin"]
    )
    try:
        pydantic.TypeAdapter(models.SdkDocResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
