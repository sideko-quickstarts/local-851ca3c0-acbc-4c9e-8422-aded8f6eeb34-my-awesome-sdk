
### Get current user profile <a name="get"></a>



**API Endpoint**: `GET /user/me`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.user.me.get()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.user.me.get()

```

#### Response

##### Type
[User](/local_api_21_py/types/models/user.py)

##### Example
`{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string"}`

### Get API key for the current user <a name="get_key"></a>



**API Endpoint**: `GET /user/me/api_key`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.user.me.get_key()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.user.me.get_key()

```

#### Response

##### Type
[UserApiKey](/local_api_21_py/types/models/user_api_key.py)

##### Example
`{"avatar_url": "http://www.example.com", "created_at": "1970-01-01T00:00:00", "email": "mail@example.com", "expiration": "1970-01-01T00:00:00", "first_name": "string", "id": "3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", "is_service_account": True, "last_name": "string", "api_key": "sideko_live_abc123"}`
