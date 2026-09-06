# Pagination, Filtering, Sorting, Versioning and Idempotency

## Analogy
Say we have piles of commodities (resource) in the warehouse. When sharing commodities in the city, its not wise to send the warehouse to the client if they ask something. 
There should be certain constraints we set by which we send them the resources. The following are the methods to send commodities between houses.

- Pagination is sending the resources one by one in a bundle.
- Filtering is sending the resources by the fields the client is interested in.
- Versioning is the method of sharing resources to the client even if we do internal changes in the warehouse (database/server) so that the client doesn't affect during the transaction.
- Idempotency is when asking multiple times is same as asking once.

HTTP is a protocol for sharing resources between networks and internet. While sharing, I may ask for a data or bunch of data from a resource, but the resource may have millions of data inside it.

Example, say I go to a library and ask for books, what if the librarian hands me every book in the library. The librarian is not wrong here. I asked for /library/book but the every book in the library comes under it.

So if there are large number of items to choose from, we need to set constraints to not get overwhelmed and pick the exact item we need.
The following concepts are methods to solve this issue.

## Pagination, Filtering, Sorting

### Pagination
The act of split data into smaller chunks of data (pages) is called pagination.

Say I want to access a resource from a server which is a list of shopping products. The problem is, there are millions of products under the products resources. After the HTTP request, if the server returns the whole million list, this creates huge overload to the client and network traffic.

To avoid this, the server decides to send the data by chunks, one at a time.

This is called pagination.

There are **two** ways for the server to paginate. The information about size and position is passed on to the query parameters.
1. Page - Number Pagination:
The data is split into pages and sent to the client.
Page - Page number
Limit - Page size

Example:
```text
GET /products?page=10&limit=10

- pick the 10th page and read 10 product from it
```

2. Cursor Pagination:
The data is picked by position and the chunk is determined by the limit.
cursor - Starting page location
limit - page size

Example:
```text
GET /products?cursor=10&limit=10

- from the 10th item, read 10 products from it
```

### Filtering
The act of narrowing down the result set to match specific criteria is called filtering.

Example:
GET /cars?color=red&make=hyundai

### Sorting
Sorting out the results of the response based on the given field in the query is called sorting.
Example:
- GET /users?sort=lastName
- GET /users?sort=-createdAt

Note: to sort them in descending order, minus sign (-) is added in front of the value. Ascending order doesn't need a sign.

## Versioning
The process of making changes to the API without breaking the API for existing clients is called versioning.

Methods of doing it:
- URL Path: GET /api/v2/users
- Custom Headers: 
    - GET /users
    - API_version: 2026-09-02
- Query Params: GET /users?version=2

## Idempotency
If the process of making multiple quest of the same request means the same as making it once, it's called idempotent.
A method is called idempotent if the action is same as doing it once rather than doing it multiple times.

Idempotent HTTP Method:
GET, PUT, DELETE, HEAD, OPTIONS

Not idempotent HTTP Method:
POST