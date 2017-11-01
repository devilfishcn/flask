import orm
from sqlalchemy import or_
from conn import session_scope

def insert_account(name,password,title,salary):
    with session_scope() as session:
        account=orm.Account(user_name=name,pass_word=password,title=title,salary=salary)
        session.add(account)
        
def get_account(id=None,name=None):
    with session_scope() as session:
        return session.query(orm.Account).filter(
            or_(orm.Account.id==id,orm.Account.user_name==name)
            ).first()
            
def delete_account(name):
    with session_scope() as session:
        account = get_account(name=name)
        return session.delete(account)
    
insert_account('wxf','admin','cto',3000)