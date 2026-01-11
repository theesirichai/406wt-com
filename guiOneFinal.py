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
root.geometry("400x200")

tk.Label(root, text="การหาพื้นที่สามเหลี่ยมใดๆ").pack()
entry_width = tk.Entry(root)
entry_width.pack()

tk.Label(root, text="ความกว้างฐาน (width):").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Button(root, text="ตกลง", command=calculate).pack()
label_result = tk.Label(root, text="ผลลัพธ์")
label_result.pack()

root.mainloop()