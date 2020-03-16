from mysql import DB

class users:
    def __init__(self):
        self.db = DB("cineAdmin", "p@ssw0rd", "prueba")

    def add_user(self, id_user, name, email, password):
        sql = "insert into users (name, email, password) \
        value ({}, {}, {})".format(name, email, password)
        self.db.run(sql)
