import customtkinter

class RaumFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        self.raeume = []
        self.title_label = customtkinter.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            raum = customtkinter.CTkButton(self, text = value, command=self.raum_geklickt)
            raum.grid(row = i + 1, column=0, padx=10, pady=(10,0), sticky="w")
            self.raeume.append(raum)

    def raum_geklickt(self):
        print("Raum ausgewählt")
class Hauptansicht(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Heizungssteuerung")
        self.geometry("700x1080")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight = 1)
        values = ["A068", "A069","A068", "A069","A068", "A069","A068", "A069" ]
        self.raum_frame = RaumFrame(self, "Räume", values = values)
        self.raum_frame.grid(row=1, column=0,padx=10, pady=(10, 0), sticky="w", columnspan = 2)
        self.button =customtkinter.CTkButton(self, text="Notsteuerung", fg_color="red", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20,sticky="ew", columnspan=1)
    def button_callback(self):
        print("Button pressed")

hauptansicht = Hauptansicht()
hauptansicht.mainloop()
