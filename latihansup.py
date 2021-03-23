from bs4 import BeautifulSoup

dokumen = '''
<html>
<head>
    <title>Tutorial BeautifulSoup</title>
</head>

<body>
    <p class="judul">Judul Dokumen</p>

    <p class="paragraf">Ini adalah contoh paragraf</p>

    <a href="https://ngodingdata.com" class="url">Ngodingdata</a>
</body>

</html>
'''

html_soup = BeautifulSoup(dokumen, 'html.parser')

print(html_soup)

#mengambil konten dari html tanpa kode html tinggal tambahkan text
# judul = html_soup.find('p', class_='judul').text

#mengambil konten html dengan tag yang sama
all_par = html_soup.find_all('p')
print(all_par)