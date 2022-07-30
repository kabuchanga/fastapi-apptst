from email.policy import default
import fastapi
import uvicorn
from fastapi import Body, FastAPI, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import  jwtBearer



posts = [{
    "id":1,
    "title":"peguins ",
    "text":"peguins are a group of aquatic flightless birds. "
},{
    "id":2,
    "title":"tigers ",
    "text":"Tigers are largest living cat species and a members of genus panthera"
},
{
    "id":3,
    "title":"Koalas ",
    "text":"Koala is arboreal hebivorous marsupial native to Australia. "
}]

users =[]

app = FastAPI()

app = FastAPI(
    title="fastapi-apptst",
    version=0.1,
    root_path="/dev/"
)

#1 get - for testing
'''
@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World", "Welcome":"To my FastAPI Demo"}
 '''
@app.get("/", tags=["FastAPI"])
def root():
    return {"message": "hello world again"}
#2 get all posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

#3 Get a sinlge post by {id}
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id:int):
    if id > len(posts):
        return{
            "error":"post with this Id does not exist! "
        }
    for post in posts:
        if post["id"]== id:
            return{
                "data":post
            }
#4 post a blog post[A handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearer)], tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts)+1
    posts.append(post.dict())
    return {
        "info":"post added"
    }

#5 user signup [create a new user ]
@app.post("/user/sigup", tags=["user"])
def user_signup(user : UserSchema):
    users.append(user)
    return signJWT(user.email)

#6 Funtion to check if the user existss
def check_user(data: UserLoginSchema = Body(default=None)):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"Invalid loging details"
        }



