
# How to deploy FastAPI Application to Digital Ocean
Use this as a template to deploy FastAPI on digitalOcean
* In digital ocean, the settings should be as shown in the snapshot below
*  The run command should be the same as that in the ***Procfile*** 
* make sure the Host port is same as that in the ***gunicorn.conf.py***
#### Credit to:          
* https://dev.to/mrcartoonster/fastapi-do-deploy-1h10 
* https://github.com/zubin-madon/NFTrees
* https://docs.digitalocean.com/products/app-platform/reference/buildpacks/python/
#### NB:

* When deploying to Digital Ocean 2 applictions will be detected. Ignore Docker app and choose the webservice app(one that uses Procfile)


![plot](./FastAPIdigitalOceanDeploy.png)
