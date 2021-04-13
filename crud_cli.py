import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="09",
    database="sbk_family"
)


def insert_data(db):
    nama = input("Masukkan Nama Anggota :")
    no_hp = input("Masukkan No Hp :")
    iuran = input("Masukkan Iuran :")
    val = (nama, no_hp, iuran)
    cursor = db.cursor()
    sql = "INSERT INTO tb_anggota(nm_anggota, no_hp, iuran) VALUES(%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM tb_anggota"
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for data in result:
            print(data)


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    id_anggota = input("Pilih id anggota > ")
    nm_anggota = input("Nama Anggota: ")
    no_hp = input("No Hp: ")
    iuran = input("Iuran: ")
    sql = "UPDATE tb_anggota SET nm_anggota=%s, no_hp=%s, iuran=%s WHERE id_anggota=%s"
    val = (nm_anggota, no_hp, iuran, id_anggota)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diupdate".format(cursor.rowcount))


def delete_data(db):
    cursor = db.sursor()
    show_data(db)
    id_anggota = input("Pilih id anggota > ")
    sql = "DELETE FROM tb_anggota WHERE id_anggota=%s"
    val = (id_anggota)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata Kunci: ")
    sql = "SELECT * FROM tb_anggota WHERE nm_anggota LIKE %s OR no_hp LIKE %s OR iuran LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(
        keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak Ada Data")
    else:
        for data in results:
            print(data)


def show_menu(db):
    print("\n")
    print("##### SBK FAMILY #####")
    print("\n")
    print("1. Tambah Data Anggota")
    print("2. Tampilkan Data Anggota")
    print("3. Update Data Anggota")
    print("4. Hapus Data Anggota")
    print("5. Cari Data Anggota")
    print("0. Keluar")
    print("\n")
    print("=========================")
    menu = input("Pilih menu > ")

    # clear screen
    os.system("clear")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu Yang Anda Pilih Salah")


if __name__ == "__main__":
    while(True):
        show_menu(db)
