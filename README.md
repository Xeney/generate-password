# Password Generator

Это простой генератор паролей, который позволяет создавать случайные пароли и сохранять их в файл.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.x.
2. Клонируйте репозиторий:
```
git clone https://github.com/%D0%B2%D0%B0%D1%88_%D0%BB%D0%BE%D0%B3%D0%B8%D0%BD/%D0%B2%D0%B0%D1%88_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9.git
```

4. Перейдите в каталог проекта:

```
cd password-generator
```


## Использование
```
from password_generator import GenerateFoPassword

# Создаем генератор паролей
password_generator = GenerateFoPassword(file_name="passwords.csv", count_generate=10, password_length=8)
# Без указания файла для сохранения
password_generator = GenerateFoPassword(count_generate=10, password_length=8)
# Возвращает 1 сгенерированный пароль
password_generator = GenerateFoPassword()

# Генерируем пароли
password_generator.generate_passwords()

# Сохраняем пароли в файл
password_generator.save_passwords()
```
