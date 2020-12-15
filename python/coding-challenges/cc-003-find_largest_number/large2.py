def max(a):
    
    res = a[0]  # İşlevin son satırı, işlevden çıkan ve res değişkeninin değerini çeviriyor.
    for i in a:
        if res < i:
            res = i
    return res

array = (15, 23, 78, 24, 15)

print(max(array))