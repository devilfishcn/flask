from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

Base=declarative_base()

class Account(Base):
    __tablename__=u'account'
    
    id=Column(Integer,primary_key=True)
    user_name=Column(String(50),nullable=False)
    pass_word=Column(String(200),nullable=False)
    title=Column(String(50))
    salary=Column(Integer)
    
    def is_active(self):
        return True
    
    def get_id(self):
        return self.id
    
    def is_authenticate(self):
        return True
    
    def is_anonymous(self):
        return False
    
    
# use mysql;
# CREATE TABLE account (
#    id int  AUTO_INCREMENT,
#    user_name VARCHAR(50) NOT NULL,
#    pass_word VARCHAR(200) NOT NULL,
#    title VARCHAR(50),
#    salary int,
#    PRIMARY KEY ( id )
# )