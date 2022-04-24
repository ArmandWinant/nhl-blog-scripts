import psycopg2

def db_connect():
    conn = psycopg2.connect(database="nhl_db")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    return conn, cur

def close_db_connect(conn, cur):
    cur.close()
    conn.close() 