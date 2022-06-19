with base as (
    -- CTE 1: Column correctness. Ensures each column only contains data of that column
    select
        case when name is null and price ~ '[a-zA-Z]+'
            then price::text
        else name::text
            end as name,
        case when name is null and price ~ '[a-zA-Z]+'
            then null 
        else price
            end as price
    from dataset2
),
base2 as (
    -- CTE2: name splitting, price resolution of traling zero
    select 
        string_to_array(name, ' ')                  as name_array,
        array_length(string_to_array(name, ' '), 1) as length,
        -- removes trailing zero and cast as float
        ltrim(price, '0')::float                    as price
    from base
),
base3 as (
    -- CTE3: First name, last name resolution, price above 100 column criteria definition
    select
        case when length = 2
            -- if there are only two elements in array, the first one is first name
            then name_array[1]
        when length = 3
            -- if there are three elements in array, the first one is either the first name or salutation
            then 
                case when name_array[1] ~ '\w+\.' or name_array[1] ~* 'miss|mister'
                    then name_array[2]
                else name_array[1]
                    end
        when length = 4
            -- if there are four elements in array, the second one is the first name
            then name_array[2]
                                                                                                                    end as first_name,
        case when length = 2
            -- if there are only two elements in array, the second one is last name
            then name_array[2]
        when length = 3
            -- if there are three elements in array, the last one is either the last name or degree
            then 
                case when name_array[length] ~ '\w+\.' or name_array[length] ~* 'md|dds|dvm|jr.|phd'
                    then name_array[length - 1]
                else name_array[length]
                    end
        when length = 4
            -- if there are four elements in array, the third one is the last name
            then name_array[3]
                                                                                                                    end as last_name,
        price,
        case when price > 100
            then true
            else false
                                                                                                                    end as above_100
    from base2
)
select 
    first_name,
    last_name,
    price,
    above_100
from base3
where first_name notnull and last_name notnull --rows without a name is deleted
