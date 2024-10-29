SELECT id, name, (SELECT name FROM states s WHERE s.id = c.state_id) as name FROM cities c
ORDER BY c.id;