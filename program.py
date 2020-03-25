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
        values ('%s', '%s', '%s')" % (self.name, self.email, self.password)
        write_log(sql)
        self.db.run(sql)

class loggins:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def login(self):
        sql = f'SELECT email, password FROM users WHERE email = "{self.email}" \
        and password = "{self.password}"'
        self.db.run(sql)

        if (sql[0] != self.email) or (sql[1] != self.password):
            print("No estas registrado")

        write_log(sql)
