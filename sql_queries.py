# DROP TABLE
summary_table_drop = "DROP TABLE IF EXISTS summary;"

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
        PRIMARY KEY (team, date)
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
    VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
"""

# QUERY LISTS