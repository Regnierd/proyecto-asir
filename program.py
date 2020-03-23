from mysql import DB

class users:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def add_user(self):
        sql = "insert into users (name, email, password) \
        value ({}, {}, {})".format(self.name, self.email, self.password)
        print(sql)
        self.db.run(sql)

    #def login(self, email, password):
    #    leer_email = DB.query(f'SELECT email FROM users WHERE email = "{email}"')
    #    leer_password = DB.query(f'SELECT password FROM users WHERE password = "{password}"')
