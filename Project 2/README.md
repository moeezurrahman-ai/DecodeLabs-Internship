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
