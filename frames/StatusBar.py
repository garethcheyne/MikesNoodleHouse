import os
import yaml
import tkinter as tk
import customtkinter as ctk
from PIL import Image

class Frame(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.label = ctk.CTkLabel(self, text="Status Bar")
        self.label.pack(side="left", padx=10)
        self.pack(side="bottom", fill="x")
