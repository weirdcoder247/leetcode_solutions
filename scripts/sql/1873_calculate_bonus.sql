select a.employee_id
    , coalesce(bonus, 0) as bonus
from Employees a
left join
    (select employee_id, salary as bonus
    from Employees
    where left(name, 1) != 'M'
        and employee_id % 2 = 1) b
on a.employee_id = b.employee_id
