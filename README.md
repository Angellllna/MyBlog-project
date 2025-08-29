# MyBlog-project
# MyBlog — навчальний Django-блог

Простий блог на Django з моделями **Author**, **Post**, **Comment**, виводом списку постів, деталей поста, фільтрацією за автором і інлайновими коментарями в адмінці.

## Вимоги
- Python 3.10+
- pip, venv

## Запуск локально

```bash
# 1) Клон/перехід у каталог
git clone <YOUR_REPO_URL> myblog
cd myblog

# 2) Віртуальне оточення
python -m venv venv
# Win: venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3) Залежності
pip install django

# 4) Міграції
python manage.py migrate

# 5) (опц.) Створити адміністратора
python manage.py createsuperuser

# 6) Запуск
python manage.py runserver

Відкрий:

Головна: http://127.0.0.1:8000/

Адмінка: http://127.0.0.1:8000/admin/

URL-и

/ — список постів

/post/<id>/ — детальна сторінка поста

/author/<id>/ — усі пости конкретного автора

/admin/ — адмін-панель