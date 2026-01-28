import tkinter as tk

# 1. Khởi tạo cửa sổ chính
root = tk.Tk()

# 2. Thiết lập tiêu đề cho cửa sổ
root.title("Cửa Sổ Đầu Tiên Của Tôi")

# 3. Thiết lập kích thước (chiều rộng x chiều cao)
root.geometry("1000x1000")

# 4. Thêm nội dung (ví dụ: một label)
label = tk.Label(root, text="Chào mừng đến với Tkinter!")
label.pack(pady=50) # .pack() để đặt widget vào cửa sổ

# 5. Bắt đầu vòng lặp sự kiện (giữ cửa sổ mở)
root.mainloop()