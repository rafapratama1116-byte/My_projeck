meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" :"untuk menjadi agresif/marah",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")  

if word in meme_dict.keys():
     print("kata yang anda masukkan adalah", word)
     print(word,"artinya", meme_dict[word])
else:
    print("maaf kata tidak ada dalam data")
