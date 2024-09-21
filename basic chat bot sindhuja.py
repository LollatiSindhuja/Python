import os
import shutil
import pandas as pd
import glob

def organize_files(directory):
    """Organize files into subfolders based on their file types."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            ext = filename.split('.')[-1]
            # Create a folder for the file type if it doesn't exist
            type_folder = os.path.join(directory, ext)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            # Move the file into the corresponding folder
            shutil.move(os.path.join(directory, filename), os.path.join(type_folder, filename))
    print("Files organized by type.")

def clean_data(input_file, output_file):
    """Remove duplicates from a CSV file and save cleaned data."""
    df = pd.read_csv(input_file)
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}.")

def delete_temp_files(directory):
    """Delete temporary files from a specified directory."""
    temp_files = glob.glob(os.path.join(directory, '*.tmp'))
    for file in temp_files:
        os.remove(file)
    print("Temporary files deleted.")

if __name__ == "__main__":
    # Uncomment the task you want to run

    # Task 1: Organize Files
    # organize_files('/path/to/your/directory')

    # Task 2: Clean Data
    # clean_data('input_data.csv', 'cleaned_data.csv')

    # Task 3: Delete Temporary Files
    # delete_temp_files('/path/to/your/temp/directory')
