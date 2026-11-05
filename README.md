# name.com Core API Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fnamedotcom%2Fcore-api-python)
[![pypi](https://img.shields.io/pypi/v/namecom-core-api)](https://pypi.python.org/pypi/namecom-core-api)

Official SDK for the name.com Core API.

List endpoints are paginated: use the `page` and `perPage` query parameters.
Responses include `totalCount`, `nextPage`, and `lastPage`, and most list
endpoints also return a `Link` header with `next`/`prev`/`last` URLs.

Write endpoints that accept an idempotency key are safe to retry — reusing
the same key returns the original result instead of repeating the operation.

See https://docs.name.com for full guides and the API reference.


## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Documentation

API reference documentation is available [here](https://docs.name.com).

## Installation

```sh
pip install namecom-core-api
```

## Reference

A full reference for this library is available [here](https://github.com/namedotcom/core-api-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.hello()
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.account_info.check_account_balance()
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.domains.search(
    keyword="mydomain",
)
```

```python
from namecom_core_api import Namecom, DomainCreatePayload

client = Namecom(
    username="<username>",
    password="<password>",
)

client.domains.create_domain(
    domain=DomainCreatePayload(
        domain_name="example.com",
    ),
)
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.domains.list_domains()
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.domains.get_domain(
    domain_name="example.com",
)
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.dns.list_records(
    domain_name="domainName",
)
```

```python
from namecom_core_api import Namecom

client = Namecom(
    username="<username>",
    password="<password>",
)

client.dns.create_record(
    domain_name="domainName",
    answer="answer",
    host="host",
    type="A",
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from namecom_core_api import Namecom
from namecom_core_api.environment import NamecomEnvironment

client = Namecom(
    environment=NamecomEnvironment.SANDBOX,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from namecom_core_api import AsyncNamecom

client = AsyncNamecom(
    username="<username>",
    password="<password>",
)


async def main() -> None:
    await client.hello()


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from namecom_core_api.core.api_error import ApiError

try:
    client.hello()
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from namecom_core_api import Namecom

client = Namecom(...)
response = client.with_raw_response.hello()
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.hello(request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from namecom_core_api import Namecom

client = Namecom(..., timeout=20.0)

# Override timeout for a specific method
client.hello(request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from namecom_core_api import Namecom

client = Namecom(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
