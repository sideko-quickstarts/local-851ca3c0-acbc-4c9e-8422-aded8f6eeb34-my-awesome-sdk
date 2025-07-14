import pydantic
import pytest

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_update_200_success_all_params():
    """Tests a PUT request to the /organization/theme endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Theme

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
    response = client.org.theme.update(
        api_reference_group_variant="grouped",
        dark_active_button_bg_color="#FFFFFF",
        dark_active_button_text_color="#FFFFFF",
        dark_bg_color="#FFFFFF",
        dark_navbar_color="#FFFFFF",
        dark_navbar_text_color="#FFFFFF",
        light_active_button_bg_color="#FFFFFF",
        light_active_button_text_color="#FFFFFF",
        light_bg_color="#FFFFFF",
        light_navbar_color="#FFFFFF",
        light_navbar_text_color="#FFFFFF",
    )
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params():
    """Tests a PUT request to the /organization/theme endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Theme

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
    response = await client.org.theme.update(
        api_reference_group_variant="grouped",
        dark_active_button_bg_color="#FFFFFF",
        dark_active_button_text_color="#FFFFFF",
        dark_bg_color="#FFFFFF",
        dark_navbar_color="#FFFFFF",
        dark_navbar_text_color="#FFFFFF",
        light_active_button_bg_color="#FFFFFF",
        light_active_button_text_color="#FFFFFF",
        light_bg_color="#FFFFFF",
        light_navbar_color="#FFFFFF",
        light_navbar_text_color="#FFFFFF",
    )
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /organization/theme endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Theme

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
    response = client.org.theme.get()
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /organization/theme endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Theme

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
    response = await client.org.theme.get()
    try:
        pydantic.TypeAdapter(models.Theme).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
