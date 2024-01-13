import pickle
import traceback  


def make_prediction(processed_data):
    try:
        # Load the model
        with open(r'rf_model', 'rb') as file:
            loaded_model = pickle.load(file)

        # Make predictions
        
        rf_prediction = loaded_model.predict(processed_data)
        return rf_prediction
    except Exception as e:
        print(f"Error making prediction: {e}")
        traceback.print_exc()
        return None
 