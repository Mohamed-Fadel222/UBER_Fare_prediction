﻿# UBER_Fare_prediction

This project aims to predict Uber fare amounts based on various factors such as pickup and dropoff locations, distance, and time of day.

## Preprocessing

The following preprocessing steps were performed on the dataset:
- Handling missing values
- Removing outliers based on fare amount and distance
- Feature engineering: extracting year, month, weekday, and hour from pickup datetime
- Calculating distance between pickup and dropoff locations using geopy library
- Encoding categorical variables using LabelEncoder
- Scaling numerical features using StandardScaler

## Model Building

Several regression models were trained and evaluated for fare prediction:
- Linear Regression
- Huber Regression
- Ridge Regression
- Lasso Regression
- ElasticNet Regression
- Random Forest Regression
- XGBoost Regression
- Decision Tree Regression

## Evaluation

The performance of each model was evaluated using Mean Squared Error (MSE) on both training and testing datasets.

## Model Deployment

The XGBoost Regression model was chosen as the final model and saved as a pickle file named "XGboost.pkl".


