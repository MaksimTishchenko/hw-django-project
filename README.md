# 🏠 HW: Django Homework Project

Это домашнее задание по созданию Django-проекта с кастомными моделями, админкой, миграциями и генерацией данных через фабрики.

---

## ✅ Основные функции

- Модель `Category`: категории продуктов
- Модель `Product`: товары с привязкой к категории
- Продвинутая настройка админки
- Кастомная команда генерации данных (`generate_data`)
- Управление зависимостями через **Poetry**

---

## 🧰 Технологии

- Python 3.13
- Django 5.x
- Poetry (управление пакетами и виртуальным окружением)
- SQLite (по умолчанию)

---

## 🚀 Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/ ваш_репозиторий/hw-django-project.git
cd hw-django-project
```
### 2. Установите Poetry
Если у вас ещё не установлен Poetry, выполните:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org  -OutFile poetry-installer.py)
python poetry-installer.py
```
### 3. Добавьте Poetry в PATH, если нужно:

```powershell
[Environment]::SetEnvironmentVariable("Path", "$env:Path;$env:APPDATA\Python\Python313\Scripts", "Machine")
```
### 4. Установите зависимости
```powershell
poetry install
```
### 5. Активируйте виртуальное окружение
```powershell
poetry env activate
$ACTIVATE_CMD = poetry env activate | Out-String
Invoke-Expression $ACTIVATE_CMD
```
### 6. Выполните миграции
```powershell
python manage.py migrate
```
### 7. Создайте суперпользователя
```powershell
python manage.py createsuperuser
```
### 8. Запустите сервер
```powershell
python manage.py runserver
```
Откройте браузер: http://127.0.0.1:8000/admin

## 🧬 Генерация тестовых данных
Вы можете автоматически создать тестовые данные:
```powershell
python manage.py generate_data --categories 5 --products 20
```
## 📁 Структура проекта
- hw-django-project/
- ├── myproject/            
- │   ├── settings.py
- │   ├── urls.py
- │   └── ...
- ├── store_app/            
- │   ├── models.py
- │   ├── admin.py
- │   └── management/       
- │       └── commands/
- │           └── generate_data.py
- ├── manage.py
- ├── pyproject.toml        
- ├── poetry.lock           
- ├── .gitignore            
- └── README.md             