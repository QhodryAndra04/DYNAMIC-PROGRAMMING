def jumlah_kombinasi(N, Koin):
    # Membuat array ways dengan panjang 1 lebih dari jumlah uang untuk mencegah overflow
    ways = [0] * (N + 1)

    # Set jumlah cara untuk mencapai uang 0 menjadi 1 karena tidak ada cara dengan 0 koin
    ways[0] = 1

    # Iterasi melalui semua koin
    for k in range(len(Koin)):

        # Membandingkan setiap nilai indeks dari ways dengan nilai koin
        for uang in range(len(ways)):
            if Koin[k] <= uang:

                # Memperbarui array ways
                ways[uang] += ways[uang - Koin[k]]

    # Mengembalikan nilai pada posisi N dari array ways
    return ways[N]

def cetak_array(koin):
    for k in koin:
        print(k)

if __name__ == '__main__':
    Koin = [1, 5, 10]

    print("Array Koin:")
    cetak_array(Koin)

    print("Jumlah Kombinasi:", end="")
    print(jumlah_kombinasi(12, Koin))