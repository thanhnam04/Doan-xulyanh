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

# Tính phổ biên độ (log scale) và chuẩn hóa cho rõ
magnitude_filtered = 20 * np.log(np.abs(G) + 1)
magnitude_filtered = magnitude_filtered / np.max(magnitude_filtered)

# --- Hiển thị kết quả ---
fig, axes = plt.subplots(1, 3, figsize=(14, 6))

# 1. Ảnh gốc
axes[0].imshow(img_np, cmap='gray')
axes[0].set_title('Ảnh gốc (miền không gian)')
axes[0].axis('off')

# 2. Mặt nạ thông thấp
axes[1].imshow(H, cmap='gray')
axes[1].set_title(f'Mặt nạ Ideal Low-Pass (D0={D0})')
axes[1].axis('off')

# 3. Ảnh trong miền tần số sau khi áp mặt nạ (phóng to)
axes[2].imshow(magnitude_filtered, cmap='gray')
axes[2].set_title('Miền tần số sau khi áp mặt nạ')
axes[2].axis('off')

# --- Thêm mũi tên giữa ảnh 2 và ảnh 3 ---
arrow_x = 0.65  # vị trí tương đối
arrow_y = 0.5
arrow = FancyArrow(0.57, arrow_y, 0.05, 0, transform=fig.transFigure,
                   width=0.01, color='black', head_width=0.04, head_length=0.02)
fig.patches.append(arrow)

plt.tight_layout()
plt.show()
