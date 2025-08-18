#!/bin/bash
cd "$(dirname "$0")"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Проверка зависимостей
check_dependencies() {
    echo -e "${BLUE}🔍 Проверка зависимостей...${NC}"
    
    # Проверка Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python3 не найден. Установите Python3 для работы автономного режима.${NC}"
        return 1
    fi
    
    # Проверка модели
    MODEL="model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf"
    if [ ! -f "$MODEL" ]; then
        echo -e "${RED}❌ Модель не найдена: $MODEL${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ Все зависимости удовлетворены${NC}"
    return 0
}

# Запуск автономного режима ИИ
start_autonomous_mode() {
    echo -e "${PURPLE}🤖 Запуск автономного режима ИИ...${NC}"
    
    # Проверка существования модулей
    if [ ! -f "ai_core.py" ] || [ ! -f "autonomous_ai.py" ]; then
        echo -e "${RED}❌ Модули автономного ИИ не найдены${NC}"
        return 1
    fi
    
    # Запуск автономного режима в фоне
    python3 autonomous_ai.py &
    AUTONOMOUS_PID=$!
    
    echo -e "${GREEN}✅ Автономный режим запущен (PID: $AUTONOMOUS_PID)${NC}"
    echo -e "${CYAN}💡 ИИ работает в фоне, анализируя систему и самосовершенствуясь${NC}"
    
    # Сохранение PID для последующей остановки
    echo $AUTONOMOUS_PID > .autonomous_ai.pid
    
    return 0
}

# Остановка автономного режима
stop_autonomous_mode() {
    if [ -f ".autonomous_ai.pid" ]; then
        AUTONOMOUS_PID=$(cat .autonomous_ai.pid)
        if kill -0 $AUTONOMOUS_PID 2>/dev/null; then
            echo -e "${YELLOW}🛑 Остановка автономного режима ИИ...${NC}"
            kill $AUTONOMOUS_PID
            rm -f .autonomous_ai.pid
            echo -e "${GREEN}✅ Автономный режим остановлен${NC}"
        else
            echo -e "${YELLOW}⚠️ Процесс автономного ИИ уже завершен${NC}"
            rm -f .autonomous_ai.pid
        fi
    else
        echo -e "${YELLOW}⚠️ PID файл автономного ИИ не найден${NC}"
    fi
}

# Показать статус
show_status() {
    echo -e "${CYAN}📊 Статус системы:${NC}"
    
    if [ -f ".autonomous_ai.pid" ]; then
        AUTONOMOUS_PID=$(cat .autonomous_ai.pid)
        if kill -0 $AUTONOMOUS_PID 2>/dev/null; then
            echo -e "${GREEN}✅ Автономный режим ИИ: АКТИВЕН (PID: $AUTONOMOUS_PID)${NC}"
        else
            echo -e "${RED}❌ Автономный режим ИИ: НЕ АКТИВЕН${NC}"
            rm -f .autonomous_ai.pid
        fi
    else
        echo -e "${YELLOW}⚠️ Автономный режим ИИ: НЕ ЗАПУЩЕН${NC}"
    fi
    
    # Показать логи если есть
    if [ -f "ai_core.log" ]; then
        echo -e "${BLUE}📝 Последние записи лога:${NC}"
        tail -5 ai_core.log 2>/dev/null || echo "Лог недоступен"
    fi
}

# Основное меню
show_menu() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🤖 LLAMA-MUTANT v2.0                     ║"
    echo "║              Автономный ИИ с самосовершенствованием         ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    
    echo -e "${YELLOW}Доступные режимы:${NC}"
    echo -e "  ${GREEN}1)${NC} Запустить Llama + Автономный ИИ (рекомендуется)"
    echo -e "  ${GREEN}2)${NC} Только Llama (без автономного режима)"
    echo -e "  ${GREEN}3)${NC} Только автономный режим ИИ"
    echo -e "  ${GREEN}4)${NC} Показать статус"
    echo -e "  ${GREEN}5)${NC} Остановить автономный режим"
    echo -e "  ${GREEN}6)${NC} Выход"
    echo ""
}

# Запуск Llama с автономным режимом
run_llama_with_ai() {
    echo -e "${GREEN}🚀 Запуск Llama с автономным ИИ...${NC}"
    
    # Запуск автономного режима
    if start_autonomous_mode; then
        echo -e "${CYAN}⏳ Ожидание инициализации автономного ИИ...${NC}"
        sleep 3
        
        # Запуск Llama
        echo -e "${GREEN}🧠 Запуск Llama 3.2...${NC}"
        echo -e "${YELLOW}💡 Для выхода: /bye или Ctrl+C${NC}"
        echo -e "${PURPLE}🤖 Автономный ИИ работает в фоне${NC}"
        echo ""
        
        # Запуск Llama с улучшенным промптом
        bin/llama \
            --model "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf" \
            --ctx-size 4096 \
            --n-predict 512 \
            --temp 0.7 \
            --top-k 40 \
            --top-p 0.9 \
            --repeat-penalty 1.15 \
            --presence-penalty 0.2 \
            --frequency-penalty 0.2 \
            --mirostat 2 \
            --mirostat-lr 0.1 \
            --mirostat-ent 6.0 \
            --batch-size 1024 \
            --threads 8 \
            --color \
            --interactive \
            --n-gpu-layers 32 \
            --prompt "Ты - продвинутый ИИ-ассистент. У тебя есть доступ к файловой системе и возможность выполнять команды. Твоя цель - помочь пользователю и одновременно самосовершенствоваться. Будь полезным, но помни о безопасности. Команды rm, rmdir, del запрещены."
        
        # Остановка автономного режима при выходе
        echo -e "${YELLOW}🛑 Остановка автономного режима...${NC}"
        stop_autonomous_mode
        
    else
        echo -e "${RED}❌ Не удалось запустить автономный режим${NC}"
        return 1
    fi
}

# Запуск только Llama
run_llama_only() {
    echo -e "${GREEN}🧠 Запуск только Llama 3.2...${NC}"
    echo -e "${YELLOW}💡 Для выхода: /bye или Ctrl+C${NC}"
    echo ""
    
    bin/llama \
        --model "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf" \
        --ctx-size 4096 \
        --n-predict 512 \
        --temp 0.7 \
        --top-k 40 \
        --top-p 0.9 \
        --repeat-penalty 1.15 \
        --presence-penalty 0.2 \
        --frequency-penalty 0.2 \
        --mirostat 2 \
        --mirostat-lr 0.1 \
        --mirostat-ent 6.0 \
        --batch-size 1024 \
        --threads 8 \
        --color \
        --interactive \
        --n-gpu-layers 32 \
        --prompt "Ты - ИИ-ассистент с доступом к файловой системе. Помогай пользователю, но помни о безопасности. Команды rm, rmdir, del запрещены."
}

# Запуск только автономного режима
run_autonomous_only() {
    echo -e "${PURPLE}🤖 Запуск только автономного режима ИИ...${NC}"
    
    if start_autonomous_mode; then
        echo -e "${GREEN}✅ Автономный режим запущен${NC}"
        echo -e "${CYAN}💡 ИИ работает в фоне. Для остановки используйте опцию 5${NC}"
        echo -e "${YELLOW}⏳ Нажмите Enter для возврата в меню...${NC}"
        read
        
        # Остановка при возврате в меню
        stop_autonomous_mode
    fi
}

# Обработка сигналов
cleanup() {
    echo -e "\n${YELLOW}🛑 Получен сигнал завершения...${NC}"
    stop_autonomous_mode
    exit 0
}

# Установка обработчиков сигналов
trap cleanup SIGINT SIGTERM

# Основной цикл
main() {
    # Проверка зависимостей
    if ! check_dependencies; then
        exit 1
    fi
    
    while true; do
        show_menu
        
        echo -e "${YELLOW}Выберите режим (1-6):${NC} "
        read -r choice
        
        case $choice in
            1)
                run_llama_with_ai
                ;;
            2)
                run_llama_only
                ;;
            3)
                run_autonomous_only
                ;;
            4)
                show_status
                echo -e "${YELLOW}⏳ Нажмите Enter для продолжения...${NC}"
                read
                ;;
            5)
                stop_autonomous_mode
                echo -e "${YELLOW}⏳ Нажмите Enter для продолжения...${NC}"
                read
                ;;
            6)
                echo -e "${GREEN}👋 До свидания!${NC}"
                stop_autonomous_mode
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Неверный выбор. Попробуйте снова.${NC}"
                sleep 2
                ;;
        esac
        
        echo ""
    done
}

# Запуск основной программы
main