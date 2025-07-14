import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_create_201_success_all_params():
    """Tests a POST request to the /doc_project endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.DocProject

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
    response = client.doc.create(name="my-company-docs")
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /doc_project endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.DocProject

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
    response = await client.doc.create(name="my-company-docs")
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_patch_200_success_all_params():
    """Tests a PATCH request to the /doc_project/{doc_name} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DocProject

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
    response = client.doc.patch(
        doc_name="my-project",
        logos={
            "dark": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "favicon": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "light": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        },
        name="my-company-docs",
        settings={
            "action_button": {
                "enabled": True,
                "label": "string",
                "url": "http://www.example.com",
            },
            "metadata": {"description": "string", "title": "string"},
        },
    )
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_all_params():
    """Tests a PATCH request to the /doc_project/{doc_name} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DocProject

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
    response = await client.doc.patch(
        doc_name="my-project",
        logos={
            "dark": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "favicon": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "light": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        },
        name="my-company-docs",
        settings={
            "action_button": {
                "enabled": True,
                "label": "string",
                "url": "http://www.example.com",
            },
            "metadata": {"description": "string", "title": "string"},
        },
    )
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_check_preview_200_success_required_only():
    """Tests a GET request to the /doc_project/{doc_name}/preview endpoint.

    Operation: check_preview
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : bool

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
    response = client.doc.check_preview(
        doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
    )
    try:
        pydantic.TypeAdapter(bool).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_check_preview_200_success_required_only():
    """Tests a GET request to the /doc_project/{doc_name}/preview endpoint.

    Operation: check_preview
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : bool

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
    response = await client.doc.check_preview(
        doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
    )
    try:
        pydantic.TypeAdapter(bool).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_check_preview_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/preview endpoint.

    Operation: check_preview
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : bool

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
    response = client.doc.check_preview(
        doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
    )
    try:
        pydantic.TypeAdapter(bool).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_check_preview_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/preview endpoint.

    Operation: check_preview
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : bool

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
    response = await client.doc.check_preview(
        doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
    )
    try:
        pydantic.TypeAdapter(bool).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DocProject

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
    response = client.doc.get(doc_name="my-project")
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DocProject

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
    response = await client.doc.get(doc_name="my-project")
    try:
        pydantic.TypeAdapter(models.DocProject).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /doc_project endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.DocProject]

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
    response = client.doc.list()
    try:
        pydantic.TypeAdapter(typing.List[models.DocProject]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /doc_project endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.DocProject]

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
    response = await client.doc.list()
    try:
        pydantic.TypeAdapter(typing.List[models.DocProject]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name} endpoint.

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
    response = client.doc.delete(doc_name="my-project")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name} endpoint.

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
    response = await client.doc.delete(doc_name="my-project")
    assert response is None
