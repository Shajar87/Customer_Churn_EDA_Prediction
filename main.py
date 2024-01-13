# main_module.py
import pandas as pd
from preprocessing_module import preprocess_data
from prediction_module import make_prediction

def predict():
                    # Load your dataset
                    data = pd.read_csv(r'data\entered_dataset.csv', encoding='utf-8')

                    # Data scaling
                    scaled_data = preprocess_data(data)

                    # Make predictions
                    prediction = make_prediction(scaled_data)

                    #print("Scaled Data Shape",scaled_data.shape)
                    #print("\nPrediction about Customer:", prediction)
                    return prediction
