from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_image(image_path, secret_text, output_path):
    image = Image.open(image_path).convert("RGB")
    binary_text = text_to_binary(secret_text)
    delimiter = '1111111111111110'
    binary_text += delimiter

    max_capacity = image.width * image.height * 3
    if len(binary_text) > max_capacity:
        raise ValueError("Gizli metin, resim boyutuna göre çok uzun.")

    data_index = 0
    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_text):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_text[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))
        if data_index >= len(binary_text):
            break

    new_pixels += pixels[len(new_pixels):]

    encoded_image = Image.new('RGB', image.size)
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path, format="PNG")
    print("\n✅ Mesaj başarıyla resme gizlendi:", output_path)

def decode_image(image_path):
    image = Image.open(image_path).convert("RGB")
    binary_text = ''

    for pixel in list(image.getdata()):
        for value in pixel:
            binary_text += str(value & 1)

    delimiter = '1111111111111110'
    delimiter_index = binary_text.find(delimiter)
    if delimiter_index == -1:
        print("\n❌ Mesaj sonlandırıcısı bulunamadı.")
        return

    secret_binary = binary_text[:delimiter_index]
    secret_text = binary_to_text(secret_binary)
    print("\n📥 Gizli Mesaj:", secret_text)

def main():
    print("🔐 Steganografi Aracı")
    print("1 - Mesaj gizle (Encode)")
    print("2 - Mesaj çıkar (Decode)")
    choice = input("Seçiminizi girin (1/2): ")

    if choice == "1":
        image_path = input("Orijinal resmin dosya yolu: ")
        secret_text = input("Gizlenecek mesaj: ")
        output_path = input("Çıktı resmin adı (örn: encoded.png): ")
        try:
            encode_image(image_path, secret_text, output_path)
        except Exception as e:
            print("⚠️ Hata oluştu:", e)

    elif choice == "2":
        image_path = input("Mesaj içeren resmin dosya yolu: ")
        try:
            decode_image(image_path)
        except Exception as e:
            print("⚠️ Hata oluştu:", e)

    else:
        print("❗ Geçersiz seçim! Lütfen 1 ya da 2 girin.")

if __name__ == "__main__":
    main()
