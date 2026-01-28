🏡 House Price Predictor

A machine learning project that predicts house prices using historical house data from Bengaluru.
This end-to-end solution includes data cleaning, exploratory analysis, model training (Random Forest), and deployment using Streamlit.

📁 Repository Contents
File / Folder	Description
app.py	Streamlit app for real-time price prediction
EDA_analysis.ipynb	Notebook for exploratory data analysis
cleaned_house_data.csv	Preprocessed dataset used for training
Bengaluru_House_Data.csv	Raw dataset
RFmodelHPP.pkl	Serialized Random Forest model
requirements.txt	Python dependencies
house_logo.png	Logo used in app
venv/	Local virtual environment (should be ignored)
🚀 Project Description

This project uses machine learning to predict house prices based on key features such as:

✔ Location
✔ Area (sq. ft)
✔ Number of bedrooms
✔ Number of bathrooms

The model was trained on a cleaned dataset and deployed as an interactive web app using Streamlit. Users can input house details to get instant price predictions.

🧠 Features

Data preprocessing and cleaning

Exploratory Data Analysis

Feature encoding and transformation

Random Forest Regression model

Model persistence using pickle

Streamlit deployment for user interface

🧪 Installation

Clone the repository:

git clone https://github.com/Srinivaslv2109/House-Price-Predictor.git
cd House-Price-Predictor


Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

📊 Run the Streamlit App
streamlit run app.py


This will open a web interface where you can input house features and get predicted prices in real time.
🧠 How It Works

Load and clean the dataset

Encode categorical variables

Train a Random Forest Regression model

Save the model as RFmodelHPP.pkl

Use the model in app for live prediction

📈 Model Evaluation (Example)
Metric	Value
Training Accuracy	0.89322
Testing Accuracy	0.84675
Model Used	Random Forest Regressor
