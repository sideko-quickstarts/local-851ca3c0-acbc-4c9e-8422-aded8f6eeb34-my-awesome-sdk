
### Get the theme attached to a documentation project <a name="get"></a>



**API Endpoint**: `GET /doc_project/{doc_name}/theme`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = client.doc.theme.get(doc_name="my-project")

```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
res = await client.doc.theme.get(doc_name="my-project")

```

#### Response

##### Type
[Theme](/local_api_21_py/types/models/theme.py)

##### Example
`{"owner": "default", "values": {"api_reference_group_variant": "grouped", "dark_active_button_bg_color": "#FFFFFF", "dark_active_button_text_color": "#FFFFFF", "dark_bg_color": "#FFFFFF", "dark_navbar_color": "#FFFFFF", "dark_navbar_text_color": "#FFFFFF", "light_active_button_bg_color": "#FFFFFF", "light_active_button_text_color": "#FFFFFF", "light_bg_color": "#FFFFFF", "light_navbar_color": "#FFFFFF", "light_navbar_text_color": "#FFFFFF"}}`

### Update a document project theme <a name="update"></a>



**API Endpoint**: `PUT /doc_project/{doc_name}/theme`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `doc_name` | ✓ |  | `"my-project"` |
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
res = client.doc.theme.update(
    doc_name="my-project",
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
res = await client.doc.theme.update(
    doc_name="my-project",
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
