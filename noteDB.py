# import sqlite3
# con = sqlite3.connect('Notebook.db')
# cur = con.cursor()
#
# cur.execute('''CREATE TABLE Students
#                    (title varchar UNIQUE, note varchar)''')
# con.commit()
#
#
#
# cur.close()

import sqlite3

con = sqlite3.connect('Notebook.db')
cur = con.cursor()


def create_new_table(name_of_table, **fields):
    d = '('
    for field_name in fields:
        d = d + f'{field_name} {fields[field_name]},'
    d = d[:-1]
    d = d + ')'
    print(d)
    q = f'''CREATE TABLE {name_of_table} {d}'''
    # cur.execute('''CREATE TABLE Students
    #                    (title varchar UNIQUE, note varchar)''')
    print(q)
    cur.execute(q)
    con.commit()


# create_new_table('test1',name='varchar',data='varchar')
cur.execute('''INSERT INTO test1 (name, data)
VALUES ('andrii3', 'builuk2')''')
con.commit()

sqlite_select_query = """SELECT *
  FROM test1
"""  # тут меняем SELECT
cur.execute(sqlite_select_query)
record = cur.fetchall()
for s in record:
    print(s)

cur.close()
