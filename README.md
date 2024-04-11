# cintel-06-custom
## Project: Custom Tips Dashboard

### Objective
The objective of this project is to create a customized app that filters the data from the tips seaborn data frame.

### The Data
The data in this app comes from the tips seaborn dataset and includes the total bill, tip amount, sex of the payor, if the payor smokes, day of the transaction, time of the transaction, and party size. 

### Tip Dashboard
Taking the seaborn data, this dashboard can be used to evaluate things like tip percent based on total bill size, number of transactions where the payor smokes, and many other things that you might find important. 

### Filters
- App users can filter the app by tip size
- App users can filter the app based on the sex of the payor
- App users can filter the app based on whether or not the payor smokes

### Dark/Light Mode
App contains a toggle where you can switch the app from dark mode to light mode. 

### Value Boxes
This app contains several value boxes that are updated based on the use of the filters including:
- Value box that counts the number of transactions that meet the filters
- Value box that averages the tip amount of the transactions that meet the filters
- Value box that calculates the tip percentage of the total bill for transactions that meet the filters

### Data Grid
The app contains a data grid that can be sorted. It is also on an accordion panel, so it can be opened or closed as you please. 

### Violin Plot
The violin plot evaluates the tip percent between male and female payors, while also evaluating the tip percentage between smokers and non-smokers from the given sex. The violin plot contains quartiles every 25% to evaluate differences in median tips between the groups. 

### Scatter Plot
The Scatter Plot compares the total bill to the tip amount, and contains a guideline that shows what a 10% tip would be at each transaction dollar amount. This allows users to easily identify outliers in the data, as well as better identify the trend of the data. 



