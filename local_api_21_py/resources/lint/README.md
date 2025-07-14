
### Lint an OpenAPI spec <a name="run"></a>



**API Endpoint**: `POST /lint`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_name` | ✗ |  | `"my-project"` |
| `api_version` | ✗ |  | `"latest"` |
| `openapi` | ✗ |  | `open("uploads/openapi.yaml", "rb")` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.lint.run(openapi=open("uploads/openapi.yaml", "rb"))

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.lint.run(openapi=open("uploads/openapi.yaml", "rb"))

```

#### Response

##### Type
[LintReport](/local_api_21_py/types/models/lint_report.py)

##### Example
`{"results": [{"category": "string", "how_to_fix": "string", "location": {"end_column": 123, "end_line": 123, "path": "string", "start_column": 123, "start_line": 123}, "message": "string", "rule": "string", "severity": "error"}], "summary": {"errors": 123, "infos": 123, "warns": 123}}`
