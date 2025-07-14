
### Exchange one-time auth key for api key <a name="exchange_code"></a>



**API Endpoint**: `GET /auth/exchange_key`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `code` | ✓ |  | `"string"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.auth.exchange_code(code="string")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.auth.exchange_code(code="string")

```

#### Response

##### Type
[UserApiKey](/local_api_21_py/types/models/user_api_key.py)

##### Example
`{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string", "api_key": "sideko_live_abc123"}`
