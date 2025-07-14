
### Delete an API Specification and it's associated metadata <a name="delete"></a>



**API Endpoint**: `DELETE /api/{api_name}/spec/{api_version}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✓ |  | `"latest"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.delete(api_name="my-project", api_version="latest")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.delete(api_name="my-project", api_version="latest")

```

### List specs of a collection <a name="list"></a>



**API Endpoint**: `GET /api/{api_name}/spec`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.list(api_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.list(api_name="my-project")

```

#### Response

##### Type
List of [ApiSpec](/local_api_21_py/types/models/api_spec.py)

##### Example
`[{"api": {"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}, "created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "mock_server": {"enabled": True, "url": "http://www.example.com"}, "notes": "<p>This version includes a number of excellent improvements</p>", "version": "string"}]`

### Get API specification metadata <a name="get"></a>



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✓ |  | `"latest"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.get(api_name="my-project", api_version="latest")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.get(api_name="my-project", api_version="latest")

```

#### Response

##### Type
[ApiSpec](/local_api_21_py/types/models/api_spec.py)

##### Example
`{"api": {"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}, "created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "mock_server": {"enabled": True, "url": "http://www.example.com"}, "notes": "<p>This version includes a number of excellent improvements</p>", "version": "string"}`

### Get OpenAPI specification <a name="get_openapi"></a>



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}/openapi`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✓ |  | `"latest"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.get_openapi(api_name="my-project", api_version="latest")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.get_openapi(api_name="my-project", api_version="latest")

```

#### Response

##### Type
[OpenApi](/local_api_21_py/types/models/open_api.py)

##### Example
`{"extension": "json", "is_config_valid": True, "is_valid": True, "openapi": "string", "validations": [{"message": "string", "severity": "error"}]}`

### Get Stats about the specification <a name="get_stats"></a>



**API Endpoint**: `GET /api/{api_name}/spec/{api_version}/stats`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✓ |  | `"latest"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.get_stats(api_name="my-project", api_version="latest")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.get_stats(api_name="my-project", api_version="latest")

```

#### Response

##### Type
[ApiSpecStats](/local_api_21_py/types/models/api_spec_stats.py)

##### Example
`{"authenticated_methods": 123, "authentication_schemes": ["string"], "endpoints": 123, "lint_errors": {"incorrect_examples": [{"location": "request-body", "message": "the object is missing a required property", "method": "GET", "path": "/api/v1/path"}], "incorrect_paths": ["string"], "missing_operation_ids": [{"location": "request-body", "message": "the object is missing a required property", "method": "GET", "path": "/api/v1/path"}]}, "methods": 123, "public_methods": 123, "response_codes": [123]}`

### Update an API Specification and/or metadata <a name="patch"></a>



**API Endpoint**: `PATCH /api/{api_name}/spec/{api_version}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✓ |  | `"latest"` |
| `allow_lint_errors` | ✗ | Allow API spec to be updated with a new OpenAPI spec even if it has linting errors | `True` |
| `mock_server_enabled` | ✗ | Enable a public mock server requests for this API Specification | `True` |
| `notes` | ✗ | Text field to add any notes (comments, changelog, etc.) relevant to the version in html format | `"<p>This version includes a number of excellent improvements</p>"` |
| `openapi` | ✗ | An OpenAPI specification in YAML or JSON | `open("uploads/openapi.yaml", "rb")` |
| `version` | ✗ | Semantic Version of the API | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api.spec.patch(
    api_name="my-project",
    api_version="latest",
    notes="<p>This version includes a number of excellent improvements</p>",
    openapi=open("uploads/openapi.yaml", "rb"),
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api.spec.patch(
    api_name="my-project",
    api_version="latest",
    notes="<p>This version includes a number of excellent improvements</p>",
    openapi=open("uploads/openapi.yaml", "rb"),
)

```

#### Response

##### Type
[ApiSpec](/local_api_21_py/types/models/api_spec.py)

##### Example
`{"api": {"created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "my-api-spec-name", "version_count": 10}, "created_at": "1970-01-01T00:00:00", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "mock_server": {"enabled": True, "url": "http://www.example.com"}, "notes": "<p>This version includes a number of excellent improvements</p>", "version": "string"}`

### Add a new API specification <a name="create"></a>



**API Endpoint**: `POST /api/{api_name}/spec`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
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
res = client.api.spec.create(
    api_name="my-project",
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
res = await client.api.spec.create(
    api_name="my-project",
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
