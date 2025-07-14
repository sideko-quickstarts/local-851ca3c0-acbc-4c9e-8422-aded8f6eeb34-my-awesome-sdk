
### Delete an API <a name="delete"></a>



**API Endpoint**: `DELETE /api/{api_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.delete(api_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.delete(api_name="my-project")

```

### List your APIs <a name="list"></a>



**API Endpoint**: `GET /api`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.list()

```

#### Response

##### Type
List of [Api](/local_api_21_py/types/models/api.py)

##### Example
`[{"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}]`

### Get one API <a name="get"></a>



**API Endpoint**: `GET /api/{api_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.get(api_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.get(api_name="my-project")

```

#### Response

##### Type
[Api](/local_api_21_py/types/models/api.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}`

### Update an existing API <a name="patch"></a>



**API Endpoint**: `PATCH /api/{api_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `name` | ✗ |  | `"my-new-api-name"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.patch(api_name="my-project", name="my-new-api-name")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.patch(api_name="my-project", name="my-new-api-name")

```

#### Response

##### Type
[Api](/local_api_21_py/types/models/api.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}`

### Create a new API <a name="create"></a>



**API Endpoint**: `POST /api`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"my-api-spec"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.create(name="my-api-spec")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.create(name="my-api-spec")

```

#### Response

##### Type
[Api](/local_api_21_py/types/models/api.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}`

### Create an API with an initial version <a name="init"></a>



**API Endpoint**: `POST /api/init`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"my-api-spec"` |
| `openapi` | ✓ | An OpenAPI specification in YAML or JSON | `open("uploads/openapi.yaml", "rb")` |
| `version` | ✓ |  | `"major"` |
| `allow_lint_errors` | ✗ | Allow API spec to be created even if it has linting errors | `True` |
| `mock_server_enabled` | ✗ | Enable a public mock server requests for this API Specification | `True` |
| `notes` | ✗ | Text field to add any notes (comments, changelog, etc.) relevant to the version in html format | `"<p>This version includes a number of excellent improvements</p>"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.init(
    name="my-api-spec",
    openapi=open("uploads/openapi.yaml", "rb"),
    version="major",
    notes="<p>This version includes a number of excellent improvements</p>",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.init(
    name="my-api-spec",
    openapi=open("uploads/openapi.yaml", "rb"),
    version="major",
    notes="<p>This version includes a number of excellent improvements</p>",
)

```

#### Response

##### Type
[ApiSpec](/local_api_21_py/types/models/api_spec.py)

##### Example
`{"api": {"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}, "created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "mock_server": {"enabled": True, "url": "http://www.example.com"}, "notes": "<p>This version includes a number of excellent improvements</p>", "version": "string"}`
