
### Checks if current CLI has updates <a name="check_updates"></a>



**API Endpoint**: `GET /cli/updates/{cli_version}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `cli_version` | ✓ | semver of running cli | `"0.1.0"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.cli.check_updates(cli_version="0.1.0")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.cli.check_updates(cli_version="0.1.0")

```

#### Response

##### Type
List of [CliUpdate](/local_api_21_py/types/models/cli_update.py)

##### Example
`[{"message": "Requires update to 0.2.0 for security patch", "severity": "info"}]`
