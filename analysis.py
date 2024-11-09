import matplotlib.pyplot as plt
import seaborn as sns
import web_scrape

def stats_analysis():
    df = web_scrape.nba_teams_preseason_stats()

    # Offense Ratings Formula
    def estimated_possession(): #Correct
        fga = df['FGA'].astype(float)
        fta = df['FTA'].astype(float)
        orb = df['ORB'].astype(float)
        tov = df['TOV'].astype(float)

        df['Estimated Possession'] = fga + 0.44 * fta - orb + (tov / 2)

        return df['Estimated Possession']

    def point_scored(): #Correct
        ppg = df['PPG'].astype(float)
        gp = df['GP'].astype(float)
        df['Points Scored'] = ppg * gp

        return df['Points Scored']

    def eff_fg(): #Correct
        fga = df['FGA'].astype(float)
        fgm = df['FGM'].astype(float)
        three = df['3PM'].astype(float)

        fgm_three = fgm + 0.5 * three
        div_by_fga = fgm_three / fga

        df["EFG%"] = div_by_fga * 100

        return df['EFG%']

    def true_shooting():
        total_points = df['Points Scored'].astype(float)
        fga = df['FGA'].astype(float)
        fta = df['FTA'].astype(float)

        each_fga = fga*5
        each_fta = fta*5

        denominator = 2 * (each_fga + 0.44 * each_fta)
        nume_deno = total_points / denominator
        df['TS%'] = nume_deno * 100

        return df['TS%']

    def pace():
        mpg = df['MPG'].astype(float)
        poss = df['Estimated Possession'].astype(float)

        df['Pace'] = (poss / mpg) * 48

        return df['Pace']

    def turnover_ratio():
        tov = df['TOV'].astype(float)
        poss = df['Estimated Possession'].astype(float)

        df['TO Ratio'] = (tov / poss) * 100

        return df['TO Ratio']

    df['Estimated Possession'] = round(estimated_possession(), 1)
    df['Points Scored'] = round(point_scored())
    df['EFG%'] = round(eff_fg(), 1)
    df['TS%'] = round(true_shooting(), 1)
    df['Pace'] = round(pace(), 1)
    df['TO Ratio'] = round(turnover_ratio(), 1)

    top_offensive_teams = (df['PPG'].astype(float) * 0.20) + (df['EFG%'].astype(float) * 0.20) + (df['TS%'].astype(float) * 0.15) + (df['APG'].astype(float) * 0.15) + (df['TO Ratio'].astype(float) * 0.05)

    df['Off Ratings'] = round(top_offensive_teams, 1)

    sorted_offense_team = df.sort_values(by='Off Ratings', ascending=False)

    top_10_offense_teams = sorted_offense_team.head(10)


    # Defensive Ratings Formula

    top_defensive_teams = (df['DRB'].astype(float) * 0.45) + (df['SPG'].astype(float) * 0.25) + (df['BPG'].astype(float) * 0.20) + (df['TOV'].astype(float) * 0.10)

    df['Def Ratings'] = round(top_defensive_teams, 1)

    sorted_defense_teams = df.sort_values(by='Def Ratings', ascending=False).head(10)
    
    return df


'''plt.figure(figsize=(14,8))

# Subplot 1: Top 10 Offensive Teams
plt.subplot(1, 2, 1)  # (1 row, 2 columns, 1st subplot)
sns.barplot(data = top_10_offense_teams, y="Team", x="Off Ratings", estimator="sum", ci=None, width=0.6)
plt.title("Top 10 Offensive Teams for 2024-2025 NBA Season\n(Based on Pre-Season Performance)")
plt.xlabel("Offensive Ratings")
plt.ylabel("Teams")

# Subplot 2: Top 10 Defensive Teams
plt.subplot(1, 2, 2)  # (1 row, 2 columns, 2nd subplot)
sns.barplot(data = sorted_defense_teams, y="Team", x="Def Ratings", estimator="sum", ci=None, width=0.6)
plt.title("Top 10 Defensive Teams for 2024-2025 NBA Season\n(Based on Pre-Season Performance)")
plt.xlabel("Defensive Ratings")
plt.ylabel("Teams")

plt.tight_layout() 
plt.show()'''
