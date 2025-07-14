import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_create_201_success_all_params():
    """Tests a POST request to the /role endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Role

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
    response = client.role.create(
        object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        object_type="api_project",
        role_definition_id="ApiProjectAdmin",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.Role).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /role endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Role

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
    response = await client.role.create(
        object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        object_type="api_project",
        role_definition_id="ApiProjectAdmin",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.Role).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only():
    """Tests a GET request to the /role endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.Role]

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
    response = client.role.list()
    try:
        pydantic.TypeAdapter(typing.List[models.Role]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /role endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.Role]

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
    response = await client.role.list()
    try:
        pydantic.TypeAdapter(typing.List[models.Role]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /role endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.Role]

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
    response = client.role.list(
        object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        object_type="api_project",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(typing.List[models.Role]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /role endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.Role]

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
    response = await client.role.list(
        object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        object_type="api_project",
        user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(typing.List[models.Role]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params():
    """Tests a DELETE request to the /role/{id} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

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
    response = client.role.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params():
    """Tests a DELETE request to the /role/{id} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

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
    response = await client.role.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    assert response is None
