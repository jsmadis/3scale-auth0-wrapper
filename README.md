# 3scale-auth0-wrapper

This is a wrapper between 3scale and auth0. It exposes API for zync (a component of 3scale which manages communication with IDPs).

It implements an openAPI specification shared in zync component https://github.com/3scale/zync/tree/master/examples/rest-api


## Run locally:
```
docker pull jsmadis/3scale-auth0-wrapper
docker run -p 80:80 --env AUTH0_URL="https://example" 
```
Where `AUTH0_URL` is URL to your auth0 API.
