import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import argparse
import os

def train_model(train_data_path, test_data_path, model_output_path):
    """Trains a model, evaluates it, and saves it."""
    print("Reading training and testing data...")
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    # Separate features (X) and target (y)
    X_train = train_df.drop('species', axis=1)
    y_train = train_df['species']
    X_test = test_df.drop('species', axis=1)
    y_test = test_df['species']

    # 3. Initialize and train the model
    print("Training Decision Tree model...")
    model = DecisionTreeClassifier(max_depth=3, random_state=1)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 4. Make predictions
    print("Making predictions on the test set...")
    y_pred = model.predict(X_test)

    # 5. Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")

    # Save the trained model
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)
    print(f"Model saved to {model_output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a Decision Tree classifier.")
    parser.add_argument("--train_data", type=str, required=True, help="Path to training data CSV.")
    parser.add_argument("--test_data", type=str, required=True, help="Path to test data CSV.")
    parser.add_argument("--model_output", type=str, required=True, help="Path to save the trained model.")
    args = parser.parse_args()

    train_model(args.train_data, args.test_data, args.model_output)
