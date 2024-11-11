/*
with FriendCounts as (
SELECT requester_id AS person_id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION
    SELECT accepter_id AS person_id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendNumbers AS (
    SELECT person_id, COUNT(DISTINCT friend_id) AS num
    FROM FriendCounts
    GROUP BY person_id
)
select person_id as id, num
from FriendNumbers
order by num desc
limit 1;
*/