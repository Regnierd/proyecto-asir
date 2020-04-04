from mysql import DB
from datetime import datetime
import os

def write_log(msg):
    '''Función para escribir los logs del sistema'''
    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S] ") # Creamos el mensaje que queremos guardar
    f_msg = dt_string+": "+msg+"\n"

    try:
        with open(os.path.dirname(os.path.abspath(__file__))+"/logs/log.txt", "a") as log_file:
            log_file.write(f_msg)
            log_file.close()
    except FileNotFoundError:
        open(os.path.dirname(os.path.abspath(__file__))+"/logs/log.txt", "w").close()
        exit()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def add_user(self):
        sql = "insert into users (name, email, password) \
        values ('%s', '%s', '%s')" % (self.name, self.email, self.password)
        #print(sql)
        write_log(sql)
        self.db.run(sql)



class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def login(self):
        sql = f'select password, email, name from users where password = "{self.password}" \
        and email = "{self.email}"'
        result = self.db.run(sql)
        try:
            return result[0]["name"]
        except IndexError:
            return None
        write_log(sql)

class EditProfile:
    def __init__(self, name, email, password, session):
        self.name = name
        self.email = email
        self.password = password
        self.session = session
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def edit(self):
        sql = f"update users set name = {self.name}, email = {self.email}, password = {self.password} \
        where name = {self.session}"
        write_log(sql)
        self.db.run(sql)
