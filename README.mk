# Log Processing Project

This project is aimed at processing log files containing information about songs listened to by users in different countries. The goal is to compute the top 50 songs for each country and the top 50 songs for each user, and save the results to separate output files.

## Solution Overview

The solution is implemented using Python and the pandas library for data processing. It follows a modular approach with separate functions for different tasks. Here's an overview of the solution components:

1. `clean_logs(log_file)`: This function reads the log file, removes corrupted rows, and saves the cleaned data to a new file.

2. `compute_top_songs(df, groupby_column, output_prefix)`: This function computes the top 50 songs based on the specified group (country or user) and saves the results to an output file.

3. `main()`: This is the main function that orchestrates the entire process. It performs the following steps:
   - Cleans and reads the log file.
   - Computes the top 50 songs for each country and saves the results.
   - Computes the top 50 songs for each user and saves the results.

## Usage

Follow the steps below to run the project and compute the files daily:

1. Clone the repository or download the project files.

2. Install the required dependencies. Ensure that Python 3.x and the pandas library are installed.

3. Place the log file (`sample_listen-2023-05_2Mlines.log`) in the project directory.

4. Open a terminal or command prompt and navigate to the project directory.

5. Run the following command to execute the script:

   ```bash
   python main.py

This will execute the main function and perform the log processing tasks.

6. Once the script completes execution, you will find two output files in the project directory:
- `country_top50_YYYYMMDD.txt`: Contains the top 50 songs for each country, with the date appended to the file name.
- `user_top50_YYYYMMDD.txt`: Contains the top 50 songs for each user, with the date appended to the file name.

7. To automate the process and run it daily, you can set up a cron job or a scheduled task on your operating system. Configure it to execute the script at the desired time every day.

## License

This project is licensed under the [MIT License](LICENSE).

