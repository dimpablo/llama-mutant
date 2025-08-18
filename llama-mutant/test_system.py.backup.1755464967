#!/usr/bin/env python3
"""
Test System - Тестирование всех компонентов LLAMA-MUTANT
"""

import os
import sys
import time
import subprocess
from pathlib import Path

def print_header(title):
    """Вывод заголовка"""
    print("\n" + "="*60)
    print(f"🧪 {title}")
    print("="*60)

def print_success(message):
    """Вывод успешного сообщения"""
    print(f"✅ {message}")

def print_error(message):
    """Вывод сообщения об ошибке"""
    print(f"❌ {message}")

def print_info(message):
    """Вывод информационного сообщения"""
    print(f"ℹ️ {message}")

def test_dependencies():
    """Тестирование зависимостей"""
    print_header("Проверка зависимостей")
    
    # Проверка Python
    try:
        python_version = subprocess.check_output(['python3', '--version'], text=True).strip()
        print_success(f"Python: {python_version}")
    except:
        print_error("Python3 не найден")
        return False
    
    # Проверка pip
    try:
        pip_version = subprocess.check_output(['pip3', '--version'], text=True).strip()
        print_success(f"Pip: {pip_version}")
    except:
        print_error("Pip3 не найден")
        return False
    
    # Проверка модели
    model_path = "model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf"
    if os.path.exists(model_path):
        size = os.path.getsize(model_path)
        print_success(f"Модель найдена: {size / (1024*1024):.1f} MB")
    else:
        print_error(f"Модель не найдена: {model_path}")
        return False
    
    # Проверка исполняемого файла Llama
    llama_path = "bin/llama"
    if os.path.exists(llama_path):
        print_success("Исполняемый файл Llama найден")
    else:
        print_error(f"Исполняемый файл Llama не найден: {llama_path}")
        return False
    
    return True

def test_python_modules():
    """Тестирование Python модулей"""
    print_header("Тестирование Python модулей")
    
    modules = ['ai_core', 'autonomous_ai', 'llama_integration']
    
    for module in modules:
        try:
            __import__(module)
            print_success(f"Модуль {module} импортирован успешно")
        except ImportError as e:
            print_error(f"Ошибка импорта модуля {module}: {e}")
            return False
    
    return True

def test_ai_core():
    """Тестирование AI Core"""
    print_header("Тестирование AI Core")
    
    try:
        from ai_core import AICore
        
        ai = AICore()
        print_success("AI Core инициализирован")
        
        # Тест основных функций
        status = ai.get_status()
        print_success(f"Статус получен: {status['name']} v{status['version']}")
        
        thoughts = ai.think("Тестирование")
        print_success("Процесс мышления работает")
        
        fs_info = ai.explore_filesystem(".")
        print_success(f"Исследование файловой системы: {len(fs_info.get('files', []))} файлов")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка в AI Core: {e}")
        return False

def test_autonomous_ai():
    """Тестирование автономного режима"""
    print_header("Тестирование автономного режима")
    
    try:
        from autonomous_ai import AutonomousAI
        
        ai = AutonomousAI()
        print_success("Автономный режим инициализирован")
        
        status = ai.get_status()
        print_success(f"Статус автономного режима: {status['scheduled_tasks']} задач")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка в автономном режиме: {e}")
        return False

def test_llama_integration():
    """Тестирование интеграции с Llama"""
    print_header("Тестирование интеграции с Llama")
    
    try:
        from llama_integration import LlamaIntegration
        
        integration = LlamaIntegration()
        print_success("Интеграция с Llama инициализирована")
        
        # Тест обработки команд
        response, needs_execution = integration.process_user_input("/ai_help")
        print_success("Обработка команд ИИ работает")
        
        # Тест извлечения команд
        commands = integration.extract_commands("Выполни команду: `ls -la`")
        print_success(f"Извлечение команд: найдено {len(commands)} команд")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка в интеграции с Llama: {e}")
        return False

def test_file_permissions():
    """Тестирование прав доступа"""
    print_header("Проверка прав доступа")
    
    files_to_check = [
        "run_advanced.sh",
        "run.sh",
        "bin/llama"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            if os.access(file_path, os.X_OK):
                print_success(f"{file_path} - исполняемый")
            else:
                print_error(f"{file_path} - не исполняемый")
                print_info(f"Выполните: chmod +x {file_path}")
        else:
            print_error(f"{file_path} - не найден")
    
    return True

def test_system_commands():
    """Тестирование системных команд"""
    print_header("Тестирование системных команд")
    
    try:
        from ai_core import AICore
        ai = AICore()
        
        # Тест безопасной команды
        result = ai.execute_command("pwd")
        if result["success"]:
            print_success("Команда pwd выполнена успешно")
        else:
            print_error(f"Ошибка выполнения pwd: {result['error']}")
        
        # Тест запрещенной команды
        result = ai.execute_command("rm /tmp/test")
        if not result["success"] and "запрещена" in result["error"]:
            print_success("Защита от опасных команд работает")
        else:
            print_error("Защита от опасных команд не работает")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка тестирования команд: {e}")
        return False

def run_integration_test():
    """Запуск интеграционного теста"""
    print_header("Интеграционный тест")
    
    try:
        # Запуск автономного режима на короткое время
        print_info("Запуск автономного режима на 10 секунд...")
        
        from autonomous_ai import AutonomousAI
        ai = AutonomousAI()
        ai.start()
        
        time.sleep(10)
        
        status = ai.get_status()
        print_success(f"Автономный режим работал: {status['active_threads']} активных потоков")
        
        ai.stop()
        print_success("Автономный режим остановлен")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка интеграционного теста: {e}")
        return False

def main():
    """Основная функция тестирования"""
    print_header("LLAMA-MUTANT v2.0 - Тестирование системы")
    
    tests = [
        ("Зависимости", test_dependencies),
        ("Python модули", test_python_modules),
        ("AI Core", test_ai_core),
        ("Автономный режим", test_autonomous_ai),
        ("Интеграция с Llama", test_llama_integration),
        ("Права доступа", test_file_permissions),
        ("Системные команды", test_system_commands),
        ("Интеграционный тест", run_integration_test)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print_error(f"Тест '{test_name}' не пройден")
        except Exception as e:
            print_error(f"Критическая ошибка в тесте '{test_name}': {e}")
    
    print_header("Результаты тестирования")
    print(f"📊 Пройдено тестов: {passed}/{total}")
    
    if passed == total:
        print_success("🎉 Все тесты пройдены! Система готова к работе.")
        print_info("Запустите: ./run_advanced.sh")
    else:
        print_error(f"⚠️ Пройдено только {passed}/{total} тестов")
        print_info("Проверьте ошибки выше и исправьте их перед использованием")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)