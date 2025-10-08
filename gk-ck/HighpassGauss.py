import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# === 1️⃣ ĐỌC ẢNH GỐC ===
img = Image.open("img/duahau1.png").convert('L')  # ảnh xám
img_np = np.array(img)
M, N = img_np.shape

# === 2️⃣ TẠO BỘ LỌC THÔNG CAO GAUSS ===
u = np.arange(M)
v = np.arange(N)
U, V = np.meshgrid(u - M/2, v - N/2, indexing='ij')



D0 = 40  # tần số cắt (điều chỉnh để thấy rõ)
H = 1 - np.exp(-(U**2 + V**2) / (2 * (D0**2)))

# === 3️⃣ BIẾN ĐỔI FOURIER ẢNH ===
F = np.fft.fft2(img_np)
F_shift = np.fft.fftshift(F)

# === 4️⃣ ÁP BỘ LỌC TRONG MIỀN TẦN SỐ ===
G = H * F_shift

# === 5️⃣ BIẾN ĐỔI NGƯỢC VỀ MIỀN KHÔNG GIAN ===
G_ishift = np.fft.ifftshift(G)
filtered_img = np.abs(np.fft.ifft2(G_ishift))

# === 6️⃣ HIỂN THỊ ===
plt.figure(figsize=(12, 4))

# Ảnh gốc
plt.subplot(1, 4, 1)
plt.imshow(img_np, cmap='gray')
plt.title("Ảnh gốc")
plt.axis('off')


# Mũi tên
plt.subplot(1, 4, 2)
plt.text(0.5, 0.5, "→", fontsize=15, ha='center', va='center')
plt.axis('off')

# Ảnh sau khi lọc
plt.subplot(1, 4, 4)
plt.imshow(filtered_img, cmap='gray')
plt.title("Ảnh sau lọc thông cao Gauss")
plt.axis('off')

# Ảnh phổ Fourier
plt.subplot(1, 4, 3)
plt.imshow(np.log(1 + np.abs(F_shift)), cmap='gray')
plt.title("Miền tần số (Fourier)")
plt.axis('off')


plt.tight_layout()
plt.show()
