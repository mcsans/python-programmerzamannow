# Belajar Set

# list => []
# tuple => () : tidak bisa mengubah data
# set => {} : tidak menerima data duplikat, pemanggilan tidak bisa menggunakan index (name[0])

nama = {"Eko", "Joko", "Eko", "Joko", "Andi"}

nama.add("Kurniawan")
nama.add("Kurniawan")
nama.add("Kurniawan")

for data in nama:
    print(data)

nama.remove("Eko")
nama.remove("Andi")

print(nama)