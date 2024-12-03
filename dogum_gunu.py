# Python ile HTML dosyası oluşturma
html_content = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doğum Günü Kutlaması</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
        }
        h1 {
            color: #ff6347;
        }
        .message {
            font-size: 24px;
            color: #333;
        }
        .birthday-image {
            width: 300px;
            height: 300px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<h1>Mutlu Yıllar!</h1>
<p class="message">Yeni yaşın hayırlı olsun biraderim. Yeni yaşın sana güzellikler getirsin. Seviliyosun.</p>

<!-- Fotoğraf ekleme -->
<img src="dogum_gunu_fotografi.jpg" alt="Doğum Günü Fotoğrafı" class="birthday-image">

</body>
</html>
"""

# HTML dosyasını kaydetme
with open("dogum_gunu.html", "w") as file:
    file.write(html_content)

print("HTML dosyası başarıyla oluşturuldu!")
