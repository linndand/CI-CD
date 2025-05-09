# Sistem Login Sederhana

saved_username = "admin"
saved_password = "12345"

print("=== Sistem Login Sederhana By Linnda dan winda update berhasil===")
#username = input("Username: ")
#password = input("Password: ")

username = saved_username
password = saved_password

if username == saved_username and password == saved_password:
    print(f"\nLogin berhasil! Selamat datang, {username}.")
else:
    print("\nLogin gagal. Username atau password salah.")
