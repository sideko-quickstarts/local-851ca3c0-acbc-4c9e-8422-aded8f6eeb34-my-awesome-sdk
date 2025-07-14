
### Deletes a preview environment password <a name="delete_password"></a>



**API Endpoint**: `DELETE /doc_project/{doc_name}/password`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `name` | ✓ |  | `"My customer preview"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.preview.delete_password(
    doc_name="my-project", name="My customer preview"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.preview.delete_password(
    doc_name="my-project", name="My customer preview"
)

```

### Lists generated passwords for a documentation project preview environment <a name="list_passwords"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/password`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.preview.list_passwords(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.preview.list_passwords(doc_name="my-project")

```

#### Response

##### Type
List of [DocPreviewPassword](/local_api_21_py/types/models/doc_preview_password.py)

##### Example
`[{"name": "My customer preview", "password": "asdfj12124inklwgas123"}]`

### A password generator for a documentation project preview environment <a name="create_password"></a>



**API Endpoint**: `POST /doc_project/{doc_name}/password`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `name` | ✓ |  | `"My customer preview"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.preview.create_password(
    doc_name="my-project", name="My customer preview"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.preview.create_password(
    doc_name="my-project", name="My customer preview"
)

```

#### Response

##### Type
[DocPreviewPassword](/local_api_21_py/types/models/doc_preview_password.py)

##### Example
`{"name": "My customer preview", "password": "asdfj12124inklwgas123"}`
