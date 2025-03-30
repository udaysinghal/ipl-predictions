'''
import joblib
import pandas as pd

# Define the path to your downloaded model
model_path = r"D:\IPL predictions\new_model (1).pkl"

# Load the trained model
try:
    final_model = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Model file not found! Please check the path.")
    exit()

# Sample input data (Modify as per your match details)
l = [['Sunrisers Hyderabad','Lucknow Super Giants', 'Hyderabad', 
                0, 120, 10, 0.00, 0.00, 180]]
# Define the column names (Make sure these match your model's requirements)
columns = ['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left',
           'wickets_left', 'current_run_rate', 'required_run_rate', 'target']

# Convert to DataFrame
season_25 = pd.DataFrame(l, columns=columns)

# Predict win probability
win_probability = final_model.predict_proba(season_25)

# Display results
print(f"Winning Probability:\n{win_probability}")
print(f"Win probability of SH: {win_probability[0][1] * 100:.2f}%")
print(f"Win probability of LSG: {win_probability[0][0] * 100:.2f}%")
'''
import joblib
import pandas as pd

# Load the trained model
model_path = r"D:\IPL predictions\new_model (1).pkl"
final_model = joblib.load(model_path)
print("Model loaded successfully!")

# List of valid teams and venues
teams = [
    'Kolkata Knight Riders', 'Chennai Super Kings', 'Delhi Daredevils',
    'Royal Challengers Bangalore', 'Rajasthan Royals', 'Kings XI Punjab',
    'Deccan Chargers', 'Mumbai Indians', 'Pune Warriors',
    'Kochi Tuskers Kerala', 'Sunrisers Hyderabad', 'Rising Pune Supergiants',
    'Gujarat Lions', 'Rising Pune Supergiant', 'Delhi Capitals',
    'Punjab Kings', 'Gujarat Titans', 'Lucknow Super Giants',
    'Royal Challengers Bengaluru'
]

venues = [
    'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
    'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
    'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Rajkot', 'Kanpur', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
    'Lucknow', 'Guwahati', 'Mohali'
]

# Function to get user input with validation
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please enter a valid option.")

# Taking user input for teams and venue
batting_team = get_valid_input("Enter the batting team: ", teams)
bowling_team = get_valid_input("Enter the bowling team: ", teams)
venue = get_valid_input("Enter the match venue: ", venues)

# Asking whether the match has started
match_started = input("Has the match started? (yes/no): ").strip().lower()

if match_started == "no":
    # Set pre-match default values
    runs_left = 0
    balls_left = 120
    wickets_left = 10
    current_run_rate = 0.00
    required_run_rate = 0.00
    target = 180
else:
    # Take live match input
    runs_left = int(input("Enter runs left: "))
    balls_left = int(input("Enter balls left: "))
    wickets_left = int(input("Enter wickets left: "))
    current_run_rate = float(input("Enter current run rate: "))
    required_run_rate = float(input("Enter required run rate: "))
    target = int(input("Enter target score: "))

# Create a pandas DataFrame instead of a NumPy array
columns = ['batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left',
           'wickets_left', 'current_run_rate', 'required_run_rate', 'target']

features = pd.DataFrame([[batting_team, bowling_team, venue, runs_left, balls_left, 
                          wickets_left, current_run_rate, required_run_rate, target]],
                        columns=columns)

# Predict winning probability
winning_probability = final_model.predict_proba(features)

print(f"\nWinning Probability:\n{winning_probability}")
print(f"Win probability of Batting team: {winning_probability[0][1] * 100:.2f}%")
print(f"Win probability of Bowling team: {winning_probability[0][0] * 100:.2f}%")
