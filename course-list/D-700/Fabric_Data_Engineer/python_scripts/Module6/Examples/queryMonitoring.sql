/*
Code example 2: Query Monitoring 

    Query Monitoring Example
    This script demonstrates how to monitor running queries in SQL Server.
    It retrieves information about currently executing requests, including their IDs, session IDs, start times, and total elapsed times.
*/
-- Query Monitoring Example
-- This script demonstrates how to monitor running queries in SQL Server.
-- It retrieves information about currently executing requests, including their IDs, session IDs, start times, and total elapsed times.

SELECT request_id, session_id, start_time, total_elapsed_time
    FROM sys.dm_exec_requests
    WHERE status = 'running'
    ORDER BY total_elapsed_time DESC;

SELECT login_name
    FROM sys.dm_exec_sessions
    WHERE session_id = 'SESSION_ID WITH LONG-RUNNING QUERY';

KILL 'SESSION_ID WITH LONG-RUNNING QUERY';

