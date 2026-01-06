import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        width = float(entry_width.get())
        length = float(entry_length.get())
        
        area = 0.5 * width * length
        
        label_result.config(text=f"พื้นที่สามเหลี่ยมคือ: {area:.2f}", fg="blue")
        
    except:
        messagebox.showerror("Error", "กรุณากรอกเฉพาะตัวเลข")

root = tk.Tk()
root.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")
root.geometry("400x300")

tk.Label(root, text="การหาพื้นที่สามเหลี่ยมใดๆ", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="ความกว้างฐาน (width):").pack()
entry_width = tk.Entry(root)
entry_width.pack(pady=5)

tk.Label(root, text="ความสูง (length):").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

tk.Button(root, text="ตกลง", command=calculate).pack(pady=20)

label_result = tk.Label(root, text="ผลลัพธ์", font=("Arial", 12))
label_result.pack()

root.mainloop()