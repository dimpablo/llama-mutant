#!/bin/bash

# === Настройка Git LFS для репозитория llama-mutant ===

REPO_DIR="$HOME/GIT/llama-mutant"
GGUF_PATTERN="model/*.gguf"
LFS_TYPES=(".gguf" ".bin" ".pt" ".pth" ".ckpt" ".safetensors")

cd "$REPO_DIR" || { echo "❌ Не могу перейти в папку: $REPO_DIR"; exit 1; }

echo "📁 Работаем в репозитории: $REPO_DIR"

# 1. Проверка, установлен ли git-lfs
if ! command -v git-lfs &> /dev/null; then
    echo "⬇️ Устанавливаю Git LFS..."
    cd /tmp || exit 1
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    apt-get install git-lfs -y || { echo "❌ Ошибка установки git-lfs"; exit 1; }
    cd "$REPO_DIR"
else
    echo "✅ Git LFS уже установлен"
fi

# 2. Инициализация Git LFS
echo "🔧 Инициализирую Git LFS..."
git lfs install

# 3. Добавляем отслеживание типов файлов
echo "🎯 Настраиваю отслеживание больших файлов через LFS..."

for ext in "${LFS_TYPES[@]}"; do
    git lfs track "$ext"
done

# Также отслеживаем конкретный путь к модели (на всякий случай)
git lfs track "model/*.gguf"

# 4. Убедимся, что .gitattributes добавлен в индекс
echo "📝 Проверяю .gitattributes..."
if [ ! -f ".gitattributes" ]; then
    echo "⚠️ Файл .gitattributes не найден, создаем..."
    git lfs track > .gitattributes
else
    git lfs track >> .gitattributes 2>/dev/null || true
fi

# 5. Добавляем изменения
echo "✅ Добавляю .gitattributes и настройки LFS в коммит..."
git add .gitattributes

# 6. Удаляем из обычного Git'а большой файл (если он уже закоммичен)
echo "🧹 Удаляю .gguf из обычного Git (чтобы перенести в LFS)..."
git rm --cached model/*.gguf 2>/dev/null || echo "➡️ Нет кэшированных .gguf файлов для удаления"

# 7. Коммитим изменения
git add .
git commit -m "🔧 LFS: включено отслеживание .gguf и других бинарников" || echo "➡️ Нечего коммитить (возможно, изменения уже есть)"

# 8. Пушим всё
echo "🚀 Выполняю push..."
git push origin main

echo "✅ Настройка Git LFS завершена!"
echo "💡 Теперь большие файлы будут храниться в LFS. Следующие типы файлов теперь под LFS: ${LFS_TYPES[*]}"
