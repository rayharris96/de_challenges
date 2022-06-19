-- Query 1: I want to know the list of our customers and their spending.

-- Aggregate sale price information based on customer id
with base_agg as (
    select
        customer_id,
        count(distinct serial_number)           as total_cars_bought,
        sum(price)                              as total_transaction_spent,
        avg(price)                              as average_sum_spent,
        min(date)                               as earliest_transaction_date,
        max(date)                               as latest_transaction_date,
    from sales
    group by customer_id
)
-- Join with customer table to get the name and phone
select
    customer_id,
    customers.name,
    customers.phone,
    total_cars_bought,
    total_transaction_spent,
    average_sum_spent,
    earliest_transaction_date,
    latest_transaction_date
from base_agg
left join customers using (customer_id);
