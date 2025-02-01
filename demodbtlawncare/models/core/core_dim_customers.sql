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
    FROM {{ ref('clean_customers') }}
)
SELECT * FROM customers