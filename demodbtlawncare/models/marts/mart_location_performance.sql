WITH location_performance AS (
    SELECT 
        SERVICE_TYPE,
        SUM(PAYMENT_AMOUNT) AS TOTAL_REVENUE,
        COUNT(TRANSACTION_ID) AS TOTAL_TRANSACTIONS,
        AVG(PAYMENT_AMOUNT) AS AVG_TRANSACTION_VALUE
    FROM {{ ref('core_fact_transactions') }}
    GROUP BY SERVICE_TYPE
)
SELECT * FROM location_performance