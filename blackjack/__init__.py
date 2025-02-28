import customtkinter as ctk
import os
import json
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from UX.theme.colors import BG_COLOR

class App(ctk.CTk):

    def __init__(self, window_bar=None):
        super().__init__()
        self.window_bar = True if window_bar is None else False

        self.maximized = False
        self.normal_geometry = None

        self.__dataFile(0)
        self._dataUpdate()

        if self.window_bar:
            self.titleBar()

        self._userProcess()

    def titleBar(self):
        self.title_bar = ctk.CTkFrame(self, height=40, corner_radius=0)
        self.title_bar.pack(fill="x", side="top")

        minimize_button = ctk.CTkButton(self.title_bar, text="_", width=30, height=30, command=self.simulateMinimize)
        minimize_button.pack(side="right", padx=5, pady=5)

        self.maximize_button = ctk.CTkButton(self.title_bar, text="□", width=30, height=30, command=self.toggle_maximize)
        self.maximize_button.pack(side="right", padx=5, pady=5)

        close_button = ctk.CTkButton(self.title_bar, text="X", width=30, height=30, fg_color="red", hover_color="darkred", command=self.destroy)
        close_button.pack(side="right", padx=5, pady=5)

        title_label = ctk.CTkLabel(self.title_bar, text="Bueno's Casino")
        title_label.pack(side="left", padx=10)

    def run(self):
        self.overrideredirect(self.window_bar)

        #? centralize the window on the run
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"1000x500+{int((self.screen_width - 1000) / 2)}+{int((self.screen_height - 500) / 2)}")

        self.title("Bueno's Casino")
        self.mainloop()

    def simulateMinimize(self):
        if not self.normal_geometry:
            self.normal_geometry = self.geometry()
        self.withdraw()
        self.minimized = True

    def toggle_maximize(self):
        if self.maximized:
            if self.normal_geometry:
                self.geometry(self.normal_geometry)
            self.maximize_button.configure(text="□")
            self.maximized = False
        else:
            self.normal_geometry = self.geometry()
            self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
            self.maximize_button.configure(text="🗗")
            self.maximized = True

    def __dataFile(self, entrance):
        if entrance == 0:
            new_data = {
                "data": {
                    "bank_data": {
                        "money": 150,
                        "debt": 0
                    },
                    "user_data": {
                        "username": None
                    }
                }
            }

            if not os.path.exists("data/data.json"):
                os.makedirs("data", exist_ok=True)
                with open("data/data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
                self.data = new_data
            else:
                with open("data/data.json", "r") as f:
                    self.data = json.load(f)
        else:
            with open("data/data.json", "w") as f:
                json.dump(self.data, f, indent=4)

    def _dataUpdate(self):
        #? uptade the bank variables
        self.money = self.data["data"]["bank_data"]["money"]
        self.debt = self.data["data"]["bank_data"]["debt"]

        #? update the username variable 
        self.username = self.data["data"]["user_data"]["username"]

    def _userProcess(self):
        if self.username is None:
            self._newUserDetected()
        else:
            # self._gameMenu()
            pass

    def _newUserDetected(self):
        frame_user = ctk.CTkFrame(self, width=200, height=200)
        frame_user.pack(pady=100)

        username_entry = ctk.CTkEntry(frame_user, placeholder_text="enter username")
        username_entry.pack(pady=20)

        def on_enter():
            username = username_entry.get()
            if any(char.isnumeric() or char.isspace() for char in username):
                enter_button.configure(fg_color="red")
            else:
                self.data["data"]["user_data"]["username"] = username
                self.__dataFile(1)
                frame_user.pack_forget()

        enter_button = ctk.CTkButton(frame_user, text="Enter", command=on_enter)
        enter_button.pack(pady=20)

    def returnData(self):
        return self.data

if __name__ == "__main__":
    app = App()
    app.run()