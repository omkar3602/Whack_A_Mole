import mysql.connector


class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="whacamole"
        )
        self.mycursor = self.mydb.cursor()

    def Query_fetchall(self, query, val):
        self.mycursor.execute(query, val)
        result = self.mycursor.fetchall()
        return result

    def Query_fetchone(self, query, val):
        print("fetchone")
        self.mycursor.execute(query, val)
        result = self.mycursor.fetchone()
        return result

    def Query_insert(self, query, val):
        self.mycursor.execute(query, val)
        self.mydb.commit()
        return self.mycursor.rowcount

    def Query_update(self, query, val):
        self.mycursor.execute(query, val)
        self.mydb.commit()
        print("Data changed")

    def Query_fetchall_leaderboard(self, query):
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result