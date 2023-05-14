import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image
import functions as _ # My Customer DB Functions


# Init database and create tables and admin user if not exists, ie first run
conn = _.database()
conn.create_db_tabels()
conn.create_admin_user(password="happy123")

# Intit GUI.
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{1100}x{580}")
        self.title("Menu Mister Noodles")
        # self.resizable(False, False)
        self.is_admin = False

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.frm_login = ctk.CTkFrame(master=self)
        self.frm_login .pack(pady=60, padx=60, fill="both", expand=True)

        img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.img_logo = ctk.CTkImage(Image.open(os.path.join(img_path, "logo.png")), size=(220, 220))
        self.logo = ctk.CTkLabel(master=self.frm_login, image=self.img_logo, text="")
        self.logo.pack(pady=30, padx=30)

        self.username = ctk.CTkEntry(master=self.frm_login , placeholder_text="username")
        self.username.pack(pady=10, padx=10)

        self.password = ctk.CTkEntry(master=self.frm_login , placeholder_text="password", show="*")
        self.password.pack(pady=10, padx=10)

        self.btn_signin = ctk.CTkButton(master=self.frm_login , text="Sign In", command=self.sign_in)
        self.btn_signin.pack(pady=10, padx=10)
        self.btn_signin.bind("<Return>", self.sign_in)

    def sign_in(self):
        res = conn.auth_user(self.username.get(), self.password.get())
        if res['status'] == 200: 
            print("Login Success")       
            self.user=res['user']
            self.frm_login.destroy()            
            self.main()
        else:
            status_var = tk.StringVar(value="LOGIN FAILED! TRY AGAIN...")
            label = ctk.CTkLabel(master=self.frm_login,textvariable=status_var, width=240, height=40, font=("bold", 16), text_color=("black","black"), fg_color=("white", "white"), corner_radius=8)
            label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # All Click Events
    def evt_home(self):
        print('evt_home')


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.btn_home.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.btn_customers.configure(fg_color=("gray75", "gray25") if name == "customers" else "transparent")
        self.btn_bookings.configure(fg_color=("gray75", "gray25") if name == "bookings" else "transparent")
        self.btn_menu.configure(fg_color=("gray75", "gray25") if name == "menu" else "transparent")

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

    ## Main Menu Page
    def main(self):
        # Set Images/Icons
        img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.img_logo = ctk.CTkImage(Image.open(os.path.join(img_path, "logo.png")), size=(120, 120))
        self.icon_home = ctk.CTkImage(light_image=Image.open(os.path.join(img_path, "home_dark.png")), dark_image=Image.open(os.path.join(img_path, "home_light.png")), size=(20, 20))

        # Left Side Navigation Frame        
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Place logo in Left Side Navigation Frame
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, image=self.img_logo, compound="center", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Place Buttons in Left Side Navigation Frame
        self.btn_home = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.icon_home, anchor="w", command=self.evt_home)
        self.btn_home.grid(row=1, column=0, sticky="ew")

        self.btn_customers = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.icon_home, anchor="w", command=self.evt_home)
        self.btn_customers.grid(row=2, column=0, sticky="ew")

        self.btn_bookings = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.icon_home, anchor="w", command=self.evt_home)
        self.btn_bookings.grid(row=3, column=0, sticky="ew")

        self.btn_menu = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.icon_home, anchor="w", command=self.evt_home)
        self.btn_menu.grid(row=4, column=0, sticky="ew")

        # Home Frame    
        self.frm_home = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_home.grid_columnconfigure(0, weight=1)

        self.frm_customers = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_customers.grid_columnconfigure(0, weight=1)

        self.frm_orders = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_orders.grid_columnconfigure(0, weight=1)

        # self.select_frame_by_name("home")
        self.select_frame_by_name("orders")

    # Run Main Loop
if __name__ == "__main__":
    app = App()
    app.mainloop()