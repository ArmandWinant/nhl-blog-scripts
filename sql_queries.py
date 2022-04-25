# DROP TABLE
summary_table_drop = "DROP TABLE IF EXISTS summary;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"

# CREATE TABLES
summary_table_create = """
    CREATE TABLE summary (
        team VARCHAR(50) NOT NULL,
        season CHAR(7) NOT NULL,
        game_date DATE NOT NULL,
        opponent VARCHAR(3) NOT NULL,
        win BOOLEAN,
        loss BOOLEAN,
        tie BOOLEAN,
        points SMALLINT,
        points_percentage REAL,
        regulation_win BOOLEAN,
        regulation_overtime_win BOOLEAN,
        shootout_win BOOLEAN,
        goals_for SMALLINT,
        goals_against SMALLINT,
        pp_percentage REAL,
        pk_percentage REAL,
        net_pp_percentage REAL,
        net_pk_percentage REAL,
        shots_for SMALLINT,
        shots_against SMALLINT,
        fo_win_percentage REAL,
        PRIMARY KEY (team, game_date)
    );
"""

teams_table_create = """
    CREATE TABLE IF NOT EXISTS teams (
        team VARCHAR(50) PRIMARY KEY,
        abbreviation CHAR(3) NOT NULL,
        conference CHAR(7) NOT NULL,
        division VARCHAR(30) NOT NULL
    );
"""

# INSERT RECORDS
summary_table_insert = """
    INSERT INTO summary (
        team,
        season,
        game_date,
        opponent,
        win,
        loss,
        tie,
        points,
        points_percentage,
        regulation_win,
        regulation_overtime_win,
        shootout_win,
        goals_for,
        goals_against,
        pp_percentage,
        pk_percentage,
        net_pp_percentage,
        net_pk_percentage,
        shots_for,
        shots_against,
        fo_win_percentage
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

teams_table_insert = """
    INSERT INTO teams (
        team,
        abbreviation,
        conference,
        division
    )
    VALUES (%s, %s, %s, %s);
"""
# QUERY LISTS
drop_table_queries = {
    "teams": teams_table_drop,
    "summary": summary_table_drop
}

create_table_queries = {
    "teams": teams_table_create,
    "summary": summary_table_create
}