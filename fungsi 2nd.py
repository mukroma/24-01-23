#variable global
nama="python"
versi="1.0.0"

def help():
    #variable lokal
    nama="c#"
    versi="1.0.2"
    #akses variable lokal
    print ("nama:%s"%nama)
    print("versi:%s"%versi)

#akses variable global
print("nama:%s"%nama)
print("versi:%s"%versi)

#memanggil fungsi help()
help()