# 📁 File Sorter - Ứng dụng sắp xếp file tự động

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📖 Giới thiệu

**File Sorter** là ứng dụng Windows giúp bạn **tự động sắp xếp và tổ chức các file** trong thư mục một cách nhanh chóng và hiệu quả. Thay vì phải thủ công di chuyển từng file vào các thư mục riêng, ứng dụng sẽ tự động phân loại tất cả các file theo phần mở rộng (.jpg, .pdf, .mp3, .docx, v.v.) chỉ với một cú click chuột.

### 🎯 Công dụng

- ✅ **Dọn dẹp thư mục Downloads** - Tự động sắp xếp hàng trăm file tải về theo loại
- 📂 **Quản lý thư mục dự án** - Phân loại file code, hình ảnh, tài liệu một cách ngăn nắp
- 🔄 **Sắp xếp hàng loạt** - Xử lý cả thư mục con với chức năng recursive
- 💾 **Sao lưu có tổ chức** - Tự động phân loại file backup theo định dạng
- 🚀 **Tiết kiệm thời gian** - Thay thế việc di chuyển file thủ công hàng giờ đồng hồ

### ✨ Tính năng nổi bật

- 🖥️ **Giao diện đồ họa thân thiện** - Dễ sử dụng, không cần dòng lệnh
- 📊 **Hiển thị tiến trình realtime** - Theo dõi quá trình xử lý với progress bar
- 📝 **Tạo file log chi tiết** - Ghi lại tất cả thao tác để dễ dàng kiểm tra
- 🔀 **Xử lý trùng tên thông minh** - Tự động đánh số file (1), (2), (3)...
- ⚡ **Xử lý đa luồng** - Giao diện không bị lag khi xử lý nhiều file
- 🎛️ **Tùy chỉnh linh hoạt** - Chọn quét thư mục con, tạo log, v.v.

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

---

## 🛠️ Công nghệ sử dụng

Ứng dụng được xây dựng với các công nghệ và thư viện sau:

### Ngôn ngữ lập trình
- **Python 3.7+** - Ngôn ngữ lập trình chính, dễ học và mạnh mẽ

### Thư viện & Framework
- **Tkinter** - Thư viện GUI có sẵn trong Python để tạo giao diện đồ họa
- **os / shutil** - Thư viện chuẩn Python để xử lý file và thư mục
- **threading** - Thư viện đa luồng để xử lý không làm đơ giao diện
- **pathlib** - Thư viện xử lý đường dẫn file hiện đại

### Công cụ đóng gói
- **PyInstaller** - Công cụ chuyển đổi script Python thành file .exe độc lập

### Ưu điểm của stack công nghệ này
- ✅ **Không cần cài đặt phức tạp** - Python và các thư viện đều miễn phí
- ✅ **Cross-platform** - Có thể chạy trên Windows, Linux, macOS
- ✅ **Nhẹ và nhanh** - Không cần framework nặng như Electron
- ✅ **Dễ bảo trì** - Code Python dễ đọc và dễ sửa đổi

---

## 🚀 Cách sử dụng nhanh (File EXE)

### ⚡ Dùng file .exe có sẵn (Khuyến nghị)

**Bước 1:** Tải file `FileSorter.exe` từ thư mục `dist/` hoặc từ [Releases](https://github.com/DevGO2003/SortFileGO/releases)

**Bước 2:** Double-click vào file `FileSorter.exe` để mở ứng dụng

**Bước 3:** Sử dụng giao diện:
1. Click nút **"🔍 Chọn thư mục"** → Chọn thư mục cần sắp xếp
2. Tùy chọn:
   - ✅ **Recursive**: Bật để quét cả thư mục con
   - ✅ **Create Log**: Bật để tạo file log chi tiết
3. Click nút **"▶️ Bắt đầu sắp xếp"**
4. Đợi progress bar hoàn tất
5. Xem kết quả trong thư mục đã chọn

**Lưu ý quan trọng:**
- ⚠️ File .exe **không cần cài đặt Python** hay bất kỳ thư viện nào
- ⚠️ Có thể chạy trực tiếp trên bất kỳ máy Windows nào (Windows 7+)
- ⚠️ Nếu Windows Defender cảnh báo, chọn "Run anyway" (file an toàn 100%)

### 📦 Tự tạo file .exe (Cho developer)

Nếu bạn muốn tự build file .exe từ source code:

```bash
# 1. Cài PyInstaller
pip install pyinstaller

# 2. Tạo file .exe
pyinstaller --onefile --noconsole --name "FileSorter" file_sorter.py

# 3. File .exe sẽ nằm trong thư mục dist/
# dist/FileSorter.exe
```

---

## 📞 Hỗ trợ & Liên hệ

Nếu gặp vấn đề hoặc cần hỗ trợ:
- 📧 **Email**: DevGO2003@gmail.com
- 🐛 **Báo lỗi**: Tạo [Issue](https://github.com/DevGO2003/SortFileGO/issues) trên GitHub
- 💬 **Góp ý**: Tạo [Discussion](https://github.com/DevGO2003/SortFileGO/discussions)

## 📄 License

MIT License - Xem file LICENSE để biết thêm chi tiết

---

**Made with ❤️ by thaiGO - DevGO2003 Company**

*Dự án được tạo ra để giúp người dùng sắp xếp và quản lý file một cách dễ dàng, thay thế các công cụ thủ công truyền thống.*

## 🔗 Thông tin thêm

- **GitHub**: https://github.com/DevGO2003/SortFileGO
- **Company**: DevGO2003
- **Version**: 1.0.0

---

# 📁 File Sorter - Automatic File Sorting Application

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📖 Introduction

**File Sorter** is a Windows application that helps you **automatically organize and sort files** in folders quickly and efficiently. Instead of manually moving files to separate folders, the application automatically categorizes all files by their extension (.jpg, .pdf, .mp3, .docx, etc.) with just one click.

### 🎯 Use Cases

- ✅ **Clean up Downloads folder** - Automatically sort hundreds of downloaded files by type
- 📂 **Manage project folders** - Organize code files, images, and documents neatly
- 🔄 **Batch sorting** - Handle subfolders with recursive functionality
- 💾 **Organized backups** - Automatically categorize backup files by format
- 🚀 **Save time** - Replace hours of manual file moving with one click

### ✨ Key Features

- 🖥️ **User-friendly GUI** - Easy to use, no command line needed
- 📊 **Real-time progress display** - Track processing with progress bar
- 📝 **Detailed logging** - Record all operations for easy verification
- 🔀 **Smart duplicate handling** - Automatically rename files (1), (2), (3)...
- ⚡ **Multi-threaded processing** - UI stays responsive while processing
- 🎛️ **Flexible customization** - Choose recursive scan, logging, etc.

## 🎯 How It Works

```
D:\Downloads\
├── photo1.jpg
├── photo2.jpg
├── document.pdf
├── song.mp3
└── video.mp4

    ↓ After sorting ↓

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

- Files **without extension** → Go to `._no_ext\` folder
- **Duplicate names** → Automatically renamed to `file (1).jpg`, `file (2).jpg`

---

## 🛠️ Technologies Used

The application is built with the following technologies and libraries:

### Programming Language
- **Python 3.7+** - Main programming language, easy to learn and powerful

### Libraries & Framework
- **Tkinter** - Built-in Python GUI library for creating graphical interface
- **os / shutil** - Standard Python libraries for file and folder operations
- **threading** - Multi-threading library for non-blocking processing
- **pathlib** - Modern file path handling library

### Packaging Tool
- **PyInstaller** - Tool to convert Python scripts into standalone .exe files

### Advantages of This Tech Stack
- ✅ **No complex setup** - Python and libraries are free
- ✅ **Cross-platform** - Can run on Windows, Linux, macOS
- ✅ **Lightweight and fast** - No need for heavy frameworks like Electron
- ✅ **Easy to maintain** - Python code is readable and easy to modify

---

## 🚀 Quick Start (EXE File)

### ⚡ Using Pre-built .exe (Recommended)

**Step 1:** Download `FileSorter.exe` from the `dist/` folder or from [Releases](https://github.com/DevGO2003/SortFileGO/releases)

**Step 2:** Double-click `FileSorter.exe` to open the application

**Step 3:** Use the interface:
1. Click **"🔍 Select Folder"** → Choose the folder to sort
2. Options:
   - ✅ **Recursive**: Enable to scan subfolders
   - ✅ **Create Log**: Enable to create detailed log file
3. Click **"▶️ Start Sorting"**
4. Wait for progress bar to complete
5. Check results in the selected folder

**Important Notes:**
- ⚠️ .exe file **doesn't require Python** or any libraries
- ⚠️ Can run directly on any Windows machine (Windows 7+)
- ⚠️ If Windows Defender warns, click "Run anyway" (file is 100% safe)

### 📦 Build Your Own .exe (For Developers)

If you want to build .exe from source code:

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Create .exe file
pyinstaller --onefile --noconsole --name "FileSorter" file_sorter.py

# 3. .exe will be in dist/ folder
# dist/FileSorter.exe
```

---

## 📞 Support & Contact

If you encounter issues or need support:
- 📧 **Email**: DevGO2003@gmail.com
- 🐛 **Report Bug**: Create an [Issue](https://github.com/DevGO2003/SortFileGO/issues) on GitHub
- 💬 **Suggestions**: Create a [Discussion](https://github.com/DevGO2003/SortFileGO/discussions)

## 📄 License

MIT License - See LICENSE file for details

---

**Made with ❤️ by thaiGO - DevGO2003 Company**

*This project was created to help users organize and manage files easily, replacing traditional manual tools.*

## 🔗 More Information

- **GitHub**: https://github.com/DevGO2003/SortFileGO
- **Company**: DevGO2003
- **Version**: 1.0.0
