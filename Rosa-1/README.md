# Rosa Project

## Overview
The Rosa project is designed to help users analyze delivery performance and profitability based on various parameters such as promise times, zones, time blocks, and costs associated with late deliveries. The application allows users to input their criteria and calculates the most profitable promise options.

## File Descriptions

### app2.py
This file contains the main application logic. It sets up a user interface that allows users to:
- Select a range of promise times.
- Choose a zone and time block.
- Adjust profit margin, churn per late order, and refund cost per late order.

It utilizes existing functionality from `net_profit.py` to calculate and display the most profitable promise options based on user input.

### data.py
This file exports constants `ZONES` and `TIME_BLOCKS`, which provide the available zones and time blocks for the user to select from in the app.

### costs.py
This file exports constants `COSTS`, which include the default values for:
- Profit margin
- Churn per late order
- Refund cost per late order

It may also contain functions to retrieve or validate these costs.

### promises.py
This file contains functions related to handling promise values, including any necessary calculations or validations for the promise times that users can select.

### delivery_times.py
This file exports the `delivery_times` function, which calculates delivery times based on the selected zone, time block, and promise values. This function is used in `app2.py` to determine the delivery performance based on user inputs.

### net_profit.py
This file contains the logic for calculating net profit based on delivery performance, costs, and user-defined parameters. It is utilized in `app2.py` to determine the most profitable promise options based on the user's selections.

## How to Run the Application
1. Ensure you have Python installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory in your terminal.
4. Run the application using the command:
   ```
   python app2.py
   ```
5. Follow the prompts to input your desired parameters.

## Contribution
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome!