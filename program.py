from mysql import DB

class users:
    def __init__(self):
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def add_user(self, name, email, password):
        sql = "insert into users (name, email, password) \
        value ({}, {}, {})".format(name, email, password)
        self.DB.run(sql)

    #def login(self, email, password):
    #    leer_email = DB.query(f'SELECT email FROM users WHERE email = "{email}"')
    #    leer_password = DB.query(f'SELECT password FROM users WHERE password = "{password}"')
