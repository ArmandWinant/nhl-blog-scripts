import pandas as pd
import DML
from sql_queries import teams_table_create, teams_table_drop, teams_table_insert

def populate_teams_table():
    teams_df = pd.read_csv('teams.csv')
    conn, cur = DML.db_connect()
    
    for _, row_values in teams_df.iterrows():
        cur.execute(teams_table_insert, row_values)
    
    DML.close_db_connect(conn, cur)
    
    
if __name__=="__main__":
    populate_teams_table()