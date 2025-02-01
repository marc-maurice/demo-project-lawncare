WITH transactions AS (
    SELECT 
        t.TRANSACTION_ID,
        t.CUSTOMER_ID,
        c.CUSTOMER_NAME,
        c.CUSTOMER_SEGMENT,
        t.SERVICE_DATE,
        t.SERVICE_TYPE,
        t.PAYMENT_AMOUNT,
        t.REFUND_AMOUNT,
        t.PAYMENT_STATUS,
        t.PAYMENT_METHOD
    FROM {{ ref('clean_transactions') }} t
    LEFT JOIN {{ ref('core_dim_customers') }} c
    ON t.CUSTOMER_ID = c.CUSTOMER_ID
)
SELECT * FROM transactions