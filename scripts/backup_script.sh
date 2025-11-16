#!/bin/bash

# Папка с вашим сайтом
SITE_DIR="/var/www/rk-01.ru"

# Папка для бэкапов
BACKUP_DIR="/var/www/backups"

# Дата для имени файла
DATE=$(date +%Y-%m-%d)

# Имя файла бэкапа
BACKUP_FILE="rk-01-website_$DATE.tar.gz"

# Полный путь к файлу
FULL_PATH="$BACKUP_DIR/$BACKUP_FILE"

echo "=== БЭКАП САЙТА rk-01.ru ==="
echo "Время: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Источник: $SITE_DIR"
echo "Бэкап: $BACKUP_FILE"

# Проверяем существует ли папка с сайтом
if [ ! -d "$SITE_DIR" ]; then
    echo "❌ ОШИБКА: Папка $SITE_DIR не существует!"
    exit 1
fi

# Создаем папку для бэкапов если нет
mkdir -p "$BACKUP_DIR"

# Создаем бэкап
echo "📦 Создаем бэкап..."
tar -czf "$FULL_PATH" -C "$SITE_DIR" .

# Проверяем успешность
if [ $? -eq 0 ]; then
    echo "✅ Бэкап успешно создан!"
    
    # Показываем информацию о файле
    FILE_SIZE=$(du -h "$FULL_PATH" | cut -f1)
    echo "📊 Размер бэкапа: $FILE_SIZE"
    
    # Количество файлов в бэкапе
    FILE_COUNT=$(tar -tzf "$FULL_PATH" | wc -l)
    echo "📁 Файлов в бэкапе: $FILE_COUNT"
    
    # Пример файлов
    echo "🔍 Пример файлов:"
    tar -tzf "$FULL_PATH" | head -5
    
else
    echo "❌ Ошибка при создании бэкапа!"
    exit 1
fi

echo "=== БЭКАП ЗАВЕРШЕН ==="
