import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Đọc ảnh grayscale
img = Image.open("img/moon.jpg").convert('L')
img_np = np.array(img)

# Biến đổi Fourier 2 chiều
f = np.fft.fft2(img_np)

# Dịch tâm phổ về giữa (cho dễ quan sát)
fshift = np.fft.fftshift(f)

# Tính phổ biên độ và pha
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # +1 tránh log(0)
phase_spectrum = np.angle(fshift)

# Hiển thị kết quả
plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(img_np, cmap='gray')
plt.title('Ảnh gốc')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Phổ biên độ (log scale)')
plt.axis('off')

# plt.subplot(1,3,3)
# plt.imshow(phase_spectrum, cmap='gray')
# plt.title('Phổ pha')
# plt.axis('off')

plt.tight_layout()
plt.show()
