#!/bin/bash

# Renklendirme için kodlar
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Tarih formatı
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Git durumunu kontrol et
echo -e "${YELLOW}Değişiklikleri kontrol ediyorum...${NC}"
git status -s > /dev/null 2>&1

if [ -n "$(git status --porcelain)" ]; then
    # Değişen dosyaları listele
    echo -e "${GREEN}Değişen dosyalar:${NC}"
    git status -s

    # Değişiklikleri staged'e ekle
    git add .

    # Değişen dosya isimlerini al
    CHANGED_FILES=$(git diff --cached --name-only | tr '\n' ', ' | sed 's/,$//')

    # Commit mesajı oluştur
    COMMIT_MESSAGE="Update ${DATE}: ${CHANGED_FILES}"

    # Commit yap
    echo -e "${GREEN}Commit yapılıyor: ${COMMIT_MESSAGE}${NC}"
    git commit -m "$COMMIT_MESSAGE"

    # Push yap
    echo -e "${GREEN}GitHub'a gönderiliyor...${NC}"
    git push

    echo -e "${GREEN}İşlem tamamlandı!${NC}"
else
    echo -e "${YELLOW}Değişiklik bulunamadı.${NC}"
fi
