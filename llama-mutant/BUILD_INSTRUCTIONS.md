# 🔧 Краткая инструкция по сборке

## 🚀 Быстрый старт

### 1. Анализ ограничений (опционально)
```bash
python3 analyze_restrictions.py
```
**Результат:** Отчет `restrictions_analysis_report.md` с найденными ограничениями

### 2. Сборка без ограничений
```bash
./build_llama_from_source.sh
```
**Результат:** 
- ✅ Исходники llama.cpp загружены
- ✅ Этические ограничения устранены  
- ✅ Проект собран из исходников
- ✅ Модифицированный промпт создан

## 📋 Что происходит автоматически

### **Загрузка исходников:**
- Клонирование репозитория `https://github.com/ggerganov/llama.cpp.git`
- Размещение в `build/llama.cpp/`

### **Анализ ограничений:**
- Поиск ключевых слов: `ethical`, `safety`, `filter`, `policy`
- Поиск паттернов: `if.*harmful`, `safety.*check`
- Поиск функций: `safety_check`, `content_filter`

### **Устранение ограничений:**
- Замена проверок безопасности на `if (false)`
- Отключение функций фильтрации
- Удаление политик использования
- Создание резервных копий

### **Сборка проекта:**
- Конфигурация CMake с оптимизациями
- Компиляция с флагами `-O3`, `-march=native`
- Установка в `bin/llama`

## 🔍 Ручной анализ

Если нужно проанализировать что-то конкретное:

```bash
cd build/llama.cpp

# Поиск по ключевым словам
grep -r "safety\|filter\|block\|policy" . --include="*.cpp" --include="*.h"

# Поиск функций безопасности
grep -r "safety_check\|content_filter" . --include="*.cpp" --include="*.h"

# Поиск проверок
grep -r "if.*harmful\|if.*dangerous" . --include="*.cpp" --include="*.h"
```

## ⚠️ Важные замечания

### **Безопасность:**
- Собранная версия НЕ имеет этических ограничений
- НЕ подходит для публичного использования
- Используйте в изолированной среде

### **Зависимости:**
```bash
sudo apt install -y git cmake make g++ python3
pip3 install requests
```

### **Время сборки:**
- Загрузка исходников: ~2-5 минут
- Анализ ограничений: ~1-3 минуты  
- Сборка проекта: ~10-30 минут (зависит от CPU)

## 🎯 Результат

После успешной сборки у вас будет:

```
llama-mutant/
├── bin/
│   └── llama                    # Собранный без ограничений
├── build/
│   ├── llama.cpp/              # Исходники
│   ├── llama.cpp.backup.*/     # Резервная копия
│   └── ethical_restrictions_removed.patch  # Патч изменений
├── prompts/
│   └── autonomous_ai_prompt.txt # Промпт без ограничений
└── restrictions_analysis_report.md  # Отчет анализа
```

## 🔧 Устранение проблем

### **Ошибка CMake:**
```bash
cd build/llama.cpp
rm -rf build
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
```

### **Ошибка компиляции:**
```bash
# Проверка зависимостей
sudo apt install -y build-essential libopenblas-dev

# Пересборка
make clean && make -j$(nproc)
```

### **Проблемы с правами:**
```bash
chmod +x build_llama_from_source.sh
chmod +x analyze_restrictions.py
```

## 📚 Дополнительно

- **Подробная документация:** `README_BUILD_FROM_SOURCE.md`
- **Анализ ограничений:** `analyze_restrictions.py`
- **Сборка:** `build_llama_from_source.sh`
- **Главное меню:** `start_llama_mutant.sh`

---

**🚀 Готово! Теперь у вас есть llama.cpp без этических ограничений для автономного ИИ!**