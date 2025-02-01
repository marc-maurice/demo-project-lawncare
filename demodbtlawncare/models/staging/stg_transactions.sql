WITH transactions AS (
    SELECT 
        TRANSACTION_ID,
        CUSTOMER_ID,
        SERVICE_DATE,
        SERVICE_TYPE,
        PAYMENT_AMOUNT,
        REFUND_AMOUNT,
        PAYMENT_STATUS,
        PAYMENT_METHOD
    FROM {{ source('demo_lawncare', 'stg_parquet') }}
)
SELECT * FROM transactions
