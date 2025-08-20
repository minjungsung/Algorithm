/* 
    SQL Query: Retrieve employees whose salary is greater than their manager's salary. 
    This query uses an INNER JOIN to combine rows from the Employee table based on the manager-employee relationship.
*/

/* 
    INNER JOIN:
    - Combines rows from the `Employee` table where there is a matching manager-employee relationship.
    - The condition `e.managerId = m.id` establishes the relationship between an employee (`e`) and their manager (`m`).
    - Use INNER JOIN when you only want rows where there is a matching relationship in both joined tables.
*/

SELECT 
    e.name AS Employee         -- Retrieves the name of the employee who earns more than their manager.
FROM 
    Employee e                 -- Alias 'e' refers to employees in the `Employee` table.
INNER JOIN 
    Employee m                 -- Alias 'm' refers to managers in the same `Employee` table.
ON 
    e.managerId = m.id         -- Join condition: Matches employees with their respective managers based on `managerId`.
WHERE 
    e.salary > m.salary;       -- Filters rows to include only employees whose salary exceeds their manager's salary.

/* 
    Explanation of Logic:
    - The query performs a self-join on the `Employee` table to compare employee data (`e`) with manager data (`m`).
    - The INNER JOIN ensures that only employees who have a matching manager in the table are considered.
    - The `WHERE` clause applies a filter to retrieve only those employees whose `salary` is greater than their manager's `salary`.
*/