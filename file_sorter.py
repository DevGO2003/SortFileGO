#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Sorter - Ứng dụng sắp xếp file theo extension
Tự động tạo thư mục theo đuôi file và di chuyển file vào đúng thư mục
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
from pathlib import Path
import threading
from datetime import datetime
import ctypes
import sys


class FileSorterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📁 File Sorter - Sắp xếp file theo đuôi")
        self.root.geometry("750x650")
        self.root.resizable(True, True)
        
        # Set minimum size để không bị nhỏ quá
        self.root.minsize(600, 500)
        
        # Biến
        self.source_folder = tk.StringVar()
        self.is_sorting = False
        self.total_files = 0
        self.processed_files = 0
        
        # Cấu hình style
        self.setup_styles()
        
        # Tạo giao diện
        self.create_widgets()
        
    def setup_styles(self):
        """Cấu hình style cho các widget"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Style cho buttons
        style.configure('Action.TButton', 
                       font=('Segoe UI', 10, 'bold'),
                       padding=10)
        
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        
        # ===== FRAME HEADER =====
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=65)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="📁 FILE SORTER",
            font=('Segoe UI', 16, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=5)
        
        subtitle = tk.Label(
            header_frame,
            text="Sắp xếp file tự động theo phần mở rộng",
            font=('Segoe UI', 9),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle.pack()
        
        # ===== FRAME CHỌN THƯ MỤC =====
        folder_frame = ttk.LabelFrame(self.root, text="  📂 Chọn thư mục cần sắp xếp  ", padding=10)
        folder_frame.pack(fill='x', padx=15, pady=8)
        
        # Entry hiển thị đường dẫn
        entry_frame = tk.Frame(folder_frame)
        entry_frame.pack(fill='x')
        
        self.folder_entry = ttk.Entry(
            entry_frame,
            textvariable=self.source_folder,
            font=('Segoe UI', 10),
            state='readonly'
        )
        self.folder_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        # Nút chọn thư mục
        browse_btn = ttk.Button(
            entry_frame,
            text="🔍 Chọn thư mục",
            command=self.browse_folder,
            style='Action.TButton'
        )
        browse_btn.pack(side='left')
        
        # ===== FRAME OPTIONS =====
        options_frame = ttk.LabelFrame(self.root, text="  ⚙️ Tùy chọn  ", padding=10)
        options_frame.pack(fill='x', padx=15, pady=8)
        
        # Checkbox recursive
        self.recursive_var = tk.BooleanVar(value=True)
        recursive_check = ttk.Checkbutton(
            options_frame,
            text="Bao gồm thư mục con (recursive)",
            variable=self.recursive_var
        )
        recursive_check.pack(anchor='w')
        
        # Checkbox create log
        self.create_log_var = tk.BooleanVar(value=True)
        log_check = ttk.Checkbutton(
            options_frame,
            text="Tạo file log (sort_log.txt)",
            variable=self.create_log_var
        )
        log_check.pack(anchor='w')
        
        # ===== FRAME TIẾN TRÌNH =====
        progress_frame = ttk.LabelFrame(self.root, text="  📊 Tiến trình  ", padding=10)
        progress_frame.pack(fill='x', padx=15, pady=8)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode='determinate',
            length=300
        )
        self.progress_bar.pack(fill='x', pady=(0, 10))
        
        # Label status
        self.status_label = tk.Label(
            progress_frame,
            text="Sẵn sàng...",
            font=('Segoe UI', 9),
            fg='#7f8c8d'
        )
        self.status_label.pack()
        
        # ===== FRAME LOG =====
        log_frame = ttk.LabelFrame(self.root, text="  📝 Chi tiết  ", padding=8)
        log_frame.pack(fill='both', expand=True, padx=15, pady=8)
        
        # Text widget với scrollbar
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            font=('Consolas', 8),
            wrap='word',
            height=8,
            bg='#f8f9fa',
            fg='#2c3e50'
        )
        self.log_text.pack(fill='both', expand=True)
        
        # ===== FRAME BUTTONS =====
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack(fill='x', padx=15, pady=(0, 10))
        
        # Nút bắt đầu
        self.start_btn = ttk.Button(
            button_frame,
            text="▶️ Bắt đầu sắp xếp",
            command=self.start_sorting,
            style='Action.TButton'
        )
        self.start_btn.pack(side='left', padx=5)
        
        # Nút clear log
        clear_btn = ttk.Button(
            button_frame,
            text="🗑️ Xóa log",
            command=self.clear_log
        )
        clear_btn.pack(side='left', padx=5)
        
        # Nút thoát
        exit_btn = ttk.Button(
            button_frame,
            text="❌ Thoát",
            command=self.root.quit
        )
        exit_btn.pack(side='right', padx=5)
        
        # ===== FOOTER - CREDIT =====
        footer_frame = tk.Frame(self.root, bg='#34495e', height=30)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        credit_label = tk.Label(
            footer_frame,
            text="Made with ❤️ by thaiGO - DevGO2003 Company",
            font=('Segoe UI', 8),
            bg='#34495e',
            fg='#ecf0f1'
        )
        credit_label.pack(pady=7)
        
    def browse_folder(self):
        """Mở dialog chọn thư mục"""
        folder = filedialog.askdirectory(
            title="Chọn thư mục cần sắp xếp file"
        )
        if folder:
            self.source_folder.set(folder)
            self.log_message(f"✅ Đã chọn thư mục: {folder}")
            
    def log_message(self, message, color='black'):
        """Thêm message vào log text"""
        self.log_text.insert('end', f"{message}\n")
        self.log_text.see('end')
        self.root.update_idletasks()
        
    def clear_log(self):
        """Xóa nội dung log"""
        self.log_text.delete('1.0', 'end')
        
    def update_progress(self, current, total):
        """Cập nhật progress bar"""
        if total > 0:
            percentage = (current / total) * 100
            self.progress_bar['value'] = percentage
            self.status_label.config(
                text=f"Đã xử lý: {current}/{total} file ({percentage:.1f}%)"
            )
        self.root.update_idletasks()
        
    def start_sorting(self):
        """Bắt đầu quá trình sắp xếp file"""
        if self.is_sorting:
            messagebox.showwarning("Cảnh báo", "Đang trong quá trình sắp xếp!")
            return
            
        source = self.source_folder.get()
        if not source:
            messagebox.showerror("Lỗi", "Vui lòng chọn thư mục nguồn!")
            return
            
        if not os.path.exists(source):
            messagebox.showerror("Lỗi", "Thư mục không tồn tại!")
            return
        
        # Confirm
        result = messagebox.askyesno(
            "Xác nhận",
            f"Bạn có chắc muốn sắp xếp tất cả file trong:\n{source}\n\n"
            "File sẽ được di chuyển vào các thư mục theo đuôi (.jpg, .pdf, ...)"
        )
        
        if not result:
            return
            
        # Chạy trong thread riêng để không block UI
        self.is_sorting = True
        self.start_btn.config(state='disabled')
        thread = threading.Thread(target=self.sort_files, args=(source,))
        thread.daemon = True
        thread.start()
        
    def sort_files(self, source_folder):
        """Logic sắp xếp file"""
        try:
            self.log_message("="*60)
            self.log_message(f"🚀 BẮT ĐẦU SẮP XẾP FILE")
            self.log_message(f"📂 Thư mục: {source_folder}")
            self.log_message(f"⏰ Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.log_message("="*60)
            
            # Đếm tổng số file
            all_files = []
            recursive = self.recursive_var.get()
            
            if recursive:
                for root, dirs, files in os.walk(source_folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        all_files.append(file_path)
            else:
                for item in os.listdir(source_folder):
                    item_path = os.path.join(source_folder, item)
                    if os.path.isfile(item_path):
                        all_files.append(item_path)
            
            self.total_files = len(all_files)
            self.processed_files = 0
            
            self.log_message(f"\n📊 Tìm thấy {self.total_files} file\n")
            
            # Log file
            log_file_path = None
            if self.create_log_var.get():
                log_file_path = os.path.join(source_folder, "sort_log.txt")
                with open(log_file_path, 'w', encoding='utf-8') as f:
                    f.write(f"FILE SORTER LOG - {datetime.now()}\n")
                    f.write("="*60 + "\n\n")
            
            # Di chuyển từng file
            moved_count = 0
            error_count = 0
            
            for file_path in all_files:
                try:
                    # Lấy extension
                    ext = Path(file_path).suffix[1:]  # Bỏ dấu chấm
                    if not ext:
                        ext = "_no_ext"
                    
                    # Tạo thư mục đích
                    target_folder = os.path.join(source_folder, f".{ext}")
                    os.makedirs(target_folder, exist_ok=True)
                    
                    # Đường dẫn đích
                    file_name = os.path.basename(file_path)
                    target_path = os.path.join(target_folder, file_name)
                    
                    # Xử lý trùng tên
                    if os.path.exists(target_path):
                        base_name = Path(file_name).stem
                        ext_name = Path(file_name).suffix
                        counter = 1
                        while os.path.exists(target_path):
                            new_name = f"{base_name} ({counter}){ext_name}"
                            target_path = os.path.join(target_folder, new_name)
                            counter += 1
                    
                    # Di chuyển file
                    shutil.move(file_path, target_path)
                    moved_count += 1
                    
                    # Log
                    log_msg = f"✅ {file_name} → .{ext}/"
                    self.log_message(log_msg)
                    
                    if log_file_path:
                        with open(log_file_path, 'a', encoding='utf-8') as f:
                            f.write(f"{log_msg}\n")
                    
                except Exception as e:
                    error_count += 1
                    error_msg = f"❌ Lỗi: {file_path} - {str(e)}"
                    self.log_message(error_msg)
                    
                    if log_file_path:
                        with open(log_file_path, 'a', encoding='utf-8') as f:
                            f.write(f"{error_msg}\n")
                
                # Cập nhật progress
                self.processed_files += 1
                self.update_progress(self.processed_files, self.total_files)
            
            # Kết thúc
            self.log_message("\n" + "="*60)
            self.log_message("✅ HOÀN THÀNH!")
            self.log_message(f"📊 Tổng số file: {self.total_files}")
            self.log_message(f"✅ Đã di chuyển: {moved_count}")
            self.log_message(f"❌ Lỗi: {error_count}")
            
            if log_file_path:
                self.log_message(f"📝 File log: {log_file_path}")
            
            self.log_message("="*60)
            
            messagebox.showinfo(
                "Hoàn thành!",
                f"✅ Đã sắp xếp {moved_count}/{self.total_files} file thành công!\n"
                f"❌ Lỗi: {error_count} file"
            )
            
        except Exception as e:
            error_msg = f"❌ LỖI NGHIÊM TRỌNG: {str(e)}"
            self.log_message(error_msg)
            messagebox.showerror("Lỗi", error_msg)
            
        finally:
            self.is_sorting = False
            self.start_btn.config(state='normal')
            self.progress_bar['value'] = 0


def is_admin():
    """Kiểm tra quyền admin trên Windows"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """Chạy lại với quyền admin"""
    if sys.platform != 'win32':
        return
        
    if is_admin():
        return
        
    # Chạy lại với quyền admin
    ctypes.windll.shell32.ShellExecuteW(
        None, 
        "runas", 
        sys.executable, 
        " ".join(sys.argv), 
        None, 
        1
    )
    sys.exit()


def main():
    """Hàm chính"""
    # Uncomment dòng dưới nếu muốn bắt buộc chạy với quyền admin
    # run_as_admin()
    
    root = tk.Tk()
    app = FileSorterGUI(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
