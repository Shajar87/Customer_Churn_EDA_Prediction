import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
import seaborn as sns
from main_module import predict 

# reading csv file
data = pd.read_csv("data\Customer-Churn-Records.csv")
df = data.head(5)

#set title of the App
st.title("Customer Churn Predictor")
nav_options = ["Home", "Predictor", "Contact Us"]
nav = st.sidebar.radio("Navigation", nav_options)


#If "Home" is selected as the navigator 
if nav == 'Home':
    st.image("Data\churn_image.png")
    st.write(f' ### Welcome to Customer Churn Predictor App.')
    st.write("""Your go-to solution for predicting and preventing customer churn in the banking sector. 
             Our cutting-edge app utilizes a powerful machine learning model 
that has been meticulously trained on an extensive dataset of bank customers,
providing you with invaluable insights to proactively retain your customer base.""")

    if st.checkbox("Show me the dataset."):
                    st.table(df)
                     
                    if st.checkbox("Want to see some graphs?"): 
                        graph = st.selectbox("Select any one graph to see.",['Churn Rate by Age','Churn Rate by Active Member Status'])
                        if graph == 'Churn Rate by Active Member Status':
                            fig, ax = plt.subplots()    
                            churn_rate_by_active = df.groupby('IsActiveMember')['Exited'].mean().reset_index()
                            
                            # Bar plot
                            plt.bar(churn_rate_by_active['IsActiveMember'], churn_rate_by_active['Exited'], color=['skyblue', 'lightcoral'])
                            
                            plt.xlabel('Active Member (1) or Not (0)')
                            plt.ylabel('Churn Rate')
                            plt.title('Churn Rate by Active Member Status')
                            
                            # Set x-axis ticks and labels
                            plt.xticks(churn_rate_by_active['IsActiveMember'], ['Not Active', 'Active'])
                            # Display the plot in Streamlit
                            st.pyplot(fig)

                        if graph == 'Churn Rate by Age':
                            type = st.selectbox("What Kind of Graph?",['Interactive','Non-Interactive'])
                            if type == "Non-Interactive":
                                # Calculate churn rate by age
                                churn_rate_age = data.groupby('Age')['Exited'].mean().reset_index()

                                # Create scatter plot for churn rate by age
                                fig, ax = plt.subplots()
                                ax.scatter(churn_rate_age['Age'], churn_rate_age['Exited'], label='Churn Rate by Age', color='blue', alpha=0.7)

                                plt.title('Churn Rate by Age')
                                plt.xlabel('Age')
                                plt.ylabel('Churn Rate')
                                plt.legend()

                                st.pyplot(fig)

                            if type == "Interactive":
                                # Calculate churn rate by age
                                churn_rate_age = data.groupby('Age')['Exited'].mean().reset_index()

                                # Create an interactive scatter plot
                                fig = px.scatter(data_frame=churn_rate_age, x='Age', y='Exited',
                                                title='Churn Rate by Age')
                                fig.update_layout(xaxis_title='Age', yaxis_title='Churn Rate')
                                st.plotly_chart(fig)


                    

#If "Predictor" is selected as the navigator 
elif nav == "Predictor":
    st.header('Predict Customer Churn')
    column_names = [
        'CreditScore', 'Age', 'Tenure', 'Balance', 
        'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 
        'Complain', 'Satisfaction Score', 'Point Earned',
    ]

    # Initialize a dictionary to store user input
    user_input = {}

    # Get user input for each column
    for column in column_names:
        st.write(f"### {column}")
        
        if column in ['HasCrCard', 'IsActiveMember', 'Complain']:
                unique_identifier = f"selectbox_{column}"
                user_input[column] = st.selectbox(f"Select 0 (for No), 1 (for Yes)", [1, 0], key=unique_identifier)

        
        else:
            user_input[column] = st.number_input(f"Enter {column}", value=0)
    
    
    


    # Display the entered values
    if st.button("Show Entered Values"):
        st.write("Entered Values:")
        user_series = pd.Series(user_input)
        st.write(user_series)

        # Convert the series to a DataFrame
        user_df = pd.DataFrame(user_series).transpose()
        user_df.columns = column_names
        st.write("Entered Values as DataFrame:")
        st.write(user_df)
        user_df.to_csv('data\entered_dataset.csv', index=False)
        st.success("Entered Values saved to 'Data\entered_dataset.csv'")


    if st.button('Show Prediction'):
        prediction = predict()
        prediction_scalar = int(prediction)
        pred_dic = {0:"Customer will not churn.",1:"Customer will churn."}
        st.write(f'## {pred_dic[prediction_scalar]}')

#If "Contact Us" is selected as the navigator 
elif nav == 'Contact Us':
    st.write(f'### {"Please Fill Out Your Details And Submit it."}')
    first, last = st.columns(2)
    first.text_input("First Name")
    last.text_input("Last Name")

    email, mob = st.columns([3, 1])
    email.text_input("Email ID")
    mob.text_input("Mobile Number")

    det = st.columns(2)  
    det[0].text_input("What is the purpose of reaching out to us?")


    ag,sub = st.columns(2)
    ag.checkbox("I Agree")
    sub = st.button("Submit")
    if sub == True:
         st.success("Submitted successfully.")
