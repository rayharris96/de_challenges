-- Query 2: I want to find out the top 3 car manufacturers that customers bought by sales (quantity) 
-- and the sales number for it in the current month.

with base as (
    -- CTE1: Narrow down car serial number transactions this month
    select
        serial_number, -- assumed is unique for each car
        date -- assume date format is YYYY-MM-DD
    from sales
    where date_part('year', date)::int = date_part('year', now())::int
    and date_part('month', date)::int = date_part('month', now())::int
),
joined as (
    -- CTE2: Join transactions with car table - get the count of cars sold by their respective manufacturers
    select
        cars.manufacturer,
        count(distinct base.serial_number) as total_car_sold_by_manufacturer
    from base
    inner join cars on base.serial_number = cars.serial_number
    group by cars.manufacturer
)
select
    manufacturer,
    total_car_sold_by_manufacturer
from joined
order by 2 desc limit 3; -- Order by top 3 sold
