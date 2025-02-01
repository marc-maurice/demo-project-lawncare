WITH customers AS (
    SELECT 
        CUSTOMER_ID,
        CUSTOMER_NAME,
        CUSTOMER_AGE,
        CUSTOMER_GENDER,
        CUSTOMER_EMAIL,
        CUSTOMER_PHONE,
        CUSTOMER_TYPE,
        CUSTOMER_SEGMENT
    FROM {{ source('demo_lawncare', 'stg_parquet') }}
)
SELECT * FROM customers
