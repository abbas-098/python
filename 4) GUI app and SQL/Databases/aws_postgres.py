import psycopg2

host = "dbname = '' user = 'postgres' password = 'abbas098' host = 'database-1.cr6osid7sbrn.us-east-1.rds.amazonaws.com' port = '5432'"

def create_table():
    conn = psycopg2.connect(host)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect(host)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(host)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))       # have to put comma at end if one item
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect(host)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity,price,item))
    conn.commit()
    conn.close()
    
create_table()
#update(20,15.0,"Apple")
print(view())
