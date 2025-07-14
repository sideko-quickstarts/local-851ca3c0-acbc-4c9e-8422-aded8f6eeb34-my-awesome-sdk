
### Initialize an SDK configuration with all defaults applied <a name="init"></a>

Creates a sdk config with default configurations for the api/api version

**API Endpoint**: `POST /sdk/config/init`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✓ |  | `"my-project"` |
| `api_version` | ✗ |  | `"latest"` |
| `default_module_structure` | ✗ |  | `"flat"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.config.init(api_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.config.init(api_name="my-project")

```

### Sync an SDK configuration with the latest state of the API <a name="sync"></a>

Updates provided config with missing default configurations for the api version

**API Endpoint**: `POST /sdk/config/sync`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `config` | ✓ |  | `open("uploads/config.yaml", "rb")` |
| `api_version` | ✗ |  | `"latest"` |
| `openapi` | ✗ | Use api_version in typical use. If this field is supplied, the configuration sync will match the spec rather than any API that lives in Sideko. | `open("uploads/openapi.yaml", "rb")` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.config.sync(
    config=open("uploads/config.yaml", "rb"), openapi=open("uploads/openapi.yaml", "rb")
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.config.sync(
    config=open("uploads/config.yaml", "rb"), openapi=open("uploads/openapi.yaml", "rb")
)

```
