# Promised Time Calculator

This project is a Streamlit application designed to help users calculate the recommended promised time for service delivery based on various inputs. The application takes into account factors such as promised time range, profit margin, estimated churn, and refund cost to provide a calculated recommendation.

## Project Structure

- `app.py`: The main entry point of the Streamlit application. It sets up the user interface, collects user inputs for promised time calculations, and displays the recommended promised time based on the calculations.
  
- `src/calculator.py`: Contains the function `calculate_recommended_time`, which implements the logic for calculating the recommended promised time based on the user's inputs.

- `src/constants.py`: Defines constants used in the application, such as `ZONES` and `TIME_BLOCKS`, which represent the available zones and time blocks for user selection.

- `requirements.txt`: Lists the dependencies required to run the Streamlit application, including Streamlit itself and any other necessary libraries.

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```
   streamlit run app.py
   ```

## Usage

Once the application is running, users can interact with the interface to select their desired promised time range, zone, time block, profit margin, estimated churn, and refund cost. After entering the necessary inputs, click the "Calculate Recommended Promised Time" button to receive the recommended time in minutes.

## License

This project is licensed under the MIT License.