import sqlite3

## Connect to SQLite
connection = sqlite3.connect("justpay.db")

# Create a cursor object to insert records, create tables
cursor = connection.cursor()

## Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    Date TEXT,
    Total_Transactions INTEGER,
    Merchant TEXT,
    Aggregator TEXT,
    Bank TEXT,
    Transaction_Status TEXT
);
"""

cursor.execute(table_info)

## Insert provided records
def insert_data(conn, data):
    try:
        cursor = conn.cursor()
        for row in data:
            cursor.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?, ?, ?)", row)
        conn.commit()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print("Error:", e)

# Provided data to insert
data = [
    ('4/14/2016', '21', 'Merchant1', 'Agg2', 'Bank2', ''),
    ('4/14/2016','9', 'Merchant2', 'Agg2', 'Bank2', '', ''),
    ('4/14/2016','3', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('4/14/2016','7', 'Merchant2', '', 'Bank1', 'SUCCESS', ''),
    ('4/14/2016','680', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('4/14/2016','23', 'Merchant2', 'Agg3', 'Bank2', '', ''),
    ('4/14/2016','12', 'Merchant2', 'Agg3', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','5', 'Merchant2', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('4/14/2016','1', 'Merchant1', '', 'Bank3', '', ''),
    ('4/14/2016','63', 'Merchant1', 'Agg2', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','107', 'Merchant1', 'Agg2', 'Bank2', 'FAILURE', ''),
    ('4/14/2016','206', 'Merchant1', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('4/14/2016','1', 'Merchant2', '', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','14', 'Merchant1', '', 'Bank2', '', ''),
    ('4/14/2016','1372', 'Merchant1', 'Agg4', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','5767', 'Merchant1', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('4/14/2016','41', 'Merchant2', '', 'Bank2', '', ''),
    ('4/14/2016','1', 'Merchant1', 'Agg5', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','3', 'Merchant1', 'Agg5', 'Bank1', 'FAILURE', ''),
    ('4/14/2016','2', 'Merchant2', 'Agg2', 'Bank1', 'FAILURE', ''),
    ('4/14/2016','12', 'Merchant2', 'Agg3', 'Bank1', 'FAILURE', ''),
    ('4/14/2016','1936', 'Merchant1', 'Agg4', 'Bank2', 'FAILURE', ''),
    ('4/14/2016','2', 'Merchant2', 'Agg2', 'Bank1', '', ''),
    ('4/14/2016','140', 'Merchant2', 'Agg3', 'Bank1', 'SUCCESS', ''),
    ('4/14/2016','56', 'Merchant2', '', 'Bank1', '', ''),
    ('4/14/2016','1', 'Merchant2', 'Agg2', 'Bank3', 'SUCCESS', ''),
    ('4/14/2016','2715', 'Merchant1', 'Agg2', 'Bank1', 'FAILURE', ''),
    ('4/14/2016','5314', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('4/14/2016','455', 'Merchant1', 'Agg4', 'Bank2', '', ''),
    ('4/14/2016','68', 'Merchant1', 'Agg2', 'Bank3', 'FAILURE', ''),
    ('4/14/2016','633', 'Merchant1', 'Agg4', 'Bank3', 'FAILURE', ''),
    ('4/14/2016','6', 'Merchant1', '', 'Bank1', 'FAILURE', ''),
    ('4/14/2016','13', 'Merchant2', '', 'Bank3', '', ''),
    ('4/14/2016','12', 'Merchant1', '', 'Bank1', '', ''),
    ('4/14/2016','61', 'Merchant2', 'Agg3', 'Bank1', '', ''),
    ('4/14/2016','6', 'Merchant2', 'Agg3', 'Bank3', '', ''),
    ('4/14/2016','70', 'Merchant2', 'Agg3', 'Bank2', 'SUCCESS', ''),
    ('4/14/2016','2', 'Merchant1', 'Agg5', 'Bank2', 'FAILURE', ''),
    ('4/14/2016','4', 'Merchant1', 'Bank3', '', 'FAILURE', ''),
    ('4/14/2016','285', 'Merchant1', 'Agg4', 'Bank3', '', ''),
    ('4/14/2016','11', 'Merchant2', 'Agg2', 'Bank3', '', ''),
    ('4/14/2016','7', 'Merchant1', '', 'Bank2', 'FAILURE', ''),
    ('4/14/2016','7', 'Merchant1', 'Agg2', 'Bank3', '', ''),
    ('4/15/2016', '257', 'Merchant2', 'Agg2', 'Bank3', 'SUCCESS'),
    ('673', 'Merchant1', 'Agg4', 'Bank3', 'FAILURE', ''),
    ('272', 'Merchant2', 'Agg2', 'Bank1', 'FAILURE', ''),
    ('318', 'Merchant1', 'Agg4', 'Bank3', '', ''),
    ('980', 'Merchant2', 'Agg3', 'Bank3', '', ''),
    ('8', 'Merchant1', '', 'Bank1', '', ''),
    ('210', 'Merchant2', '', 'Bank1', 'SUCCESS', ''),
    ('2284', 'Merchant2', 'Agg3', 'Bank1', '', ''),
    ('545', 'Merchant1', 'Agg4', 'Bank2', '', ''),
    ('2258', 'Merchant2', 'Agg3', 'Bank1', 'FAILURE', ''),
    ('5545', 'Merchant1', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('3', 'Merchant2', 'Agg2', 'Bank3', 'FAILURE', ''),
    ('1933', 'Merchant2', 'Agg3', 'Bank2', '', ''),
    ('32', 'Merchant1', 'Agg2', 'Bank3', 'FAILURE', ''),
    ('630', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('2', 'Merchant1', '', 'Bank1', 'FAILURE', ''),
    ('1', 'Merchant1', '', 'Bank2', 'SUCCESS', ''),
    ('1', 'Merchant1', 'Agg5', 'Bank2', 'SUCCESS', ''),
    ('50', 'Merchant2', 'Agg2', 'Bank2', 'FAILURE', ''),
    ('354', 'Merchant2', '', 'Bank2', '', ''),
    ('46', 'Merchant2', '', 'Bank1', 'FAILURE', ''),
    ('443', 'Merchant2', 'Agg2', 'Bank3', '', ''),
    ('121', 'Merchant2', 'Agg3', 'Bank2', 'FAILURE', ''),
    ('13', 'Merchant1', '', 'Bank2', '', ''),
    ('6196', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('2466', 'Merchant1', 'Agg4', 'Bank2', 'FAILURE', ''),
    ('895', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('428', 'Merchant2', '', 'Bank1', '', ''),
    ('20', 'Merchant1', 'Agg2', 'Bank3', 'SUCCESS', ''),
    ('1349', 'Merchant2', 'Agg3', 'Bank3', 'SUCCESS', ''),
    ('217', 'Merchant2', '', 'Bank3', '', ''),
    ('25', 'Merchant2', '', 'Bank3', 'SUCCESS', ''),
    ('14', 'Merchant2', 'Agg3', 'Bank3', 'FAILURE', ''),
    ('1901', 'Merchant1', 'Agg2', 'Bank1', 'FAILURE', ''),
    ('724', 'Merchant2', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('2', 'Merchant1', '', 'Bank1', 'SUCCESS', ''),
    ('1452', 'Merchant1', 'Agg4', 'Bank3', 'SUCCESS', ''),
    ('7', 'Merchant1', 'Agg2', 'Bank2', '', ''),
    ('519', 'Merchant2', 'Agg2', 'Bank2', '', ''),
    ('3', 'Merchant1', '', 'Bank3', 'FAILURE', ''),
    ('60', 'Merchant1', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('267', 'Merchant2', 'Agg2', 'Bank1', '', ''),
    ('5', 'Merchant1', '', 'Bank3', '', ''),
    ('1', 'Merchant1', '', 'Bank3', 'SUCCESS', ''),
    ('2', 'Merchant1', '', 'Bank2', 'FAILURE', ''),
    ('7788', 'Merchant2', 'Agg3', 'Bank1', 'SUCCESS', ''),
    ('53', 'Merchant1', 'Agg2', 'Bank2', 'FAILURE', ''),
    ('6', 'Merchant1', 'Agg2', 'Bank3', '', ''),
    ('4221', 'Merchant2', 'Agg3', 'Bank2', 'SUCCESS', ''),
    ('2', 'Merchant1', 'Agg5', 'Bank1', 'FAILURE', ''),
    ('1', 'Merchant2', '', 'Bank2', 'SUCCESS', ''),
    ('4/16/2016', '7176', 'Merchant2', 'Agg3', 'Bank1', 'SUCCESS'),
    ('2332', 'Merchant1', 'Agg4', 'Bank2', 'FAILURE', ''),
    ('577', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('59', 'Merchant1', 'Agg2', 'Bank2', 'FAILURE', ''),
    ('1', 'Merchant1', 'Agg5', 'Bank1', 'SUCCESS', ''),
    ('1', 'Merchant1', '', 'Bank1', 'SUCCESS', ''),
    ('547', 'Merchant2', '', 'Bank1', '', ''),
    ('8', 'Merchant1', '', 'Bank1', '', ''),
    ('122', 'Merchant2', 'Agg2', 'Bank1', '', ''),
    ('1133', 'Merchant2', 'Agg3', 'Bank3', '', ''),
    ('337', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('171', 'Merchant1', 'Agg2', 'Bank2', '', ''),
    ('1', 'Merchant1', '', 'Bank2', 'FAILURE', ''),
    ('1237', 'Merchant1', 'Agg2', 'Bank2', '', ''),
    ('1761', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('4', 'Merchant1', 'Agg5', 'Bank1', 'FAILURE', ''),
    ('3', 'Merchant1', 'Agg5', 'Bank3', 'SUCCESS', ''),
    ('293', 'Merchant2', 'Agg2', 'Bank1', '', ''),
    ('192', 'Merchant1', 'Agg2', 'Bank3', '', ''),
    ('2', 'Merchant2', '', 'Bank3', 'SUCCESS', ''),
    ('58', 'Merchant1', 'Agg2', 'Bank1', 'FAILURE', ''),
    ('305', 'Merchant2', 'Agg3', 'Bank2', '', ''),
    ('763', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('1', 'Merchant2', 'Agg5', 'Bank3', '', ''),
    ('21', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('1135', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('3', 'Merchant2', 'Agg5', 'Bank3', '', ''),
    ('54', 'Merchant2', 'Agg2', 'Bank2', '', ''),
    ('309', 'Merchant1', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('32', 'Merchant2', 'Agg3', 'Bank3', '', ''),
    ('8', 'Merchant1', '', 'Bank2', '', ''),
    ('5', 'Merchant1', 'Agg2', 'Bank2', '', ''),
    ('25', 'Merchant2', 'Agg3', 'Bank1', 'FAILURE', ''),
    ('55', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('1', 'Merchant2', '', 'Bank1', 'SUCCESS', ''),
    ('1795', 'Merchant2', 'Agg2', 'Bank2', 'SUCCESS', ''),
    ('31', 'Merchant2', 'Agg3', 'Bank1', '', ''),
    ('5', 'Merchant2', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('148', 'Merchant1', 'Agg4', 'Bank2', '', ''),
    ('3', 'Merchant1', 'Agg5', 'Bank3', 'SUCCESS', ''),
    ('429', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('9', 'Merchant1', 'Agg2', 'Bank3', '', ''),
    ('44', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('2', 'Merchant2', '', 'Bank2', 'SUCCESS', ''),
    ('57', 'Merchant1', 'Agg2', 'Bank1', 'SUCCESS', ''),
    ('66', 'Merchant2', 'Agg2', 'Bank3', 'SUCCESS', ''),
    ('23', 'Merchant1', '', 'Bank3', '', ''),
    ('109', 'Merchant2', 'Agg2', 'Bank3', '', ''),
    ('108', 'Merchant2', 'Agg2', 'Bank1', '', ''),
    ('543', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('141', 'Merchant1', 'Agg2', 'Bank3', '', ''),
    ('1', 'Merchant1', 'Agg5', 'Bank2', '', ''),
    ('101', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('1381', 'Merchant1', 'Agg4', 'Bank2', 'SUCCESS', ''),
    ('10', 'Merchant2', 'Agg2', 'Bank2', '', ''),
    ('1', 'Merchant2', 'Agg5', 'Bank1', '', ''),
    ('5', 'Merchant1', 'Agg2', 'Bank1', '', ''),
    ('2', 'Merchant1', 'Agg5', 'Bank2', ''),
]


# Insert data into the table
insert_data(connection, data)

## Display all the records
print("The inserted records are:")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
