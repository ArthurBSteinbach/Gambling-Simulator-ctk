import customtkinter as ctk

#? file address UX/theme/colors.py
#? file for variables holding hex string values

#? defining the colors

#? title bar colors
cTITLE_BAR = "#212021"
cTITLE_BAR_LABEL = "#FF0000"  #? title bar color
cBACKGROUND_ROOT = "#FFD700"   #? background of he app color

#? new users colors
cBACKGROUND_NEW_USER = "#212021"
cNEW_USER_ENTRY = ""


ALL_COLORS = [cTITLE_BAR,cTITLE_BAR_LABEL, cBACKGROUND_ROOT, ]

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
    testColors()