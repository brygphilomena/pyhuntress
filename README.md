# pyhuntress - An API library for Huntress SIEM and Huntress Managed SAT, written in Python

pyHuntress is a full-featured, type annotated API client written in Python for the Huntress APIs.

This library has been developed with the intention of making the Huntress APIs simple and accessible to non-coders while allowing experienced coders to utilize all features the API has to offer without the boilerplate.

pyHuntress currently supports both Huntress SIEM and Huntress Managed SAT products.

Features:
=========
- **100% API Coverage.** All endpoints and response models.
- **Non-coder friendly.** 100% annotated for full IDE auto-completion. Clients handle requests and authentication - just plug the right details in and go!
- **Fully annotated.** This library has a strong focus on type safety and type hinting. Models are declared and parsed using [Pydantic](https://github.com/pydantic/pydantic)

pyHuntress is currently in **development**.

Known Issues:
=============
- As this project is still a WIP, documentation or code commentary may not always align.
- Huntress Managed SAT is not built

Road Map:
=============
- Add Huntress Managed SAT Report

How-to:
=============
- [Install](#install)
- [Initializing the API Clients](#initializing-the-api-clients)
    - [Huntress Managed SAT](#huntress-managed-sat)
    - [Huntress SIEM](#huntress-siem)
- [Working with Endpoints](#working-with-endpoints)
    - [Get many](#get-many)
    - [Get one](#get-one)
    - [Get with params](#get-with-params)
- [Pagination](#pagination)
- [Contributing](#contributing)
- [Supporting the project](#supporting-the-project)

# Install
Open a terminal and run ```pip install pyhuntress```

# Initializing the API Clients

### Huntress Managed SAT
```python
from pyhuntress import HuntressSATAPIClient

# init client
sat_api_client = HuntressSATAPIClient(
  mycurricula.com,
  # your api public key,
  # your api private key,
)
```

### Huntress SIEM
```python
from pyhuntress import HuntressSIEMAPIClient

# init client
siem_api_client = HuntressSIEMAPIClient(
  # huntress siem url
  # your api public key,
  # your api private key,
)
```


# Working with Endpoints
Endpoints are 1:1 to what's available for both the Huntress Managed SAT and Huntress SIEM.

For more information, check out the following resources:
- [Huntress Managed SAT REST API Docs](https://support.meetgradient.com/huntress-managed-sat)
- [Huntress SIEM REST API Docs](https://api.huntress.io/docs)

### Get many
```python
### Managed SAT ###

# sends GET request to /company/companies endpoint
companies = manage_api_client.company.companies.get()

### SIEM ###

# sends GET request to /agents endpoint
agents = siem_api_client.agents.get()
```

### Get one
```python
### Managed SAT ###

# sends GET request to /company/companies/{id} endpoint
company = sat_api_client.company.companies.id(250).get()

### SIEM ###

# sends GET request to /agents/{id} endpoint
agent = siem_api_client.agents.id(250).get()
```

### Get with params
```python
### Managed SAT ###

# sends GET request to /company/companies with a conditions query string
conditional_company = sat_api_client.company.companies.get(params={
  'conditions': 'company/id=250'
})

### SIEM ###
# sends GET request to /agents endpoint with a condition query string
conditional_agent = siem_api_client.clients.get(params={
  'platform': 'windows'
})
```

# Pagination
The Huntress SIEM API paginates data for performance reasons through the ```page``` and ```limit``` query parameters. ```limit``` is limited to a maximum of 500.

To make working with paginated data easy, Endpoints that implement a GET response with an array also supply a ```paginated()``` method. Under the hood this wraps a GET request, but does a lot of neat stuff to make working with pages easier.

Working with pagination
```python
# initialize a PaginatedResponse instance for /agents, starting on page 1 with a pageSize of 100
paginated_agents = siem_api_client.agents.paginated(1,100)

# access the data from the current page using the .data field
page_one_data = paginated_agents.data

# if there's a next page, retrieve the next page worth of data
paginated_agents.get_next_page()

# if there's a previous page, retrieve the previous page worth of data
paginated_agents.get_previous_page()

# iterate over all companies on the current page
for agent in paginated_agents:
  # ... do things ...

# iterate over all companies in all pages
# this works by yielding every item on the page, then fetching the next page and continuing until there's no data left
for agent in paginated_agents.all():
  # ... do things ...
```

# Contributing
Contributions to the project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

# Supporting the project
:heart:

# Inspiration and Stolen Code
The premise behind this came from the [pyConnectWise](https://github.com/HealthITAU/pyconnectwise) package and I stole **most** of the code and adapted it to the Huntress API endpoints.