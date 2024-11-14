import customtkinter

class RaumFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title_label = customtkinter.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.raum_1 = customtkinter.CTkButton(self, text = "A068", command=self.raum_geklickt)
        self.raum_1.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")
        self.raum_2 = customtkinter.CTkButton(self, text="A069", command=self.raum_geklickt)
        self.raum_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
    def raum_geklickt(self):
        print("Raum ausgewählt")
class Hauptansicht(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Heizungssteuerung")
        self.geometry("700x1080")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight = 1)
        self.raum_frame = RaumFrame(self, "Räume")
        self.raum_frame.grid(row=1, column=0,padx=10, pady=(10, 0), sticky="w", columnspan = 2)
        self.button =customtkinter.CTkButton(self, text="Notsteuerung", fg_color="red", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20,sticky="ew", columnspan=1)
    def button_callback(self):
        print("Button pressed")

hauptansicht = Hauptansicht()
hauptansicht.mainloop()
