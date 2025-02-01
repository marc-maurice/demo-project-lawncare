WITH payments AS (
    SELECT 
        TRANSACTION_ID,
        PAYMENT_AMOUNT,
        REFUND_AMOUNT,
        PAYMENT_STATUS,
        PAYMENT_METHOD
    FROM {{ source('demo_lawncare', 'stg_parquet') }}
)
SELECT * FROM payments
