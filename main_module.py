# main_module.py
import pandas as pd
import pickle
import traceback  

def predict():
                    # Load your dataset
                    data = pd.read_csv(r'data\entered-dataset.csv')

                    # Call prediction module 
                    prediction = make_prediction(data)

                    #print("Scaled Data Shape",scaled_data.shape)
                    #print("\nPrediction about Customer:", prediction)
                    return prediction

def make_prediction(df):
    try:

        #Fill missing values if any
        df.ffill(inplace=True)
        # Load the pre-trained model
        with open(r'model', 'rb') as file:
            loaded_model = pickle.load(file)

        # Make predictions
        
        rf_prediction = loaded_model.predict(df)
        return rf_prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        traceback.print_exc()
