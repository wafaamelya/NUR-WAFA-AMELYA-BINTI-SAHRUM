import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def collect_data():
    accepted = accept_var.get()

    if accepted=="Accepted":

        # User info
        username = user_name.get()
        usertn = user_tn.get()

        if username and usertn:
            size_type = size_combobox.get()
            item = int(item_spinbox.get())
        
        # Connect to MySQL
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="unimail"
            )

            mycursor = mydb.cursor()

            # the price below is the price for each size of the parcel
            prices = {
                "Size S": 5,
                "Size M": 10,
                "Size L": 20,

            }

            # The calculation to calculate total price
            total_price = (prices[size_type] * item)

            # Database for user and parcel data to insert the data inside phpmyadmin
            sql = "INSERT INTO parcel (user_name, tracking_number, parcel_size, total_item, parcel_price) VALUES (%s, %s, %s, %s, %s)"
            val = (username, usertn, size_type, item, total_price)
            mycursor.execute(sql, val)
            mydb.commit()

            output_label.config(text=f"Tracking Number: {usertn},Size: {size_type}, Total Item: {item}, Total Price: RM{total_price}")
        else:
            tk.messagebox.showwarning(title="Error", message="User Name and Tracking Number are required.")
    else:
        tk.messagebox.showwarning(title="Error", message="You have not accepted the terms and condition")


# This is my main window, the title, geometry 
root = tk.Tk()
root.title("UniMail")
root.geometry('600x770')
root.configure(bg='#98BF64')      

# Page Title
frame = tk.Label(root, text="Welcome to UniMail :)", font= ('Gill Sans Ultra Bold', 18))
frame.pack(padx= 20, pady= 20 )

box = tk.Frame(root)
box.pack()

# Saving User Info and Parcel Info
user_info_frame =tk.LabelFrame(box, text="User Information", font=('new times roman', 10, 'bold'))
user_info_frame.grid(row= 0, column=0, sticky="news", padx=20, pady=10)

user_name = tk.Label(user_info_frame, text="Name")
user_name.grid(row= 1, column=0, padx=10, pady=10)
user_name = tk.Entry(user_info_frame)
user_name.grid(row=1, column=1, padx=20, pady=10)

user_tn = tk.Label(user_info_frame, text= "Tracking Number")
user_tn.grid(row= 2, column=0, padx=20, pady=10)
user_tn = tk.Entry(user_info_frame)
user_tn.grid(row=2, column=1, padx=20, pady=10)

# Prices List by using textbox
parcel_prices = tk.Text(root, height=10, width=43)
parcel_prices.pack(pady=20)

# The defined list by using pricebox
parcel_prices.insert(tk.END, "Size & Prices:\n\n")
parcel_prices.insert(tk.END, "Size S: 5gram to 300gram \nPrice: RM5\n\n")
parcel_prices.insert(tk.END, "Size M: 301gram to 700gram \nPrice: RM10\n\n")
parcel_prices.insert(tk.END, "Size L: 701gram until no limit \nPrice: RM20\n\n")
parcel_prices.configure(state='disabled')

# List of size to choose and user's total item and user can insert the number thru spinbox
box_two = tk.Frame(root)
box_two.pack()

pracel_info_frame =tk.LabelFrame(box_two, text="Parcel Information", font=('new times roman', 10, 'bold'))
pracel_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

size_label = tk.Label(pracel_info_frame, text="Select Your Size")
size_combobox = ttk.Combobox(pracel_info_frame, values=["Size S", "Size M", "Size L"])
size_label.grid(row=2, column=0, padx=20, pady=10)
size_combobox.grid(row=2, column=1, padx=20, pady=10)

item_label = tk.Label(pracel_info_frame, text="Total Item")
item_spinbox = tk.Spinbox(pracel_info_frame, from_=1, to=110)
item_label.grid(row=3, column=0, padx=20, pady=10)
item_spinbox.grid(row=3, column=1, padx=20, pady=10)

# Accept terms
terms_label = tk.Label(root, text="Terms & Conditions")
accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.pack(pady=10)

# Save Button
button = tk.Button(root, text="Submit", command=collect_data)
button.pack(pady=10)

# Output Label & result
box_three = tk.Frame(root)
box_three.pack()

price_info_frame =tk.LabelFrame(box_three, text="")
price_info_frame.grid(row=0, column=0, padx=20, pady=20)

label = tk.Label(price_info_frame, text='Total Price: ', font=("stencil", 13))
label.grid(row= 4, column=0, padx=20, pady=10)
output_label = tk.Label(price_info_frame, text="")
output_label.grid(row= 4, column=1, padx=20, pady=10)

root.mainloop()