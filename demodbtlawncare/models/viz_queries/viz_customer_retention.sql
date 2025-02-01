WITH customer_activity AS (
    SELECT 
        t.CUSTOMER_ID,
        COUNT(t.TRANSACTION_ID) AS TRANSACTION_COUNT
    FROM {{ ref('core_fact_transactions') }} t
    GROUP BY t.CUSTOMER_ID
)
SELECT 
    CASE 
        WHEN TRANSACTION_COUNT = 1 THEN 'One-Time Customer'
        WHEN TRANSACTION_COUNT BETWEEN 2 AND 5 THEN 'Low Engagement'
        ELSE 'Loyal Customer'
    END AS CUSTOMER_TYPE,
    COUNT(DISTINCT customer_activity.CUSTOMER_ID) AS TOTAL_CUSTOMERS,
    SUM(t.PAYMENT_AMOUNT) AS TOTAL_REVENUE
FROM customer_activity
JOIN {{ ref('core_fact_transactions') }} t 
    ON customer_activity.CUSTOMER_ID = t.CUSTOMER_ID
GROUP BY CUSTOMER_TYPE
ORDER BY TOTAL_CUSTOMERS DESC