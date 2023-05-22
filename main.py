import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image
# import orm as _orm # My Customer DB Functions
import events as _events # My Customer Events Functions
from sqlalchemy import create_engine, insert, select, update, delete, and_, or_, not_
from sqlalchemy.orm import sessionmaker
from database.models import Base, User, Product
# from database import models as db# My Customer DB Models
from helpers import *



## Init DB
engine = create_engine(f"sqlite:///database/database.db", echo=True) # echo=True for debug
Session = sessionmaker(bind=engine)
session = Session()

## Create models if not exist.
Base.metadata.create_all(engine)


# Intit GUI.
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{1100}x{680}")
        self.title("Menu Mister Noodles")
        # self.resizable(False, False)
        self.is_admin = False

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.frame_login()

    def sign_in(self):
        print(self.username.get())

        # There would be a more elegant way to do this
        res = session.query(User).filter(and_(
            User.username == self.username.get(),
            User.password == hash_password(self.password.get())))

        if len(res.all()) > 0: 
            print("Login Success")       
            self.user=res.first().username
            self.frm_login.destroy()       
            self.frame_main()
        else:
            status_var = tk.StringVar(value="LOGIN FAILED! TRY AGAIN...")
            label = ctk.CTkLabel(master=self.frm_login,textvariable=status_var, width=200, height=35, font=("bold", 14), text_color=("white","white"), fg_color=("red", "red"), corner_radius=8)
            label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def sign_out(self):
        self.user = None
        self.navigation_frame.destroy()
        self.frame_login()


    def frame_login(self):
        # Login Frame
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
        self.btn_signin.pack(pady=10, padx=25)
        self.btn_signin.bind("<Return>", self.sign_in)


    ## Main Menu Page
    def frame_main(self):
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

        # Frames 
        self.frm_home = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_home.grid_columnconfigure(0, weight=1)

        self.frm_customers = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_customers.grid_columnconfigure(0, weight=1)

        self.frm_orders = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_orders.grid_columnconfigure(0, weight=1)

        self.frm_menu = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_menu.grid_columnconfigure(0, weight=1)

 
        # Place Buttons in Left Side Navigation Frame
        self.btn_home = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "home"))  
        self.btn_home.grid(row=1, column=0, sticky="ew")

        self.btn_customers = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Customers", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "customers"))
        self.btn_customers.grid(row=2, column=0, sticky="ew")

        self.btn_bookings = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Bookings", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "bookings"))
        self.btn_bookings.grid(row=3, column=0, sticky="ew")

        self.btn_menu = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Menu", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "menu"))
        self.btn_menu.grid(row=4, column=0, sticky="ew")

        self.btn_sign_out= ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sign Out", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=self.sign_out)
        self.btn_sign_out.grid(row=5, column=0, sticky="ews")

        self.frm_menu = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frm_menu.grid_columnconfigure(0, weight=1)

    # Run Main Loop
if __name__ == "__main__":
    app = App()
    app.mainloop()