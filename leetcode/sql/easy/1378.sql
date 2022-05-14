select unique_id, name
from employeeuni
right join employees using(id);