#!/bin/bash
set -o errexit

# Python sürümünü kontrol et
echo "Python version:"
python --version

# Pip'i yükselt
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Gerekli paketleri yükle
echo "Installing dependencies..."
pip install -r requirements.txt

# Statik dosyalar için dizin oluştur
echo "Creating static directory..."
mkdir -p staticfiles

# Statik dosyaları topla
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Veritabanı migration'larını çalıştır
echo "Running database migrations..."
python manage.py migrate --noinput

echo "Build completed successfully!"
