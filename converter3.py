import tkinter as tk
from tkinter import ttk
import requests
import json

app = tk.Tk()
app.geometry('300x300')
app.title('Currency converter')

def btn_click():
    cur1 = currency1.get()
    cur2 = currency2.get()
    num = numberInput.get()
    url = f"https://api.apilayer.com/fixer/convert?to={cur2}&from={cur1}&amount={num}"

    payload = {}
    headers = {
        "apikey": "3bZ2GQ7gh1ExOGmmu9edVHTh9iDQDPeG"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    result = json.loads(result)
    result1 = result["result"]
    labelResult = tk.Label(app, text=result1, font=80)
    labelResult.grid(column=0, row=14, padx=80)
    return result1

labelTop = tk.Label(app,
                    text="FROM:", font= 20)
labelTop.grid(column=0, row=1, padx= 80)

currency1 = ttk.Combobox(app,
                            values=[
                                "RUB",
                                "EUR",
                                "USD",
                                "JPY",
                                "CNY"])

currency1.grid(column=0, row=2, padx= 80)
currency1.current()

currency1.bind("<<ComboboxSelected>>")

labelTop2 = tk.Label(app,
                    text="IN:", font= 20)
labelTop2.grid(column=0, row=6, padx= 80)

currency2 = ttk.Combobox(app,
                            values=[
                                "RUB",
                                "EUR",
                                "USD",
                                "JPY",
                                "CNY"])

currency2.grid(column=0, row=7, padx= 80)
currency2.current()

currency2.bind("<<ComboboxSelected>>")

labelTop3 = tk.Label(app,
                    text="INPUT NUMBER", font= 20)
labelTop3.grid(column=0, row=10, padx= 80)

numberInput = tk.Entry()
numberInput.grid(column=0, row=11, padx= 80)

btn = tk.Button(text= 'Button', bg= 'yellow', command= btn_click)
btn.grid(column=0, row=13, padx= 80)

app.mainloop()
