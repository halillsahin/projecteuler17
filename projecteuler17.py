def sayi_kelime_uzunlugu(n):
    birler = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    onlar = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 20:
        return len(birler[n])
    elif 20 <= n < 100:
        onlar_basamagi = n // 10
        birler_basamagi = n % 10
        return len(onlar[onlar_basamagi]) + len(birler[birler_basamagi])
    elif 100 <= n < 1000:
        yuzler_basamagi = n // 100
        geriye_kalan = n % 100
        if geriye_kalan == 0:
            return len(birler[yuzler_basamagi]) + len("hundred")
        else:
            return len(birler[yuzler_basamagi]) + len("hundredand") + sayi_kelime_uzunlugu(geriye_kalan)
    elif n == 1000:
        return len("onethousand")
    else:
        return 0

toplam_kelime_uzunlugu = sum(sayi_kelime_uzunlugu(i) for i in range(1, 1001))
print(toplam_kelime_uzunlugu)
