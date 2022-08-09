import sqlite3

con = sqlite3.connect('University.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE Students
#                    (LastName varchar, FirstName varchar,
#            BirthDate date, Grants int,Email varchar)''')

# #INSERT
cur.execute('''INSERT INTO Students (LastName, FirstName,
            BirthDate, Grants,Email)
VALUES ('andrii', 'builuk','1999-01-01',1000,'g')''')
cur.execute('''INSERT INTO Students (LastName, FirstName,
            BirthDate, Grants,Email)
VALUES ('andrii1', 'builuk1','1999-01-11',1200,'g')''')
con.commit()  # тут меняем копируем и меняем VALUES
cur.execute('''INSERT INTO Students (LastName, FirstName,
            BirthDate, Grants,Email)
VALUES ('andrii3', 'builuk2','1999-05-21',1500,'g')''')
con.commit()
# cur.close()

# con = sqlite3.connect('University.db')
# cur = con.cursor()

# SELECT
sqlite_select_query = """SELECT [LastName]
      ,[FirstName]
      ,[BirthDate]
      ,[Grants]
      ,[Email]
  FROM Students
  WHERE [LastName] LIKE '[a]%'
"""  # тут меняем SELECT
cur.execute(sqlite_select_query)
record = cur.fetchall()
for s in record:
    print(s)
# WHERE strftime('%y', [BirthDate]) = '01'
# ORDER BY [FirstName] DESC
