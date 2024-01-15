import pickle
import traceback  

def make_prediction(df):
    try:

        #Fill missing values
        df.ffill(inplace=True)
        # Load the model
        with open(r'model', 'rb') as file:
            loaded_model = pickle.load(file)

        # Make predictions
        
        rf_prediction = loaded_model.predict(df)
        return rf_prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        traceback.print_exc()
        return None
 
