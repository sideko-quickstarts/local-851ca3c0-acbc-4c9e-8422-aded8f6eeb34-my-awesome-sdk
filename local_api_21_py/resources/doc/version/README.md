
### List versions of a specific Documentation Project <a name="list"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/version`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.list(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.list(doc_name="my-project")

```

#### Response

##### Type
List of [DocVersion](/local_api_21_py/types/models/doc_version.py)

##### Example
`[{"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}]`

### Get a specific version of an Documentation Project <a name="get"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}`

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
res = client.doc.version.get(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.get(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
[DocVersion](/local_api_21_py/types/models/doc_version.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}`
