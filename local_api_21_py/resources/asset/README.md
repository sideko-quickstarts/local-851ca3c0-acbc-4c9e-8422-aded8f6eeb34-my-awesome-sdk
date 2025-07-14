
### Delete Asset <a name="delete"></a>

Delete a media asset in your organization

**API Endpoint**: `DELETE /organization/asset/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.asset.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.asset.delete(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### List Assets <a name="list"></a>

Get all media assets for an organization

**API Endpoint**: `GET /organization/asset`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✗ |  | `"string"` |
| `page` | ✗ |  | `123` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.asset.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.asset.list()

```

#### Response

##### Type
[ListAssetsPage](/local_api_21_py/types/models/list_assets_page.py)

##### Example
`{"pagination": {"page": 123, "page_count": 123, "page_limit": 123, "total_count": 123}, "results": [{"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}]}`

### Update Asset <a name="patch"></a>

Update a media asset in your organization

**API Endpoint**: `PATCH /organization/asset/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `name` | ✗ | Asset name (without any extension) | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.asset.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.asset.patch(id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Response

##### Type
[Asset](/local_api_21_py/types/models/asset.py)

##### Example
`{"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}`

### Upload Assets <a name="create"></a>

Add a media asset like logos or other media to an organization

**API Endpoint**: `POST /organization/asset`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `file` | ✓ |  | `open("uploads/file.pdf", "rb")` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.asset.create(file=open("uploads/image.png", "rb"))

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.asset.create(file=open("uploads/image.png", "rb"))

```

#### Response

##### Type
List of [Asset](/local_api_21_py/types/models/asset.py)

##### Example
`[{"extension": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "name": "string", "url": "http://www.example.com"}]`
