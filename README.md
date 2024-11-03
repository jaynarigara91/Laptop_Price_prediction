# 💻 Laptop Price Prediction

A data science project to predict laptop prices based on various features, built with **Streamlit** for an intuitive user interface and deployed in a **Docker** container. This project implements a **machine learning pipeline** and leverages a **voting model** to combine multiple algorithms for improved accuracy. 

---

## 📋 Project Overview

This **Laptop Price Prediction** project aims to provide a realistic price estimate for laptops based on features like processor, RAM, storage, screen size, and more. Utilizing a comprehensive dataset, the model processes and selects relevant features to predict prices, making it a valuable tool for users and retailers seeking current price predictions in a competitive market. 

Key steps include:
- **Data Preprocessing**: Cleaning, handling missing values, and feature engineering.
- **Machine Learning Pipeline**: A structured pipeline that integrates preprocessing and modeling.
- **Voting Model**: Combines multiple algorithms for a balanced approach, improving the robustness of predictions.

---

## 🚀 Features

- **Streamlit Interface**: A responsive web app that allows users to interactively input laptop features and receive predictions.
- **Machine Learning Pipeline**: An end-to-end automated pipeline for data preprocessing and model execution.
- **Voting Model**: Combines predictions from multiple algorithms for enhanced accuracy.
- **Docker Integration**: Runs seamlessly in a Docker container, ensuring consistency and portability across environments.

---

## 🛠️ Technologies Used

- **Python**: Core programming language for data processing and machine learning.
- **Streamlit**: Builds an interactive web app for user-friendly interaction.
- **Scikit-Learn**: Provides tools for pipelines, model building, and the voting ensemble.
- **Pandas**: For data manipulation and preprocessing.
- **Docker**: Packages the application into a container for easy deployment.

---

## ⚙️ Project Structure

├── Laptop_price.ipynb # Jupyter notebook with EDA and model building steps.  
├── app.py # Streamlit app for the interactive web interface.  
├── Dockerfile # Docker configuration for containerizing the app.  
├── requirements.txt # List of required packages and dependencies.  
└── README.md # Project documentation and overview.  


---

## 📈 Model Pipeline and Voting Model

This project uses a machine learning pipeline that includes data preprocessing, feature selection, and model training. The **Voting Model** combines predictions from several algorithms (such as Random Forest, Gradient Boosting, etc.) to enhance prediction accuracy and reliability, taking advantage of each algorithm’s strengths in a balanced way.

---

## 🖥️ Running the Project

### Prerequisites

- **Docker** installed on your machine.
- **Python** environment with dependencies from `requirements.txt`.

---

## 📊 Results

The model has been evaluated using standard regression metrics and has achieved reliable performance on test data, providing accurate price predictions based on various laptop specifications.
