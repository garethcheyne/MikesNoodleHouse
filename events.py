
def frm_show(self, name):
    # set button color for selected button
    self.btn_home.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    self.btn_customers.configure(fg_color=("gray75", "gray25") if name == "customers" else "transparent")
    self.btn_bookings.configure(fg_color=("gray75", "gray25") if name == "bookings" else "transparent")
    self.btn_menu.configure(fg_color=("gray75", "gray25") if name == "menu" else "transparent")

    print("frm_show: " + name)

    # show selected frame
    if name == "home":
        self.frm_home.grid(row=0, column=1, sticky="nsew")   
    else:
        self.frm_home.grid_forget()

    if name == "customers":
        self.frm_customers.grid(row=0, column=1, sticky="nsew")
    else:
        self.frm_customers.grid_forget()

    if name == "orders":
        self.frm_orders.grid(row=0, column=1, sticky="nsew")
    else:
        self.frm_orders.grid_forget()

    if name == "menu":
        self.frm_menu.grid(row=0, column=1, sticky="nsew")
    else:
        self.frm_menu.grid_forget()
