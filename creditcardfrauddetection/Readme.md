# 🕵️‍♂️ Credit Card Fraud Detection Case Study

## 🔍 Problem Statement
The objective of this project is to predict fraudulent credit card transactions using machine learning techniques. The dataset used in this case study comes from a research collaboration between Worldline and the Machine Learning Group.

📊 **Dataset**: [Credit Card Fraud Detection - Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- Total Transactions: **284,807**  
- Fraudulent Transactions: **492**  
- Class Imbalance: Highly imbalanced (fraud class = 0.172%)

---

## 💼 Business Problem Overview
Credit card fraud poses a major threat to financial institutions, causing:

- Massive financial losses
- Reduced trust and credibility
- Customer dissatisfaction

According to the Nilson Report, banking fraud was estimated to reach **$30 billion** worldwide by 2020. Machine learning helps detect fraud by:

- Reducing manual reviews
- Lowering chargeback costs
- Minimizing false positives (legitimate transaction denials)

---

## 💳 Understanding Fraud
Fraud refers to unauthorized acts intended to gain financially by manipulating card information. Common fraud techniques include:

- **Skimming** (copying magnetic strip data)
- **Card alteration or duplication**
- **Lost or stolen cards**
- **Fraudulent telemarketing**

---

## 📚 Dataset Description

- **Time**: Seconds elapsed since the first transaction.
- **Amount**: Transaction amount.
- **V1 to V28**: Principal components obtained via PCA (for confidentiality).
- **Class**: Target variable (1 = Fraudulent, 0 = Legitimate).

🧪 Note: The dataset has undergone PCA, so normalization (like Z-scaling) is not required, but skewness should be checked.

---

## 🧭 Project Pipeline

### 1. Data Understanding
- Load the dataset and explore feature distributions.
- Analyze the structure of the dataset.
- Understand the imbalance and characteristics of fraud vs. non-fraud cases.

### 2. Exploratory Data Analysis (EDA)
- Perform univariate and bivariate analysis.
- Detect any skewness and apply transformations if necessary.
- Understand relationships between features and the target variable.

### 3. Train/Test Split
- Use stratified sampling or **k-fold cross-validation** to ensure representation of the minority (fraud) class.
- Split the data into training and testing sets.

### 4. Model Building & Hyperparameter Tuning
- Experiment with algorithms like:
  - Logistic Regression
  - Decision Trees / Random Forest
  - XGBoost
  - Neural Networks
- Apply sampling techniques:
  - SMOTE (Synthetic Minority Oversampling Technique)
  - Under-sampling
- Fine-tune model hyperparameters for best performance.

### 5. Model Evaluation
- Use metrics that account for class imbalance:
  - **Precision**
  - **Recall**
  - **F1-Score**
  - **AUC-ROC**
- Focus on minimizing **false negatives** (missed frauds).

---

## ✅ Conclusion
By using machine learning and proper data handling techniques, we can create models that efficiently detect fraudulent transactions, helping banks:
- Prevent financial losses
- Improve customer experience
- Enhance operational efficiency

---

## 📁 Resources
- 📦 Dataset: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
