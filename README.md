# Bank Customer Churn EDA and Prediction

**Overview:**
Bank Customer Churn EDA and Prediction is a data science project that combines exploratory data analysis (EDA) and predictive modeling to gain insights into customer behavior and forecast potential churn in the banking sector. The project utilizes machine learning "Random Forest" technique, visualizations, and an interactive user interface to provide a comprehensive solution for understanding and addressing customer churn.


**Dataset Used Review**

| RowNumber | CustomerId | Surname   | CreditScore | Geography | Gender | Age | Tenure | Balance   | NumOfProducts | HasCrCard | IsActiveMember | EstimatedSalary | Exited | Complain | Satisfaction Score | Card Type | Point Earned |
|-----------|------------|-----------|-------------|-----------|--------|-----|--------|-----------|---------------|-----------|----------------|-----------------|--------|----------|--------------------|-----------|--------------|
| 1         | 15634602   | Hargrave  | 619         | France    | Female | 42  | 2      | 0         | 1             | 1         | 1              | 101348.88       | 1      | 1        | 2                  | DIAMOND   | 464          |
| 2         | 15647311   | Hill      | 608         | Spain     | Female | 41  | 1      | 83807.86  | 1             | 0         | 1              | 112542.58       | 0      | 1        | 3                  | DIAMOND   | 456          |
| 3         | 15619304   | Onio      | 502         | France    | Female | 42  | 8      | 159660.8  | 3             | 1         | 0              | 113931.57       | 1      | 1        | 3                  | DIAMOND   | 377          |


---


## Key Features:

### 1. Exploratory Data Analysis (EDA):
- Conducted a thorough analysis of the dataset to unveil patterns, trends, and correlations.
- Identified pivotal features influencing customer churn.

### 2. Data Visualization:
- Visualized EDA results through a variety of charts and graphs.
- Developed interactive visualizations for an intuitive exploration of churn-related insights.

### To see detailed analysis, checkout the notebook:https://github.com/Shajar87/Customer_Churn_EDA_Prediction/blob/main/Bank_Customer_Churn_Analysis.ipynb

### 3. Predictive Modeling:
- Implemented a predictive model using the machine learning "Random Forest" technique.
- Trained the model on the historical customer data to forecast future churn risks.
- Evaluated model performance using relevant metrics.

### 4. Analysis Findings and Recommendations:
- Summarize key findings from the analysis, such as customer demographics, churn patterns, and factors influencing churn.
- Provide insights into the causes behind the findings.
- Make recommendations based on the analysis, such as strategies to decrease churn rate.

### 5. User Interaction:
- Created a Streamlit-based interactive interface, enabling users to explore the dataset seamlessly.
- Enabled real-time prediction of customer churn based on user inputs.
- Integrated a user-friendly "Contact Us" form for inquiries and submissions (backend work pending).

     
### 6. How to Use:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app with `streamlit run app.py`.
   

### 7. Contributing:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push to your branch.
- Submit a pull request, and your contributions will be reviewed.


Feel free to explore, contribute, and provide feedback on this project!

