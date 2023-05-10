### What is a transaction? What are its properties?
A transaction is a sequence of database operations that are treated as a single unit of work. It is a logical unit of work that ensures data consistency even in the event of multiple concurrent database access or system failures. In other words, a transaction allows a set of database operations to be executed as a single, all-or-nothing operation.

The four key properties of a transaction are commonly referred to as the ACID properties:

* Atomicity: A transaction is atomic, meaning that it is an indivisible and irreducible series of database operations. Either all of the operations in the transaction are executed, or none of them are. If any operation in the transaction fails, then the entire transaction is rolled back to its previous state.
* Consistency: A transaction ensures that the database is in a consistent state before and after the transaction is executed. The transaction cannot leave the database in an inconsistent state.
* Isolation: A transaction is isolated from other transactions that are executing concurrently. This means that the operations in a transaction do not interfere with the operations in another transaction, even if they are executing simultaneously.
* Durability: Once a transaction is committed, its changes to the database are permanent and will survive any subsequent system failures, such as power outages or crashes.
---
### explain.

When you want to read a table, PostgreSQL has many ways to do it. The simpler one is to read it sequentially, block by block.
```sql
db=# explain select  * from users;
                           QUERY PLAN                           
----------------------------------------------------------------
Seq Scan on users  (cost=0.00..15406.00 rows=1000000 width=14)
```

**Seq Scan** - read all the rows of a tabble sequentially. <br/>
**cost** - the first cost number is the cost to get the first row, 
the second number is the cost to get all the rows from the sequential scan.<br/>
**rows** - estimated number of rows output by this plan node.<br/>
**width** - estimated average width of rows output by this plan node (in bytes).

### pg_stats. Width.
```sql
SELECT sum(avg_width) AS width FROM pg_stats
WHERE tablename='users';
...
 width 
-------
    14
(1 row)
```
**Average size (in bytes) of a row in the resulting data set.** 

### pg_stats. Rows.
```sql
SELECT reltuples FROM pg_class WHERE relname='users';
...
 reltuples 
-----------
     1e+06
(1 row)
```
**All relations metadata appear in the pg_class catalog.**

### explain analyze.

```sql
explain analyze select  * from users;
                          QUERY PLAN                                                
 --------------------------------------------------------------------------------
Seq Scan on users  (cost=0.00..15406.00 rows=1000000 width=14)
(actual time=0.023..6974.370 rows=1000000 loops=1)
 Planning Time: 0.099 ms
 Execution Time: 13644.037 ms
(3 rows)
```
**actual time** - the time taken to run the query. <br/>
**rows** - reql number of rows. <br/>
**loops** - number of loops. <br/>
**Execution Time** - real execution time in milliseconds.

### buffers.

```sql
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM users;
...
                         QUERY PLAN                                               
---------------------------------------------------------------------------------------------
Seq Scan on users (cost=0.00..15406.00 rows=1000000 width=14)
(actual time=0.022..11558.195 rows=1000000 loops=1)
 Buffers: shared hit=5406
 Planning Time: 0.037 ms
 Execution Time: 22673.007 ms
 ...
 EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM users;
 ...
                         QUERY PLAN                                               
---------------------------------------------------------------------------------------------
 Seq Scan on users  (cost=0.00..15406.00 rows=1000000 width=14)
(actual time=0.022..11649.875 rows=1000000 loops=1)
 Buffers: shared hit=5406
 Planning Time: 0.136 ms
 Execution Time: 22832.806 ms
(4 rows)
```

