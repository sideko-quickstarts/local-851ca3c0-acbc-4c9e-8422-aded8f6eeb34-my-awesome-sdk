import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_create_password_200_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/password endpoint.

    Operation: create_password
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DocPreviewPassword

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
    response = client.doc.preview.create_password(
        doc_name="my-project", name="My customer preview"
    )
    try:
        pydantic.TypeAdapter(models.DocPreviewPassword).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_password_200_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/password endpoint.

    Operation: create_password
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DocPreviewPassword

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
    response = await client.doc.preview.create_password(
        doc_name="my-project", name="My customer preview"
    )
    try:
        pydantic.TypeAdapter(models.DocPreviewPassword).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_passwords_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/password endpoint.

    Operation: list_passwords
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.DocPreviewPassword]

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
    response = client.doc.preview.list_passwords(doc_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.DocPreviewPassword]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_passwords_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/password endpoint.

    Operation: list_passwords
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.DocPreviewPassword]

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
    response = await client.doc.preview.list_passwords(doc_name="my-project")
    try:
        pydantic.TypeAdapter(typing.List[models.DocPreviewPassword]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_password_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name}/password endpoint.

    Operation: delete_password
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
    response = client.doc.preview.delete_password(
        doc_name="my-project", name="My customer preview"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_password_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name}/password endpoint.

    Operation: delete_password
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
    response = await client.doc.preview.delete_password(
        doc_name="my-project", name="My customer preview"
    )
    assert response is None
