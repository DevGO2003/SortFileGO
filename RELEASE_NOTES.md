# 📁 File Sorter v1.0.0

## 🎉 Release đầu tiên - File Sorter GUI Application

Ứng dụng Windows có giao diện đồ họa để sắp xếp file tự động theo phần mở rộng.

---

## ✨ Tính năng chính

- ✅ **Giao diện đồ họa đẹp mắt** - Tkinter GUI hiện đại
- 📂 **Chọn thư mục tùy ý** - Không bị giới hạn ổ đĩa
- 🔄 **Hỗ trợ recursive** - Quét toàn bộ thư mục con
- 📊 **Progress bar realtime** - Theo dõi tiến trình
- 📝 **Tạo file log** - Ghi lại tất cả thao tác
- 🔀 **Xử lý trùng tên** - Auto rename file (1), (2)...
- 🚀 **Multi-threading** - Không làm đơ giao diện
- 💻 **Tối ưu cho 720p** - Giao diện vừa màn hình

---

## 📥 Tải về

### Windows (64-bit)
**📦 FileSorter.exe** (~12 MB)
- Không cần cài đặt Python
- Chạy trực tiếp bằng double-click
- Hỗ trợ Windows 10/11

### Source Code
```bash
git clone https://github.com/DevGO2003/SortFileGO.git
cd SortFileGO
python file_sorter.py
```

---

## 🚀 Cách sử dụng

1. **Tải file `FileSorter.exe`** từ phần Assets bên dưới
2. **Double-click** để chạy
3. **Chọn thư mục** cần sắp xếp
4. **Click "Bắt đầu sắp xếp"**
5. **Xem kết quả** trong log window

---

## 📋 Yêu cầu hệ thống

- **OS**: Windows 10/11 (64-bit)
- **RAM**: 2GB trở lên
- **Disk**: 50MB trống

Nếu chạy từ source code:
- **Python**: 3.7+ với Tkinter

---

## 🎯 Ví dụ

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
└── .mp3\
    └── music.mp3
```

---

## 🐛 Known Issues

Không có issue nào được báo cáo trong phiên bản này.

---

## 🔜 Roadmap

- [ ] Thêm tính năng undo
- [ ] Hỗ trợ custom rules (ví dụ: .jpg → "Images")
- [ ] Dark mode
- [ ] Multi-language support
- [ ] Drag & drop folder

---

## 👨‍💻 Credits

**Developed by**: thaiGO  
**Company**: DevGO2003  
**License**: MIT

---

## 📞 Hỗ trợ

- **GitHub Issues**: https://github.com/DevGO2003/SortFileGO/issues
- **Tài liệu**: Xem file README.md

---

**Made with ❤️ by thaiGO - DevGO2003 Company**
