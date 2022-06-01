# DROP TABLE
summary_table_drop = "DROP TABLE IF EXISTS summary;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"

# CREATE TABLES
summary_table_create = """
    CREATE TABLE summary (
        team CHAR(3),
        season CHAR(7),
        game_date DATE,
        home_game BOOLEAN,
        opponent CHAR(3),
        win SMALLINT,
        loss SMALLINT,
        tie SMALLINT,
        ot_loss SMALLINT,
        points SMALLINT,
        points_percentage REAL,
        regulation_win SMALLINT,
        regulation_overtime_win SMALLINT,
        shootout_win SMALLINT,
        goals_for SMALLINT,
        goals_against SMALLINT,
        pp_percentage REAL,
        pk_percentage REAL,
        net_pp_percentage REAL,
        net_pk_percentage REAL,
        shots_for REAL,
        shots_against REAL,
        fo_win_percentage REAL,
        playoffs BOOLEAN,
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
        home_game,
        opponent,
        win,
        loss,
        tie,
        ot_loss,
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
        fo_win_percentage,
        playoffs
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (team, game_date) DO UPDATE
    SET
        team = EXCLUDED.team,
        season = EXCLUDED.season,
        game_date = EXCLUDED.game_date,
        home_game = EXCLUDED.home_game,
        opponent = EXCLUDED.opponent,
        win = EXCLUDED.win,
        loss = EXCLUDED.loss,
        tie = EXCLUDED.tie,
        ot_loss = EXCLUDED.ot_loss,
        points = EXCLUDED.points,
        points_percentage = EXCLUDED.points_percentage,
        regulation_win = EXCLUDED.regulation_win,
        regulation_overtime_win = EXCLUDED.regulation_overtime_win,
        shootout_win = EXCLUDED.shootout_win,
        goals_for = EXCLUDED.goals_for,
        goals_against = EXCLUDED.goals_against,
        pp_percentage = EXCLUDED.pp_percentage,
        pk_percentage = EXCLUDED.pk_percentage,
        net_pp_percentage = EXCLUDED.net_pp_percentage,
        net_pk_percentage = EXCLUDED.net_pk_percentage,
        shots_for = EXCLUDED.shots_for,
        shots_against = EXCLUDED.shots_against,
        fo_win_percentage = EXCLUDED.fo_win_percentage,
        playoffs = EXCLUDED.playoffs;
"""

teams_table_insert = """
    INSERT INTO teams (
        team,
        abbreviation,
        conference,
        division
    )
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (team) DO UPDATE
    SET
        team = EXCLUDED.team,
        abbreviation = EXCLUDED.abbreviation,
        conference = EXCLUDED.conference,
        division = EXCLUDED.division;
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