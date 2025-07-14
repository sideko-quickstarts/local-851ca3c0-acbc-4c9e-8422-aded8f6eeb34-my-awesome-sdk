
### Delete a specific guide for a specific version of a documentation project <a name="delete"></a>



**API Endpoint**: `DELETE /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `guide_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.delete(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.delete(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

### List guides for a specific version of a documentation project <a name="list"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide`

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
res = client.doc.version.guide.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.list(
    doc_name="my-project", doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
List of [GuideWithChildren](/local_api_21_py/types/models/guide_with_children.py)

##### Example
`[]`

### Get a specific guide for a specific version of a documentation project <a name="get"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `guide_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.get(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.get(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Response

##### Type
[Guide](/local_api_21_py/types/models/guide.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "icon": "house", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_parent": True, "nav_label": "string", "order": 123, "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "slug": "string", "table_of_contents": True, "default_next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "default_prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}}`

### Get content for a specific guide for a specific version of a documentation project <a name="get_content"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}/content`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `guide_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.get_content(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.get_content(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Response

##### Type
[GuideContent](/local_api_21_py/types/models/guide_content.py)

##### Example
`{"content": "string"}`

### Update a specific guide for a specific version of a documentation project <a name="patch"></a>



**API Endpoint**: `PATCH /doc_project/{doc_name}/version/{doc_version}/guide/{guide_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `guide_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `content` | ✗ |  | `"string"` |
| `icon` | ✗ |  | `"house"` |
| `nav_label` | ✗ | the label that shows on the navbar for this guide | `"string"` |
| `next_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `prev_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `slug` | ✗ | the url slug (route) for this guide. Must be one word. Use - for spaces. optimize the name for SEO | `"string"` |
| `table_of_contents` | ✗ |  | `True` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.patch(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.patch(
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    guide_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Response

##### Type
[Guide](/local_api_21_py/types/models/guide.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "icon": "house", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_parent": True, "nav_label": "string", "order": 123, "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "slug": "string", "table_of_contents": True, "default_next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "default_prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}}`

### Create a guide for a specific version of a documentation project <a name="create"></a>



**API Endpoint**: `POST /doc_project/{doc_name}/version/{doc_version}/guide`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `content` | ✓ |  | `"string"` |
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `is_parent` | ✓ |  | `True` |
| `nav_label` | ✓ | the label that shows on the navbar for this guide | `"string"` |
| `slug` | ✓ | the url slug (route) for this guide. Must be one word. Use - for spaces. optimize the name for SEO | `"string"` |
| `icon` | ✗ |  | `"house"` |
| `next_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `parent_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `prev_id` | ✗ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `table_of_contents` | ✗ |  | `True` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.create(
    content="string",
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    is_parent=True,
    nav_label="string",
    slug="string",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.create(
    content="string",
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    is_parent=True,
    nav_label="string",
    slug="string",
)

```

#### Response

##### Type
[Guide](/local_api_21_py/types/models/guide.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "icon": "house", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_parent": True, "nav_label": "string", "order": 123, "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "slug": "string", "table_of_contents": True, "default_next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "default_prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "next_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}, "prev_href": {"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "nav_label": "string"}}`

### Reorder guides for a specific version of a documentation project <a name="reorder"></a>



**API Endpoint**: `POST /doc_project/{doc_name}/version/{doc_version}/guide/reorder`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✓ |  | `[{"id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "order": 123, "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"}]` |
| `doc_name` | ✓ |  | `"my-project"` |
| `doc_version` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.version.guide.reorder(
    data=[
        {
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
            "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        }
    ],
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.version.guide.reorder(
    data=[
        {
            "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            "order": 123,
            "parent_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        }
    ],
    doc_name="my-project",
    doc_version="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
)

```

#### Response

##### Type
List of [GuideWithChildren](/local_api_21_py/types/models/guide_with_children.py)

##### Example
`[]`
