## Реализация REST API для учебного проекта Yatube на Яндекс Практикуме.
## Стек: Django Rest Framework.

## Описание

Проект обращается к сервису Yatube посредством API и
позволяет отправлять запросы на публикации: записей, комментариев,
а также подписываться и отписываться от других авторов.

## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
   ```bash
   git clone git@github.com:Pa11ady/api_final_yatube.git
   ```
   ```bash
   cd api_final_yatube
   ```

2. Cоздать и активировать виртуальное окружение:
   ```bash
   python3 -m venv env
   ```
   ```bash
   source env/bin/activate
   ```
   ```bash
   python3 -m pip install --upgrade pip
   ```

3. Установить зависимости из файла requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполнить миграции:
   ```bash
   python3 manage.py migrate
   ```

5. Запустить проект:
   ```bash
   python3 manage.py runserver
   ```

Чтобы заполнить проект тестовыми данными  перейдите в директорию *postman_collection* и запустите bash-скрипт:
```bash
   bash set_up_data.sh
```

*Внимание, скрипт предварительно очищает существующую базу данных.*

## Автор

Павел Воробьёв
