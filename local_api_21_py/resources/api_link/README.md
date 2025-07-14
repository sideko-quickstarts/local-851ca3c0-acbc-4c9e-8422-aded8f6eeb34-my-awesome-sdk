
### Removes an API link <a name="delete"></a>



**API Endpoint**: `DELETE /api_link/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### List API links for doc version <a name="list"></a>



**API Endpoint**: `GET /api_link`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
List of [ApiLink](/local_api_21_py/types/models/api_link.py)

##### Example
`[{"api_version": {"api_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "api_name": "my-api-spec", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": "1.0.0"}, "build_request_enabled": True, "created_at": "1970-01-01T00:00:00", "doc_version": {"doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "doc_project_name": "my-company-docs", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": 1}, "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "include_mock_server": True, "nav_label": "Generation API", "order": 0, "policy": "latest", "slug": "generation-api"}]`

### Retrieve single API link <a name="get"></a>



**API Endpoint**: `GET /api_link/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.get(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Response

##### Type
[ApiLink](/local_api_21_py/types/models/api_link.py)

##### Example
`{"api_version": {"api_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "api_name": "my-api-spec", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": "1.0.0"}, "build_request_enabled": True, "created_at": "1970-01-01T00:00:00", "doc_version": {"doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "doc_project_name": "my-company-docs", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": 1}, "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "include_mock_server": True, "nav_label": "Generation API", "order": 0, "policy": "latest", "slug": "generation-api"}`

### Updates an API link <a name="patch"></a>



**API Endpoint**: `PATCH /api_link/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `api_version` | ✗ | the api version can only be patched on api links with a `pinned` policy | `{"api_id": "my-api", "version": "0.1.0"}` |
| `build_request_enabled` | ✗ |  | `True` |
| `include_mock_server` | ✗ | automatically add the sideko mock server as one of the server options when building a request in the api reference (requires mock server to be enabled on the linked Api Version) | `True` |
| `nav_label` | ✗ |  | `"string"` |
| `policy` | ✗ |  | `"latest"` |
| `slug` | ✗ |  | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Response

##### Type
[ApiLink](/local_api_21_py/types/models/api_link.py)

##### Example
`{"api_version": {"api_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "api_name": "my-api-spec", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": "1.0.0"}, "build_request_enabled": True, "created_at": "1970-01-01T00:00:00", "doc_version": {"doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "doc_project_name": "my-company-docs", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": 1}, "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "include_mock_server": True, "nav_label": "Generation API", "order": 0, "policy": "latest", "slug": "generation-api"}`

### Links API Version to Documentation project version with a specified update policy <a name="create"></a>



**API Endpoint**: `POST /api_link`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_version_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `group_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `nav_label` | ✓ |  | `"string"` |
| `policy` | ✓ |  | `{"api_id": "my-api", "type_": "latest"}` |
| `slug` | ✓ |  | `"string"` |
| `build_request_enabled` | ✗ |  | `True` |
| `include_mock_server` | ✗ | automatically add the sideko mock server as one of the server options when building a request in the api reference (requires mock server to be enabled on the linked Api Version) | `True` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    policy={"api_id": "my-api", "type_": "latest"},
    slug="string",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    group_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    policy={"api_id": "my-api", "type_": "latest"},
    slug="string",
)

```

#### Response

##### Type
[ApiLink](/local_api_21_py/types/models/api_link.py)

##### Example
`{"api_version": {"api_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "api_name": "my-api-spec", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": "1.0.0"}, "build_request_enabled": True, "created_at": "1970-01-01T00:00:00", "doc_version": {"doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "doc_project_name": "my-company-docs", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "version": 1}, "group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "include_mock_server": True, "nav_label": "Generation API", "order": 0, "policy": "latest", "slug": "generation-api"}`

### Reorder API links and groups <a name="reorder"></a>



**API Endpoint**: `POST /api_link/reorder`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_version_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `groups` | ✓ |  | `[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}]` |
| `links` | ✓ |  | `[{"group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}]` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.reorder(
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

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.reorder(
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

```

#### Response

##### Type
[ApiReorder](/local_api_21_py/types/models/api_reorder.py)

##### Example
`{"doc_version_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "groups": [{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}], "links": [{"group_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123}]}`
