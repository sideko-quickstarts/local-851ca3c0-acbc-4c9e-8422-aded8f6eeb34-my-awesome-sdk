
### Get Organization <a name="get"></a>

Retrieves the organization of the current authenticated user

**API Endpoint**: `GET /organization`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.org.get()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.org.get()

```

#### Response

##### Type
[Organization](/local_api_21_py/types/models/organization.py)

##### Example
`{"features": {"allow_sdk_cli": True, "allow_sdk_csharp": True, "allow_sdk_go": True, "allow_sdk_java": True, "allow_sdk_python": True, "allow_sdk_rust": True, "allow_sdk_tests": True, "allow_sdk_typescript": True, "max_api_projects": 123, "max_doc_projects": 123, "max_mock_servers": 123, "max_sdk_api_methods": 123, "max_service_accounts": 123, "max_teammates": 123}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "subdomain": "string"}`

### Create a new organization <a name="create"></a>



**API Endpoint**: `POST /organization`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"My Organization"` |
| `subdomain` | ✓ |  | `"my-org"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.org.create(name="My Organization", subdomain="my-org")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.org.create(name="My Organization", subdomain="my-org")

```

#### Response

##### Type
[OrganizationWithRedirect](/local_api_21_py/types/models/organization_with_redirect.py)

##### Example
`{"organization": {"features": {"allow_sdk_cli": True, "allow_sdk_csharp": True, "allow_sdk_go": True, "allow_sdk_java": True, "allow_sdk_python": True, "allow_sdk_rust": True, "allow_sdk_tests": True, "allow_sdk_typescript": True, "max_api_projects": 123, "max_doc_projects": 123, "max_mock_servers": 123, "max_sdk_api_methods": 123, "max_service_accounts": 123, "max_teammates": 123}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "subdomain": "string"}, "redirect_to": "string"}`
