{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "24cb122a-24b0-4cb2-8c86-9c047fea4079",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.preprocessing import LabelEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8a2d7acf-aa07-47c5-968a-93aa164057f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "heart_data = pd.read_csv('C:/Users/HP/OneDrive/Desktop/Documents/Degree Stuff/heart.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6ed424c3-f088-4984-87b3-2293351331a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "label_encoders = {}\n",
    "for column in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:\n",
    "    le = LabelEncoder()\n",
    "    heart_data[column] = le.fit_transform(heart_data[column])\n",
    "    label_encoders[column] = le"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4c2b34fb-2a35-4048-9117-9ca3c4b4a86c",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = heart_data.drop('HeartDisease', axis=1)\n",
    "y = heart_data['HeartDisease']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "86868553-ac84-491f-bef9-6650d0b558e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = GaussianNB()\n",
    "model.fit(X, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "f62a73d1-9743-4ed9-b4e0-6275fca3e0a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title(\"Heart Disease Prediction\")\n",
    "st.write(\"This app predicts whether a person is likely to have heart disease based on input features.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2f099f72-d2f3-4162-b1b6-35a76dce9c8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-09-07 13:34:31.174 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "age = st.number_input('Age', min_value=1, max_value=120, value=25)\n",
    "sex = st.selectbox('Sex', label_encoders['Sex'].classes_)  # Use encoded class options\n",
    "chest_pain_type = st.selectbox('Chest Pain Type', label_encoders['ChestPainType'].classes_)\n",
    "resting_bp = st.number_input('Resting Blood Pressure', min_value=0, max_value=200, value=120)\n",
    "cholesterol = st.number_input('Cholesterol', min_value=0, max_value=600, value=200)\n",
    "fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])\n",
    "resting_ecg = st.selectbox('Resting ECG', label_encoders['RestingECG'].classes_)\n",
    "max_hr = st.number_input('Max Heart Rate', min_value=60, max_value=220, value=150)\n",
    "exercise_angina = st.selectbox('Exercise Angina', label_encoders['ExerciseAngina'].classes_)\n",
    "oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=6.0, value=1.0, step=0.1)\n",
    "st_slope = st.selectbox('ST Slope', label_encoders['ST_Slope'].classes_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "75b6ede9-5363-47d3-a903-fd51c6f20ac6",
   "metadata": {},
   "outputs": [],
   "source": [
    "input_data = np.array([[age,\n",
    "                        label_encoders['Sex'].transform([sex])[0],\n",
    "                        label_encoders['ChestPainType'].transform([chest_pain_type])[0],\n",
    "                        resting_bp,\n",
    "                        cholesterol,\n",
    "                        fasting_bs,\n",
    "                        label_encoders['RestingECG'].transform([resting_ecg])[0],\n",
    "                        max_hr,\n",
    "                        label_encoders['ExerciseAngina'].transform([exercise_angina])[0],\n",
    "                        oldpeak,\n",
    "                        label_encoders['ST_Slope'].transform([st_slope])[0]]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "950a3ecc-8516-4707-8d6d-f852d57642a0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
