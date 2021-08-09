import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="whacamole"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (username VARCHAR(20) PRIMARY KEY, name VARCHAR(20), email VARCHAR(50),password VARCHAR(16), security_question VARCHAR(50), security_answer VARCHAR(20), total_score VARCHAR(11), highscore VARCHAR(11))")

mycursor.execute("INSERT INTO users values('omkarm','Omkar Mudkanna','omkar.mudkanna20@vit.edu','1','Which is your favourite color?','blue', '0' , '0');")
mycursor.execute("INSERT INTO users values('omkarj','Omkar Jahagirdar','omkar.jahagirdar20@vit.edu','1','Which is your favourite color?','blue', '0' , '0');")
mycursor.execute("INSERT INTO users values('onkarp','Onkar Pardeshi','onkar.pardeshi20@vit.edu','1','Which is your favourite color?','blue', '0' , '0');")
mycursor.execute("INSERT INTO users values('abhisheko','Abhishek Otari','abhishek.otari20@vit.edu','1','Which is your favourite color?','yellow', '0' , '0');")
mycursor.execute("INSERT INTO users values('sakshio','Sakshi Ozarde','sakshi.ozarde20@vit.edu','1','Which is your favourite color?','black', '0' , '0');")
mycursor.execute("INSERT INTO users values('adityap','Aditya Pachore','aditya.pachore20@vit.edu','1','Which is your favourite color?','blue', '0' , '0');")

mycursor.execute("CREATE TABLE levels_and_skins (username VARCHAR(20) PRIMARY KEY, e1 BOOLEAN,e2 BOOLEAN, e3 BOOLEAN, m1 BOOLEAN,m2 BOOLEAN, m3 BOOLEAN, h1 BOOLEAN,h2 BOOLEAN, h3 BOOLEAN, s1 BOOLEAN,s2 BOOLEAN, s3 BOOLEAN, s4 BOOLEAN,s5 BOOLEAN, s6 BOOLEAN, s7 BOOLEAN,s8 BOOLEAN, s9 BOOLEAN);")

mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('omkarm', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")
mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('omkarj', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")
mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('onkarp', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")
mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('abhisheko', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")
mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('sakshio', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")
mycursor.execute("INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES ('adityap', 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)")

mycursor.execute("CREATE TABLE highscores( username VARCHAR(20),score INT(11), date DATE, time TIME);")
mydb.commit()
print(mycursor.rowcount, "record inserted.")
