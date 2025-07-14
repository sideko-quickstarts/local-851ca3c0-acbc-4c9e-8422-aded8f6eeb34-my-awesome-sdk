
### Get organization theme <a name="get"></a>

Retrieves the documentation project theme configured at the organization level

**API Endpoint**: `GET /organization/theme`

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.org.theme.get()

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.org.theme.get()

```

#### Response

##### Type
[Theme](/local_api_21_py/types/models/theme.py)

##### Example
`{"owner": "default", "values": {"api_reference_group_variant": "grouped", "dark_active_button_bg_color": "#FFFFFF", "dark_active_button_text_color": "#FFFFFF", "dark_bg_color": "#FFFFFF", "dark_navbar_color": "#FFFFFF", "dark_navbar_text_color": "#FFFFFF", "light_active_button_bg_color": "#FFFFFF", "light_active_button_text_color": "#FFFFFF", "light_bg_color": "#FFFFFF", "light_navbar_color": "#FFFFFF", "light_navbar_text_color": "#FFFFFF"}}`

### Update organization theme <a name="update"></a>

Update documentation project theme configured at the organization level

**API Endpoint**: `PUT /organization/theme`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `api_reference_group_variant` | ✗ | set a group variant to collapse all of references under one dropdown in the sidebar | `"grouped"` |
| `dark_active_button_bg_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `dark_active_button_text_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `dark_bg_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `dark_navbar_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `dark_navbar_text_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `light_active_button_bg_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `light_active_button_text_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `light_bg_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `light_navbar_color` | ✗ | in HEX format | `"#FFFFFF"` |
| `light_navbar_text_color` | ✗ | in HEX format | `"#FFFFFF"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.org.theme.update(
    api_reference_group_variant="grouped",
    dark_active_button_bg_color="#FFFFFF",
    dark_active_button_text_color="#FFFFFF",
    dark_bg_color="#FFFFFF",
    dark_navbar_color="#FFFFFF",
    dark_navbar_text_color="#FFFFFF",
    light_active_button_bg_color="#FFFFFF",
    light_active_button_text_color="#FFFFFF",
    light_bg_color="#FFFFFF",
    light_navbar_color="#FFFFFF",
    light_navbar_text_color="#FFFFFF",
)

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.org.theme.update(
    api_reference_group_variant="grouped",
    dark_active_button_bg_color="#FFFFFF",
    dark_active_button_text_color="#FFFFFF",
    dark_bg_color="#FFFFFF",
    dark_navbar_color="#FFFFFF",
    dark_navbar_text_color="#FFFFFF",
    light_active_button_bg_color="#FFFFFF",
    light_active_button_text_color="#FFFFFF",
    light_bg_color="#FFFFFF",
    light_navbar_color="#FFFFFF",
    light_navbar_text_color="#FFFFFF",
)

```

#### Response

##### Type
[Theme](/local_api_21_py/types/models/theme.py)

##### Example
`{"owner": "default", "values": {"api_reference_group_variant": "grouped", "dark_active_button_bg_color": "#FFFFFF", "dark_active_button_text_color": "#FFFFFF", "dark_bg_color": "#FFFFFF", "dark_navbar_color": "#FFFFFF", "dark_navbar_text_color": "#FFFFFF", "light_active_button_bg_color": "#FFFFFF", "light_active_button_text_color": "#FFFFFF", "light_bg_color": "#FFFFFF", "light_navbar_color": "#FFFFFF", "light_navbar_text_color": "#FFFFFF"}}`
