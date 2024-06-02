from fastapi.security import OAuth2PasswordBearer ,OAuth2PasswordRequestForm
from jose import JWTError , jwt
from fastapi import status,HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer ,OAuth2PasswordRequestForm
from main import app , FastAPI
from pydantic import BaseModel ,utils

app=FastAPI()

#MODEL
class User(BaseModel):
    username:str
    password:str or None=None
    
class userin_DB(User):
    hashed_password:str   

class user_out(BaseModel):
    username:str
    


#temporary_database
tem_db={
    "user1":{
        "password":"hello@123",
        "username":"20BCE5677",
        "name":"",
        "id":"",
        "disbled":False,
    "user2":{
        "password":"hededd",
        "username":"20BCE5578",
        "name":"",
        "id":"",
        "disbled":False,
        
    }
        
    }
}

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl="token")

def password_hashed(password):
    return pwd_context.hash(password)

def verification_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)



@app.post("/login")
def login(user:User):
    User=user.username==tem_db.username
    
    if not User:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid credentials")
    
    
    hass_password=password_hashed(tem_db.password)
    
    if not verification_password.verify(user.password,hass_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid credentials")
    
    return{"loged in"} #home page

    
    
    
    
    
    
    
    
    

    
    
    
    
    
    