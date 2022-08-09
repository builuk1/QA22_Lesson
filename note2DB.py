import sqlite3

con = sqlite3.connect('Notebook.db')
cur = con.cursor()


def create_new_tablev2(name_of_table, *fields):
    d = '('
    for inner_field in fields:
        for text in inner_field:
            d = d + f'{text} '
        d = d + ','
    d = d[:-1]
    d = d + ')'
    print(d)
    q = f'''CREATE TABLE {name_of_table} {d}'''
    # cur.execute('''CREATE TABLE Students
    #                    (title varchar UNIQUE, note varchar)''')
    print(q)
    cur.execute(q)
    con.commit()


# create_new_tablev2('test2',['name','varchar','UNIQUE'],['data','varchar'])


def insert(name_of_table, field_name1, field_name2, data1, data2):
    q = f'''INSERT INTO {name_of_table} ({field_name1}, {field_name2})
    VALUES ('{data1}', '{data2}')'''
    cur.execute(q)
    con.commit()


def insertv2(name_of_table, **data):
    k = '('
    v = 'VALUES('
    for row in data:
        k = k + f'{row},'
        v = v + f"'{data[row]}',"
    k = k[:-1]
    v = v[:-1]
    k = k + ')'
    v = v + ')'
    q = 'INSERT INTO ' + k + ' ' + v
    cur.execute(q)
    con.commit()


insertv2('test2', name='data', abc='qwe')
# * DELETE

insert('test2', 'name', 'data', 'abc', 'qwe')

sqlite_select_query = """SELECT *
  FROM test2
"""  # тут меняем SELECT
cur.execute(sqlite_select_query)
record = cur.fetchall()
for s in record:
    print(s)

cur.close()
