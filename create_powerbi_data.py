import pandas as pd
import numpy as np
np.random.seed(42)
products = ["Adire Fabric", "Ankara", "Aso Oke", "Lace Material", "Adire Gown"]
markets = ["Oja Oba", "Orisumbare", "Alekuwodo", "Oke Baale"]
payments = ["Transfer", "Cash", "POS", "USSD"]
customers = ["Sokoto", "Osogbo", "Lagos", "Ibadan"]
price_map = {"Adire Fabric":8000, "Ankara":5000, "Aso Oke":15000, "Lace Material":12000, "Adire Gown":25000}
rows=[]
for i in range(120):
    prod = np.random.choice(products)
    qty = np.random.randint(1,16)
    rows.append([f"2024-0{np.random.randint(1,9)}-{np.random.randint(10,28)}", prod, np.random.choice(markets), qty, price_map[prod], qty*price_map[prod], np.random.choice(payments), np.random.choice(customers)])
pd.DataFrame(rows, columns=["Date","Product","Market","Quantity","Unit_Price","Total_Sales","Payment_Method","Customer_Type"]).to_csv("osogbo_powerbi_sales.csv", index=False)
print("SUCCESS! File created in Documents")