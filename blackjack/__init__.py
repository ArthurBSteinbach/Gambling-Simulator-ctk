import customtkinter as ctk
import os
import json

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.__dataFile(0)
        self._dataUpdate
        self._userProcess

    def run(self):
        self.geometry("1000x500")
        self.title("Bueno's Casino")
        self.mainloop()

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

            if not os.path.exists("data\data.json"):
                with open("data\data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
                self.data = new_data
            else:
                with open("data\data.json", "r") as f:
                    self.data = json.load(f)
        else:
            with open("data\data.json", "w") as f:
                json.dump(self.data, f, indent=4)

    def _dataUpdate(self):
        #? bank_data
        self.money = self.data["data"]["bank_data"]["money"]
        self.debt = self.data["data"]["bank_data"]["debt"]

        #? user_data
        self.username = self.data["data"]["user_data"]["username"]

    def _userProcess(self):
        if self.username == None:
            self._newUserDetected
        else:
            # self._gameMenu
            pass
    def _newUserDetected(self):
        frame = ctk.CTkFrame(self,width=200,height=200)
        frame.pack_propagate(False)
        frame.pack(pady=300)
        

if __name__ == "__main__":
    app = App()
    app.run()