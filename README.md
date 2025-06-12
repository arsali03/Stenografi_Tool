# 🕵️ Stenografi Aracı - LSB Tabanlı Mesaj Gizleme

Bu Python projesi, bir görselin içerisine gizli bir mesaj yerleştirmenizi (encode) ve daha sonra bu mesajı çözmenizi (decode) sağlar. Kullanılan teknik, resim piksellerinin RGB değerlerinin en düşük anlamlı biti (LSB) kullanılarak veri gömülmesidir.

## ✨ Özellikler

- Resme metin mesajı gizleme
- Gizli mesajı çözme
- LSB (Least Significant Bit) yöntemi
- PNG gibi kayıpsız görsellerle çalışma

## 🧪 Gereksinimler

- Python 3.x
- Pillow (PIL)

Kurulum:

```bash
pip install pillow

🚀 Kullanım
Encode (Mesaj Gizleme)
bash
Copy
Edit
python stenografi.py
# Seçenek 1: Mesaj gizle
# Orijinal resmin dosya yolu: örnekler/orijinal.png
# Gizlenecek mesaj: Merhaba, bu gizli bir mesajdır!
# Çıktı resmin adı: örnekler/encoded.png
Decode (Mesaj Çıkarma)
bash
Copy
Edit
python stenografi.py
# Seçenek 2: Mesaj çıkar
# Mesaj içeren resmin dosya yolu: örnekler/encoded.png
🧠 Teknik Detaylar
Her karakter ASCII karşılığı ile 8-bit’e çevrilir.

Sonuna 1111111111111110 bit dizisi (delimiter) eklenir.

RGB değerlerinin son biti bu verilerle değiştirilir.

Decode işlemi sırasında bu bitler birleştirilip tekrar metne çevrilir.

📸 Ekran Görüntüleri
Gizlenmeden önce:![input](https://github.com/user-attachments/assets/82140bf9-ae3b-4b28-a7e2-eb1c43f134a5)


Mesaj gizlendikten sonra:![encoded](https://github.com/user-attachments/assets/a0f07e4d-ed0a-489a-b4af-2d912a1840c3)
