
#!/bin/sh

# Останавливаем скрипт при возникновении ошибки.
set -e

echo "Applying database migrations..."

# Применяем миграции Django к PostgreSQL.
python manage.py migrate --noinput

echo "Collecting static files..."

# Собираем статические файлы Django.
python manage.py collectstatic --noinput

echo "Starting Django application..."

# Запускаем команду, переданную контейнеру.
exec "$@"
