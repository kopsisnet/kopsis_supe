#!/usr/bin/env bash
set -o errexit  # Script'i herhangi bir hata durumunda durdur

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating static directory..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate

echo "Build completed successfully!"
