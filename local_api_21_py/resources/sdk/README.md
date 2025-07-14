
### List all managed SDKs <a name="list"></a>



**API Endpoint**: `GET /sdk`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✗ | Filter by API name or ID (uuid) | `"my-project"` |
| `successful` | ✗ | Filter by SDK generation success | `True` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.list()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.list()

```

#### Response

##### Type
List of [SdkGeneration](/local_api_21_py/types/models/sdk_generation.py)

##### Example
`[{"api_version_id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "created_at": "1970-01-01T00:00:00", "language": "csharp", "name": "my_sdk_py", "successful": True, "version": "0.1.0"}]`

### Generate a new managed SDK from a Sideko configuration file <a name="generate"></a>



**API Endpoint**: `POST /sdk`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `config` | ✓ |  | `open("uploads/config.yaml", "rb")` |
| `language` | ✓ |  | `"csharp"` |
| `allow_lint_errors` | ✗ | force generate the SDK even if there are linting errors | `True` |
| `api_version` | ✗ |  | `"latest"` |
| `github_actions` | ✗ | include github action boilerplate for running tests and publishing the sdk | `True` |
| `sdk_version` | ✗ |  | `"0.1.0"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.generate(config=open("uploads/config.yaml", "rb"), language="csharp")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.generate(
    config=open("uploads/config.yaml", "rb"), language="csharp"
)

```

### Update an SDK to reflect the latest state of the API <a name="update"></a>



**API Endpoint**: `POST /sdk/update`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `config` | ✓ |  | `open("uploads/config.yaml", "rb")` |
| `prev_sdk_git` | ✓ | compressed .tar.gz of .git/ directory of previous SDK | `open("uploads/git.tar.gz", "rb")` |
| `prev_sdk_id` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `sdk_version` | ✓ |  | `"major"` |
| `allow_lint_errors` | ✗ | force generate the SDK even if there are linting errors | `True` |
| `api_version` | ✗ |  | `"latest"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.sdk.update(
    config=open("uploads/config.yaml", "rb"),
    prev_sdk_git=open("uploads/git.tar.gz", "rb"),
    prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    sdk_version="major",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.sdk.update(
    config=open("uploads/config.yaml", "rb"),
    prev_sdk_git=open("uploads/git.tar.gz", "rb"),
    prev_sdk_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    sdk_version="major",
)

```
