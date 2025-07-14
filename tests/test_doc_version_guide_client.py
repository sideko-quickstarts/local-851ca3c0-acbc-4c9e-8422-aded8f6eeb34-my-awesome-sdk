import pydantic
import pytest
import typing

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment
from local_api_21_py.types import models


def test_reorder_200_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/version/{doc_version}/guide/reorder endpoint.

    Operation: reorder
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.GuideWithChildren]

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
    response = client.doc.version.guide.reorder(
        data=[
            {
                "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "order": 123,
                "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            }
        ],
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(typing.List[models.GuideWithChildren]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_reorder_200_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/version/{doc_version}/guide/reorder endpoint.

    Operation: reorder
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.GuideWithChildren]

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
    response = await client.doc.version.guide.reorder(
        data=[
            {
                "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
                "order": 123,
                "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            }
        ],
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(typing.List[models.GuideWithChildren]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_201_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/version/{doc_version}/guide endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Guide

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
    response = client.doc.version.guide.create(
        content="string",
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        is_parent=True,
        nav_label="string",
        slug="string",
        icon="house",
        next_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        parent_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        prev_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        table_of_contents=True,
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /doc_project/{doc_name}/version/{doc_version}/guide endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Guide

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
    response = await client.doc.version.guide.create(
        content="string",
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        is_parent=True,
        nav_label="string",
        slug="string",
        icon="house",
        next_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        parent_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        prev_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        table_of_contents=True,
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_patch_200_success_all_params():
    """Tests a PATCH request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Guide

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
    response = client.doc.version.guide.patch(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        content="string",
        icon="house",
        nav_label="string",
        next_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        prev_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        slug="string",
        table_of_contents=True,
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_patch_200_success_all_params():
    """Tests a PATCH request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

    Operation: patch
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Guide

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
    response = await client.doc.version.guide.patch(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        content="string",
        icon="house",
        nav_label="string",
        next_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        prev_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        slug="string",
        table_of_contents=True,
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_content_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}/content endpoint.

    Operation: get_content
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.GuideContent

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
    response = client.doc.version.guide.get_content(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.GuideContent).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_content_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}/content endpoint.

    Operation: get_content
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.GuideContent

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
    response = await client.doc.version.guide.get_content(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.GuideContent).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Guide

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
    response = client.doc.version.guide.get(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Guide

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
    response = await client.doc.version.guide.get(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    try:
        pydantic.TypeAdapter(models.Guide).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.List[models.GuideWithChildren]

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
    response = client.doc.version.guide.list(
        doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.GuideWithChildren]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /doc_project/{doc_name}/version/{doc_version}/guide endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.List[models.GuideWithChildren]

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
    response = await client.doc.version.guide.list(
        doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(typing.List[models.GuideWithChildren]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

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
    response = client.doc.version.guide.delete(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_204_success_all_params():
    """Tests a DELETE request to the /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id} endpoint.

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
    response = await client.doc.version.guide.delete(
        doc_name="my-project",
        doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    )
    assert response is None
