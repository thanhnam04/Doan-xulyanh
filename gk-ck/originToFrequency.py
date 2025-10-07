import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Đọc ảnh xám
img = Image.open("img/moon.jpg").convert('L')
img_np = np.array(img)

# Biến đổi Fourier 2D
f = np.fft.fft2(img_np)
fshift = np.fft.fftshift(f)  # Dịch tần số thấp ra giữa

# Tính phổ biên độ (magnitude spectrum)
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

# Hiển thị kết quả
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_np, cmap='gray')
plt.title('Ảnh miền không gian')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Ảnh chuyển sang miền tần số')
plt.axis('off')

plt.tight_layout()
plt.show()
