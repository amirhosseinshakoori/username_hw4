from getpass import getpass
import hashlib
import uuid

class User:
    """
    A class representing a user in the system.
    """

    users = {}

    def __init__(self, username: str, password: str, phone_number: str = None) -> None:
        """
        Initializes a new user with the given username, password, and optional phone number.

        Parameters:
        - username (str): The username for the user.
        - password (str): The password for the user.
        - phone_number (str, optional): The phone number for the user. Defaults to None.

        Raises:
        - ValueError: If the username is already taken.
        """
        if username in User.users:
            raise ValueError("نام کاربری تکراری است.")
        self.username = username
        self.password = self.encrypt_password(password)
        self.phone_number = phone_number
        self.id = self.generate_id()
        User.users[username] = self

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
        - str: A string representation of the user.
        """
        return f"نام کاربری: {self.username}\nشماره تلفن: {self.phone_number}\nشناسه کاربر: {self.id}"

    def encrypt_password(self, password: str) -> str:
        """
        Encrypts the given password using SHA-256 algorithm.

        Parameters:
        - password (str): The password to encrypt.

        Returns:
        - str: The encrypted password as a hexadecimal string.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_id(self) -> str:
        """
        Generates a unique identifier for the user.

        Returns:
        - str: A unique identifier for the user.
        """
        return str(uuid.uuid4())

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        Validates the given password to make sure it is at least 4 characters long.

        Parameters:
        - password (str): The password to validate.

        Returns:
        - bool: True if the password is valid, False otherwise.
        """
        return len(password) >= 4

    def change_password(self) -> None:
        """
        Changes the user's password after verifying the old password and validating the new password.
        """
        old_password = getpass("گذرواژه فعلی را وارد کنید: ")
        if self.password != self.encrypt_password(old_password):
            print("گذرواژه صحیح نیست.")
            return
        new_password = getpass("گذرواژه جدید را وارد کنید: ")
        if not self.validate_password(new_password):
            print("گذرواژه نامعتبر است.")
            return
        new_password_confirm = getpass("گذرواژه جدید را مجدداً وارد کنید: ")
        if new_password != new_password_confirm:
            print("گذرواژه‌ها با هم مطابقت ندارند.")
            return
        self.password = self.encrypt_password(new_password)
        print("گذرواژه با موفقیت تغییر یافت.")

    @classmethod
    def register(cls) -> None:
        """
        Registers a new user by taking the username, password, and phone number as input from the user.
        """
        while True:
            try:
                username = input("نام کاربری را وارد کنید: ")
                password = getpass("گذرواژه را وارد کنید: ")
                phone_number = input("شماره تلفن را وارد کنید: ")
                user = cls(username, password, phone_number)
                print("ثبت نام با موفقیت انجام شد.")
                break
            except ValueError as e:
                print(str(e))
                continue
    
    @classmethod
    def login(cls) -> None:
        """
        Logs in an existing user by taking the username and password as input from the user.
        """
        while True:
            username = input("نام کاربری را وارد کنید: ")
            password = getpass("گذرواژه را وارد کنید: ")
            user = cls.users.get(username)
            if not user:
                print("کاربری با این نام کاربری وجود ندارد.")
                continue
            if user.password != user.encrypt_password(password):
                print("گذرواژه نادرست است.")
                continue
            print("ورود موفقیت‌آمیز.")
            while True:
                print("لطفاً یکی از گزینه‌های زیر را انتخاب کنید:")
                print("1. نمایش اطلاعات کاربری")
                print("2. ویرایش اطلاعات کاربری")
                print("3. تغییر گذرواژه")
                print("4. خروج")
                choice = input()
                if choice == "1":
                    print(user)
                elif choice == "2":
                    new_username = input("نام کاربری جدید را وارد کنید: ")
                    if new_username != username and new_username in cls.users:
                        print("نام کاربری تکراری است.")
                        continue
                    new_phone_number = input("شماره تلفن جدید را وارد کنید: ")
                    user.username = new_username
                    user.phone_number = new_phone_number
                    cls.users[new_username] = user
                    del cls.users[username]
                    username = new_username
                    print("اطلاعات با موفقیت به‌روزرسانی شدند.")
                elif choice == "3":
                    user.change_password()
                elif choice == "4":
                    print("خروج از حساب کاربری.")
                    break
                else:
                    print("گزینه نامعتبر است.")

