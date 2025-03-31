from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_path = "new_model (1).pkl"
final_model = joblib.load(model_path)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form inputs
        batting_team = request.form["batting_team"]
        bowling_team = request.form["bowling_team"]
        venue = request.form["venue"]
        match_started = request.form["match_started"]

        # Pre-match or live match?
        if match_started == "no":
            runs_left, balls_left, wickets_left = 0, 120, 10
            current_run_rate, required_run_rate, target = 0.00, 0.00, 180
        else:
            runs_left = int(request.form["runs_left"])
            balls_left = int(request.form["balls_left"])
            wickets_left = int(request.form["wickets_left"])
            current_run_rate = float(request.form["current_run_rate"])
            required_run_rate = float(request.form["required_run_rate"])
            target = int(request.form["target"])

        # Create a DataFrame for prediction
        features = pd.DataFrame([[batting_team, bowling_team, venue, runs_left, balls_left, 
                                  wickets_left, current_run_rate, required_run_rate, target]],
                                columns=['batting_team', 'bowling_team', 'city', 'runs_left', 
                                         'balls_left', 'wickets_left', 'current_run_rate', 
                                         'required_run_rate', 'target'])

        # Make prediction
        winning_probability = final_model.predict_proba(features)

        # Get probabilities
        batting_win_prob = round(winning_probability[0][1] * 100, 2)
        bowling_win_prob = round(winning_probability[0][0] * 100, 2)

        return render_template("result.html", 
                               batting_team=batting_team, 
                               bowling_team=bowling_team,
                               batting_win_prob=batting_win_prob, 
                               bowling_win_prob=bowling_win_prob)
    
    return render_template("index.html", teams=teams, venues=venues)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)