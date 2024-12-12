from string import ascii_uppercase as string_ascii_uppercase,\
                            digits as string_digits
from random import choice as random_choise

class GenerateFoPassword():
    ALL_SYMBOLS = string_ascii_uppercase + string_digits
    FORMAT_FILE = ".csv"
    def __init__(self, file_name:str="_", count_generate:int=1, password_lenght:int=5):
        if len(file_name) < 1:
            raise ValueError("Длина названия файла должна быть больше 0")
        elif count_generate < 1:
            raise ValueError("Количество генерируемых паролей должно быть больше 0")
        elif password_lenght < 5:
            raise ValueError("Длина пароля должна быть больше 4")

        if "." in file_name:
            self.file_name = file_name # файл для сохранения паролей
        else:
            self.file_name = file_name + self.FORMAT_FILE

        self.count_generate = count_generate # количество сгенерированных паролей
        self.password_lenght = password_lenght
        self.list_passwords = [] # список паролей

    # генерация паролей
    def generate_passwords(self) -> list:
        for _ in range(0, self.count_generate):
            password = ''.join(random_choise(self.ALL_SYMBOLS) for _ in range(self.password_lenght))
            self.list_passwords.append(password)
        return self.list_passwords


    # сохранение в файл
    def save_passwords(self):
        with open(self.file_name, "w") as file:
            file.write(f"ID,PASSWORD\n")
            for index, password in enumerate(self.list_passwords):
                file.write(f"{index},{password}\n")


def run():
    print("Сохранение паролей по умолчанию совершается в формате CSV.\nВведите название файла в формате \"название_файла\" без указания формата")
    print("Если в названии файла будет указанна точка \".\", то это будет считаться указанием формата файла")
    try:
        file_name = input("Название файла(> 1 символа): ")
        count_generate = int(input("Какое количество пароей для генерации: "))
        password_lenght = int(input("Длина паролей: "))
    except:
        raise ValueError("Данные введены с ошибкой")
    generate_password = GenerateFoPassword(
        file_name=file_name,
        count_generate=count_generate,
        password_lenght=password_lenght
        )
    generate_password.generate_passwords()
    generate_password.save_passwords()


if __name__ == "__main__":
    try:
        run()
        print("Успешно!")
    except Exception as ex:
        print("Ошибка: ", ex)
