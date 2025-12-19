import tkinter as tk
from tkinter import messagebox
import subprocess

APP_NAME = "Mordad Connect – Network Utility"
VERSION = "Version 1.1"

DNS_LIST = {
    "Cafe Net Mode": ("1.1.1.1", "1.0.0.1"),
    "Game Net Mode": ("9.9.9.9", "149.112.112.112")
}

def apply_dns(dns):
    try:
        output = subprocess.check_output(
            'netsh interface show interface',
            shell=True, text=True
        )
        iface = None
        for line in output.splitlines():
            if "Connected" in line:
                iface = line.split()[-1]
                break

        if not iface:
            return False

        subprocess.call(
            f'netsh interface ip set dns name="{iface}" static {dns[0]}',
            shell=True
        )
        subprocess.call(
            f'netsh interface ip add dns name="{iface}" {dns[1]} index=2',
            shell=True
        )
        subprocess.call('ipconfig /flushdns', shell=True)
        return True
    except:
        return False

def set_mode(mode):
    global current_mode
    current_mode = mode
    dns = DNS_LIST[mode]
    dns_label.config(text=f"{dns[0]} / {dns[1]}")
    status_label.config(text=f"Mode: {mode}")

def apply_action():
    dns = DNS_LIST[current_mode]
    if apply_dns(dns):
        messagebox.showinfo(APP_NAME, "DNS configuration applied successfully.")
    else:
        messagebox.showerror(APP_NAME, "Administrator access is required.")

# UI
root = tk.Tk()
root.title(APP_NAME)
root.geometry("400x520")
root.resizable(False, False)

tk.Label(root, text=APP_NAME, font=("Segoe UI", 16, "bold")).pack(pady=12)
tk.Label(root, text=VERSION, fg="gray", font=("Segoe UI", 9)).pack()

current_mode = "Cafe Net Mode"

mode_frame = tk.Frame(root)
mode_frame.pack(pady=15)

tk.Button(
    mode_frame, text="Cafe Net Mode",
    width=16, command=lambda: set_mode("Cafe Net Mode")
).pack(side="left", padx=8)

tk.Button(
    mode_frame, text="Game Net Mode",
    width=16, command=lambda: set_mode("Game Net Mode")
).pack(side="left", padx=8)

status_label = tk.Label(root, text="Mode: Cafe Net Mode")
status_label.pack(pady=10)

tk.Label(root, text="Recommended DNS:", font=("Segoe UI", 10, "bold")).pack()
dns_label = tk.Label(root, text="-")
dns_label.pack(pady=5)

tk.Button(
    root, text="Apply DNS Configuration",
    width=24, height=2,
    command=apply_action
).pack(pady=25)

tk.Label(
    root,
    text="Created by Mordad Cafenet\nGorgan – Iran",
    fg="gray",
    font=("Segoe UI", 8)
).pack(side="bottom", pady=10)

set_mode("Cafe Net Mode")
root.mainloop()
