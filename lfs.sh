# Перейти в корень репозитория
cd /root/GIT/llama-mutant

# Установить Git LFS (если ещё не установлен)
apt update && apt install git-lfs -y

# Инициализировать LFS
git lfs install

# Отслеживать нужные типы файлов
git lfs track "*.gguf"
git lfs track "*.bin"
git lfs track "*.safetensors"

# Убедиться, что .gitattributes добавлен
git add .gitattributes

# Удалить из индекса старый .gguf (если был добавлен без LFS)
git rm --cached llama-mutant/model/*.gguf 2>/dev/null || true

# Добавить сам .gguf-файл через LFS
git add llama-mutant/model/*.gguf

# Проверить, что добавилось
if git diff --cached --name-only | grep -q ".gguf"; then
    echo "✅ Файл .gguf успешно добавлен"
else
    echo "❌ Ошибка: .gguf файл не добавлен. Проверь путь."
    exit 1
fi

# Установить remote с токеном
TOKEN=$(cat /root/GIT/token)
git remote set-url origin https://$TOKEN@github.com/dimpablo/llama-mutant.git

# Сделать коммит
git config --local user.name "root"
git config --local user.email "root@kali"
git commit -m "-lfs: enable for model/*.gguf"

# Выполнить push
git push origin main

# Вернуть обратный URL (опционально, безопасность)
git remote set-url origin https://github.com/dimpablo/llama-mutant.git

echo "✅ Push выполнен! LFS настроен, модель отправлена."
