
### Deletes the api group and all its links <a name="delete"></a>



**API Endpoint**: `DELETE /api_link_group/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.group.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.group.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### List API groups for doc version <a name="list"></a>



**API Endpoint**: `GET /api_link_group`

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
res = client.api_link.group.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.group.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
List of [ApiLinkGroup](/local_api_21_py/types/models/api_link_group.py)

##### Example
`[{"doc_version_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string", "order": 123, "slug": "string"}]`

### Updates API link group <a name="patch"></a>



**API Endpoint**: `PATCH /api_link_group/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `nav_label` | ✗ |  | `"string"` |
| `slug` | ✗ |  | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.group.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.group.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Response

##### Type
[ApiLinkGroup](/local_api_21_py/types/models/api_link_group.py)

##### Example
`{"doc_version_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string", "order": 123, "slug": "string"}`

### Create API group to organize API links <a name="create"></a>



**API Endpoint**: `POST /api_link_group`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_version_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `nav_label` | ✓ |  | `"string"` |
| `slug` | ✓ |  | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.api_link.group.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    slug="string",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.api_link.group.create(
    doc_version_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    nav_label="string",
    slug="string",
)

```

#### Response

##### Type
[ApiLinkGroup](/local_api_21_py/types/models/api_link_group.py)

##### Example
`{"doc_version_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string", "order": 123, "slug": "string"}`
