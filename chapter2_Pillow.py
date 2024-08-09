from PIL import Image

# Memuat gambar
image =Image.open('Teknologi.jpg')

# Menyimpan gambar
image.save('result.jpg')

# Memotong gambar
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

# Mengubah ukuran gambar
resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

from PIL import ImageFilter

# Menerapkan filter pada gambar
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')