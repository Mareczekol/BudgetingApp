import customtkinter
import csv

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry('800x720')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

category = {}


def add():
    category_name = entry1.get()
    category[category_name] = {}
    entry1.delete(0, customtkinter.END)
    display_categories()


def display_categories():
    for category_name in category:
        label = customtkinter.CTkLabel(master=frame, text=category_name)
        label.bind("<Button-1>", lambda event, name=category_name:
                   category_clicked(name))
        label.pack(pady=5, padx=10)

    # display_summary()


def category_clicked(category_name):
    category_window = customtkinter.CTkToplevel(master=root)
    category_window.title(category_name)
    category_window.geometry('400x400')

    category_label = customtkinter.CTkLabel(master=category_window,
                                            text=f"Kategoria: {category_name}")
    category_label.pack(pady=10, padx=10)

    product_name_label = customtkinter.CTkLabel(master=category_window,
                                                text="Nazwa produktu:")
    product_name_label.pack(pady=5, padx=10)

    product_name_entry = customtkinter.CTkEntry(master=category_window)
    product_name_entry.pack(pady=5, padx=10)

    price_label = customtkinter.CTkLabel(master=category_window,
                                         text="Cena:")
    price_label.pack(pady=5, padx=10)

    price_entry = customtkinter.CTkEntry(master=category_window)
    price_entry.pack(pady=5, padx=10)

    quantity_label = customtkinter.CTkLabel(master=category_window,
                                            text="Ilość:")
    quantity_label.pack(pady=5, padx=10)

    quantity_entry = customtkinter.CTkEntry(master=category_window)
    quantity_entry.pack(pady=5, padx=10)

    category_button = customtkinter.CTkButton(master=category_window,
                                              text="Zapisz",
                                              command=lambda:
                                              zapisz(category_name,
                                                     product_name_entry.get(),
                                                     price_entry.get(),
                                                     quantity_entry.get()))
    category_button.pack(pady=10, padx=10)


def zapisz(category_name, product_name, price, quantity):
    product_name = product_name.get()
    price = price.get()
    quantity = quantity.get()

    category[category_name] = {
        'Nazwa produktu': product_name,
        'Cena': price,
        'Ilość': quantity
    }

    # Calculate the total cost for the category
    total_cost = float(price) * int(quantity)

    # Save the changes to a CSV file
    with open('categories.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Kategoria', 'Nazwa produktu', 'Cena', 'Ilość', 'Koszt'])
        for category_name, data in category.items():
            writer.writerow([category_name, data['Nazwa produktu'],
                             data['Cena'], data['Ilość'], total_cost])

    display_summary()

    product_name.delete(0, customtkinter.END)
    price.delete(0, customtkinter.END)
    quantity.delete(0, customtkinter.END)


def display_summary():
    total_expenses = 0
    for data in category.values():
        if 'Cena' in data and 'Ilość' in data:
            price = float(data['Cena'])
            quantity = int(data['Ilość'])
            total_expenses += price * quantity

    summary_label = customtkinter.CTkLabel(master=frame,
                                           text=f"Podsumowanie wydatków: "
                                                f"{total_expenses}")
    summary_label.pack(pady=10, padx=10)


label = customtkinter.CTkLabel(master=frame, text="Budget App")
label.pack(pady=12, padx=10)

label1 = customtkinter.CTkLabel(master=frame, text="Kategoria")
label1.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(master=frame)
entry1.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Dodaj", command=add)
button.pack(pady=12, padx=10)

root.mainloop()
