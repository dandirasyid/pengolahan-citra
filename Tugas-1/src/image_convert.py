import cv2
import matplotlib.pyplot as plt

def convert_image(image_path):
    # Membaca gambar
    img = cv2.imread(image_path)

    # Memeriksa apakah gambar berhasil dibaca dari path
    if img is None:
        raise ValueError(f"Gambar tidak ditemukan di path: {image_path}")

    # Konversi gambar menjadi grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Konversi gambar grayscale menjadi biner
    _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    # Tampilkan hasil konversi dengan matplotlib
    plt.figure(figsize=(10, 5))

    # Gambar Asli
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Mengonversi gambar dari format BGR, yang merupakan format warna default di OpenCV, ke format RGB
    plt.title('Gambar')
    plt.axis('off')

    # Gambar Grayscale
    plt.subplot(1, 3, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Gambar Grayscale')
    plt.axis('off')

    # Gambar Biner
    plt.subplot(1, 3, 3)
    plt.imshow(binary_img, cmap='gray')
    plt.title('Gambar Biner')
    plt.axis('off')

    # Tampilkan semua gambar
    plt.show()