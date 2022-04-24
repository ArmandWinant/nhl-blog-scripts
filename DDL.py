import psycopg2
from sql_queries import drop_table_queries, create_table_queries

def create_database():
    conn = psycopg2.connect(database="nhl_db")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    cur.execute("DROP DATABASE IF EXISTS nhl_db;")
    cur.execute("CREATE DATABASE nhl_db;")
    
    cur.close()
    conn.close()
    
    conn = psycopg2.connect(database="nhl_db")
    cur = conn.cursor()
    
    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def reinitialise_db():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    
    cur.close()
    conn.close()