/* Top 5 Funds by AUM */
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


 /* Average NAV Per Month */

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

/* Transactions By State */
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

/* Funds with Expense Ratio Below 1% */
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

/* Average Investment Amount by Transaction Type */
SELECT
    transaction_type,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;

/* Top 10 States by Total Investment */

SELECT
    state,
    ROUND(SUM(amount_inr),2) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

/* Funds by Risk Category */


SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;

/* Top 10 Funds by 3-Year Return */

SELECT
    scheme_name,
    return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

/* Average AUM by Fund House */

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

/* Average AUM by Fund House */

SELECT
    fund_house,
    ROUND(AVG(aum_crore),2) AS avg_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY avg_aum DESC;


