# Project 2 — Iris Flower Classification

**Internship:** DecodeLabs  
**Project:** 2 — Data Classification Using AI

## Overview

This project demonstrates a basic supervised machine learning classification workflow using the Iris flower dataset.

A K-Nearest Neighbours (KNN) classifier is trained to predict the species of an Iris flower based on four measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The project covers dataset exploration, train-test splitting, model training, prediction, and model evaluation.

## Objective

The objective of this project is to:

- Load and understand a dataset.
- Separate input features from the target variable.
- Split the dataset into training and testing sets.
- Train a classification model.
- Evaluate the model's performance.
- Use the trained model to classify a new flower.

## Dataset

The project uses the Iris dataset.

The dataset contains:

- **150 samples**
- **4 numerical features**
- **3 target classes**
- **No missing values**

The three classes are:

- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`

Each species contains 50 samples.

### Features

| Feature | Description |
|---|---|
| `sepal_length` | Length of the sepal |
| `sepal_width` | Width of the sepal |
| `petal_length` | Length of the petal |
| `petal_width` | Width of the petal |

## Methodology

The project follows these steps:

```text
Iris Dataset
     ↓
Dataset Exploration
     ↓
Feature / Target Separation
     ↓
Train-Test Split
     ↓
KNN Model Training
     ↓
Prediction
     ↓
Model Evaluation
     ↓
New Flower Classification

---------

*1. Dataset Exploration

The dataset was inspected for:

Number of samples
Number of features
Missing values
Species distribution
Basic statistical information

No missing values were found, and the three species were evenly represented.

*2. Train-Test Split

The dataset was divided into:

80% training data: 120 samples
20% testing data: 30 samples

A fixed random state was used to make the experiment reproducible, and stratification was used to preserve the class distribution.

*3. Classification Algorithm

The project uses K-Nearest Neighbours (KNN) with:

n_neighbors = 5

KNN classifies a new sample by examining its nearest examples in the training dataset and assigning the class most commonly represented among those neighbours.

*Model Evaluation

The trained model was evaluated using the 30 samples in the test set.

*Accuracy
100.00%

The model correctly classified all 30 test samples.

*Classification Report
Class	           Precision	Recall	F1-Score
Iris-setosa	        1.00	      1.00	   1.00
Iris-versicolor        1.00	      1.00	   1.00
Iris-virginica	        1.00	      1.00        1.00

*Confusion Matrix
[[10  0  0]
 [ 0 10  0]
 [ 0  0 10]]

This indicates that all 30 test samples were classified correctly in this experiment.

*New Flower Prediction

The trained model was also tested with a new flower having the following measurements:

Sepal Length: 5.1
Sepal Width:  3.5
Petal Length: 1.4
Petal Width:  0.2

*Prediction
Iris-setosa

*Technologies Used
Python
Pandas
Scikit-learn

*Installation

Clone or download the project and install the required dependencies:

pip install -r requirements.txt

*How to Run

Make sure classification.py and iris.data are in the same directory.

Run:

python classification.py

*Project Structure
Project 2/
│
├── classification.py
├── iris.data
├── README.md
└── requirements.txt

*Conclusion

This project demonstrates a complete basic supervised machine learning classification workflow.

The KNN classifier achieved 100.00% accuracy on the 30-sample test set used in this experiment and successfully classified a new flower sample as Iris-setosa.
