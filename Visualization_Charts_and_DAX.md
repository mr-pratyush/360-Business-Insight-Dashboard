# Visualization Charts and DAX Used

## Visualization Details

### 1. KPI Cards
- **Metrics:** Total Revenue, Total Orders, Average NPS Score
- **Purpose:** Quick insights into overall performance.

### 2. Line Chart
- **X-Axis:** Order Date
- **Y-Axis:** Order Amount
- **Purpose:** Visualize trends in sales over time.

### 3. Stacked Bar Chart
- **Axis:** Region
- **Values:** Count of Orders, Total Revenue
- **Purpose:** Understand regional performance.

### 4. Pie Chart
- **Values:** Customer Distribution by Region
- **Purpose:** Visualize customer demographics.

### 5. Waterfall Chart
- **Categories:** Financial Year
- **Values:** Total Revenue, Cost of Goods Sold, Operating Expenses
- **Purpose:** Show financial performance breakdown.

### 6. Matrix Table
- **Rows:** Customer Names
- **Columns:** Order Count, Total Spend
- **Values:** Calculate and display spend per customer.

## DAX Formulas

### Total Revenue
```DAX
Total Revenue = SUM(Orders[OrderAmount])

Average NPS = AVERAGE(Customers[NPSScore])
```
### Order Fulfillment Rate
```
Fulfillment Rate = 
DIVIDE(
    COUNTROWS(FILTER(Orders, Orders[Status] = "Fulfilled")),
    COUNTROWS(Orders),
    0
)
```
### Gross Margin
```
Gross Margin = 
DIVIDE(
    [Total Revenue] - SUM(Financials[CostOfGoodsSold]),
    [Total Revenue],
    0
)


