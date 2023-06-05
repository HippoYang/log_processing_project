import pandas as pd

def clean_logs(log_file):
    """
    Clean the log file by removing corrupted rows and return the cleaned DataFrame.
    """
    # Read the log file into a DataFrame
    columns = ['sng_id', 'user_id', 'country']
    try:
        df = pd.read_csv(log_file, sep='|', header=None, names=columns, dtype=str, on_bad_lines='skip')
    except pd.errors.ParserError:
        print(f"Error reading log file: {log_file}")
        return None

    # Drop rows with missing or invalid values
    try:
        df = df.dropna()
        df = df[df['sng_id'].str.isdigit()]
        df = df[df['user_id'].str.isdigit()]
        df = df[df['country'].str.isalpha() & (df['country'].str.len() == 2)]
    except KeyError:
        print(f"Error cleaning log file: {log_file}")
        return None
    
    # Save the cleaned data to a new file
    cleaned_file = f"cleaned_{log_file}"
    df.to_csv(cleaned_file, sep='|', header=False, index=False)
    print(f"Cleaned log file saved as: {cleaned_file}")

    # Return the cleaned DataFrame
    return df


def compute_top_songs(df, groupby_column, output_prefix, date):
    """
    Compute the top 50 songs for countries or users and save the results to a file.

    Parameters:
    - df: DataFrame containing the cleaned log data
    - groupby_column: Column name to group the data by (e.g., 'country', 'user_id')
    - output_prefix: Prefix for the output file name
    """
    # Group the data by the specified column and count the occurrences of each song
    top_songs_per_group = df.groupby([groupby_column, 'sng_id']).size().reset_index(name='count')

    # Sort the data within each group by count in descending order
    top_songs_per_group.sort_values([groupby_column, 'count'], ascending=[True, False], inplace=True)

    # Keep only the top 50 songs for each group
    top_songs_per_group = top_songs_per_group.groupby([groupby_column]).head(50)

    # Create a 'result' column with song_id:count format
    top_songs_per_group['result'] = top_songs_per_group['sng_id'] + ':' + top_songs_per_group['count'].astype(str)

    # Group the data by the groupby_column and join the 'result' values into a single string
    top_songs_per_group = top_songs_per_group.groupby([groupby_column])['result'].apply(','.join).reset_index()
    
    # Save the results to an output file
    output_file = f"{output_prefix}_{date}.txt"
    top_songs_per_group.to_csv(output_file, sep='|', header=False, index=False)


def main():
    # Set the path for the log file
    log_file = "sample_listen-2023-05_2Mlines.log"

    # Clean the log file
    cleaned_df = clean_logs(log_file)
    
    # Extract the date
    date = 'YYYYMMDD'

    # Compute the top 50 songs per country
    compute_top_songs(cleaned_df, 'country', 'country_top50', date)
    print(f"Top 50 songs per country saved as: country_top50_{date}.txt")

    # Compute the top 50 songs per user
    compute_top_songs(cleaned_df, 'user_id', 'user_top50', date)
    print(f"Top 50 songs per user saved as: user_top50_{date}.txt")
    

if __name__ == '__main__':
    main()
