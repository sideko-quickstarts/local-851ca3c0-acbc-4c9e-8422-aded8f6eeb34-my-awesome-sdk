
### List deployments for a specific documentation project <a name="list"></a>

Retrieves all deployments for a doc project

**API Endpoint**: `GET /doc_project/{doc_name}/deployment`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `limit` | ✗ |  | `123` |
| `target` | ✗ |  | `"Preview"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.deployment.list(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.deployment.list(doc_name="my-project")

```

#### Response

##### Type
List of [Deployment](/local_api_21_py/types/models/deployment.py)

##### Example
`[{"created_at": "1970-01-01T00:00:00", "current_preview": True, "current_prod": True, "doc_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "id": "string", "metadata": {}, "status": "Building", "target": "Preview"}]`

### Get a specific deployment for a specific documentation project <a name="get"></a>

Retrieves single deployment

**API Endpoint**: `GET /doc_project/{doc_name}/deployment/{deployment_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `deployment_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.deployment.get(
    deployment_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", doc_name="my-project"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.deployment.get(
    deployment_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", doc_name="my-project"
)

```

#### Response

##### Type
[Deployment](/local_api_21_py/types/models/deployment.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "current_preview": True, "current_prod": True, "doc_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "id": "string", "metadata": {}, "status": "Building", "target": "Preview"}`

### Deploy a new generated version of documentation with linked guides & APIs <a name="trigger"></a>

Deploys a new generated version of documentation with linked guides & APIs

**API Endpoint**: `POST /doc_project/{doc_name}/deployment`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `target` | ✓ |  | `"Preview"` |
| `doc_version_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.deployment.trigger(doc_name="my-project", target="Preview")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.deployment.trigger(doc_name="my-project", target="Preview")

```

#### Response

##### Type
[Deployment](/local_api_21_py/types/models/deployment.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "current_preview": True, "current_prod": True, "doc_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "id": "string", "metadata": {}, "status": "Building", "target": "Preview"}`
