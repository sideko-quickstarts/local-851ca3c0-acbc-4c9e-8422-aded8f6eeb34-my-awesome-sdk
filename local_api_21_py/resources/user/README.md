
### Invite a user to an organization with a specific role <a name="invite"></a>



**API Endpoint**: `POST /user/invite`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `email` | ✓ |  | `"user@example.com"` |
| `role_definition_id` | ✓ |  | `"ApiProjectAdmin"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.user.invite(email="user@example.com", role_definition_id="ApiProjectAdmin")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.user.invite(
    email="user@example.com", role_definition_id="ApiProjectAdmin"
)

```
