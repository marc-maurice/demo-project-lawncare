import random
import string
from datetime import datetime, timedelta

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_daily_data(date):
    data = []
    num_locations = 50
    locations = [f"Location_{i}" for i in range(1, num_locations + 1)]
    lawn_packages = [f"Package_{i}" for i in range(1, 11)]

    for location in locations:
        num_transactions = random.randint(10, 100)
        for _ in range(num_transactions):
            transaction_id = generate_random_string(12)
            register_id = f"Reg_{random.randint(1, 10)}"
            employee_id = f"Emp_{random.randint(1, 100)}"
            item_id = generate_random_string(8)
            item_category = random.choice(["Fertilizer", "Lawn Maintenance", "Pest Control"])
            item_cost = round(random.uniform(20, 500), 2)
            item_tax = round(item_cost * 0.08, 2)
            payment_method = random.choice(["Credit Card", "Cash", "Mobile Payment"])
            payment_status = random.choice(["Paid", "Pending", "Failed"])
            transaction_notes = random.choice(["", "Customer mentioned service issues", "Discount applied manually"])
            discount_code = random.choice(["DISC10", "NEWCUST", "SUMMER20", ""])
            refund_id = generate_random_string(10) if random.random() < 0.01 else ""
            void_flag = random.choice([True, False]) if refund_id else False

            customer_id = generate_random_string(10)
            communication_opt_in = random.choice([True, False])
            lawn_package = random.choice(lawn_packages)
            revenue = round(random.uniform(300, 2000), 2)

            # Create transaction record
            record = {
                "transaction_id": transaction_id,
                "register_id": register_id,
                "location": location,
                "transaction_date": date.strftime("%Y-%m-%d"),
                "payment_method": payment_method,
                "payment_status": payment_status,
                "transaction_notes": transaction_notes,
                "discount_code": discount_code,
                "refund_id": refund_id,
                "void_flag": void_flag,
                "employee_id": employee_id,
                "item_id": item_id,
                "item_category": item_category,
                "item_cost": item_cost,
                "item_tax": item_tax,
                "customer_id": customer_id,
                "lawn_package": lawn_package,
                "revenue": revenue,
                "communication_opt_in": communication_opt_in,
                "transaction_timestamp": date.isoformat(),
                "audit_flag": False,
                "last_update_timestamp": date.isoformat(),
            }
            data.append(record)
    return data
