import os
from qgis.core import (
    QgsRasterLayer,
    QgsProject,
    QgsRasterFileWriter,
    QgsRasterPipe,
    QgsRasterProjector,
    QgsCoordinateReferenceSystem,
)

def export_rendered_raster(input_dir, output_dir):
    """
    Export tất cả GeoTIFF files từ input_dir sang output_dir dạng rendered image
    """
    print("="*60)
    print("BẮT ĐẦU XỬ LÝ")
    print("="*60)
    
    # Kiểm tra thư mục input
    if not os.path. exists(input_dir):
        print(f"✗ LỖI:  Thư mục input không tồn tại: {input_dir}")
        return
    
    print(f"✓ Thư mục input: {input_dir}")
    
    # Tạo thư mục output nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✓ Đã tạo thư mục output: {output_dir}")
    else:
        print(f"✓ Thư mục output:  {output_dir}")
    
    # Lấy danh sách tất cả file . tif và .tiff
    all_files = os.listdir(input_dir)
    print(f"\nTổng số file trong thư mục: {len(all_files)}")
    
    geotiff_files = [f for f in all_files 
                     if f.lower().endswith(('.tif', '. tiff'))]
    
    print(f"Số file GeoTIFF tìm thấy: {len(geotiff_files)}")
    
    if len(geotiff_files) == 0:
        print("\n✗ Không tìm thấy file GeoTIFF nào!")
        print(f"Danh sách file trong thư mục: {all_files[: 10]}")
        return
    
    print(f"\nDanh sách file GeoTIFF:")
    for f in geotiff_files: 
        print(f"  - {f}")
    
    print("\n" + "="*60)
    
    success_count = 0
    error_count = 0
    
    for idx, filename in enumerate(geotiff_files, 1):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"rendered_{filename}")
        
        print(f"\n[{idx}/{len(geotiff_files)}] Đang xử lý: {filename}")
        print(f"  Input:   {input_path}")
        print(f"  Output: {output_path}")
        
        try:
            # Load raster layer
            raster_layer = QgsRasterLayer(input_path, filename)
            
            if not raster_layer.isValid():
                print(f"  ✗ Không thể load file!")
                error_count += 1
                continue
            
            print(f"  ✓ Layer loaded - Kích thước: {raster_layer.width()}x{raster_layer.height()}")
            
            # Thêm layer vào project
            QgsProject.instance().addMapLayer(raster_layer, False)
            
            # Lấy thông tin raster
            extent = raster_layer.extent()
            width = raster_layer.width()
            height = raster_layer.height()
            crs = raster_layer.crs()
            renderer = raster_layer.renderer()
            provider = raster_layer.dataProvider()
            
            print(f"  CRS: {crs. authid()}")
            print(f"  Renderer: {renderer.type() if renderer else 'None'}")
            
            # Tạo raster pipe
            pipe = QgsRasterPipe()
            
            # Set provider
            if not pipe.set(provider. clone()):
                print(f"  ✗ Không thể set provider!")
                QgsProject.instance().removeMapLayer(raster_layer)
                error_count += 1
                continue
            
            # Set renderer
            if renderer:
                pipe.set(renderer.clone())
            
            # Setup projector
            projector = QgsRasterProjector()
            projector.setCrs(crs, crs)
            pipe.insert(2, projector)
            
            # Tạo file writer
            file_writer = QgsRasterFileWriter(output_path)
            file_writer.setOutputFormat('GTiff')
            
            print(f"  Đang ghi file...")
            
            # Write rendered raster
            error = file_writer.writeRaster(
                pipe,
                width,
                height,
                extent,
                crs
            )
            
            if error == QgsRasterFileWriter.NoError:
                file_size = os.path.getsize(output_path) / (1024*1024)  # MB
                print(f"  ✓ ĐÃ EXPORT THÀNH CÔNG!  ({file_size:.2f} MB)")
                success_count += 1
            else:
                print(f"  ✗ LỖI KHI EXPORT: {error}")
                error_count += 1
            
            # Remove layer khỏi project
            QgsProject.instance().removeMapLayer(raster_layer)
            
        except Exception as e:
            print(f"  ✗ LỖI: {str(e)}")
            import traceback
            traceback.print_exc()
            error_count += 1
            continue
    
    print("\n" + "="*60)
    print("KẾT QUẢ")
    print("="*60)
    print(f"✓ Thành công:  {success_count}/{len(geotiff_files)}")
    print(f"✗ Lỗi:  {error_count}/{len(geotiff_files)}")
    print("="*60)

# ==================== CHẠY NGAY TẠI ĐÂY ====================
# THAY ĐỔI ĐƯỜNG DẪN BÊN DƯỚI: 

INPUT_DIR = r"C:/Users/soiqualang/Desktop/data/CD2.3.Radar"
OUTPUT_DIR = r"C:/Users/soiqualang/Desktop/data/CD2.3.Radar_output"

# Gọi hàm ngay lập tức (không dùng if __name__ == "__main__")
export_rendered_raster(INPUT_DIR, OUTPUT_DIR)