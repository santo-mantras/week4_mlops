import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
import os

def split_data(input_file, output_dir):
    """Reads a CSV, splits it, and saves the output."""
    print(f"Reading data from {input_file}...")
    df = pd.read_csv(input_file)

    # Split data 70:30
    train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
    print(f"Data split complete. Training set: {train_df.shape[0]} rows, Test set: {test_df.shape[0]} rows.")

    # Save the splits to the output directory
    train_path = os.path.join(output_dir, "train-data.csv")
    test_path = os.path.join(output_dir, "test-data.csv")

    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    print(f"Train and test data saved to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split CSV data into training and testing sets.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument("--output", type=str, required=True, help="Directory to save the split files.")
    args = parser.parse_args()

    split_data(args.input, args.output)
