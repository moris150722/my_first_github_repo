import csv
from statistics import mean

# Helper function to convert win-loss record to win percentage
def win_percentage(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

# Read the CSV file and inspect headers
with open("nba_standings.csv", mode="r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    print("CSV Headers:", headers)
    data = [row for row in csv.DictReader(file)]

# Print the first row to inspect the data structure
if data:
    print("First row:", data[0])

# Adjust this part if the headers in your CSV file are different
# Ensure column names are consistent with the CSV file
expected_headers = ["Conference", "Team", "W-L", "PCT", "GB", "PF", "PA", "HOME", "AWAY", "CONE", "DIV", "L10", "STRK"]
if headers != expected_headers:
    print("Warning: The CSV headers do not match the expected headers.")
    print("Please check the column names and adjust the script accordingly.")

# (1) Eastern Conference teams with Home win percentage lower than Away win percentage
eastern_teams = [
    row["Team"]
    for row in data
    if "Conference" in row and row["Conference"] == "Eastern" and "HOME" in row and "AWAY" in row 
    and win_percentage(row["HOME"]) < win_percentage(row["AWAY"])
]


print("\n(1) Eastern Conference teams with Home win percentage lower than Away win percentage:")
for team in eastern_teams:
    print(team)

# (2) Conference with a higher average difference of PF minus PA


conference_differences = {"Eastern": [], "Western": []}

for row in data:
    if "PF" in row and "PA" in row:
        pf = int(row["PF"])
        pa = int(row["PA"])
        diff = pf - pa
        conference_differences[row["Conference"]].append(diff)

avg_diff_eastern = mean(conference_differences["Eastern"])
avg_diff_western = mean(conference_differences["Western"])
higher_avg_diff_conference = "Eastern" if avg_diff_eastern > avg_diff_western else "Western"

print("\n(2) Conference with a higher average difference of PF minus PA:")
print(higher_avg_diff_conference)

# (3) Ranking teams based on win percentage against the other conference
# Assuming "vs_Other" column contains the record against the other conference in "Wins-Losses" format
teams_vs_other_pct = []

for row in data:
    if "vs_Other" in row:
        vs_other_pct = win_percentage(row["vs_Other"])
        teams_vs_other_pct.append((row["Team"], vs_other_pct))

ranking = sorted(teams_vs_other_pct, key=lambda x: x[1], reverse=True)

print("\n(3) Ranking of all teams based on win percentage against the other conference:")
for rank, (team, pct) in enumerate(ranking, start=1):
    print(f"{rank}. {team} ({pct:.3f})")
