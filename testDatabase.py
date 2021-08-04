import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="root",
	database="testdatabase"
	)

users = [("tim", "techwithtim"),
		("joe", "joey123"),
		("sarah", "sarah1234")]

user_scores = [(45, 10),
			  (30, 200),
			  (46, 124)]

mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"

Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"

for x, user in enumerate(users):
	mycursor.execute(Q3, user)
	last_id = mycursor.lastrowid

	mycursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()

mycursor.execute("SELECT * FROM Scores")
for x in mycursor:
	print(x)

mycursor.execute("SELECT * FROM Users")
for x in mycursor:
	print(x)
