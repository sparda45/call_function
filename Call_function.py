def menu(): #funnction main menu untuk mengakses function lainnya 
    print ("\nProgram Menghitung volume & luas bangun ruang ")
    print ("-----------------")
    print ("1) menghitung luas segitiga")
    print ("2) menghitung Volume balok")
    print ("3) Exit\n")
    inp =  int(input("masukan Pilihan= ")) #untuk menginput pilihan diatas
    #membuat conditional statment agar bisa mengakses setiap fungsi yang dibuat
    if inp == 1:
        segitiga() #memanggil fungsi segitiga
    elif inp ==  2:
        balok() #memanggil fungsi balok
    elif inp == 3:
        print("TERIMA KASIH")
        exit()#bila input nomor 3 maka program akan berhenti
            
def segitiga():#function segitiga
    alas =  float(input("Alas segitiga= "))
    tinggi = float(input("Tinggi Segitiga= "))
    
    #menghitung luas
    luas = (alas * tinggi) / 2
    print("luas segitiga adalah %0.2f" %luas)
    
    print("kembali ke main menu? (y/n)") #ketika sudah mendapatkan hasil apakah ingin kembali ke main menu atau akhiri program
    pil = str(input("masukan pilihan= "))
    if pil == "y":
        menu()
    elif pil == "n":
        exit()
    else:
        print("Inputan salah")

def balok(): #fungsi menghitung volume balok
    p = int(input("Panjang Balok= "))
    l = int(input("Luas Balok= "))
    t = int(input("Tinggi Balok= "))
    v = p*l*t
    print("volume balok adalah = ",v)
    print("kembali ke main menu? (y/n)")
    pil = str(input("masukan pilihan= "))#ketika sudah mendapatkan hasil apakah ingin kembali ke main menu atau akhiri program
    if pil == "y":
        menu()
    elif pil == "n":
        exit()
    else:
        print("Inputan salah")

menu()