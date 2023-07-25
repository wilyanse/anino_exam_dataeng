-- Question 1
-- SQL query to get Unique Players in the Data

SELECT 
    COUNT(DISTINCT event_user)
FROM
    game_data;

-- Question 2
-- SQL query to get average number of slot machines per session
SELECT 
    AVG(number_of_slot_machines) AS average_number_of_slot_machines
FROM
    (SELECT 
        session_id,
            COUNT(DISTINCT session_token) AS number_of_slot_machines
    FROM
        game_data
    GROUP BY session_id);

-- SQL query to get the average number of spins per machine session
SELECT 
    AVG(spins_count) AS average_spins_count
FROM
    (SELECT 
        session_token, COUNT(*) AS spins_count
    FROM
        game_data
    GROUP BY session_token);

-- Question 3
-- SQL query to get the probability of hitting the various win_types
SELECT 
    win_type,
    (COUNT(*) / (SELECT 
            COUNT(*)
        FROM
            game_data)) AS win_type_count
FROM
    game_data
GROUP BY win_type;

-- Question 4
-- SQL query to get the retention rate
SELECT 
    count_more_than_24_hours / total_count AS retention_rate
FROM
    (SELECT 
        COUNT(DISTINCT event_user) AS count_more_than_24_hours
    FROM
        game_data
    WHERE
        event_time > install_date + INTERVAL 24 HOUR) AS subquery1
        CROSS JOIN
    (SELECT 
        COUNT(DISTINCT event_user) AS total_count
    FROM
        game_data) AS subquery2;

-- Question 5
-- SQL query to get the average RTP
SELECT 
    AVG(rtp) AS avg_rtp
FROM
    (SELECT 
        total_winnings / total_bettings AS rtp
    FROM
        (SELECT 
        slotmachine_id,
            SUM(amount) AS total_winnings,
            SUM(total_bet_amount) AS total_bettings
    FROM
        game_data
    GROUP BY slotmachine_id) AS summary) AS rtp_calc;