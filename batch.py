import csv
from analysisengine import generate_summary, analyze_source
import os
from dotenv import load_dotenv
import pandas as pd
import time


load_dotenv()

CSV_FILE = os.environ.get("CSV_FILE", "cleaned_projects.tsv")

def analyze_projects_from_csv(csv_filepath=CSV_FILE):
    """Reads, analyzes, summarizes, and saves to CSV."""
    print(f"Analyzing projects from file: {csv_filepath}")
    try:
        df = pd.read_csv(csv_filepath, sep='\t')  # Use pandas for TSV/CSV

        # Create a new column for the summaries if it doesn't exist.
        if "Summary" not in df.columns:
            df["Summary"] = ""

        for index, row in df.iterrows():
            project_name = row["Name"]
            if pd.notna(project_name):
                print(f"Analyzing project: {project_name}")
                analyses = []

                if pd.notna(row["Website"]):
                    analyses.append(analyze_source("website", row["Website"]))
                
                # Check if "Twitter" column exists and has data before analyzing
                if "Twitter" in df.columns and pd.notna(row["Twitter"]):  
                    analyses.append(analyze_source("twitter", row["Twitter"]))

                # Check if "Github" column exists and has data before analyzing
                if "Github" in df.columns and pd.notna(row["Github"]):
                    analyses.append(analyze_source("github", row["Github"]))

                # Add other optional sources in the same way...

                if analyses:
                    combined_analysis = "\n\n".join(analyses)
                    summary = generate_summary(combined_analysis)
                    time.sleep(60)  # Add a delay to avoid rate limits
                    df.loc[index, "Summary"] = summary # Save the summary
                    print(f"Summary for {project_name}:\n{summary}\n---")

            else:
                print("Skipping row. Missing 'Project Name'.")

        df.to_csv(csv_filepath, sep='\t', index=False)  # Save the updated DataFrame

    except FileNotFoundError:
        print(f"Error: File '{csv_filepath}' not found.")
    except pd.errors.ParserError as e:  # Handle pandas parsing errors
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    analyze_projects_from_csv()
