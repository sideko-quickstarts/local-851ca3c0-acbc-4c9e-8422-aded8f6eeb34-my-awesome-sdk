
### Delete a specific Documentation Project <a name="delete"></a>



**API Endpoint**: `DELETE /doc_project/{doc_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.delete(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.delete(doc_name="my-project")

```

### List Documentation Projects <a name="list"></a>



**API Endpoint**: `GET /doc_project`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.list()

```

#### Response

##### Type
List of [DocProject](/local_api_21_py/types/models/doc_project.py)

##### Example
`[{"created_at": "1970-01-01T00:00:00", "current_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "domains": {"preview": "string", "production": "string"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "logos": {"dark": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "favicon": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "light": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}}, "name": "string", "settings": {"action_button": {"enabled": True, "label": "string", "url": "http://www.example.com"}, "metadata": {"description": "string", "title": "string"}}}]`

### Get a specific Documentation Project <a name="get"></a>



**API Endpoint**: `GET /doc_project/{doc_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.get(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.get(doc_name="my-project")

```

#### Response

##### Type
[DocProject](/local_api_21_py/types/models/doc_project.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "current_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "domains": {"preview": "string", "production": "string"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "logos": {"dark": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "favicon": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "light": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}}, "name": "string", "settings": {"action_button": {"enabled": True, "label": "string", "url": "http://www.example.com"}, "metadata": {"description": "string", "title": "string"}}}`

### A simple check to see if the requesting user has access to the preview doc project <a name="check_preview"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/preview`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `pathname` | ✗ | relative path within docgen site requesting view permissions | `"%2Freferences%my-api%2Fmy-get-documentation"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.check_preview(
    doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.check_preview(
    doc_name="my-project", pathname="%2Freferences%my-api%2Fmy-get-documentation"
)

```

### Update an existing Documentation Project <a name="patch"></a>



**API Endpoint**: `PATCH /doc_project/{doc_name}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
| `logos` | ✗ |  | `{}` |
| `name` | ✗ |  | `"my-company-docs"` |
| `settings` | ✗ |  | `{}` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.patch(doc_name="my-project", name="my-company-docs")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.patch(doc_name="my-project", name="my-company-docs")

```

#### Response

##### Type
[DocProject](/local_api_21_py/types/models/doc_project.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "current_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "domains": {"preview": "string", "production": "string"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "logos": {"dark": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "favicon": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "light": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}}, "name": "string", "settings": {"action_button": {"enabled": True, "label": "string", "url": "http://www.example.com"}, "metadata": {"description": "string", "title": "string"}}}`

### Create a new Documentation Project <a name="create"></a>



**API Endpoint**: `POST /doc_project`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"my-company-docs"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.create(name="my-company-docs")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.create(name="my-company-docs")

```

#### Response

##### Type
[DocProject](/local_api_21_py/types/models/doc_project.py)

##### Example
`{"created_at": "1970-01-01T00:00:00", "current_version": {"created_at": "1970-01-01T00:00:00", "doc_project_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "status": "Draft", "version": 1}, "domains": {"preview": "string", "production": "string"}, "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "logos": {"dark": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "favicon": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}, "light": {"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}}, "name": "string", "settings": {"action_button": {"enabled": True, "label": "string", "url": "http://www.example.com"}, "metadata": {"description": "string", "title": "string"}}}`
