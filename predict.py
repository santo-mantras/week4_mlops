import pandas as pd
import joblib
import argparse

def make_predictions(model_path, data_path):
    """Loads a model and makes predictions on new data."""
    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)

    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    X_test = df.drop('species', axis=1)
    y_test = df['species']

    print("Making predictions...")
    predictions = model.predict(X_test)

    print("\n--- Prediction Output ---")
    print("Sample of Test Data:")
    print(y_test.head())
    print("\nSample of Predictions:")
    print(predictions[:5])
    print("-------------------------\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make predictions using a trained model.")
    parser.add_argument("--model", type=str, required=True, help="Path to the trained model file.")
    parser.add_argument("--data", type=str, required=True, help="Path to the data for prediction.")
    args = parser.parse_args()

    make_predictions(args.model, args.data)
