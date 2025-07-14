
# Sideko REST API Python SDK

## Overview
The Sideko API unlocks features including generating SDKs, setting up API Specifications with mock servers, creating documentation projects with generated API references and custom pages, managing roles and permissions, and more.

#### Synchronous Client

```python
from local_api_21_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
```

#### Asynchronous Client

```python
from local_api_21_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"), api_key_1=getenv("API_KEY"))
```

## Module Documentation and Snippets

### [api](local_api_21_py/resources/api/README.md)

* [create](local_api_21_py/resources/api/README.md#create) - Create a new API
* [delete](local_api_21_py/resources/api/README.md#delete) - Delete an API
* [get](local_api_21_py/resources/api/README.md#get) - Get one API
* [init](local_api_21_py/resources/api/README.md#init) - Create an API with an initial version
* [list](local_api_21_py/resources/api/README.md#list) - List your APIs
* [patch](local_api_21_py/resources/api/README.md#patch) - Update an existing API

### [api.spec](local_api_21_py/resources/api/spec/README.md)

* [create](local_api_21_py/resources/api/spec/README.md#create) - Add a new API specification
* [delete](local_api_21_py/resources/api/spec/README.md#delete) - Delete an API Specification and it's associated metadata
* [get](local_api_21_py/resources/api/spec/README.md#get) - Get API specification metadata
* [get_openapi](local_api_21_py/resources/api/spec/README.md#get_openapi) - Get OpenAPI specification
* [get_stats](local_api_21_py/resources/api/spec/README.md#get_stats) - Get Stats about the specification
* [list](local_api_21_py/resources/api/spec/README.md#list) - List specs of a collection
* [patch](local_api_21_py/resources/api/spec/README.md#patch) - Update an API Specification and/or metadata

### [api_link](local_api_21_py/resources/api_link/README.md)

* [create](local_api_21_py/resources/api_link/README.md#create) - Links API Version to Documentation project version with a specified update policy
* [delete](local_api_21_py/resources/api_link/README.md#delete) - Removes an API link
* [get](local_api_21_py/resources/api_link/README.md#get) - Retrieve single API link
* [list](local_api_21_py/resources/api_link/README.md#list) - List API links for doc version
* [patch](local_api_21_py/resources/api_link/README.md#patch) - Updates an API link
* [reorder](local_api_21_py/resources/api_link/README.md#reorder) - Reorder API links and groups

### [api_link.group](local_api_21_py/resources/api_link/group/README.md)

* [create](local_api_21_py/resources/api_link/group/README.md#create) - Create API group to organize API links
* [delete](local_api_21_py/resources/api_link/group/README.md#delete) - Deletes the api group and all its links
* [list](local_api_21_py/resources/api_link/group/README.md#list) - List API groups for doc version
* [patch](local_api_21_py/resources/api_link/group/README.md#patch) - Updates API link group

### [asset](local_api_21_py/resources/asset/README.md)

* [create](local_api_21_py/resources/asset/README.md#create) - Upload Assets
* [delete](local_api_21_py/resources/asset/README.md#delete) - Delete Asset
* [list](local_api_21_py/resources/asset/README.md#list) - List Assets
* [patch](local_api_21_py/resources/asset/README.md#patch) - Update Asset

### [auth](local_api_21_py/resources/auth/README.md)

* [exchange_code](local_api_21_py/resources/auth/README.md#exchange_code) - Exchange one-time auth key for api key

### [cli](local_api_21_py/resources/cli/README.md)

* [check_updates](local_api_21_py/resources/cli/README.md#check_updates) - Checks if current CLI has updates

### [doc](local_api_21_py/resources/doc/README.md)

* [check_preview](local_api_21_py/resources/doc/README.md#check_preview) - A simple check to see if the requesting user has access to the preview doc project
* [create](local_api_21_py/resources/doc/README.md#create) - Create a new Documentation Project
* [delete](local_api_21_py/resources/doc/README.md#delete) - Delete a specific Documentation Project
* [get](local_api_21_py/resources/doc/README.md#get) - Get a specific Documentation Project
* [list](local_api_21_py/resources/doc/README.md#list) - List Documentation Projects
* [patch](local_api_21_py/resources/doc/README.md#patch) - Update an existing Documentation Project

### [doc.deployment](local_api_21_py/resources/doc/deployment/README.md)

* [get](local_api_21_py/resources/doc/deployment/README.md#get) - Get a specific deployment for a specific documentation project
* [list](local_api_21_py/resources/doc/deployment/README.md#list) - List deployments for a specific documentation project
* [trigger](local_api_21_py/resources/doc/deployment/README.md#trigger) - Deploy a new generated version of documentation with linked guides & APIs

### [doc.preview](local_api_21_py/resources/doc/preview/README.md)

* [create_password](local_api_21_py/resources/doc/preview/README.md#create_password) - A password generator for a documentation project preview environment
* [delete_password](local_api_21_py/resources/doc/preview/README.md#delete_password) - Deletes a preview environment password
* [list_passwords](local_api_21_py/resources/doc/preview/README.md#list_passwords) - Lists generated passwords for a documentation project preview environment

### [doc.theme](local_api_21_py/resources/doc/theme/README.md)

* [get](local_api_21_py/resources/doc/theme/README.md#get) - Get the theme attached to a documentation project
* [update](local_api_21_py/resources/doc/theme/README.md#update) - Update a document project theme

### [doc.version](local_api_21_py/resources/doc/version/README.md)

* [get](local_api_21_py/resources/doc/version/README.md#get) - Get a specific version of an Documentation Project
* [list](local_api_21_py/resources/doc/version/README.md#list) - List versions of a specific Documentation Project

### [doc.version.guide](local_api_21_py/resources/doc/version/guide/README.md)

* [create](local_api_21_py/resources/doc/version/guide/README.md#create) - Create a guide for a specific version of a documentation project
* [delete](local_api_21_py/resources/doc/version/guide/README.md#delete) - Delete a specific guide for a specific version of a documentation project
* [get](local_api_21_py/resources/doc/version/guide/README.md#get) - Get a specific guide for a specific version of a documentation project
* [get_content](local_api_21_py/resources/doc/version/guide/README.md#get_content) - Get content for a specific guide for a specific version of a documentation project
* [list](local_api_21_py/resources/doc/version/guide/README.md#list) - List guides for a specific version of a documentation project
* [patch](local_api_21_py/resources/doc/version/guide/README.md#patch) - Update a specific guide for a specific version of a documentation project
* [reorder](local_api_21_py/resources/doc/version/guide/README.md#reorder) - Reorder guides for a specific version of a documentation project

### [health](local_api_21_py/resources/health/README.md)

* [check](local_api_21_py/resources/health/README.md#check) - Health Check
* [ping](local_api_21_py/resources/health/README.md#ping) - Ping Check

### [lint](local_api_21_py/resources/lint/README.md)

* [run](local_api_21_py/resources/lint/README.md#run) - Lint an OpenAPI spec

### [org](local_api_21_py/resources/org/README.md)

* [create](local_api_21_py/resources/org/README.md#create) - Create a new organization
* [get](local_api_21_py/resources/org/README.md#get) - Get Organization

### [org.theme](local_api_21_py/resources/org/theme/README.md)

* [get](local_api_21_py/resources/org/theme/README.md#get) - Get organization theme
* [update](local_api_21_py/resources/org/theme/README.md#update) - Update organization theme

### [role](local_api_21_py/resources/role/README.md)

* [create](local_api_21_py/resources/role/README.md#create) - Create a new role
* [delete](local_api_21_py/resources/role/README.md#delete) - Delete role and all associated permissions
* [list](local_api_21_py/resources/role/README.md#list) - List roles

### [sdk](local_api_21_py/resources/sdk/README.md)

* [generate](local_api_21_py/resources/sdk/README.md#generate) - Generate a new managed SDK from a Sideko configuration file
* [list](local_api_21_py/resources/sdk/README.md#list) - List all managed SDKs
* [update](local_api_21_py/resources/sdk/README.md#update) - Update an SDK to reflect the latest state of the API

### [sdk.config](local_api_21_py/resources/sdk/config/README.md)

* [init](local_api_21_py/resources/sdk/config/README.md#init) - Initialize an SDK configuration with all defaults applied
* [sync](local_api_21_py/resources/sdk/config/README.md#sync) - Sync an SDK configuration with the latest state of the API

### [sdk.doc](local_api_21_py/resources/sdk/doc/README.md)

* [create](local_api_21_py/resources/sdk/doc/README.md#create) - Retrieve SDK documentation

### [service_account](local_api_21_py/resources/service_account/README.md)

* [create](local_api_21_py/resources/service_account/README.md#create) - Create a new service account with a set of project permissions
* [delete](local_api_21_py/resources/service_account/README.md#delete) - Delete a service account
* [get](local_api_21_py/resources/service_account/README.md#get) - Get service account by the ID
* [list](local_api_21_py/resources/service_account/README.md#list) - List all service accounts in organization

### [user](local_api_21_py/resources/user/README.md)

* [invite](local_api_21_py/resources/user/README.md#invite) - Invite a user to an organization with a specific role

### [user.me](local_api_21_py/resources/user/me/README.md)

* [get](local_api_21_py/resources/user/me/README.md#get) - Get current user profile
* [get_key](local_api_21_py/resources/user/me/README.md#get_key) - Get API key for the current user

### [webhook](local_api_21_py/resources/webhook/README.md)

* [vercel](local_api_21_py/resources/webhook/README.md#vercel) - webhooks sent to sideko by vercel

<!-- MODULE DOCS END -->
