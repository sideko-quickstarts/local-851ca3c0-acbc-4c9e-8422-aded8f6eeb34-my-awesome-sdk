
### Delete role and all associated permissions <a name="delete"></a>



**API Endpoint**: `DELETE /role/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.role.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.role.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### List roles <a name="list"></a>



**API Endpoint**: `GET /role`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `object_id` | ✗ | filter roles by object id | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `object_type` | ✗ |  | `"api_project"` |
| `user_id` | ✗ | filter roles by user id | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.role.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.role.list()

```

#### Response

##### Type
List of [Role](/local_api_21_py/types/models/role.py)

##### Example
`[{"definition": {"actions": ["api_project_delete"], "display_name": "Org Admin", "id": "ApiProjectAdmin"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "object_type": "api_project", "user": {"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string"}}]`

### Create a new role <a name="create"></a>



**API Endpoint**: `POST /role`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `object_id` | ✓ | The unique identifier of the Sideko object | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `object_type` | ✓ |  | `"api_project"` |
| `role_definition_id` | ✓ |  | `"ApiProjectAdmin"` |
| `user_id` | ✓ | unique identifier for the user that the role will be granted to | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.role.create(
    object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    object_type="api_project",
    role_definition_id="ApiProjectAdmin",
    user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.role.create(
    object_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    object_type="api_project",
    role_definition_id="ApiProjectAdmin",
    user_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Response

##### Type
[Role](/local_api_21_py/types/models/role.py)

##### Example
`{"definition": {"actions": ["api_project_delete"], "display_name": "Org Admin", "id": "ApiProjectAdmin"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "object_type": "api_project", "user": {"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string"}}`
