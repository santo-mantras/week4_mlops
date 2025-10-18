import pandas as pd
import argparse
import os

def augment_data(input1_path, input2_path, output_path):
    """Combines two CSV files into one."""
    print(f"Reading data from {input1_path} and {input2_path}...")
    df1 = pd.read_csv(input1_path)
    df2 = pd.read_csv(input2_path)

    augmented_df = pd.concat([df1, df2], ignore_index=True)
    print(f"Augmentation complete. Total rows: {augmented_df.shape[0]}")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    augmented_df.to_csv(output_path, index=False)
    print(f"Augmented data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Augment (combine) two data files.")
    parser.add_argument("--input1", type=str, required=True, help="Path to the first input CSV.")
    parser.add_argument("--input2", type=str, required=True, help="Path to the second input CSV.")
    parser.add_argument("--output", type=str, required=True, help="Path to save the combined CSV.")
    args = parser.parse_args()

    augment_data(args.input1, args.input2, args.output)
