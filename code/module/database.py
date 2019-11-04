'''
Created on Nov 4, 2019

@author: Muhammad Usman
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("app-db","dev","dev","crud_flask" )

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM lost_found_app order by name asc")
            else:
                cursor.execute("SELECT * FROM lost_found_app where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO lost_found_app(name,description,address) VALUES(%s, %s, %s)", (data['name'],data['description'],data['address'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE lost_found_app set name = %s, description = %s, address = %s where id = %s", (data['name'],data['description'],data['address'],id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM lost_found_app where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
