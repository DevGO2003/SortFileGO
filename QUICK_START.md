# 🚀 HƯỚNG DẪN NHANH - FILE SORTER

## Cách 1: Chạy trực tiếp (khuyến nghị)

1. **Mở Command Prompt hoặc PowerShell tại thư mục này**

2. **Chạy lệnh**:
   ```bash
   python file_sorter.py
   ```

3. **Cửa sổ ứng dụng sẽ hiện ra** → Làm theo hướng dẫn trên giao diện

---

## Cách 2: Đóng gói thành .exe (để chia sẻ)

### Tự động (Dễ nhất) ✨

Chỉ cần **double-click vào file**:
```
build_exe.bat
```

File `.exe` sẽ được tạo trong thư mục `dist/FileSorter.exe`

### Thủ công (Nâng cao)

```bash
# 1. Cài PyInstaller (chỉ làm 1 lần)
pip install pyinstaller

# 2. Đóng gói
pyinstaller --onefile --noconsole --name "FileSorter" file_sorter.py

# 3. Lấy file .exe
# → Nó nằm trong thư mục dist/FileSorter.exe
```

---

## 🎯 Sử dụng ứng dụng

1. **Chọn thư mục** cần sắp xếp (ví dụ: D:\Downloads)
2. **Chọn tùy chọn**:
   - ✅ Bao gồm thư mục con (recursive)
   - ✅ Tạo file log
3. **Click "Bắt đầu sắp xếp"**
4. **Xem kết quả** trong log window

---

## 💡 Ví dụ

**Trước khi sắp xếp:**
```
D:\Downloads\
├── photo.jpg
├── video.mp4
├── document.pdf
└── music.mp3
```

**Sau khi sắp xếp:**
```
D:\Downloads\
├── .jpg\
│   └── photo.jpg
├── .mp4\
│   └── video.mp4
├── .pdf\
│   └── document.pdf
├── .mp3\
│   └── music.mp3
└── sort_log.txt  (nếu bật option Create Log)
```

---

## ❓ Gặp vấn đề?

### Python chưa cài đặt
➡️ Tải tại: https://www.python.org/downloads/
✅ Nhớ tick "Add Python to PATH"

### Tkinter không có
➡️ Cài lại Python và chọn "tcl/tk and IDLE"

### Không di chuyển được file
➡️ Đảm bảo file không đang mở
➡️ Chạy Command Prompt as Administrator

---

## 📞 Hỗ trợ

Xem file `README.md` để biết chi tiết đầy đủ.
