# PyQGIS-Render-Multi-GeoTiff
PyQGIS Render Multi GeoTiff

Cách chạy trong QGIS:
---------------------

### Cách 1: Python Console trong QGIS

1.  Mở QGIS Desktop
2.  Vào Plugins → Python Console (hoặc Ctrl+Alt+P)
3.  Copy paste code vào console
4.  Thay đổi đường dẫn `INPUT_DIR` và `OUTPUT_DIR`
5.  Chạy script

### Cách 2: Script Editor

1.  Trong Python Console, click vào icon Show Editor
2.  Paste code vào editor
3.  Save file (ví dụ: `export_rendered. py`)
4.  Click Run Script

Lưu ý quan trọng:
-----------------

1.  Đường dẫn: Thay đổi `INPUT_DIR` và `OUTPUT_DIR` phù hợp với hệ thống của bạn
2.  Rendering style: Script sẽ giữ nguyên style mặc định của QGIS. Nếu muốn áp dụng style cụ thể, bạn cần load style file trước
3.  Nén file: Có thể thêm options `COMPRESS=LZW` hoặc `COMPRESS=DEFLATE` để giảm kích thước file

<img width="1444" height="839" alt="image" src="https://github.com/user-attachments/assets/2e91882a-e252-4122-aa38-37a734d9e1df" />
<img width="1858" height="1080" alt="image" src="https://github.com/user-attachments/assets/bacf4715-d524-4445-95b6-601dd06bd539" />

