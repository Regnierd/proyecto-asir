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

class users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def add_user(self):
        sql = "insert into users (name, email, password) \
        value ('%s', '%s', '%s')" % (self.name, self.email, self.password)
        write_log(sql)
        self.db.run(sql)

class loggins:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def login(self):
        leer_email = f'SELECT email FROM users WHERE email = "{self.email}"'
        leer_password = f'SELECT password FROM users WHERE password = "{self.password}"'
        self.db.run(leer_email)
        self.db.run(leer_password)
        if (leer_email != self.email) or (leer_password != self.password):
            print("No estas registrado")

        write_log(leer_email)
        write_log(leer_password)
