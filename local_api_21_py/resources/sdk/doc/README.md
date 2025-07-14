
### Retrieve SDK documentation <a name="create"></a>

Get documentation for a specific SDK

**API Endpoint**: `POST /sdk/{sdk_id}/doc`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `sdk_id` | ✓ | The SDK ID to get documentation for | `"h1jasdf123"` |
| `modules_filter` | ✗ | Optional array of module names to filter the response | `["user.admin"]` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.doc.create(sdk_id="h1jasdf123", modules_filter=["user.admin"])

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.doc.create(sdk_id="h1jasdf123", modules_filter=["user.admin"])

```

#### Response

##### Type
[SdkDocResponse](/local_api_21_py/types/models/sdk_doc_response.py)

##### Example
`{"client_init": "def x", "modules": [{"content": "## Markdown SDK Docs", "module": "user.admin"}]}`
