# main_module.py
import pandas as pd
from prediction_module import make_prediction

def predict():
                    # Load your dataset
                    data = pd.read_csv(r'data\entered-dataset.csv')

                    # Call prediction module 
                    prediction = make_prediction(data)

                    #print("Scaled Data Shape",scaled_data.shape)
                    #print("\nPrediction about Customer:", prediction)
                    return prediction
print("Prediction about the customer:", predict())
