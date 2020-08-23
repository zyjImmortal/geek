select Id from Weather w1, Weather w2 where DATEDIFF(w1.RecordDate, w2.RecordDate)=1 and w1.Temperature > w2.Temperature

-- 511. 游戏玩法分析

select player_id, min(event_date) as first_login from Activity group by  player_id

-- 512. 游戏玩法分析 II

select a.player_id, b.device_id from Activity a left join
(select player_id, min(event_date) as first_login from Activity group by  player_id) as b
on a.player_id=b.player_id and a.event_date=b.first_login

-- 577. 员工奖金

select e.name, b.bonus from Employee e join Bonus b on e.empId=b.empId where b.bonus < 1000;

-- 584. 寻找用户推荐人

select c.name from customer c where c.referee_id <> 2 or c.referee_id is null;

-- 586. 订单最多的客户
select max(c.customer_number) as customer_number from (
select customer_number from orders group by customer_number) as c

select customer_number from orders group by customer_number order by count(*) desc limit 1;

select round(ifnull((select count(*) from  (select requester_id, accepter_id from request_accepted group by requester_id, accepter_id)
            /select count(*) from (select sender_id, send_to_id from friend_request group by sender_id, send_to_id), 0), 2) as accept_rate

-- mysql要求每一个派生出来的表都必须有一个自己的别名, 所以from后面的表都必须起一个别名，不然会报错Every derived table must have its own alias
select round(
ifnull(
(select count(*) from (select requester_id, accepter_id from request_accepted group by requester_id, accepter_id) as a)
/
(select count(*) from (select sender_id, send_to_id from friend_request group by sender_id, send_to_id) as b)
,0)
,2) as accept_rate

select round(
ifnull(
(select count(*) from (select distinct requester_id, accepter_id from request_accepted) as a)
/
(select count(*) from (select distinct sender_id, send_to_id from friend_request group by sender_id, send_to_id) as b)
,0)
,2) as accept_rate


-- 603. 连续空余座位
select distinct ca.seat_id from cinema c join cinema ca on abs(ca.seat_id - c.seat_id)=1 and ca.free=1 and c.free=1 order by ca.seat_id


-- 607. 销售员
select name from salesperson where sales_id not in (
select sales_id from orders where com_id = (select com_id from company where name='RED'))

select sales_id from orders o join company c on o.com_id=c.com_id and c.name='RED'

-- 1141. 查询近30天活跃用户数

select activity_date as day, count(distinct user_id) as active_users from Activity where activity_date between '2019-06-28' and '2019-07-27' group by activity_date;
