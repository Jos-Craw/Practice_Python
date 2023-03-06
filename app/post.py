import psycopg2
import os
import csv


mydb = psycopg2.connect(host="localhost",user="postgres",password="postgres",port="5432",database="practice")

cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS posts")
cursor.execute("CREATE TABLE if not exists posts(	id SERIAL PRIMARY KEY,rubrics TEXT NOT NULL,text TEXT NOT NULL,created_date DATE NOT NULL)")

with open("posts.csv", 'r',encoding="utf8") as file:
	reader = csv.reader(file)
	next(reader)
	for row in reader:
		cursor.execute(("INSERT INTO posts (rubrics, text, created_date) VALUES  (%s, %s, %s)"), (eval(row[2]), row[0], row[1]))

mydb.commit()
mydb.close()

print(os.environ.get('POSTGRES_URL'))