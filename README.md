
# How to deploy FastAPI Application to Digital Ocean
Use this as a template to deploy FastAPI on digitalOcean

#### **1.** Using Procfile 
* In digital ocean, the settings should be as shown in the snapshot below
* The run command in digital ocean app settingg should be the same as that in the ***Procfile***
* make sure the Host port is same as that in the ***gunicorn.conf.py*** 
* See the screenshop below on how to setupp your app
* set the root-path in the main file based on you directory tree 
    ```
      app = FastAPI(
        title="fastapi-apptst",
        version=0.1,
        root_path="/"
      )
    ```
* Notice the Route in the settings */* . if not the same you will have an error when you navigate to openAPI */docs*

![plot](./FastAPIdigitalOceanDeploy_Procfile.png)

#### **1.** Using Docker
* In digital ocean, the settings for docker FastAPI should be as shown in the snapshot below
* The run command blank in digtal ocean app settings. This because it is already set in  ***entrypointcmd.sh*** bash file
* make sure the Host port is same as that in the ***gunicorn.conf.py*** 
* See the screenshop below on how to setup your digital ocean docker app
* Set the root_path in the main file based on you directory tree 
    ```
      app = FastAPI(
        title="fastapi-apptst",
        version=0.1,
        root_path="/"
      )
    ```
* Notice the Route in the settings */* . if not the same you will have an error when you navigate to openAPI */docs*

![plot](./FastAPIdigitalOceanDeploy_Procfile.png)

##### Credits to:          
* https://dev.to/mrcartoonster/fastapi-do-deploy-1h10 
* https://github.com/zubin-madon/NFTrees
* https://docs.digitalocean.com/products/app-platform/reference/buildpacks/python/
##### NB:
* When deploying to Digital Ocean, 2 applictions will be detected because I have Doker file and Procfile. Thus you will deploy two(Procfile & Docker) instances of the same code base
* You may delete any to so that you deploy one app at a time.

##### Good Luck!! with you first FastAPI on Digital Ocean



