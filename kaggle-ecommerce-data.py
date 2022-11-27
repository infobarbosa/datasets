#!/usr/bin/python3
import pandas as pd
import datetime

datatypes = {
    "InvoiceNo": str,
    "StockCode": str,
    "Description": str,
    "Quantity": "Int64",
    "UnitPrice": float,
    "CustomerID": "Int64",
    "Country" : str
}

raw_data = pd.read_csv('data.csv', encoding_errors='ignore', dtype = datatypes, parse_dates=['InvoiceDate'])

df = raw_data

# Manipulando as datas originais para hoje
df['InvoiceDate'] = df["InvoiceDate"] + df["InvoiceDate"].map(lambda invoiceDate: datetime.datetime.now() - invoiceDate)
print( df.describe() )

print( df.head() )

print( df.tail() )

df.to_csv("invoices.csv", index=None, date_format='%Y-%m-%dT%H:%M:%SZ', columns=["InvoiceDate","Country","InvoiceNo","StockCode","Description","CustomerID","Quantity","UnitPrice"])
