from nba_api.stats.endpoints import LeagueGameLog  # ~type: ignore[import-untyped]

gamelog = LeagueGameLog(season="2024-25")
real_df = gamelog.get_data_frames()[0]
df = real_df.copy(deep=True)
# print(df)
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
        "WL",
    ]
]
work_set.columns = work_set.columns.str.strip()
# print(work_set.head(20))

home_set = work_set[work_set["MATCHUP"].str.contains("vs.")]
home_set.rename(
    columns={
        "TEAM_ID": "HOME_TEAM_ID",
        "TEAM_ABBREVIATION": "HOME_TEAM_ABBREVIATION",
        "MATCHUP": "HOME_MATCHUP",
        "PTS": "HOME_PTS",
        "AST": "HOME_AST",
        "REB": "HOME_REB",
        "BLK": "HOME_BLK",
        "TOV": "HOME_TOV",
        "STL": "HOME_STL",
        "FG_PCT": "HOME_FG_PCT",
        "FG3_PCT": "HOME_FG3_PCT",
        "FT_PCT": "HOME_FT_PCT",
        "WL": "HOME_WL",
    },
    inplace=True,
)
# print(home_set.head(10))

away_set = work_set[work_set["MATCHUP"].str.contains("@")]
away_set.rename(
    columns={
        "TEAM_ID": "AWAY_TEAM_ID",
        "TEAM_ABBREVIATION": "AWAY_TEAM_ABBREVIATION",
        "PTS": "AWAY_PTS",
        "AST": "AWAY_AST",
        "REB": "AWAY_REB",
        "BLK": "AWAY_BLK",
        "TOV": "AWAY_TOV",
        "STL": "AWAY_STL",
        "FG_PCT": "AWAY_FG_PCT",
        "FG3_PCT": "AWAY_FG3_PCT",
        "FT_PCT": "AWAY_FT_PCT",
    },
    inplace=True,
)
# print(away_set.head(10))
games_merge = home_set.merge(away_set, on="GAME_ID")
# print(games_merge.head(10))
games_merge.drop(columns=["GAME_DATE_y", "MATCHUP", "HOME_MATCHUP"], inplace=True)
games_merge["WL"] = games_merge["WL"].apply(lambda W: 1 if W == "W" else 0)
games_merge.replace({"WL": {"W", 1}}, inplace=True)
print(games_merge.columns.tolist())
print(games_merge.head(10))
