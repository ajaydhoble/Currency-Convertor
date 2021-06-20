# IMPORTING REQUIRED LIBRARIES
import requests
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# $********CREATING WINDOW***********$
wind = tkinter.Tk()
wind.title("Currency Convertor")
wind.geometry("400x400")
wind.resizable(width=False, height=False)
wind.config(bg="grey")


# CLASS TO CONVERT CURRENCIES
class currencyConvertor:

    def __init__(self, url):
        # print("CONSTRUCTOR")
        self.request = requests.get(url).json()  # MAKE HTTP REQ AND MAKE A JSON FILE
        self.rates = self.request["rates"]   # EXTRACTING RATES

    # AS BASE IS USD FIRST CHECK FOR IT AND IF NOT THEN CONVERT TO USD THEN TO REQ CURR
    def exchangeRate(self, oldCurrency, newCurrency, amount):
        if oldCurrency != "USD":
            amount = amount/self.rates[oldCurrency]
        newAmount = round(amount * self.rates[newCurrency], 4)
        return newAmount


# FUNCTION TO GET TEXTS FROM WIDGETS AND PASS IT TO CONVERTOR OBJ
def convert():
    from_currency_text = from_currency_var.get()
    to_currency_text = to_currency_var.get()
    if str(from_currency_amount.get()).isnumeric():  # CHECK WEATHER INPUT IS NUMERIC OR NOT
        from_amount = float(from_currency_amount.get())
        convertor = currencyConvertor(URL)
        new_amount = round(convertor.exchangeRate(from_currency_text, to_currency_text, from_amount), 2)
        to_currency_amount.config(text=str(new_amount))
    else:
        messagebox.showerror("ERROR", "ENTER DIGITS ONLY!!")


URL = "https://api.exchangerate-api.com/v4/latest/USD"

# MAKE A OBJ FOR DROPBOX VALUES
obj = currencyConvertor(URL)
currencies = list(obj.rates.keys())

# LABELS FOR TITLE AND TO DISPLAY RESULT
title = Label(wind, text="REAL TIME \nCURRENCY CONVERTOR", font=("Fixedsys", 19, "bold"), bg="grey", fg="purple")
title.place(x=60, y=30)

from_label = Label(wind, text="From", font=("Fixedsys", 17, "bold"), fg="black", bg="grey")
from_label.place(x=30, y=140)

to_label = Label(wind, text="To", font=("Fixedsys", 17, "bold"), fg="black", bg="grey")
to_label.place(x=230, y=140)

to_currency_amount = Label(wind, text=" ", font=("System", 17), fg="black", bg="grey", relief=SUNKEN, border=3)
to_currency_amount.place(x=250, y=210, width=115, height=40)


# STRING VAR 'S FOR DEFAULT VALUES
from_currency_var = StringVar()
from_currency_var.set("USD")
to_currency_var = StringVar()
to_currency_var.set("INR")


# 2 COMBOBOX TO SELECT FROM AND TO CURRENCY
fromCurrency = ttk.Combobox(wind, textvariable=from_currency_var, values=currencies, state="readonly", width=15)
fromCurrency.place(x=50, y=170)

toCurrency = ttk.Combobox(wind, textvariable=to_currency_var, values=currencies, state="readonly", width=15)
toCurrency.place(x=250, y=170)

# ENTRY WIDGET FOR AMOUNT
from_currency_amount = Entry(wind, bg="grey", font=("System", 17), fg="black", border=3, relief=SUNKEN)
from_currency_amount.place(x=50, y=210, width=115, height=40)

# BUTTON TO CONVERT
convert = Button(wind, text="CONVERT", command=convert, font=("Courier", 16, "bold"), bg="black", fg="green",
                 relief=RAISED, bd=6)
convert.place(x=150, y=300)

# LOOP
wind.mainloop()
