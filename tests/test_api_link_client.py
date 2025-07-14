import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_reorder_200_success_all_params():
    """Tests a POST request to the /api_link/reorder endpoint.

    Operation: reorder
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiReorder

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
    response = client.api_link.reorder(
        doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        groups=[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}],
        links=[
            {
                "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "order": 123,
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.ApiReorder).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_reorder_200_success_all_params():
    """Tests a POST request to the /api_link/reorder endpoint.

    Operation: reorder
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiReorder

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
    response = await client.api_link.reorder(
        doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        groups=[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}],
        links=[
            {
                "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "order": 123,
            }
        ],
    )
    try:
        pydantic.TypeAdapter(models.ApiReorder).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_201_success_all_params():
    """Tests a POST request to the /api_link endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.ApiLink

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
    response = client.api_link.create(
        doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        nav_label="string",
        policy={"api_id": "my-api", "type_": "latest"},
        slug="string",
        build_request_enabled=True,
        include_mock_server=True,
    )
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /api_link endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.ApiLink

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
    response = await client.api_link.create(
        doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        nav_label="string",
        policy={"api_id": "my-api", "type_": "latest"},
        slug="string",
        build_request_enabled=True,
        include_mock_server=True,
    )
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_patch_200_success_all_params():
    """Tests a PATCH request to the /api_link/{id} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiLink

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
    response = client.api_link.patch(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        api_version={"api_id": "my-api", "version": "0.1.0"},
        build_request_enabled=True,
        include_mock_server=True,
        nav_label="string",
        policy="latest",
        slug="string",
    )
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_all_params():
    """Tests a PATCH request to the /api_link/{id} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiLink

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
    response = await client.api_link.patch(
        id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        api_version={"api_id": "my-api", "version": "0.1.0"},
        build_request_enabled=True,
        include_mock_server=True,
        nav_label="string",
        policy="latest",
        slug="string",
    )
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /api_link/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiLink

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
    response = client.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /api_link/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiLink

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
    response = await client.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    try:
        pydantic.TypeAdapter(models.ApiLink).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /api_link endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.ApiLink]

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
    response = client.api_link.list(
        doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.ApiLink]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /api_link endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.ApiLink]

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
    response = await client.api_link.list(
        doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.ApiLink]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params():
    """Tests a DELETE request to the /api_link/{id} endpoint.

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
    response = client.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params():
    """Tests a DELETE request to the /api_link/{id} endpoint.

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
    response = await client.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
    assert response is None
