from prettytable import PrettyTable
import numpy as np
import pandas as pd

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']

def display_table(input_data):
    """
    Display product table
    """
    try:
        # get minimum and maximum price from dataset
        min_price = float(input_data.get("min_price"))
        max_price = float(input_data.get("max_price"))
        # get range/mask for price to print
        mask_price_1 = df['price'] >= min_price
        mask_price_2 = df["price"] <= max_price
        try:
            # get start and end date from dataset
            start_date = pd.to_datetime(input_data.get("start_date"))
            stop_date = pd.to_datetime(input_data.get("stop_date"))
            mask_date_1 = df["expires"] >= start_date
            mask_date_2 = df["expires"] <= stop_date
            data = df[(mask_price_1 & mask_price_2) & (mask_date_1 & mask_date_2)]
        except Exception as e:
            data = df[mask_price_1 & mask_price_2]
            print(e)
        for i,row in data.iterrows():
            table.add_row([row['id'], row['name'], row['price'], row['expires']])
        print(table)
        table.clear_rows()
    except:
        print("Please try to enter correct/desired input: \n ")

def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        if value == 'exit':
            break
        keys = ['min_price', 'max_price', 'start_date', 'stop_date']
        values = value.split(' ')
        input_data = dict(zip(keys, values))
        display_table(input_data)


if __name__ == '__main__':
    df = pd.read_csv('products.csv')
    df['expires'] = pd.to_datetime(df['expires'])
    start()