# DROP TABLE
summary_table_drop = "DROP TABLE IF EXISTS summary;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"
powerplay_table_drop = "DROP TABLE IF EXISTS powerplay;"
shot_attempts_table_drop = "DROP TABLE IF EXISTS shot_attempts;"
goals_by_period_table_drop = "DROP TABLE IF EXISTS goals_by_period;"

# CREATE TABLES
summary_table_create = """
    CREATE TABLE IF NOT EXISTS summary (
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

powerplay_table_create = """
    CREATE TABLE IF NOT EXISTS powerplay (
        team CHAR(3),
        game_date DATE,
        pp_opportunities SMALLINT,
        pp_goals_for SMALLINT,
        sh_goals_against SMALLINT,
        pp_toi SMALLINT,
        PRIMARY KEY (team, game_date)
    );
    """

shot_attempts_table_create ="""
    CREATE TABLE IF NOT EXISTS shot_attempts (
        team CHAR(3),
        game_date DATE,
        shots SMALLINT,
        sat_for SMALLINT,
        sat_against SMALLINT,
        sat SMALLINT,
        sat_tied SMALLINT,
        sat_ahead SMALLINT,
        sat_behind SMALLINT,
        sat_close SMALLINT,
        usat_for SMALLINT,
        usat_against SMALLINT,
        usat SMALLINT,
        usat_tied SMALLINT,
        usat_ahead SMALLINT,
        usat_behind SMALLINT,
        usat_close SMALLINT,
        PRIMARY KEY (team, game_date)
    );
"""

goals_by_period_table_create = """
    CREATE TABLE IF NOT EXISTS goals_by_period (
        team CHAR(3),
        game_date DATE,
        goals_for_ev SMALLINT,
        goals_for_pp SMALLINT,
        goals_for_sh SMALLINT,
        goals_for_p1 SMALLINT,
        goals_for_p2 SMALLINT,
        goals_for_p3 SMALLINT,
        goals_for_ot SMALLINT,
        goals_against_p1 SMALLINT,
        goals_against_p2 SMALLINT,
        goals_against_p3 SMALLINT,
        goals_against_ot SMALLINT,
        PRIMARY KEY(team, game_date)
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

powerplay_table_insert = """
    INSERT INTO powerplay (
        team,
        game_date,
        pp_opportunities,
        pp_goals_for,
        sh_goals_against,
        pp_toi
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (team, game_date) DO UPDATE
    SET
        pp_opportunities = EXCLUDED.pp_opportunities,
        pp_goals_for = EXCLUDED.pp_goals_for,
        sh_goals_against = EXCLUDED.sh_goals_against,
        pp_toi = EXCLUDED.pp_toi;
"""

shot_attempts_table_insert = """
    INSERT INTO shot_attempts (
        team,
        game_date,
        shots,
        sat_for,
        sat_against,
        sat,
        sat_tied,
        sat_ahead,
        sat_behind,
        sat_close,
        usat_for,
        usat_against,
        usat,
        usat_tied,
        usat_ahead,
        usat_behind,
        usat_close
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)
    ON CONFLICT(team, game_date) DO UPDATE
    SET
        shots = EXCLUDED.shots,
        sat_for = EXCLUDED.sat_for,
        sat_against = EXCLUDED.sat_against,
        sat = EXCLUDED.sat,
        sat_tied = EXCLUDED.sat_tied,
        sat_ahead = EXCLUDED.sat_ahead,
        sat_behind = EXCLUDED.sat_behind,
        sat_close = EXCLUDED.sat_close,
        usat_for = EXCLUDED.usat_for,
        usat_against = EXCLUDED.usat_against,
        usat = EXCLUDED.usat,
        usat_tied = EXCLUDED.usat_tied,
        usat_ahead = EXCLUDED.usat_ahead,
        usat_behind = EXCLUDED.usat_behind,
        usat_close = EXCLUDED.usat_close;
"""

goals_by_period_table_insert = """
    INSERT INTO goals_by_period (
        team,
        game_date,
        goals_for_ev,
        goals_for_pp,
        goals_for_sh,
        goals_for_p1,
        goals_for_p2,
        goals_for_p3,
        goals_for_ot,
        goals_against_p1,
        goals_against_p2,
        goals_against_p3,
        goals_against_ot
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (team, game_date) DO UPDATE
    SET
        goals_for_ev = EXCLUDED.goals_for_ev,
        goals_for_pp = EXCLUDED.goals_for_pp,
        goals_for_sh = EXCLUDED.goals_for_sh,
        goals_for_p1 = EXCLUDED.goals_for_p1,
        goals_for_p2 = EXCLUDED.goals_for_p2,
        goals_for_p3 = EXCLUDED.goals_for_p3,
        goals_for_ot = EXCLUDED.goals_for_ot,
        goals_against_p1 = EXCLUDED.goals_against_p1,
        goals_against_p2 = EXCLUDED.goals_against_p2,
        goals_against_p3 = EXCLUDED.goals_against_p3,
        goals_against_ot = EXCLUDED.goals_against_ot;
"""

# QUERY LISTS
drop_table_queries = {
#     "teams": teams_table_drop,
#     "summary": summary_table_drop,
#     "powerplay": powerplay_table_drop
}

create_table_queries = {
    "teams": teams_table_create,
    "summary": summary_table_create,
    "powerplay": powerplay_table_create,
    "shot_attempts": shot_attempts_table_create,
    "goals_by_period": goals_by_period_table_create
}