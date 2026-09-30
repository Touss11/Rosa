# Rosa

## First Prompt :

I built a code that allows the user to :

- set the range of promised times to try
- select a zone and a time block
- adjust the profit margin per order, estimated churn per late order, and the refund cost per late order

I would like you to create a Streamlit App with :

- A dipstick where the user can select the range of promises time in minutes with a 5-min step
- A dropdown list for the user to select a zone
- A dropdown list for the user to select a time_block
- A text bar in which the user can adjust the profit margin per order
- A text bar in which the user can adjust the estimated churn per late order
- A text bar in which the user can adjust the refund cost per late order

Using the code (specifically net_profit.py), the App should display the recommended promised time for the selected zone and time block after clicking on a button.

You can use the notebook-to-streamlit skill to make the App

## Second Prompt :

I would like you to start again from the beginning.

Take the files I have uploaded on VS Code ie :

- Promises.py
- Data.py
- delivery_times.py
- Costs.py
- net_profit.py

This code allows the user to :

- set the range of promised times to try

- select a zone and a time block

- adjust the profit margin per order, estimated churn per late order, and the refund cost per late order

From these files, I want you to design an App (which code you will put in the file app2.py) that present to the user : 

- A dipstick where the user can select the range of promises time in minutes with a 5-min step

- A dropdown list for the user to select a zone

- A dropdown list for the user to select a time_block

- A text bar in which the user can adjust the profit margin per order in dollar, not in percentage

- A text bar in which the user can adjust the estimated churn per late order in dollar, not in percentage

- A text bar in which the user can adjust the refund cost per late order in dollar, not in percentage

Using the code (specifically net_profit.py), the App should display the recommended promised time for the selected zone, time block, profit margin, churn per late order and refund cost per late order after clicking on a button.

It should display the most profitable promise options, as the net_profit code is trying to show.

For instance, if the selected :

- Zone is north
- time_block is Lunch
- Profit margin is 9$
- churn per late order is 1.8$
- refund cost per late order is 10$

The app should display which promise is the most profitable for Rosa
