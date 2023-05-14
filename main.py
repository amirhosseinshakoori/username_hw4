from user import User

def main() -> None:
    """
    The main function that runs the user management program.
    """
    while True:
        print("لطفاً یکی از گزینه‌های زیر را انتخاب کنید:")
        print("0. خروج")
        print("1. ثبت نام")
        print("2. ورود به حساب کاربری")
        choice = input()
        if choice == "0":
            print("خروج از برنامه.")
            break
        elif choice == "1":
            User.register()
        elif choice == "2":
            User.login()
        else:
            print("گزینه نامعتبر است.")

if __name__ == '__main__':
    main()