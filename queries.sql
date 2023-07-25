-- Question 1
-- SQL query to get Unique Players in the Data

SELECT COUNT(DISTINCT event_user)
FROM df;

-- Question 2
-- SQL query to get average number of slot machines per session
SELECT AVG(number_of_slot_machines) AS average_number_of_slot_machines
FROM (
    SELECT session_id, COUNT(DISTINCT session_token) AS number_of_slot_machines
    FROM df
    GROUP BY session_id
);

-- SQL query to get the average number of spins per machine session
SELECT AVG(spins_count) AS average_spins_count
FROM (
    SELECT session_token, COUNT(*) AS spins_count
    FROM df
    GROUP BY session_token
);