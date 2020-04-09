import mysql.connector 
mydb=mysql.connector.connect(user='root',passwd='Somesh@1998',host='localhost',data base="student")
db=mydb.cursor() 
db.execute("select * from sdata")
print("The Data Inserted By The Registration Form Is:--") 
r=db.fetchall()
for i in r: 
    print(i)
