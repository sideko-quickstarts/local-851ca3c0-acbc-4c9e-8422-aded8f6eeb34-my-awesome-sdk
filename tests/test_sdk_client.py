import io
import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.core import BinaryResponse
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_update_201_success_all_params():
    """Tests a POST request to the /sdk/update endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : str

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
    response = client.sdk.update(
        config=io.BytesIO(b"123"),
        prev_sdk_git=io.BytesIO(b"123"),
        prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        sdk_version="major",
        allow_lint_errors=True,
        api_version="latest",
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_201_success_all_params():
    """Tests a POST request to the /sdk/update endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : str

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
    response = await client.sdk.update(
        config=io.BytesIO(b"123"),
        prev_sdk_git=io.BytesIO(b"123"),
        prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        sdk_version="major",
        allow_lint_errors=True,
        api_version="latest",
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_generate_201_success_all_params():
    """Tests a POST request to the /sdk endpoint.

    Operation: generate
    Test Case ID: success_all_params
    Expected Status: 201
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
    response = client.sdk.generate(
        config=io.BytesIO(b"123"),
        language="csharp",
        allow_lint_errors=True,
        api_version="latest",
        github_actions=True,
        sdk_version="0.1.0",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_generate_201_success_all_params():
    """Tests a POST request to the /sdk endpoint.

    Operation: generate
    Test Case ID: success_all_params
    Expected Status: 201
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
    response = await client.sdk.generate(
        config=io.BytesIO(b"123"),
        language="csharp",
        allow_lint_errors=True,
        api_version="latest",
        github_actions=True,
        sdk_version="0.1.0",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_list_200_success_required_only():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = client.sdk.list()
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = await client.sdk.list()
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = client.sdk.list(api_name="my-project", successful=True)
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /sdk endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.SdkGeneration]

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
    response = await client.sdk.list(api_name="my-project", successful=True)
    try:
        pydantic.TypeAdapter(typing.List[models.SdkGeneration]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
