from nba_api.stats.endpoints import LeagueGameLog  # ~type: ignore[import-untyped]

gamelog = LeagueGameLog(season="2024-25")
df = gamelog.get_data_frames()[0]
work_set = df[
    [
        "TEAM_ID",
        "GAME_DATE",
        "GAME_ID",
        "TEAM_ABBREVIATION",
        "MATCHUP",
        "PTS",
        "AST",
        "REB",
        "BLK",
        "TOV",
        "STL",
        "FG_PCT",
        "FG3_PCT",
        "FT_PCT",
    ]
]
print(work_set.head(20))
