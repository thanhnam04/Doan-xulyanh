# gaussian_highpass_duahau.py
# Loc thong cao Gauss cho anh duahau.png va hien thi pho tan so

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# === a Doc anh goc (grayscale) ===
img = Image.open("img/duahau.png").convert("L")   # anh xam
f = np.array(img, dtype=np.float64)
P, Q = f.shape

# === b Tao bo loc thong cao Gauss ===
sigma = 40.0                # do rong sigma
b = 2 * sigma * sigma

# tao luoi toa do
u = np.arange(P)
v = np.arange(Q)
U, V = np.meshgrid(u, v, indexing='ij')

# khoang cach D(u,v) den tam
D2 = (U - P/2)**2 + (V - Q/2)**2

# ham loc thong cao Gauss
H = 1 - np.exp(-D2 / b)

# === c Bien doi Fourier anh goc ===
F = np.fft.fft2(f)
F_shift = np.fft.fftshift(F)

# === d Nhan pho anh voi bo loc ===
G_shift = F_shift * H

# === e Bien doi nguoc Fourier ===
G = np.fft.ifftshift(G_shift)
g = np.fft.ifft2(G)
g_real = np.real(g)

# === f Chuan hoa ve 0–255 ===
g_min, g_max = g_real.min(), g_real.max()
g_norm = (g_real - g_min) / (g_max - g_min) * 255
g_uint8 = np.clip(g_norm, 0, 255).astype(np.uint8)

# === g Pho tan so ===
# dung log(1 + |F|) de nhin ro hon
mag_F = np.log(1 + np.abs(F_shift))
mag_G = np.log(1 + np.abs(G_shift))

# === h Hien thi ket qua ===
plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.title("Anh goc")
plt.imshow(f, cmap='gray')
plt.axis('off')

plt.subplot(2,3,2)
plt.title("Bo loc thong cao Gauss (H)")
plt.imshow(H, cmap='gray')
plt.axis('off')

plt.subplot(2,3,3)
plt.title("Anh sau khi loc")
plt.imshow(g_uint8, cmap='gray')
plt.axis('off')

plt.subplot(2,3,4)
plt.title("Pho tan so anh goc")
plt.imshow(mag_F, cmap='gray')
plt.axis('off')

plt.subplot(2,3,5)
plt.axis('off')

plt.subplot(2,3,6)
plt.title("Pho tan so sau khi loc")
plt.imshow(mag_G, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
