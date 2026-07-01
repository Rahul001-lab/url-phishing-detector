import customtkinter as ctk
from detector import scan_url

# Window Setup

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("URL Phishing Detector")
app.geometry("800x600")
app.resizable(False, False)

# Scan Function

def scan():

    url = url_entry.get().strip()

    if url == "":
        result_box.delete("0.0", "end")
        result_box.insert("0.0", "Please enter a URL.")
        return

    result = scan_url(url)

    result_box.delete("0.0", "end")

    output = f"""Status : {result['status']}

Risk Score : {result['score']}/100

Reasons:
"""

    for reason in result["reasons"]:
        output += f"\n• {reason}"

    result_box.insert("0.0", output)

# Title

title = ctk.CTkLabel(
    app,
    text="🛡 URL Phishing Detector",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# URL Label

label = ctk.CTkLabel(
    app,
    text="Enter URL:",
    font=("Arial", 18)
)
label.pack(pady=5)

# URL Entry

url_entry = ctk.CTkEntry(
    app,
    width=600,
    height=40,
    placeholder_text="https://example.com"
)
url_entry.pack(pady=10)

# Result Title

result_title = ctk.CTkLabel(
    app,
    text="Result",
    font=("Arial", 22, "bold")
)
result_title.pack(pady=10)

# Result Box

result_box = ctk.CTkTextbox(
    app,
    width=700,
    height=220
)
result_box.pack(pady=10)

result_box.insert("0.0", "Scan a URL to see the results here...")

# Scan Button

scan_button = ctk.CTkButton(
    app,
    text="Scan URL",
    width=200,
    height=40,
    command=scan
)
scan_button.pack(pady=20)

app.mainloop()