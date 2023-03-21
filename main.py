import random
from collections import defaultdict

class Team:
    def __init__(self, name, division, coach, stadium_pref, start_time_pref):
        self.name = name
        self.division = division
        self.coach = coach
        self.stadium_pref = stadium_pref
        self.start_time_pref = start_time_pref

class Game:
    def __init__(self, home_team, away_team, stadium, start_time):
        self.home_team = home_team
        self.away_team = away_team
        self.stadium = stadium
        self.start_time = start_time

def generate_schedule(teams):
    # Divide teams into their respective divisions
    divisions = defaultdict(list)
    for team in teams:
        divisions[team.division].append(team)

    # Create list of all possible games
    all_games = [(home_team, away_team) for division in divisions.values() 
                 for i, home_team in enumerate(division) 
                 for away_team in division[i+1:]
                 if home_team.coach != away_team.coach]

    # Sort games by number of stadium and start time preferences
    all_games.sort(key=lambda x: (x[0].stadium_pref.count(x[1].stadium_pref),
                                  x[0].start_time_pref.count(x[1].start_time_pref)))

    # Create list of scheduled games
    scheduled_games = []
    while all_games:
        home_team, away_team = all_games.pop(0)
        common_stadiums = set(home_team.stadium_pref) & set(away_team.stadium_pref)
        common_start_times = set(home_team.start_time_pref) & set(away_team.start_time_pref)

        for stadium in (common_stadiums or home_team.stadium_pref):
            for start_time in (common_start_times or home_team.start_time_pref):
                scheduled_games.append(Game(home_team, away_team, stadium, start_time))
                break
            else:
                continue
            break
        else:
            raise ValueError("невозможно")

    return scheduled_games


# Define the teams in the league
teams = [
    Team("Team A", "Division 1", "Coach X", ["Stadium A", "Stadium B"], ["12:00", "13:00", "14:00"]),
    Team("Team B", "Division 1", "Coach Y", ["Stadium A", "Stadium C"], ["14:00", "15:00"]),
    Team("Team C", "Division 1", "Coach Z", ["Stadium C"], ["15:00", "16:00"]),
    Team("Team D", "Division 2", "Coach W", ["Stadium B", "Stadium C"], ["13:00", "14:00"]),
    Team("Team E", "Division 2", "Coach X", ["Stadium A", "Stadium B"], ["12:00", "13:00", "14:00"]),
    Team("Team F", "Division 2", "Coach Y", ["Stadium A", "Stadium C"], ["14:00", "15:00"]),
    Team("Team G", "Division 2", "Coach Z", ["Stadium C"], ["15:00", "16:00"])]

schedule = generate_schedule(teams)

for game in schedule:
    print(f"{game.home_team.name} vs {game.away_team.name} at {game.stadium} ({game.start_time})")