# Task 2: Product Return Classification Model

## Project Description

This project implements a basic Machine Learning Classification Model using Python and Scikit-learn. The model predicts whether a product is likely to be returned based on various sales and customer-related features from a product sales dataset.

The project demonstrates the complete supervised learning workflow, including data loading, preprocessing, model training, testing, and performance evaluation.

---

## Objective

Build a basic classification model that:

- Loads and understands a dataset
- Preprocesses and prepares the data
- Splits the dataset into training and testing sets
- Trains a classification model
- Evaluates the model's performance

---

## Dataset

The dataset contains product sales information, including:

- Region
- Product
- Quantity
- Unit Price
- Store Location
- Customer Type
- Discount
- Salesperson
- Total Price
- Payment Method
- Promotion
- Shipping Cost
- Region Manager
- Returned (Target Variable)

The **Returned** column is used as the target variable for classification.

---

## Features

- Load dataset from an Excel file
- Display dataset information and structure
- Clean and preprocess the data
- Convert categorical data into numerical values
- Split data into training and testing sets
- Train a Decision Tree Classifier
- Evaluate model accuracy
- Generate a classification report
- Display sample predictions

---

## Technologies Used

- Python 3
- Pandas
- Scikit-learn
- OpenPyXL
- Visual Studio Code (VS Code)

---

## Project Structure

```
Task3/
│── classification_model.py
│── Product-Sales-Region.xlsx
│── README.md
```

---

## Required Libraries

Install the required libraries using:

```bash
pip install pandas scikit-learn openpyxl
```

---
## Sample Output

```
=========================================================
PRODUCT RETURN CLASSIFICATION MODEL
=========================================================

Dataset Loaded Successfully!

Training Records : 800
Testing Records  : 200

Model Training Completed Successfully!

Model Accuracy : 59.67%

Classification Report:

Precision    Recall    F1-Score
...
```

---

## Concepts Used

- Data Loading
- Data Exploration
- Data Cleaning
- Feature Selection
- One-Hot Encoding
- Train-Test Split
- Supervised Learning
- Decision Tree Classification
- Model Training
- Prediction
- Model Evaluation
- Accuracy Measurement

---

## Learning Outcomes

Through this project, I learned how to:

- Load datasets using Pandas
- Explore and understand structured data
- Prepare data for machine learning
- Encode categorical variables
- Split data into training and testing sets
- Train a supervised learning model
- Evaluate model performance using accuracy and classification reports
- Apply machine learning concepts to real-world datasets

---

## Future Enhancements

- Implement Random Forest Classifier for improved accuracy
- Perform feature engineering
- Handle missing values more effectively
- Compare multiple classification algorithms
- Visualize model performance using graphs
- Develop a web interface for real-time predictions

---

## Author

**Parvathi Dinesh Poduval**

AI Internship Project – Task 3

DecodeLabs AI Internship
