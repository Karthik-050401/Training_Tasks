# HTTP methods, status codes, error response standard

## Builder Analogy
If HTTP request is the query from one building to another building through internet,
- HTTP Method is the noun of the sentencem (while resource is the verb)
- Status code is the 3 digit summary for the request
- Error response is the verbal summary on what actually happened.

## HTTP Methods
HTTP is for communicating between computers and sharing resources between them.

The major actions done in a request is: CRUD (Create, Read, Update, Delete). 

HTTP has standardised keywords to show what action to be done in the HTTP request. Basically its the **verb** of the HTTP request.

The types of HTTP methods are:
- GET - Read a resource
- POST - Create a new resource
- PUT - Replace an entire resource
- PATCH - Partially update a resource
- DELETE - Remove a resource

This is used in the request line of the HTTP request to point what action is asked by the HTTP request.

## HTTP Status Code
When HTTP response is received, the client receives a 3 digit number from the server called **HTTP Status Code** as part of the HTTP response.

**HTTP Status Code** is a 3 digit number the server sends back in the response to instantly tell the client what happened to the request. Each number mean something about the request status.

### Analysing HTTP Status Code:
- 2XX - Everything went well
- 3XX - Redirection happened during the request
- 4XX - The client made a mistake
- 5XX - The server made a mistake

## HTTP Error Response
When the HTTP request-response failed for some reasons (network error, interval server error, etc), we will receive the response containing the status code (4XX, 5XX) as well as error response in the body of the response.
This is known as the HTTP Error Response.
Example: Say I access

## Implementation
This demonstration is to try out HTTP request and analysing response under different scenarios.
The tool we are going to use to make HTTP request is **"curl"**. This is a command line tool to transfer data between networks.
We are going to do a HTTP request to the website "www.cogniyon.ai" and see what the response is.
The terminal command is:
```text
curl -v "https://www.cogniyon.ai"
```
Here -v means "verbose", showing happening during the request-response cycle.
So this command uses curl to make a HTTP request to the website.

After the DNS lookup and TLS handshake, the request boils down to:
```text
> GET / HTTP/2
> Host: www.cogniyon.ai
> User-Agent: curl/8.7.1
> Accept: */*
```

The response received from the website is: (only added the request line and header for simplicity)

```text
< HTTP/2 200 
< content-type: text/html
< content-length: 29664
< date: Fri, 04 Sep 2026 13:21:05 GMT
< last-modified: Wed, 06 May 2026 10:12:47 GMT
< etag: "fbc11d28c9e8db2b56424075be9bcf71"
< x-amz-server-side-encryption: AES256
< accept-ranges: bytes
< server: AmazonS3
< x-cache: Hit from cloudfront
< via: 1.1 a17a41401eccc1af8f00a087a8c177de.cloudfront.net (CloudFront)
< x-amz-cf-pop: MAA51-P2
< alt-svc: h3=":443"; ma=86400
< x-amz-cf-id: zlaV9QsAijjw2TvumyQi2BDIblo0HQOn5mPC0IKS-JChiw7ZGcdTDQ==
< age: 1010
```

The important values to note is the status code.
The status code is 200, meaning its a successful HTTP request with no issues.

Now let's to make a HTTP request which is bound to fail and see what the error response is.

Let's make a HTTP request to an unknown resource (hopefully) called "cogniyon.ai/non-existing-file".

So the curl command is:
```text
curl -v "https://cogniyon.ai/non-existent-file"
```
As usual, after DNS lookup and TLS handshake, the request boils down to:
```text
> GET /non-existing-file HTTP/2
> Host: cogniyon.ai
> User-Agent: curl/8.7.1
> Accept: */*
```

The corresponding response is:
```text
< HTTP/2 403 
< content-type: application/xml
< server: AmazonS3
< date: Fri, 04 Sep 2026 13:45:48 GMT
< x-cache: Error from cloudfront
< via: 1.1 7d022c110a257a79b58a321d375427d0.cloudfront.net (CloudFront)
< x-amz-cf-pop: MAA51-P2
< alt-svc: h3=":443"; ma=86400
< x-amz-cf-id: OKa78atnbR-IBZ2Tu8J9e44jo5QX1kF1pffo143p0S4ZyqGh5tyfjg==
< 
<?xml version="1.0" encoding="UTF-8"?>
* Connection #0 to host cogniyon.ai left intact
<Error><Code>AccessDenied</Code><Message>Access Denied</Message></Error>
```