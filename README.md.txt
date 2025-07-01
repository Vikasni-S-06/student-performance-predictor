🎓 Student Performance Predictor

A simple yet powerful machine learning web app that predicts a student's math score based on their reading and writing scores. Built using Python, Streamlit, and scikit-learn.


📌 Overview

This project demonstrates how a basic Linear Regression model can be trained to predict one academic metric based on others. The model is trained on a real-world dataset of student performance and deployed as an interactive web app using Streamlit.


💡 Features

- 📊 Predicts Math Score based on Reading Score and Writing Score
- 🧠 Trained with Linear Regression
- 🎯 Uses StandardScaler for normalization
- ⚙️ Built with Streamlit for UI
- 📁 Organized, clean, and GitHub-ready structure


📁 Project Structure

student-performance-predictor/
├── app.py # Streamlit app
├── model.pkl # Trained Linear Regression model
├── scaler.pkl # Fitted StandardScaler
├── requirements.txt # List of Python dependencies
├── README.md # Project overview
├── data/
│ └── StudentsPerformance.csv # Original dataset
└── notebooks/
└── student_performance.ipynb # Jupyter notebook for training


🚀 How to Run Locally

🛠️ Prerequisites:

- Python 3.7+
- pip

🔧 Setup Instructions:


# Clone the repository
git clone https://github.com/Vikasni-S-06/student-performance-predictor.git
cd student-performance-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


📈 Dataset
Source: Kaggle - Students Performance in Exams

Features Used: reading score, writing score

Target Predicted: math score


📊 Sample Output
Input:

Reading Score: 88

Writing Score: 92

Output:

🎯 Predicted Math Score: 85.12


🧠 Technologies Used

Python

Pandas

Scikit-learn

Joblib

Streamlit


🙌 Acknowledgements
Streamlit for easy ML app deployment

Kaggle for providing the dataset

