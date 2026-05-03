import sqlite3
connection=sqlite3.connect('student.db')
cursor=connection.cursor()
table_info="""
create table  student(name varchar(40),class varchar(20),
section varchar(10),roll_no int );
"""
cursor.execute(table_info)
cursor.execute('''insert into student values('Pragati','btech','a',100)''')
cursor.execute('''insert into student values('Sakshi','bsc','a',99)''')    
cursor.execute('''insert into student values('Pranjali','mca','b',60)''')
cursor.execute('''insert into student values('Disha','btech','a',75)''')
cursor.execute('''insert into student values('Nainsi','bsc','b',80)''')

print("Data inserted successfully")
data=cursor.execute("select * from student")

for i in data:
    print(i)
connection.commit()
connection.close()