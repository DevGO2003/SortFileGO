# 📁 File Sorter - Ứng dụng sắp xếp file theo extension

Ứng dụng Windows có giao diện đồ họa để tự động sắp xếp file theo phần mở rộng (.jpg, .pdf, .mp3, v.v.)

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Tính năng

- ✅ **Giao diện đồ họa đẹp mắt** - Dễ sử dụng với Tkinter
- 📂 **Chọn thư mục tùy ý** - Không bị giới hạn ở ổ D:\
- 🔄 **Hỗ trợ recursive** - Quét toàn bộ thư mục con
- 📊 **Hiển thị tiến trình** - Progress bar realtime
- 📝 **Tạo file log** - Ghi lại tất cả thao tác
- 🔀 **Xử lý trùng tên** - Tự động đánh số file (1), (2), (3)...
- 🚀 **Chạy multi-thread** - Không làm đơ giao diện
- 🔒 **Hỗ trợ quyền admin** - Có thể bật nếu cần

## 📋 Yêu cầu

- Python 3.7 trở lên
- Tkinter (có sẵn trong Python)
- Windows (có thể chạy trên Linux/Mac nhưng chưa test kỹ)

## 🚀 Cách sử dụng

### Phương án 1: Chạy trực tiếp (khuyến nghị cho dev)

1. **Cài Python** (nếu chưa có):
   - Tải tại: https://www.python.org/downloads/
   - ✅ Nhớ tick "Add Python to PATH"

2. **Chạy ứng dụng**:
   ```bash
   python file_sorter.py
   ```

3. **Sử dụng**:
   - Click "🔍 Chọn thư mục" → Chọn thư mục cần sắp xếp
   - Chọn options (recursive, create log)
   - Click "▶️ Bắt đầu sắp xếp"
   - Xem tiến trình và log

### Phương án 2: Đóng gói thành file .exe (dễ chia sẻ)

1. **Cài PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Tạo file .exe**:
   ```bash
   pyinstaller --onefile --noconsole --name "FileSorter" --icon=icon.ico file_sorter.py
   ```

   Hoặc dùng lệnh đơn giản hơn:
   ```bash
   pyinstaller --onefile --noconsole file_sorter.py
   ```

3. **File .exe** sẽ ở trong thư mục `dist/`:
   ```
   dist/
   └── FileSorter.exe  ← Click đúp để chạy
   ```

4. **Chia sẻ**: Copy file `FileSorter.exe` cho bất kỳ ai, không cần cài Python!

## 🎯 Cách hoạt động

```
D:\Downloads\
├── photo1.jpg
├── photo2.jpg
├── document.pdf
├── song.mp3
└── video.mp4

    ↓ Sau khi sắp xếp ↓

D:\Downloads\
├── .jpg\
│   ├── photo1.jpg
│   └── photo2.jpg
├── .pdf\
│   └── document.pdf
├── .mp3\
│   └── song.mp3
└── .mp4\
    └── video.mp4
```

- File **không có đuôi** → Vào thư mục `._no_ext\`
- File **trùng tên** → Tự động đổi thành `file (1).jpg`, `file (2).jpg`

## ⚙️ Các tùy chọn

### 1. Recursive (Quét thư mục con)
- ✅ **Bật**: Sắp xếp tất cả file trong thư mục và thư mục con
- ❌ **Tắt**: Chỉ sắp xếp file ở thư mục gốc

### 2. Create Log (Tạo file log)
- ✅ **Bật**: Tạo file `sort_log.txt` ghi lại tất cả thao tác
- ❌ **Tắt**: Không lưu log

### 3. Quyền Admin (tùy chọn)
Nếu cần di chuyển file hệ thống hoặc file đang bị lock, bạn có thể:

**Cách 1**: Chạy Command Prompt as Administrator → chạy script

**Cách 2**: Uncomment dòng này trong `file_sorter.py`:
```python
def main():
    run_as_admin()  # ← Bỏ comment dòng này
    ...
```

## 🛠️ Sửa đổi & Tuỳ biến

### Thay đổi quy tắc sắp xếp
Hiện tại app sắp xếp theo **extension**. Nếu muốn sắp xếp theo loại file:

```python
# Thêm mapping vào đầu hàm sort_files()
CATEGORY_MAP = {
    'jpg': 'Images',
    'png': 'Images',
    'pdf': 'Documents',
    'docx': 'Documents',
    'mp3': 'Music',
    'mp4': 'Videos',
}

# Thay dòng này:
target_folder = os.path.join(source_folder, f".{ext}")

# Thành:
category = CATEGORY_MAP.get(ext.lower(), f".{ext}")
target_folder = os.path.join(source_folder, category)
```

### Thêm whitelist/blacklist extension
```python
# Chỉ sắp xếp ảnh
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
if ext.lower() not in ALLOWED_EXTENSIONS:
    continue

# Bỏ qua file hệ thống
IGNORED_EXTENSIONS = ['sys', 'dll', 'exe']
if ext.lower() in IGNORED_EXTENSIONS:
    continue
```

## 📦 Cấu trúc project

```
SortFileGO/
├── file_sorter.py      # File chính
├── requirements.txt    # Dependencies
├── README.md          # Tài liệu này
└── icon.ico           # Icon (tùy chọn, cho PyInstaller)
```

## 🐛 Xử lý lỗi thường gặp

### 1. "No module named 'tkinter'"
**Nguyên nhân**: Python không có Tkinter

**Giải pháp**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Windows: Cài lại Python và tick "tcl/tk and IDLE"
```

### 2. File .exe quá nặng (>30MB)
**Nguyên nhân**: PyInstaller đóng gói toàn bộ Python runtime

**Giải pháp**:
```bash
# Dùng UPX để nén (giảm ~50% dung lượng)
pyinstaller --onefile --noconsole --upx-dir=C:\upx file_sorter.py
```

### 3. Không di chuyển được file
**Nguyên nhân**: 
- File đang mở bởi chương trình khác
- Không đủ quyền truy cập

**Giải pháp**: 
- Đóng tất cả file đang mở
- Chạy với quyền admin (xem phần "Quyền Admin")

## 📝 Changelog

### v1.0 (2025-01-02)
- ✅ Tạo giao diện đầu tiên với Tkinter
- ✅ Chức năng di chuyển file theo extension
- ✅ Progress bar và log realtime
- ✅ Xử lý trùng tên file
- ✅ Hỗ trợ recursive và tạo log file

## 🤝 Đóng góp

Nếu bạn muốn đóng góp hoặc báo lỗi:
1. Fork repo này
2. Tạo branch mới: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Tạo Pull Request

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết

## 🙋 Hỗ trợ

Nếu gặp vấn đề, hãy tạo issue trên GitHub hoặc liên hệ trực tiếp.

---

**Made with ❤️ by thaiGO - DevGO2003 Company**

*Dự án này được tạo ra để thay thế batch script cũ và cung cấp trải nghiệm tốt hơn với giao diện đồ họa.*

## 🔗 Links

- **GitHub**: https://github.com/DevGO2003/SortFileGO
- **Company**: DevGO2003
