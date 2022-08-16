import tkinter as tk
from tkinter import ttk
from google_currency import convert
import json

app = tk.Tk()
app.geometry('300x300')
app.title('Currency converter')

def btn_click():
    cur1 = currency1.get()
    cur2 = currency2.get()
    num = float(numberInput.get())

    result = convert(cur1, cur2, num)
    result1 = json.loads(result)
    result1 = result1["amount"]
    labelResult = tk.Label(app, text=result1, font=20)
    labelResult.grid(column=0, row=14, padx=80)
    return result1

labelTop = tk.Label(app,
                    text="FROM:", font= 20)
labelTop.grid(column=0, row=1, padx= 80)

currency1 = ttk.Combobox(app,
                            values=[
                                "rub",
                                "eur",
                                "usd",
                                "jpy",
                                "cny"])

currency1.grid(column=0, row=2, padx= 80)
currency1.current()

currency1.bind("<<ComboboxSelected>>")

labelTop2 = tk.Label(app,
                    text="IN:", font= 20)
labelTop2.grid(column=0, row=6, padx= 80)

currency2 = ttk.Combobox(app,
                            values=[
                                "rub",
                                "eur",
                                "usd",
                                "jpy",
                                "cny"])

currency2.grid(column=0, row=7, padx= 80)
currency2.current()

currency2.bind("<<ComboboxSelected>>")

labelTop3 = tk.Label(app,
                    text="INPUT SUM", font= 20)
labelTop3.grid(column=0, row=10, padx= 80)

numberInput = tk.Entry()
numberInput.grid(column=0, row=11, padx= 80)

btn = tk.Button(text= 'Button', bg= 'yellow', command= btn_click)
btn.grid(column=0, row=13, padx= 80)

app.mainloop()
