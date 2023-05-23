import os
import yaml
import tkinter as tk
import customtkinter as ctk
from PIL import Image

class Frame(ctk.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../img")

        img_logo = ctk.CTkImage(Image.open(os.path.join(img_path, "logo.png")), size=(120, 120))
        icon_home = ctk.CTkImage(light_image=Image.open(os.path.join(img_path, "home_dark.png")), dark_image=Image.open(os.path.join(img_path, "home_light.png")), size=(20, 20))

        # # Left Side Navigation Frame        
        navigation_frame = ctk.CTkFrame(master, corner_radius=0)
        # navigation_frame.grid(row=0, column=0, sticky="nsew")
        # navigation_frame.grid_rowconfigure(0, weight=1)        

        # Place logo in Left Side Navigation Frame
        navigation_frame_label = ctk.CTkLabel(navigation_frame, image=img_logo, compound="center", font=ctk.CTkFont(size=15, weight="bold"))
        navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        # navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        
        # # Frames 
        # master.frm_home = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        # master.frm_home.grid(row=0, column=1, sticky="nsew")
        # master.frm_home.grid_columnconfigure(0, weight=1)

        # # ShoppingCart.Frame(master, "")

        # master.frm_customers = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        # master.frm_customers.grid_columnconfigure(0, weight=1)

        # master.frm_orders = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        # master.frm_orders.grid_columnconfigure(0, weight=1)

        # master.frm_menu = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        # master.frm_menu.grid_columnconfigure(0, weight=1)

 
        # # Place Buttons in Left Side Navigation Frame
        # master.btn_home = ctk.CTkButton(master.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", 
        # fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        # image=master.icon_home, anchor="w", 
        # command=lambda: _events.frm_show(master, "home"))  
        # master.btn_home.grid(row=1, column=0, sticky="ew")

        # master.btn_customers = ctk.CTkButton(master.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Customers", 
        # fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        # image=master.icon_home, anchor="w", 
        # command=lambda: _events.frm_show(master, "customers"))
        # master.btn_customers.grid(row=2, column=0, sticky="ew")

        # master.btn_bookings = ctk.CTkButton(master.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Bookings", 
        # fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        # image=master.icon_home, anchor="w", 
        # command=lambda: _events.frm_show(master, "bookings"))
        # master.btn_bookings.grid(row=3, column=0, sticky="ew")

        # master.btn_menu = ctk.CTkButton(master.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Menu", 
        # fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        # image=master.icon_home, anchor="w", 
        # command=lambda: _events.frm_show(master, "menu"))
        # master.btn_menu.grid(row=4, column=0, sticky="ew")

        # # master.btn_sign_out= ctk.CTkButton(master.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Sign Out", 
        # # fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        # # image=master.icon_home, anchor="w", 
        # # command=master.sign_out)
        # # master.btn_sign_out.grid(row=5, column=0, sticky="ews")

        # master.frm_menu = ctk.CTkFrame(master, corner_radius=0, fg_color="transparent")
        # master.frm_menu.grid_columnconfigure(0, weight=1)
 