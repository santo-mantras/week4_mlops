import pandas as pd
import joblib
import pytest
from sklearn.metrics import accuracy_score

# Define a minimum accuracy threshold for the model
MINIMUM_ACCURACY = 0.80

@pytest.fixture(scope="session")
def data():
    """Fixture to load test data for all tests."""
    try:
        test_data = pd.read_csv("work_data/v2/test-data.csv")
        return test_data
    except FileNotFoundError:
        pytest.fail("Test data 'work_data/v2/test-data.csv' not found. Did you run 'dvc pull'?")

@pytest.fixture(scope="session")
def model():
    """Fixture to load the v2 model for all tests."""
    try:
        trained_model = joblib.load("artifacts/v2_model.joblib")
        return trained_model
    except FileNotFoundError:
        pytest.fail("Model 'artifacts/v2_model.joblib' not found. Did you run 'dvc pull'?")

def test_data_validation(data):
    """
    Tests if the dataset has the expected columns.
    """
    print("Running data validation test...")
    expected_columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species"
    ]
    assert all(col in data.columns for col in expected_columns), "Data is missing expected columns."
    assert not data.isnull().values.any(), "There are null values in the test data."
    print("Data validation successful.")


def test_model_evaluation(model, data):
    """
    Tests if the model's accuracy is above the defined threshold.
    """
    print("Running model evaluation test...")
    X_test = data.drop("species", axis=1)
    y_test = data["species"]

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"Model accuracy on test set: {accuracy:.4f}")
    assert accuracy >= MINIMUM_ACCURACY, f"Model accuracy {accuracy:.4f} is below the threshold of {MINIMUM_ACCURACY}."
    print("Model evaluation successful.")
