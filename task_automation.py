# This is a simple GUI application that automates tasks like moving files, extracting emails, and scraping webpage titles.
import os
import shutil
import re
import requests
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# --- Task 1: Move .jpg files ---


def move_jpg_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    files_moved = 0
    for filename in os.listdir(src):
        if filename.lower().endswith('.jpg'):
            shutil.move(os.path.join(src, filename),
                        os.path.join(dst, filename))
            files_moved += 1
    return files_moved

# --- Task 2: Extract emails ---


def extract_emails_from_file(input_path, output_path):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    emails = sorted(set(re.findall(email_pattern, content)))
    if emails:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for email in emails:
                f_out.write(email + '\n')
    return len(emails)

# --- Task 3: Scrape webpage title ---


def scrape_title(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        match = re.search(r'<title>(.*?)</title>',
                          response.text, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(title)
            return title
        else:
            return None
    except requests.RequestException as e:
        return str(e)

# --- GUI Application ---


class AutomationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Automation Tool")
        self.geometry("400x300")

        tk.Label(self, text="Choose a task to perform:",
                 font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="1. Move all .jpg files", width=30,
                  command=self.run_move_jpg).pack(pady=5)
        tk.Button(self, text="2. Extract emails from .txt file",
                  width=30, command=self.run_extract_emails).pack(pady=5)
        tk.Button(self, text="3. Scrape webpage title", width=30,
                  command=self.run_scrape_title).pack(pady=5)

    def run_move_jpg(self):
        src = filedialog.askdirectory(title="Select Source Folder")
        if not src:
            return
        dst = filedialog.askdirectory(title="Select Target Folder")
        if not dst:
            return
        count = move_jpg_files(src, dst)
        messagebox.showinfo(
            "Done", f"Moved {count} .jpg files from:\n{src}\nto\n{dst}")

    def run_extract_emails(self):
        input_path = filedialog.askopenfilename(
            title="Select .txt File", filetypes=[("Text files", "*.txt")])
        if not input_path:
            return
        output_path = filedialog.asksaveasfilename(
            title="Save Emails To", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not output_path:
            return
        count = extract_emails_from_file(input_path, output_path)
        if count:
            messagebox.showinfo(
                "Done", f"Extracted {count} emails to:\n{output_path}")
        else:
            messagebox.showwarning(
                "No Emails Found", "No email addresses found in the file.")

    def run_scrape_title(self):
        url = simpledialog.askstring("Input", "Enter the webpage URL:")
        if not url:
            return
        output_path = filedialog.asksaveasfilename(
            title="Save Title To", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not output_path:
            return
        result = scrape_title(url, output_path)
        if result is None:
            messagebox.showwarning(
                "No Title Found", "Could not find a title tag on the webpage.")
        elif result.startswith("HTTP") or "Error" in result:
            messagebox.showerror(
                "Error", f"Failed to fetch the page:\n{result}")
        else:
            messagebox.showinfo("Done", f"Webpage title saved:\n{result}")


if __name__ == "__main__":
    app = AutomationApp()
    app.mainloop()
