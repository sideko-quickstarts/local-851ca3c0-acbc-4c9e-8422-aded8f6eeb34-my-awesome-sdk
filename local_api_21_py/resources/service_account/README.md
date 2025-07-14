
### Delete a service account <a name="delete"></a>



**API Endpoint**: `DELETE /service_account/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | service account id | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.service_account.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.service_account.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### List all service accounts in organization <a name="list"></a>



**API Endpoint**: `GET /service_account`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.service_account.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.service_account.list()

```

#### Response

##### Type
List of [User](/local_api_21_py/types/models/user.py)

##### Example
`[{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string"}]`

### Get service account by the ID <a name="get"></a>



**API Endpoint**: `GET /service_account/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | service account id | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.service_account.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.service_account.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Response

##### Type
[User](/local_api_21_py/types/models/user.py)

##### Example
`{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string"}`

### Create a new service account with a set of project permissions <a name="create"></a>



**API Endpoint**: `POST /service_account`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"Documentation Publisher Service Account"` |
| `object_roles` | ✓ |  | `[{"object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "object_type": "api_project", "role_definition_id": "ApiProjectAdmin"}]` |
| `expiration` | ✗ | UTC datetime when the service account key should expire (ISO 8601 format without timezone), key never expires expiration is not specified | `"2025-01-01T00:00:00"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.service_account.create(
    name="Documentation Publisher Service Account",
    object_roles=[
        {
            "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "object_type": "api_project",
            "role_definition_id": "ApiProjectAdmin",
        }
    ],
    expiration="2025-01-01T00:00:00",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.service_account.create(
    name="Documentation Publisher Service Account",
    object_roles=[
        {
            "object_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "object_type": "api_project",
            "role_definition_id": "ApiProjectAdmin",
        }
    ],
    expiration="2025-01-01T00:00:00",
)

```

#### Response

##### Type
[UserApiKey](/local_api_21_py/types/models/user_api_key.py)

##### Example
`{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string", "api_key": "sideko_live_abc123"}`
