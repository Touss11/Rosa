# Rosa Project

## Overview
The Rosa project is designed to calculate net profit based on various inputs, including costs, promise range, zone, and time block. The application provides a user-friendly interface using Streamlit, allowing users to easily adjust parameters and view results.

## Project Structure
```
rosa
├── net_profit.py
├── costs.py
├── data.py
├── requirements.txt
└── README.md
```

## Files Description

### `net_profit.py`
This file contains the logic for calculating net profit based on various inputs. It includes functions to compute profit based on costs, promise range, zone, and time block.

### `costs.py`
This file defines a dictionary `COSTS` that holds various cost parameters such as refund, churn orders, and margin. It also includes functionality to update these costs based on user input.

### `data.py`
This file contains data structures or constants used throughout the project, including initial values for costs or other relevant data.

### `requirements.txt`
This file lists the dependencies required for the project, including Streamlit and any other libraries needed to run the application.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app with the following command:
   ```
   streamlit run net_profit.py
   ```

## Usage Guidelines
- Open the Streamlit app in your web browser.
- Adjust the promise range, costs, zone, and time block using the provided input fields.
- The calculated net profit will be displayed based on the inputs provided.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.