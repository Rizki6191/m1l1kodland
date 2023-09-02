kata_gaul = {
    "mager": "males gerak",
    "gercep": "gerak cepat",
    "gabut": "gak ada kerjaan"
}

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kecil semua!): ")

if word in kata_gaul.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print('artinya adalah', kata_gaul[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('kata tersebut tidak ditemukan!')
