import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
from PIL import Image

# Đọc ảnh xám
img = Image.open("img/moon.jpg").convert('L')
img_np = np.array(img)

# Biến đổi Fourier 2D
f = np.fft.fft2(img_np)
fshift = np.fft.fftshift(f)

# Kích thước ảnh
M, N = img_np.shape
u = np.arange(M)
v = np.arange(N)
U, V = np.meshgrid(u - M//2, v - N//2, indexing='ij')

# Thiết lập tần số cắt D0 (bán kính)
D0 = 50
D = np.sqrt(U**2 + V**2)

# Tạo bộ lọc thông thấp lý tưởng (Ideal Low-Pass Filter)
H = np.zeros((M, N))
H[D <= D0] = 1

# Áp dụng mặt nạ trong miền tần số
G = fshift * H

# Biến đổi ngược về miền không gian
f_ishift = np.fft.ifftshift(G)
img_filtered = np.fft.ifft2(f_ishift)
img_filtered = np.abs(img_filtered)

# --- Hiển thị kết quả ---
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 1. Ảnh gốc
axes[0].imshow(img_np, cmap='gray')
axes[0].set_title('Ảnh gốc (miền không gian)')
axes[0].axis('off')

# 2. Mặt nạ thông thấp
axes[1].imshow(H, cmap='gray')
axes[1].set_title(f'Mặt nạ Ideal Low-Pass (D0={D0})')
axes[1].axis('off')

plt.tight_layout()
plt.show()