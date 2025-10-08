import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1 Doc anh goc
img = Image.open("img/duahau.png").convert("L")
f = np.array(img)
P, Q = f.shape

# 2 Tao bo loc thong cao Gauss
sig = 40
b = 2 * sig * sig

h = np.zeros((P, Q))
for i in range(P):
    for j in range(Q):
        D = (i - P/2)**2 + (j - Q/2)**2
        h[i, j] = 1 - np.exp(-D / b)

# Dich tam bo loc ve giua
H = np.fft.fftshift(h)

# 3 Bien doi Fourier anh va ap bo loc
F = np.fft.fft2(f)
F_shift = np.fft.fftshift(F)
G = H * F_shift

# 4 Bien doi nguoc de lay anh sau loc
G_ishift = np.fft.ifftshift(G)
filtered_img = np.abs(np.fft.ifft2(G_ishift))

# 5 Hien thi ket qua
plt.figure(figsize=(10, 6))

# Bo loc trong mien khong gian
plt.subplot(1, 3, 1)
plt.imshow(h, cmap='gray')
plt.title("Bo loc thong cao mien khong gian")
plt.axis('off')

# Bo loc trong mien tan so
plt.subplot(1, 3, 2)
plt.imshow(H, cmap='gray')
plt.title("Bo loc thong cao mien tan so")
plt.axis('off')

# Anh sau khi loc
plt.subplot(1, 3, 3)
plt.imshow(filtered_img, cmap='gray')
plt.title("Anh sau loc")
plt.axis('off')

plt.tight_layout()
plt.show()
