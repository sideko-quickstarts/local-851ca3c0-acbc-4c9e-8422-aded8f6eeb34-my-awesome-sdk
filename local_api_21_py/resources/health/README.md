
### Health Check <a name="check"></a>



**API Endpoint**: `GET /_health`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.health.check()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.health.check()

```

#### Response

##### Type
[HealthCheckResponse](/local_api_21_py/types/models/health_check_response.py)

##### Example
`{"ok": True}`

### Ping Check <a name="ping"></a>



**API Endpoint**: `GET /_ping`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.health.ping()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.health.ping()

```

#### Response

##### Type
[HealthPingResponse](/local_api_21_py/types/models/health_ping_response.py)

##### Example
`{"ok": True}`
