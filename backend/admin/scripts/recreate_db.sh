rm -rf data/db.sqlite3
rm -rf housing/migrations/*
touch housing/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
python manage.py shell < admin/scripts/create_addresses.py
python manage.py shell < admin/scripts/create_groups.py
