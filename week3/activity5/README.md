# Money Exchange System


## Features

The system provides the following functions:

1. Register Customer
2. View Customers
3. Register Currency
4. View Currencies
5. Register / Update Exchange Rate
6. Exchange Currency
7. View All Exchange Transactions
8. View Customer Exchange Transactions

## Database Design

The database contains four tables:

### 1. Customer

The Customer table stores customer information.

Attributes:
- customer_id - Primary Key(Auto Increment)
- name
- phone

### 2. Currency

The Currency table stores the currencies supported by the system.

Attributes:
- currency_code - Primary Key
- currency_name

For example, NZD represents New Zealand Dollar and USD represents US Dollar.


### 3. ExchangeRate

The ExchangeRate table stores the exchange rate between two currencies.

Attributes:
- rate_id - Primary Key(Auto increment)
- from_currency - Foreign Key
- to_currency - Foreign Key
- rate


### 4. ExchangeTransaction

The ExchangeTransaction table stores completed currency exchange transactions.

Attributes:
- transaction_id - Primary Key(Auto increment)
- customer_id - Foreign Key
- from_currency - Foreign Key
- to_currency - Foreign Key
- amount
- exchange_rate
- return_amount



## Exchange Calculation

The exchanged amount is calculated using:
return_amount = amount × exchange_rate


## ER Diagram

![Money Exchange ER Diagram](https://github.com/osy0602/pse/blob/main/week3/activity5/moneyExchange_ERD.png)

## Use Case Diagram

![Money Exchange Use Case Diagram](https://github.com/osy0602/pse/blob/main/week3/activity5/moneyexchange_UsecaseD.png)

## Activity Diagram

![Money Exchange Activity Diagram1](https://github.com/osy0602/pse/blob/main/week3/activity5/AD_1.png)
![Money Exchange Activity Diagram2](https://github.com/osy0602/pse/blob/main/week3/activity5/AD_2.png)

## Class Diagram

![Money Exchange Class Diagram](https://github.com/osy0602/pse/blob/main/week3/activity5/class_diagram.png)