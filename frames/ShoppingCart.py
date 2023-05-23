import os
import yaml
import tkinter as tk
import customtkinter as ctk
from PIL import Image

class Frame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []

        img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../img")
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