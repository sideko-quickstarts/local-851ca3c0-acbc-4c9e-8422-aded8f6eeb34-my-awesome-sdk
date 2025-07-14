import io
import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_create_201_success_all_params():
    """Tests a POST request to the /api/{api_name}/spec endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.ApiSpec

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
    response = client.api.spec.create(
        api_name="my-project",
        openapi=io.BytesIO(b"123"),
        version="major",
        allow_lint_errors=True,
        mock_server_enabled=True,
        notes="<p>This version includes a number of excellent improvements</p>",
    )
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /api/{api_name}/spec endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.ApiSpec

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
    response = await client.api.spec.create(
        api_name="my-project",
        openapi=io.BytesIO(b"123"),
        version="major",
        allow_lint_errors=True,
        mock_server_enabled=True,
        notes="<p>This version includes a number of excellent improvements</p>",
    )
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_patch_200_success_all_params():
    """Tests a PATCH request to the /api/{api_name}/spec/{api_version} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiSpec

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
    response = client.api.spec.patch(
        api_name="my-project",
        api_version="latest",
        allow_lint_errors=True,
        mock_server_enabled=True,
        notes="<p>This version includes a number of excellent improvements</p>",
        openapi=io.BytesIO(b"123"),
        version="string",
    )
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_all_params():
    """Tests a PATCH request to the /api/{api_name}/spec/{api_version} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiSpec

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
    response = await client.api.spec.patch(
        api_name="my-project",
        api_version="latest",
        allow_lint_errors=True,
        mock_server_enabled=True,
        notes="<p>This version includes a number of excellent improvements</p>",
        openapi=io.BytesIO(b"123"),
        version="string",
    )
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_stats_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version}/stats endpoint.

    Operation: get_stats
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiSpecStats

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
    response = client.api.spec.get_stats(api_name="my-project", api_version="latest")
    try:
        pydantic.TypeAdapter(models.ApiSpecStats).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_stats_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version}/stats endpoint.

    Operation: get_stats
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiSpecStats

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
    response = await client.api.spec.get_stats(
        api_name="my-project", api_version="latest"
    )
    try:
        pydantic.TypeAdapter(models.ApiSpecStats).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_openapi_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version}/openapi endpoint.

    Operation: get_openapi
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.OpenApi

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
    response = client.api.spec.get_openapi(api_name="my-project", api_version="latest")
    try:
        pydantic.TypeAdapter(models.OpenApi).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_openapi_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version}/openapi endpoint.

    Operation: get_openapi
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.OpenApi

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
    response = await client.api.spec.get_openapi(
        api_name="my-project", api_version="latest"
    )
    try:
        pydantic.TypeAdapter(models.OpenApi).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ApiSpec

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
    response = client.api.spec.get(api_name="my-project", api_version="latest")
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec/{api_version} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ApiSpec

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
    response = await client.api.spec.get(api_name="my-project", api_version="latest")
    try:
        pydantic.TypeAdapter(models.ApiSpec).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.ApiSpec]

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
    response = client.api.spec.list(api_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.ApiSpec]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /api/{api_name}/spec endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.ApiSpec]

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
    response = await client.api.spec.list(api_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.ApiSpec]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params():
    """Tests a DELETE request to the /api/{api_name}/spec/{api_version} endpoint.

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
    response = client.api.spec.delete(api_name="my-project", api_version="latest")
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params():
    """Tests a DELETE request to the /api/{api_name}/spec/{api_version} endpoint.

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
    response = await client.api.spec.delete(api_name="my-project", api_version="latest")
    assert response is None
