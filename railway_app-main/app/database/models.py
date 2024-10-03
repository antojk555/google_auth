
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from sqlalchemy.orm import Session 
from pydantic import BaseModel, EmailStr  
from typing import Optional 
from sqlalchemy import Column, String, Boolean



class User(BaseModel):  
    id: str  
    name: str  
    given_name: str  
    family_name: str  
    email: EmailStr  
    email_verified: bool  
    picture: Optional[str] = None  
    hd: Optional[str] = None



class UserRepo:  
    @staticmethod  
    def create(db: Session, user: User):  
        db_item = UserModel(  # Assuming you have a UserInformation model defined  
            id=user['sub'],  
            name=user['name'],  
            given_name=user['given_name'],  
            family_name=user['family_name'],  
            email=user['email'],  
            email_verified=user['email_verified'],  
            picture=user['picture'],  
            hd=user['hd']
        )  
        db.add(db_item)  
        db.commit()  
        db.refresh(db_item)  
        return db_item


 

Base = declarative_base()  

class UserModel(Base):  
    __tablename__ = 'users'  
    
    id = Column(String, primary_key=True)  # You can use 'sub' as the primary key  
    name = Column(String)  
    given_name = Column(String)  
    family_name = Column(String)  
    email = Column(String, unique=True)  
    email_verified = Column(Boolean)  
    picture = Column(String, nullable=True)  
    hd = Column(String, nullable=True)  

    def __repr__(self):  
        return f"<User(id={self.id}, email={self.email})>"
