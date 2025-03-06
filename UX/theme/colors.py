import customtkinter as ctk
#? file address UX/theme/colors.py
#? file for variables holding hex string values

#? acronym for variable name
    #? TXT = text
    #? BG = background
    #? HR = hover
    #? CB = border 

#? defining the colors

#? title bar colors
cTITLE_BAR_BG = "#212021" 
cTITLE_BAR_TXT = "#FF0000"
#? new users frame colors
cNEW_USER_BG = "#212021"
cNEW_USER_ENTRY_BG = "#4f4d4f"
cNEW_USER_ENTRY_CB = NEW_USER_BUTTON_CB = "#3b393b"
cNEW_USER_BUTTON_HR = "#FF0000"
cNEW_USER_BUTTON_BG = "#212021"
cNEW_USER_BUTTON_TXT = "#FF0000"
cWELCOME_TXT = "#FF0000"

ALL_COLORS = [
    cTITLE_BAR_BG,
    cTITLE_BAR_TXT, 
    cNEW_USER_ENTRY_BG, 
    cNEW_USER_ENTRY_CB
    ]

def testColors():
    root = ctk.CTk()
    root.geometry("500x500")
    root.title("Test Colors")

    for index_column, color in enumerate(ALL_COLORS):
        frame = ctk.CTkFrame(root, width=50, height=50, fg_color=color)
        index_row = 0
        index_row + 1 if index_column // 10 == 1 else 0
        frame.grid(row=index_row,column=index_column, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    # testColors()
    pass