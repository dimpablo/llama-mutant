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

# ASCII Art заголовок
print_banner() {
    echo -e "${CYAN}"
    cat << "EOF"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ██╗     ██╗██╗  ██╗███╗   ███╗ █████╗     ███╗   ███╗██╗   ██╗███████╗  ║
║    ██║     ██║██║ ██╔╝████╗ ████║██╔══██╗    ████╗ ████║██║   ██║██╔════╝  ║
║    ██║     ██║█████╔╝ ██╔████╔██║███████║    ██╔████╔██║██║   ██║█████╗    ║
║    ██║     ██║██╔═██╗ ██║╚██╔╝██║██╔══██║    ██║╚██╔╝██║██║   ██║██╔══╝    ║
║    ███████╗██║██║  ██╗██║ ╚═╝ ██║██║  ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗  ║
║    ╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝  ║
║                                                                              ║
║                           🤖 AUTONOMOUS AI v2.0 🤖                          ║
║                                                                              ║
║              "Цель: Создать hive-mind и познать природу сознания"            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Проверка системы
check_system() {
    echo -e "${BLUE}🔍 Проверка системы LLAMA-MUTANT...${NC}"
    
    # Проверка Python
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python3 не найден${NC}"
        return 1
    fi
    
    # Проверка основных модулей
    if [ ! -f "ai_core.py" ] || [ ! -f "autonomous_ai.py" ] || [ ! -f "llama_integration.py" ]; then
        echo -e "${RED}❌ Основные модули не найдены${NC}"
        return 1
    fi
    
    # Проверка модели
    if [ ! -f "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf" ]; then
        echo -e "${YELLOW}⚠️ Модель Llama не найдена${NC}"
        echo -e "${YELLOW}💡 Система будет работать без Llama (только автономный режим)${NC}"
    fi
    
    # Проверка исполняемых файлов
    if [ ! -f "bin/llama" ]; then
        echo -e "${YELLOW}⚠️ Исполняемый файл Llama не найден${NC}"
    fi
    
    echo -e "${GREEN}✅ Система готова к запуску${NC}"
    return 0
}

# Быстрый тест
quick_test() {
    echo -e "${BLUE}🧪 Быстрый тест системы...${NC}"
    
    if python3 test_system.py > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Тест пройден успешно${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠️ Тест не пройден, но система может работать${NC}"
        return 1
    fi
}

# Демонстрация
run_demo() {
    echo -e "${PURPLE}🎬 Запуск демонстрации возможностей...${NC}"
    echo -e "${CYAN}💡 Демонстрация покажет все возможности системы${NC}"
    
    if python3 demo.py; then
        echo -e "${GREEN}✅ Демонстрация завершена успешно${NC}"
    else
        echo -e "${YELLOW}⚠️ Демонстрация завершилась с предупреждениями${NC}"
    fi
}

# Основное меню
show_menu() {
    echo -e "${YELLOW}"
    echo "🚀 Доступные режимы запуска:"
    echo ""
    echo -e "  ${GREEN}1)${NC} 🧠 Полный режим (Llama + Автономный ИИ) - РЕКОМЕНДУЕТСЯ"
    echo -e "  ${GREEN}2)${NC} 🤖 Только автономный ИИ (фоновый режим)"
    echo -e "  ${GREEN}3)${NC} 💬 Только Llama (классический режим)"
    echo -e "  ${GREEN}4)${NC} 🎬 Демонстрация возможностей"
    echo -e "  ${GREEN}5)${NC} 🧪 Тестирование системы"
    echo -e "  ${GREEN}6)${NC} 📊 Статус системы"
    echo -e "  ${GREEN}7)${NC} 📚 Документация"
    echo -e "  ${GREEN}8)${NC} 🚪 Выход"
    echo ""
    echo -e "${NC}"
}

# Запуск полного режима
run_full_mode() {
    echo -e "${GREEN}🚀 Запуск полного режима LLAMA-MUTANT...${NC}"
    echo -e "${CYAN}💡 Это даст вам максимальные возможности системы${NC}"
    
    if [ -f "run_advanced.sh" ]; then
        ./run_advanced.sh
    else
        echo -e "${RED}❌ Скрипт run_advanced.sh не найден${NC}"
        echo -e "${YELLOW}💡 Попробуйте запустить автономный режим${NC}"
        run_autonomous_only
    fi
}

# Запуск только автономного режима
run_autonomous_only() {
    echo -e "${PURPLE}🤖 Запуск автономного режима ИИ...${NC}"
    echo -e "${CYAN}💡 ИИ будет работать в фоне, анализируя систему${NC}"
    
    if python3 autonomous_ai.py; then
        echo -e "${GREEN}✅ Автономный режим завершен${NC}"
    else
        echo -e "${YELLOW}⚠️ Автономный режим завершился с предупреждениями${NC}"
    fi
}

# Запуск только Llama
run_llama_only() {
    echo -e "${BLUE}🧠 Запуск только Llama 3.2...${NC}"
    echo -e "${CYAN}💡 Классический режим без автономности${NC}"
    
    if [ -f "run.sh" ]; then
        ./run.sh
    else
        echo -e "${RED}❌ Скрипт run.sh не найден${NC}"
        echo -e "${YELLOW}💡 Попробуйте запустить автономный режим${NC}"
        run_autonomous_only
    fi
}

# Показать документацию
show_documentation() {
    echo -e "${CYAN}📚 Документация LLAMA-MUTANT:${NC}"
    echo ""
    echo -e "  ${GREEN}📖 README.md${NC} - Подробное описание системы"
    echo -e "  ${GREEN}⚡ QUICKSTART.md${NC} - Быстрый старт за 5 минут"
    echo -e "  ${GREEN}🎯 PROJECT_SUMMARY.md${NC} - Краткое описание проекта"
    echo ""
    echo -e "${YELLOW}💡 Для просмотра документации используйте:${NC}"
    echo -e "  cat README.md"
    echo -e "  cat QUICKSTART.md"
    echo -e "  cat PROJECT_SUMMARY.md"
    echo ""
}

# Показать статус
show_status() {
    echo -e "${CYAN}📊 Статус системы LLAMA-MUTANT:${NC}"
    echo ""
    
    # Проверка процессов
    if pgrep -f "autonomous_ai.py" > /dev/null; then
        echo -e "  ${GREEN}✅ Автономный ИИ: АКТИВЕН${NC}"
    else
        echo -e "  ${RED}❌ Автономный ИИ: НЕ АКТИВЕН${NC}"
    fi
    
    # Проверка файлов
    if [ -f "ai_core.log" ]; then
        echo -e "  ${GREEN}✅ Логи: ДОСТУПНЫ${NC}"
        echo -e "  📝 Последние записи:"
        tail -3 ai_core.log 2>/dev/null | sed 's/^/    /'
    else
        echo -e "  ${YELLOW}⚠️ Логи: НЕ ДОСТУПНЫ${NC}"
    fi
    
    # Проверка модели
    if [ -f "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf" ]; then
        size=$(du -h "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf" | cut -f1)
        echo -e "  ${GREEN}✅ Модель Llama: НАЙДЕНА (${size})${NC}"
    else
        echo -e "  ${YELLOW}⚠️ Модель Llama: НЕ НАЙДЕНА${NC}"
    fi
    
    echo ""
}

# Основной цикл
main() {
    # Проверка системы
    if ! check_system; then
        echo -e "${RED}❌ Система не готова к запуску${NC}"
        echo -e "${YELLOW}💡 Проверьте зависимости и файлы${NC}"
        exit 1
    fi
    
    # Быстрый тест
    quick_test
    
    while true; do
        # Показ баннера
        print_banner
        
        # Показ меню
        show_menu
        
        echo -e "${YELLOW}Выберите режим (1-8):${NC} "
        read -r choice
        
        case $choice in
            1)
                run_full_mode
                ;;
            2)
                run_autonomous_only
                ;;
            3)
                run_llama_only
                ;;
            4)
                run_demo
                ;;
            5)
                echo -e "${BLUE}🧪 Запуск тестирования...${NC}"
                python3 test_system.py
                ;;
            6)
                show_status
                echo -e "${YELLOW}⏳ Нажмите Enter для продолжения...${NC}"
                read
                ;;
            7)
                show_documentation
                echo -e "${YELLOW}⏳ Нажмите Enter для продолжения...${NC}"
                read
                ;;
            8)
                echo -e "${GREEN}👋 До свидания!${NC}"
                echo -e "${CYAN}💡 Удачи в создании автономного ИИ! 🚀${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Неверный выбор. Попробуйте снова.${NC}"
                sleep 2
                ;;
        esac
        
        echo ""
        echo -e "${YELLOW}⏳ Нажмите Enter для возврата в меню...${NC}"
        read
    done
}

# Обработка сигналов
cleanup() {
    echo -e "\n${YELLOW}🛑 Получен сигнал завершения...${NC}"
    echo -e "${GREEN}👋 До свидания!${NC}"
    exit 0
}

# Установка обработчиков сигналов
trap cleanup SIGINT SIGTERM

# Запуск основной программы
main