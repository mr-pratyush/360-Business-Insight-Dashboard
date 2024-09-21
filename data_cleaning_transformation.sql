-- Data Cleaning and Transformation Script

-- 1. Remove duplicate orders
WITH CTE_Orders AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY OrderID ORDER BY OrderDate) AS rn
    FROM Orders
)
DELETE FROM CTE_Orders WHERE rn > 1;

-- 2. Update status to 'Pending' for orders not fulfilled within 3 days
UPDATE Orders
SET Status = 'Pending'
WHERE FulfillmentDate IS NULL AND DATEDIFF(DAY, OrderDate, GETDATE()) > 3;

-- 3. Normalize customer names to title case
UPDATE Customers
SET FirstName = UPPER(LEFT(FirstName, 1)) + LOWER(SUBSTRING(FirstName, 2, LEN(FirstName))),
    LastName = UPPER(LEFT(LastName, 1)) + LOWER(SUBSTRING(LastName, 2, LEN(LastName)));

-- 4. Calculate Customer Lifetime Value (CLV)
ALTER TABLE Customers ADD CLV DECIMAL(10, 2);

UPDATE Customers
SET CLV = (SELECT SUM(OrderAmount) FROM Orders WHERE Orders.CustomerID = Customers.CustomerID);

-- 5. Create summary table for financials
CREATE TABLE Financials_Summary AS
SELECT 
    FinancialYear,
    SUM(TotalRevenue) AS TotalRevenue,
    SUM(CostOfGoodsSold) AS TotalCOGS,
    SUM(OperatingExpenses) AS TotalOperatingExpenses
FROM Financials
GROUP BY FinancialYear;

-- 6. Ensure no negative values in financials
UPDATE Financials
SET TotalRevenue = CASE WHEN TotalRevenue < 0 THEN 0 ELSE TotalRevenue END,
    CostOfGoodsSold = CASE WHEN CostOfGoodsSold < 0 THEN 0 ELSE CostOfGoodsSold END,
    OperatingExpenses = CASE WHEN OperatingExpenses < 0 THEN 0 ELSE OperatingExpenses END;
