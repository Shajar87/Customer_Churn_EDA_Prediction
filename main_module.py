# main_module.py
import pandas as pd
from prediction_module import make_prediction

def predict():
                    # Load your dataset
                    data = pd.read_csv(r'data\entered_dataset.csv', encoding='utf-8')

                    # Make predictions
                    prediction = make_prediction(data)

                    #print("Scaled Data Shape",scaled_data.shape)
                    #print("\nPrediction about Customer:", prediction)
                    return prediction
print("Prediction about the customer:", predict())