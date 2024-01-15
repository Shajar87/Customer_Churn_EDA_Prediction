import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
import plotly.express as px
import seaborn as sns
from main_module import predict 

# reading csv file
data = pd.read_csv("Customer_Churn_EDA_Prediction\data\Customer-Churn-Records.csv")
df = data.head(5)

#set title of the App
st.title("Customer Churn Predictor")
nav_options = ["Home", "Predictor", "Contact Us"]
nav = st.sidebar.radio("Navigation", nav_options)


if nav == 'Home':
    with st.container(border= True):
        st.image("Data\churn_image.png")
        st.write(f' ### :red[Welcome to Customer Churn Predictor App]')
        st.write("""Your go-to solution for predicting and preventing customer churn in the banking sector. 
                Our cutting-edge app utilizes a powerful machine learning method :blue[**"Random Forest"**] 
    that has been meticulously trained on an extensive dataset of bank customers,
    providing you with invaluable insights to proactively retain your customer base.""")
    st.divider()

    if st.checkbox("Show me the dataset."):
                    st.table(df)
                     
                    if st.checkbox("Want to see some graphs?"): 
                        graph = st.selectbox("Select any one graph to see.",['Churn Rate by Age','Churn Rate by Complain Status'])
                        if graph == 'Churn Rate by Complain Status':
                            fig, ax = plt.subplots()

                            #plt.figure(figsize=(10, 6))
    
                            churn_rate_by_Complain = df.groupby('Complain')['Exited'].mean().reset_index()
                            
                            # Bar plot
                            plt.bar(churn_rate_by_Complain['Complain'], churn_rate_by_Complain['Exited'], color=['skyblue', 'lightcoral'])
                            
                            plt.xlabel('Complain Status')
                            plt.ylabel('Churn Rate')
                            plt.title('Churn Rate by Complain Status')
                            
                            # Set x-axis ticks and labels
                            plt.xticks(churn_rate_by_Complain['Complain'], ['No Complain', 'Complain'])
                            
                            st.pyplot(fig)
                            with st.expander("See Explaination:"):
                                     st.write('''- **Insights:** Customers with active complaints have a higher churn rate. Customers without any complaints have almost negligible churn rate.
- **Possible Cause:** Active complaints could indicate dissatisfaction with the bank's services, unresolved issues, or a negative customer experience. Customers who have complaints and feel unheard or unsatisfied with the bank's response are more likely to churn.''')

                        if graph == 'Churn Rate by Age':
                            type = st.selectbox("What Kind of Graph?",['Interactive','Non-Interactive'])
                            if type == "Non-Interactive":
                                # Assuming churn_rate_age is your DataFrame
                                churn_rate_age = data.groupby('Age')['Exited'].mean().reset_index()

                                # Create scatter plot for churn rate by age
                                fig, ax = plt.subplots()
                                ax.scatter(churn_rate_age['Age'], churn_rate_age['Exited'], label='Churn Rate by Age', color='blue', alpha=0.7)

                                # Customize the plot
                                plt.title('Churn Rate by Age')
                                plt.xlabel('Age')
                                plt.ylabel('Churn Rate')
                                plt.legend()

                                # Display the plot in Streamlit
                                st.pyplot(fig)
                                with st.expander("See Explaination:"):
                                     st.write('''- **Insights:** From the scatter plot, it can be seen that
Customers of age between 45 - 70 have higher tendency to leave the bank.
- **Possible Cause:** Older customers may be more likely to consider switching banks due to life changes, retirement, or seeking better financial products and services.''')

                            if type == "Interactive":
                                # Calculate churn rate by age
                                churn_rate_age = data.groupby('Age')['Exited'].mean().reset_index()

                                # Create an interactive scatter plot
                                fig = px.scatter(data_frame=churn_rate_age, x='Age', y='Exited',
                                                title='Churn Rate by Age')
                                fig.update_layout(xaxis_title='Age', yaxis_title='Churn Rate')
                                st.plotly_chart(fig)
                                with st.expander("See Explaination:"):
                                     st.write('''- **Insights:** From the scatter plot, it can be seen that
Customers of age between 45 - 70 have higher tendency to leave the bank.
- **Possible Cause:** Older customers may be more likely to consider switching banks due to life changes, retirement, or seeking better financial products and services.''')



                    


elif nav == "Predictor":
    st.subheader(":red[Instructions Before Making Prediction:]")
    st.write("""1. Fill in the required values against each field.
2. Ensure the entered values are accurate and in the appropriate format.
3. Once all values are entered, You can see your entered values by clicking on **Show Entered Values**" button.
You can see the prediction directly by clicking on the "**Show Prediction**" button. """)
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
        
        # Display an input field based on the data type
        
       
        if column in ['HasCrCard', 'IsActiveMember', 'Complain']:
                unique_identifier = f"selectbox_{column}"
                user_input[column] = st.selectbox(f"Select 0 (No), 1 (Yes)", [1, 0], key=unique_identifier)

        
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
        user_df.to_csv('Data\entered_dataset.csv', index=False)
        st.success("Entered Values saved to 'Data\entered_dataset.csv'")

    if st.button('Show Prediction'):
        prediction = predict()
        prediction_scalar = int(prediction)
        pred_dic = {0:"Customer will not churn.",1:"Customer will churn."}
        st.write(f'## {pred_dic[prediction_scalar]}')


elif nav == 'Contact Us':
    st.write(f'### {"""Want to know more about us! Please Fill Out Your Details And Submit it to us."""}')
    with st.container(border= True):
         
        first, last = st.columns(2)
        first.text_input("First Name")
        last.text_input("Last Name")

        email, mob = st.columns([3, 1])
        email.text_input("Email ID")
        mob.text_input("Mobile Number")

        det = st.columns(2)  # Assuming you want two columns
        det[0].text_input("Purpose of reaching out to us?")


    ag,sub = st.columns(2)
    ag.checkbox("I Agree")
    sub = st.button("Submit")
    if sub == True:
         st.success("Submitted successfully.")
