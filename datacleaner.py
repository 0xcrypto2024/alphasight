import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

XLSX_FILE = os.environ.get("XLSX_FILE", "raw.xlsx")
OUTPUT_TSV = os.environ.get("OUTPUT_TSV", "cleaned_projects.tsv")

def clean_and_save_data(xlsx_filepath=XLSX_FILE, output_tsv=OUTPUT_TSV):
    """Cleans the Monday.com XLSX export (starting from row 6) and saves as TSV."""
    try:
        df = pd.read_excel(xlsx_filepath, header=4)  # header is row 6 (index 5)
        print("Columns found by pandas:")
        print(df.columns)

        # Explicitly check for columns and handle if not present.
        if "Name" not in df.columns or "Website" not in df.columns:
            missing_cols = [col for col in ["Name", "Website"] if col not in df.columns]
            raise KeyError(f"Missing columns: {missing_cols}. Check Excel file and code.")

        cleaned_df = df[["Name", "Website"]]  # Select desired columns
        cleaned_df.to_csv(output_tsv, sep='\t', index=False)
        print(f"Cleaned data saved to: {output_tsv}")

    except FileNotFoundError:
        print(f"Error: File '{xlsx_filepath}' not found.")
    except KeyError as e:        # Handle KeyError (missing column names)
        print(f"KeyError: {e}") # Print the detailed KeyError message
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    clean_and_save_data()
