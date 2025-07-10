
# 🏏 IPL Match Winner Predictor

This is a Flask-based web application that predicts the winning probabilities of IPL cricket matches using machine learning models.

## 🚀 Features

- Predict match winner probabilities based on teams, venue, and match status.
- Clean and interactive web UI using Flask and HTML templates.
- Pre-trained XGBoost model with encoded match data.
- CSV files for matches and deliveries for reference.
- Deployed on [Render](https://ipl-predictions-yxve.onrender.com)

## 📸 Live Demo

🔗 [Click here to try it out!](https://ipl-predictions-yxve.onrender.com)

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Scikit-learn**
- **XGBoost**
- **HTML/CSS**
- **Pandas / NumPy**

## 📂 Project Structure

├── app.py                  # Flask backend
├── predict\_ipl.py          # ML model logic
├── templates/
│   ├── index.html          # Main form UI
│   └── result.html         # Results display
├── matches.csv             # IPL match data
├── deliveries.csv          # IPL delivery-level data
├── new\_model.pkl           # Pre-trained XGBoost model
├── encoder.pkl             # OneHotEncoder used in model
├── requirements.txt        # Python dependencies
└── README.md               # This file



## ⚙️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/udaysinghal/ipl-predictions.git
   cd ipl-predictions


2. **Create a virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. Visit `http://localhost:5000` in your browser.

## 🧠 Model Info

* Trained using historical IPL data.
* Uses features like current score, wickets, overs, city, teams, etc.
* XGBoost classifier with preprocessing (OneHotEncoding).

## 🏁 Deployment

The app is deployed on:

* **Render:** [ipl-predictions-yxve.onrender.com](https://ipl-predictions-yxve.onrender.com)

> You can also deploy it using Vercel, Railway, or Google Cloud Run.

## 📧 Contact

**Uday Singhal**
📧 [udayalwayshere@gmail.com](mailto:udayalwayshere@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/uday-singhal)

```

---

Let me know if you want to add **screenshots**, **badges**, or a **GitHub deployment button** as well!
```
