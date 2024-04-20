import copy
from constants import PLAYERS, TEAMS

def clean_data():
    cleaned_players = []
    for player in PLAYERS:
        player_copy = copy.deepcopy(player)
        player_copy['height'] = int(player_copy['height'].split(" ")[0])
        player_copy['experience'] = True if player_copy['experience'] == 'YES' else False
        cleaned_players.append(player_copy)
    return cleaned_players

def balance_teams(cleaned_players):
    num_players_team = len(cleaned_players) // len(TEAMS)
    teams = {team: [] for team in TEAMS}
    for index, player in enumerate(cleaned_players):
        teams[TEAMS[index % len(TEAMS)]].append(player)
    return teams

def display_teams():
    print("\nTeams available:")
    for i, team in enumerate(TEAMS, 1):
        print(f"  {chr(64+i)}) {team}")

def display_team_stats(team, teams):
    print(f"\nTeam: {team} Stats")
    print("--------------------")
    players = teams[team]
    print(f"Total players: {len(players)}")
    print("\nPlayers on Team:")
    player_names = ', '.join([player['name'] for player in players])
    print(f"  {player_names}\n")

def menu(teams):
    while True:
        print("\n---- MENU ----")
        print("Here are your choices:")
        print("  A) Display Team Stats")
        print("  B) Quit")
        choice = input("Enter an option: ").strip().upper()

        if choice == 'A':
            display_teams()
            team_choice = input("Enter an option: ").strip().upper()
            if team_choice in ['A', 'B', 'C']:
                team = TEAMS[ord(team_choice) - 65]  # Convert 'A', 'B', 'C' to 0, 1, 2 index
                display_team_stats(team, teams)
                input("Press ENTER to continue...")
            else:
                print("Invalid option. Please try again.")
        elif choice == 'B':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    print("Welcome to the Basketball Team Stats Tool!")
    cleaned_players = clean_data()
    teams = balance_teams(cleaned_players)
    menu(teams)

if __name__ == "__main__":
    main()
