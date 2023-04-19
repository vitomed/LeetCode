### What is a transaction? What are its properties?
A transaction is a sequence of database operations that are treated as a single unit of work. It is a logical unit of work that ensures data consistency even in the event of multiple concurrent database access or system failures. In other words, a transaction allows a set of database operations to be executed as a single, all-or-nothing operation.

The four key properties of a transaction are commonly referred to as the ACID properties:

* Atomicity: A transaction is atomic, meaning that it is an indivisible and irreducible series of database operations. Either all of the operations in the transaction are executed, or none of them are. If any operation in the transaction fails, then the entire transaction is rolled back to its previous state.
* Consistency: A transaction ensures that the database is in a consistent state before and after the transaction is executed. The transaction cannot leave the database in an inconsistent state.
* Isolation: A transaction is isolated from other transactions that are executing concurrently. This means that the operations in a transaction do not interfere with the operations in another transaction, even if they are executing simultaneously.
* Durability: Once a transaction is committed, its changes to the database are permanent and will survive any subsequent system failures, such as power outages or crashes.
---
