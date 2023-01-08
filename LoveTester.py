import customtkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x350")
app.title("Love Tester")

def generatePercent():
    percent = random.randint(1, 100)
    progressbar.set(percent / 100)
    label2.configure(text = f"{percent}%")
    clearEntries()

def clearEntries():
    entry1.delete(0, customtkinter.END)
    entry2.delete(0, customtkinter.END)

frame1 = customtkinter.CTkFrame(master=app)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

frame2 = customtkinter.CTkFrame(master=frame1)
frame2.pack(pady=10, padx=10, fill="both", expand=False)

label = customtkinter.CTkLabel(master=frame2, text="Enter the names:", font=("Cooper Black", 24))
label.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Person 1", font=("Cooper Black", 14))
entry1.pack(pady=10, padx=10)

entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Person 2", font=("Cooper Black", 14))
entry2.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame1, text="Generate", font=("Cooper Black", 16), command=generatePercent)
button.pack(padx=10, pady=10)

progressbar = customtkinter.CTkProgressBar(master=frame1)
progressbar.pack(padx=10, pady=10)
progressbar.set(0)

frame3 = customtkinter.CTkFrame(master=frame1)
frame3.pack(pady=10, padx=10, fill="both", expand=False)

label2 = customtkinter.CTkLabel(master=frame3, text="???", font=("Cooper Black", 24))
label2.pack(pady=10, padx=10)

app.bind_all("<1>", lambda event:event.widget.focus_set())

app.mainloop()