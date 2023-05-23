import os
import yaml
import tkinter as tk
import customtkinter as ctk
from PIL import Image
# import orm as _orm # My Customer DB Functions
import events as _events # My Customer Events Functions
import requests
from frames import ShoppingCart, StatusBar, NavBar
from helpers import *

DEBUG = True
WINDOW = {'width': 0, 'height':0}



p = 5

def _log(msg):
    if DEBUG:
        print(msg)

## Init Server Connection
def init_server():
    global CONFIG, BASE_URI, SESSION
    with open(file="config.yaml", mode="r") as f:
        try:
            CONFIG = yaml.load(f, Loader=yaml.FullLoader) 
            BASE_URI = f"https://{CONFIG['SERVER']['URI']}:{CONFIG['SERVER']['PORT']}/api/v{CONFIG['SERVER']['VERSION']}"
            f.close()
            SESSION = requests.Session()
            if DEBUG:
                SESSION.verify = False
                SESSION.trust_env = False
                os.environ['CURL_CA_BUNDLE']="" # Disable SSL Verification for Test, you would not do this in production.
            return True
        except yaml.YAMLError as exc:
            print(exc) 
            return False   

# Intit GUI.
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{1100}x{680}")
        self.title("Menu Mister Noodles")
        self.resizable(False, False)
        self.is_admin = False

        # set grid layout 1x2
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.frame_login()

    def resize(self, event):
        WINDOW = {'width': event.width, 'height':event.height}   
        print("Main Frame ", WINDOW)


    def sign_in(self):
        # There would be a more elegant way to do this
        _log(f"Signing in as {self.username.get()}...")

        res = SESSION.post(url=F"{BASE_URI}/auth", json={"username": self.username.get(), "password": self.password.get()})

        _log(f"Server Response {res.status_code}")
        
        if res.status_code == 200: 
            _log(f"Login Success: {res.json()['username']}") 

            self.user = res.json()['username']
            self.frm_login.destroy()       
            self.frame_main()
        elif res.status_code == 401:
            status_var = tk.StringVar(value="LOGIN FAILED! TRY AGAIN...")
            label = ctk.CTkLabel(master=self.frm_login,textvariable=status_var, width=200, height=35, font=("bold", 14), text_color=("white","white"), fg_color=("red", "red"), corner_radius=8)
            label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        elif res.status_code == 500:
            status_var = tk.StringVar(value="INTERNAL SERVER ERROR...")
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

    def frame_status(self):
        # Status Frame
        self.status_frame = ctk.CTkFrame(master=self)
        self.status_frame.grid()
  

    ## Main Menu Page
    def frame_main(self):

        self.img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.img_logo = ctk.CTkImage(Image.open(os.path.join(self.img_path, "logo.png")), size=(120, 120))
        self.icon_home = ctk.CTkImage(light_image=Image.open(os.path.join(self.img_path, "home_dark.png")), dark_image=Image.open(os.path.join(self.img_path, "home_light.png")), size=(20, 20))

        self.main = ctk.CTkFrame(master=self, bg_color='yellow')
        self.main.pack(fill="both", expand=True)
        self.main.bind("<Configure>", self.resize)        
        self.main.columnconfigure(2, weight=1)
        self.main.rowconfigure(1, weight=1)

        nav_frame = ctk.CTkFrame(master=self.main, width=200, height=655, bg_color='red')
        nav_frame.grid(row=0, column=0, sticky="nsew")
        nav_frame.rowconfigure(10, weight=1)
        nav_frame_label = ctk.CTkLabel(nav_frame, image=self.img_logo, compound="center", font=ctk.CTkFont(size=15, weight="bold"))
        nav_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.btn_home = ctk.CTkButton(nav_frame, corner_radius=0, height=40, border_spacing=10, text="Home", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "home"))  
        self.btn_home.grid(row=1, column=0, sticky="ew")

        self.btn_customers = ctk.CTkButton(nav_frame, corner_radius=0, height=40, border_spacing=10, text="Customers", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "customers"))
        self.btn_customers.grid(row=2, column=0, sticky="ew")

        self.btn_bookings = ctk.CTkButton(nav_frame, corner_radius=0, height=40, border_spacing=10, text="Bookings", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "bookings"))
        self.btn_bookings.grid(row=3, column=0, sticky="ew")

        self.btn_menu = ctk.CTkButton(nav_frame, corner_radius=0, height=40, border_spacing=10, text="Menu", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=lambda: _events.frm_show(self, "menu"))
        self.btn_menu.grid(row=4, column=0, sticky="ew")

        self.btn_sign_out= ctk.CTkButton(nav_frame, corner_radius=0, height=40, border_spacing=10, text="Sign Out", 
        fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), 
        image=self.icon_home, anchor="w", 
        command=self.sign_out)
        self.btn_sign_out.grid(row=9, column=0, sticky="nsew")



        main_frame = ctk.CTkFrame(master=self.main, width=700, bg_color='red', fg_color="yellow").grid(row=0, column=1, sticky="nsew")  

        cart_frame = ctk.CTkFrame(master=self.main, width=200, bg_color='red', fg_color="red").grid(row=0, column=2, sticky="nse")    
    
        status_frame = ctk.CTkFrame(master=self.main, bg_color='white', height=25).grid(row=1, column=0, columnspan=3, sticky="sew")
        

        # nav = NavBar.Frame(master=nav_frame)
        # nav.pack()

        # status = StatusBar.Frame(master=status_frame)
        # status.pack()
  


    # Run Main Loop
if __name__ == "__main__":
    server_up = init_server()
    if(server_up):
        app = App()
        app.mainloop()