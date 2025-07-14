import httpx
import pytest

from local_api_21_py import AsyncClient, Client
from local_api_21_py.environment import Environment


def test_invite_202_success_all_params():
    """Tests a POST request to the /user/invite endpoint.

    Operation: invite
    Test Case ID: success_all_params
    Expected Status: 202
    Mode: Synchronous execution

    Response : httpx.Response

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
    response = client.user.invite(
        email="user@example.com", role_definition_id="ApiProjectAdmin"
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_invite_202_success_all_params():
    """Tests a POST request to the /user/invite endpoint.

    Operation: invite
    Test Case ID: success_all_params
    Expected Status: 202
    Mode: Asynchronous execution

    Response : httpx.Response

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
    response = await client.user.invite(
        email="user@example.com", role_definition_id="ApiProjectAdmin"
    )
    assert isinstance(response, httpx.Response)
