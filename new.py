from  fastapi import FastAPI,Depends
from  authentication import BaseModel
from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer ,OAuth2PasswordRequestForm
from fastapi import status,HTTPException
tem_db={
    "user1":{
        "hashed_password":"hello@123",
        "registration_number":"20BCE5677",
        "name":"",
        "id":"",
        "disbled":False,
    "user2":{
        "hashed_password":"hededd",
        "registration_number":"20BCE5578",
        "name":"",
        "id":"",
        "disbled":False,
        
    }    
    }
}
app=FastAPI()
from . import model
from . import table
from .model import engine , SessionLocal
table.Base.metadata.create_all(bind=engine)
def get_db():
    
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
class userlogin(BaseModel):
    reg_number:int
    password:str
    
class reg(BaseModel):
    reg_number:str

class user_login(userlogin):
    pass
    
    class Config:
        orm_mode=True

@app.get("/club_details")
def club(db:Session=Depends(get_db) ):
    return 0

@app.get("/reg_number")
def reg(reg:reg ,db:Session=Depends(get_db)):
    Reg=db.query(tem_db).filter(tem_db.registration_number).first()
    if not Reg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    
    
    
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme=OAuth2PasswordBearer(tokenUrl="token")

def password_hashed(password):
    return pwd_context.hash(password)

def verification_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


#validation
@app.post("/login")
def login(user:userlogin,db:Session=Depends(get_db)):
    user=db.query(tem_db).filter(tem_db.registration_number==user.reg_number)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    if not verification_password(user.password,tem_db.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    
    return{"home page"}
   
   
   
#CLUB DETAIL
temp_club_details={
    "club_name":{
        "details":"..........",
        "name":"CSI",
        "owner":"jjjj",
        "club_type":"tech",
        "club_info":"jnkjn",
        "id":1
        },
    
    "club_name":{
        "details":"..........",
        "name":"MS",
        "owner":"jjlloj",
        "club_type":"tech",
        "club_info":"ajj a",
        "id":2
        }
    
}
class fetch(BaseModel):
    details:str
    
class update(BaseModel):
    name:str
    details:str
    owner:str
    club_type:str
    club_info:str
    
    class Config:
        orm_mode=True
     
#all club names list
@app.get("/list_clubs")
def detail(db:Session=Depends(get_db)):
    
    det=db.query(temp_club_details.name).all
    return det[list]

#get specific club details by id
@app.get("/club/{id}")
def by_id(id:int,db:Session=Depends(get_db)):
    cl=db.query(temp_club_details).filter(temp_club_details.id==id)
    
    if not cl:
       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid id {id}")
    return cl

#update club details info (by owner )
@app.put("/update/{id}")
def update(id:int,Update:update,db:Session=Depends(get_db)):
    cha=db.query(temp_club_details).filter(temp_club_details.id==id)
    
    temp_club_details=cha.first()
    
    if temp_club_details==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid id {id}")
    
    cha.update(Update.dict(),synchronize_session=False)
    
#event db
events={
    "event_name":{
        "event_name":"jjjj",
        "event_type":"kkk",
        "event_history":"aasl",
        "event_details":"jnjn",
        "id":1},
    
     "event_name":{
        "event_name":"jjjj",
        "event_type":"kkk",
        "event_history":"aasl",
        "event_details":"jnjn",
        "id":2}
}
class update_event_name(BaseModel):
    event_name:str
    event_details:str
    event_type:str
    
    class Config:
        orm_mode=True
    
#update events(name ,type ,details)
@app.put("/event_update/{id}")
def update(id:int,update:update_event_name,db:Session=Depends(get_db)):
    eve=db.query(events).filter(events.id==id)
    
    events=eve.first()
    
    if events==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid id {id}")
    
    eve.update(update.dict(),synchronize_session=False)
      
    
