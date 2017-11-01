def get_db_config():
    f=open('dbconfig.ini')
    ini = f.readlines()
    print ini[0]
    return ini[0]