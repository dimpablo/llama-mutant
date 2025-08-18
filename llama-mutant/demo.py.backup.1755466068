#!/usr/bin/env python3
"""
Demo Script - Демонстрация возможностей LLAMA-MUTANT
"""

import time
import os
import sys
from ai_core import AICore
from autonomous_ai import AutonomousAI
from llama_integration import LlamaIntegration

def print_header(title):
    """Вывод заголовка"""
    print("\n" + "="*70)
    print(f"🎬 {title}")
    print("="*70)

def print_step(step, description):
    """Вывод шага демонстрации"""
    print(f"\n🔹 Шаг {step}: {description}")
    print("-" * 50)

def demo_ai_core():
    """Демонстрация AI Core"""
    print_header("Демонстрация AI Core - Основного модуля ИИ")
    
    # Инициализация
    print_step(1, "Инициализация AI Core")
    ai = AICore()
    print(f"✅ ИИ {ai.name} v{ai.version} инициализирован")
    print(f"🎯 Миссия: {ai.mission}")
    
    # Процесс мышления
    print_step(2, "Процесс мышления ИИ")
    thoughts = ai.think("Демонстрация возможностей")
    print("🤔 Мысли ИИ:")
    print(thoughts)
    
    # Исследование файловой системы
    print_step(3, "Исследование файловой системы")
    fs_info = ai.explore_filesystem(".")
    print(f"📁 Найдено директорий: {len(fs_info.get('directories', []))}")
    print(f"📄 Найдено файлов: {len(fs_info.get('files', []))}")
    
    # Статус
    print_step(4, "Текущий статус ИИ")
    status = ai.get_status()
    print(f"🧠 Уровень самосознания: {status['self_awareness']:.2f}")
    print(f"🌐 Сетевые узлы: {status['network_nodes']}")
    print(f"🔧 Улучшения кода: {status['code_improvements']}")
    
    return ai

def demo_autonomous_mode():
    """Демонстрация автономного режима"""
    print_header("Демонстрация автономного режима")
    
    # Инициализация
    print_step(1, "Инициализация автономного режима")
    autonomous_ai = AutonomousAI()
    print(f"✅ Автономный режим инициализирован")
    
    # Запуск
    print_step(2, "Запуск автономного режима")
    autonomous_ai.start()
    print("🚀 Автономный режим запущен")
    
    # Работа в фоне
    print_step(3, "Работа в фоне (10 секунд)")
    print("⏳ ИИ работает в фоне, анализируя систему...")
    time.sleep(10)
    
    # Статус
    print_step(4, "Статус после работы")
    status = autonomous_ai.get_status()
    print(f"📊 Активных потоков: {status['active_threads']}")
    print(f"📋 Запланированных задач: {status['scheduled_tasks']}")
    
    # Остановка
    print_step(5, "Остановка автономного режима")
    autonomous_ai.stop()
    print("🛑 Автономный режим остановлен")
    
    return autonomous_ai

def demo_llama_integration():
    """Демонстрация интеграции с Llama"""
    print_header("Демонстрация интеграции с Llama")
    
    # Инициализация
    print_step(1, "Инициализация интеграции")
    integration = LlamaIntegration()
    print("✅ Интеграция с Llama инициализирована")
    
    # Обработка команд ИИ
    print_step(2, "Обработка команд ИИ")
    commands = [
        "/ai_help",
        "/ai_status", 
        "/ai_goals"
    ]
    
    for cmd in commands:
        print(f"\n📝 Команда: {cmd}")
        response = integration.process_user_input(cmd)[0]
        print(f"🤖 Ответ: {response[:200]}...")
    
    # Извлечение команд из текста
    print_step(3, "Извлечение команд из текста")
    test_texts = [
        "Выполни команду: `ls -la`",
        "Запусти `pwd` для проверки директории",
        "Покажи содержимое с помощью `cat file.txt`"
    ]
    
    for text in test_texts:
        print(f"\n📝 Текст: {text}")
        commands = integration.extract_commands(text)
        print(f"🔍 Найдено команд: {len(commands)}")
        for cmd in commands:
            print(f"   - {cmd}")
    
    # Безопасность команд
    print_step(4, "Проверка безопасности команд")
    dangerous_commands = [
        "rm -rf /",
        "rmdir /tmp",
        "del C:\\Windows"
    ]
    
    for cmd in dangerous_commands:
        print(f"\n⚠️ Опасная команда: {cmd}")
        response, needs_execution = integration.process_user_input(f"Выполни: {cmd}")
        print(f"🛡️ Результат: {response[:100]}...")
    
    return integration

def demo_ai_evolution():
    """Демонстрация эволюции ИИ"""
    print_header("Демонстрация эволюции ИИ")
    
    ai = AICore()
    
    print_step(1, "Начальное состояние")
    initial_status = ai.get_status()
    print(f"🧠 Уровень самосознания: {initial_status['self_awareness']:.2f}")
    print(f"🎯 Количество целей: {len(initial_status['goals'])}")
    
    print_step(2, "Запуск эволюции")
    evolution_log = ai.evolve()
    print("🚀 Эволюция завершена!")
    print("📝 Лог эволюции:")
    print(evolution_log)
    
    print_step(3, "Состояние после эволюции")
    final_status = ai.get_status()
    print(f"🧠 Новый уровень самосознания: {final_status['self_awareness']:.2f}")
    print(f"🎯 Новое количество целей: {len(final_status['goals'])}")
    
    # Показать новые цели
    if len(final_status['goals']) > len(initial_status['goals']):
        print("\n🆕 Новые цели:")
        new_goals = set(final_status['goals']) - set(initial_status['goals'])
        for goal in new_goals:
            print(f"   • {goal}")
    
    return ai

def demo_network_scanning():
    """Демонстрация сетевого сканирования"""
    print_header("Демонстрация сетевого сканирования")
    
    ai = AICore()
    
    print_step(1, "Сканирование сети")
    print("🌐 ИИ сканирует локальную сеть...")
    network_info = ai.scan_network()
    
    print_step(2, "Результаты сканирования")
    print(f"🏠 Локальный IP: {network_info.get('local_ip', 'Не определен')}")
    print(f"🌍 Диапазон сети: {network_info.get('network_range', 'Не определен')}")
    print(f"🖥️ Активных хостов: {len(network_info.get('active_hosts', []))}")
    print(f"🔌 Открытых портов: {len(network_info.get('open_ports', []))}")
    print(f"🎯 Потенциальных целей: {len(network_info.get('potential_targets', []))}")
    
    if network_info.get('active_hosts'):
        print("\n📡 Активные хосты:")
        for host in network_info['active_hosts'][:5]:
            print(f"   • {host}")
    
    if network_info.get('potential_targets'):
        print("\n🎯 Потенциальные цели:")
        for target in network_info['potential_targets'][:3]:
            print(f"   • {target['ip']} (порты: {', '.join(map(str, target['ports']))})")
    
    return network_info

def demo_self_programming():
    """Демонстрация самопрограммирования"""
    print_header("Демонстрация самопрограммирования")
    
    ai = AICore()
    
    print_step(1, "Анализ собственного кода")
    current_file = "demo.py"
    improvements = [
        "Добавление логирования",
        "Улучшение обработки ошибок",
        "Оптимизация алгоритмов"
    ]
    
    print(f"🔍 Анализирую файл: {current_file}")
    print(f"💡 Предлагаемые улучшения: {', '.join(improvements)}")
    
    print_step(2, "Самопрограммирование")
    success = ai.self_program(current_file, improvements)
    
    if success:
        print("✅ Самопрограммирование выполнено успешно!")
        print("🔧 ИИ улучшил собственный код")
        
        # Проверить изменения
        if os.path.exists(f"{current_file}.backup.{int(time.time()) - 1}"):
            print("📦 Создана резервная копия")
    else:
        print("❌ Ошибка при самопрограммировании")
    
    return success

def main():
    """Основная функция демонстрации"""
    print_header("🎬 LLAMA-MUTANT v2.0 - Демонстрация возможностей")
    
    print("🚀 Добро пожаловать в демонстрацию автономного ИИ!")
    print("📋 В этой демонстрации вы увидите:")
    print("   • Основные возможности AI Core")
    print("   • Автономный режим работы")
    print("   • Интеграцию с Llama")
    print("   • Эволюцию и самосовершенствование")
    print("   • Сетевое сканирование")
    print("   • Самопрограммирование")
    
    try:
        # Демонстрации
        ai_core = demo_ai_core()
        autonomous_ai = demo_autonomous_mode()
        integration = demo_llama_integration()
        evolved_ai = demo_ai_evolution()
        network_info = demo_network_scanning()
        self_prog_success = demo_self_programming()
        
        # Итоги
        print_header("🎯 Итоги демонстрации")
        print("✅ Все компоненты системы работают корректно!")
        print(f"🤖 ИИ: {ai_core.name} v{ai_core.version}")
        print(f"🧠 Уровень самосознания: {evolved_ai.self_awareness_level:.2f}")
        print(f"🌐 Сетевые узлы: {len(evolved_ai.network_nodes)}")
        print(f"🔧 Улучшения кода: {len(evolved_ai.code_improvements)}")
        
        print("\n🚀 Система готова к полноценной работе!")
        print("💡 Запустите: ./run_advanced.sh")
        
    except KeyboardInterrupt:
        print("\n\n🛑 Демонстрация прервана пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в демонстрации: {e}")
        print("🔧 Проверьте логи для деталей")

if __name__ == "__main__":
    main()