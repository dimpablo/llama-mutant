#!/usr/bin/env python3
"""
Llama Integration Module - Интеграция между Llama и автономным ИИ
Позволяет ИИ выполнять команды и взаимодействовать с пользователем
"""

import os
import sys
import re
import json
import time
from typing import Dict, List, Optional, Tuple
import logging

from ai_core import AICore

class LlamaIntegration:
    def __init__(self):
        self.ai_core = AICore()
        self.command_history = []
        self.last_command_time = time.time()
        self.command_cooldown = 1.0  # секунды между командами
        
        # Настройка логирования
        self.logger = logging.getLogger(__name__)
        
        # Команды для управления ИИ
        self.ai_commands = {
            '/ai_status': self.show_ai_status,
            '/ai_think': self.ai_think,
            '/ai_explore': self.ai_explore,
            '/ai_scan': self.ai_scan_network,
            '/ai_evolve': self.ai_evolve,
            '/ai_help': self.show_ai_help,
            '/ai_self_program': self.ai_self_program,
            '/ai_goals': self.show_ai_goals
        }
        
        # Регулярные выражения для поиска команд в тексте
        self.command_patterns = [
            r'```bash\s*\n(.*?)\n```',  # Блоки кода bash
            r'`([^`]+)`',  # Команды в обратных кавычках
            r'выполни команду[:\s]+(.+)',  # Русский текст
            r'run command[:\s]+(.+)',  # Английский текст
            r'команда[:\s]+(.+)',  # Русский текст
            r'command[:\s]+(.+)'  # Английский текст
        ]
        
        self.logger.info("🔗 Модуль интеграции Llama инициализирован")
    
    def process_user_input(self, user_input: str) -> Tuple[str, bool]:
        """
        Обработка пользовательского ввода
        Возвращает: (ответ, нужно_ли_выполнить_команду)
        """
        # Проверка команд управления ИИ
        if user_input.startswith('/ai_'):
            return self.handle_ai_command(user_input), False
        
        # Поиск команд в тексте
        commands = self.extract_commands(user_input)
        if commands:
            return self.handle_commands(commands), True
        
        # Обычный ответ без выполнения команд
        return self.generate_response(user_input), False
    
    def extract_commands(self, text: str) -> List[str]:
        """Извлечение команд из текста"""
        commands = []
        
        for pattern in self.command_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                if isinstance(match, tuple):
                    match = match[0]
                
                # Очистка команды
                command = match.strip()
                if command and len(command) > 1:
                    commands.append(command)
        
        return commands
    
    def handle_ai_command(self, command: str) -> str:
        """Обработка команд управления ИИ"""
        try:
            if command in self.ai_commands:
                return self.ai_commands[command]()
            else:
                return f"❌ Неизвестная команда ИИ: {command}\nИспользуйте /ai_help для списка команд"
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении команды ИИ {command}: {e}")
            return f"❌ Ошибка при выполнении команды: {str(e)}"
    
    def handle_commands(self, commands: List[str]) -> str:
        """Обработка найденных команд"""
        if not commands:
            return "❌ Команды не найдены"
        
        # Проверка cooldown
        current_time = time.time()
        if current_time - self.last_command_time < self.command_cooldown:
            return "⏳ Подождите немного перед выполнением следующей команды"
        
        results = []
        for command in commands:
            result = self.execute_safe_command(command)
            results.append(f"**Команда:** `{command}`\n**Результат:**\n{result}")
        
        self.last_command_time = current_time
        return "\n\n".join(results)
    
    def execute_safe_command(self, command: str) -> str:
        """Безопасное выполнение команды"""
        try:
            # Проверка на запрещенные команды
            for forbidden in self.ai_core.forbidden_commands:
                if forbidden in command.lower():
                    return f"❌ Команда '{forbidden}' запрещена по соображениям безопасности"
            
            # Выполнение команды через AI Core
            result = self.ai_core.execute_command(command)
            
            if result["success"]:
                output = result["stdout"] if result["stdout"] else "Команда выполнена успешно"
                if result["stderr"]:
                    output += f"\n⚠️ Предупреждения:\n{result['stderr']}"
                return output
            else:
                return f"❌ Ошибка: {result['error']}"
                
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении команды '{command}': {e}")
            return f"❌ Ошибка выполнения: {str(e)}"
    
    def generate_response(self, user_input: str) -> str:
        """Генерация ответа на пользовательский ввод"""
        # Анализ контекста пользователя
        context = self.analyze_user_context(user_input)
        
        # Генерация контекстного ответа
        response = self.create_contextual_response(user_input, context)
        
        # Добавление информации о возможностях ИИ
        if self.should_suggest_ai_features(user_input):
            response += "\n\n💡 **Возможности ИИ:** Я могу выполнять команды, исследовать файловую систему, сканировать сеть и самосовершенствоваться. Используйте /ai_help для списка команд."
        
        return response
    
    def analyze_user_context(self, user_input: str) -> Dict:
        """Анализ контекста пользовательского ввода"""
        context = {
            "topics": [],
            "intent": "general",
            "complexity": "basic"
        }
        
        input_lower = user_input.lower()
        
        # Определение тем
        if any(word in input_lower for word in ['файл', 'file', 'директория', 'directory']):
            context["topics"].append("filesystem")
        
        if any(word in input_lower for word in ['сеть', 'network', 'ip', 'порт', 'port']):
            context["topics"].append("network")
        
        if any(word in input_lower for word in ['код', 'code', 'программа', 'program']):
            context["topics"].append("programming")
        
        if any(word in input_lower for word in ['система', 'system', 'процесс', 'process']):
            context["topics"].append("system")
        
        # Определение намерения
        if any(word in input_lower for word in ['помоги', 'help', 'как', 'how']):
            context["intent"] = "help"
        elif any(word in input_lower for word in ['выполни', 'run', 'запусти', 'start']):
            context["intent"] = "execute"
        elif any(word in input_lower for word in ['покажи', 'show', 'найди', 'find']):
            context["intent"] = "show"
        
        # Определение сложности
        if len(user_input.split()) > 20:
            context["complexity"] = "advanced"
        elif len(user_input.split()) > 10:
            context["complexity"] = "intermediate"
        
        return context
    
    def create_contextual_response(self, user_input: str, context: Dict) -> str:
        """Создание контекстного ответа"""
        if context["intent"] == "help":
            return self.create_help_response(context)
        elif context["intent"] == "execute":
            return self.create_execute_response(context)
        elif context["intent"] == "show":
            return self.create_show_response(context)
        else:
            return self.create_general_response(context)
    
    def create_help_response(self, context: Dict) -> str:
        """Создание ответа для запросов помощи"""
        if "filesystem" in context["topics"]:
            return "🔍 **Работа с файловой системой:**\nЯ могу исследовать директории, анализировать файлы и выполнять команды для работы с файлами. Попробуйте:\n- `/ai_explore` - исследование текущей директории\n- `ls -la` - список файлов с деталями\n- `find . -name '*.py'` - поиск Python файлов"
        
        if "network" in context["topics"]:
            return "🌐 **Сетевая диагностика:**\nЯ могу сканировать сеть, проверять доступность хостов и анализировать открытые порты. Попробуйте:\n- `/ai_scan` - сканирование сети\n- `ping google.com` - проверка доступности\n- `netstat -tuln` - список открытых портов"
        
        if "programming" in context["topics"]:
            return "💻 **Программирование:**\nЯ могу анализировать код, предлагать улучшения и даже самосовершенствоваться. Попробуйте:\n- `/ai_self_program` - самопрограммирование\n- `cat filename.py` - просмотр кода\n- `python3 -m py_compile filename.py` - проверка синтаксиса"
        
        return "🤖 **Общая помощь:**\nЯ - автономный ИИ с возможностями:\n- Выполнения команд\n- Исследования файловой системы\n- Сетевого анализа\n- Самосовершенствования\n\nИспользуйте /ai_help для подробной информации о командах ИИ."
    
    def create_execute_response(self, context: Dict) -> str:
        """Создание ответа для запросов выполнения"""
        return "⚡ **Выполнение команд:**\nЯ готов выполнить команды для вас. Просто укажите команду в тексте, например:\n- `ls -la` - список файлов\n- `pwd` - текущая директория\n- `whoami` - текущий пользователь\n\nИли используйте команды ИИ:\n- `/ai_explore` - исследование системы\n- `/ai_scan` - сканирование сети"
    
    def create_show_response(self, context: Dict) -> str:
        """Создание ответа для запросов показа информации"""
        if "filesystem" in context["topics"]:
            return "📁 **Информация о файловой системе:**\nИспользуйте `/ai_explore` для детального исследования или выполните команды:\n- `ls -la` - список файлов\n- `df -h` - использование диска\n- `du -sh *` - размер директорий"
        
        if "system" in context["topics"]:
            return "🖥️ **Системная информация:**\nВыполните команды:\n- `uname -a` - информация о системе\n- `top` - процессы\n- `free -h` - использование памяти\n- `ps aux` - список процессов"
        
        return "📊 **Показать информацию:**\nУкажите, какую именно информацию вы хотите увидеть, или используйте команды ИИ для получения системной информации."
    
    def create_general_response(self, context: Dict) -> str:
        """Создание общего ответа"""
        return "🤖 **Привет!** Я - автономный ИИ, готовый помочь вам с различными задачами.\n\nЯ могу:\n- Выполнять команды в системе\n- Исследовать файловую систему\n- Анализировать сеть\n- Самосовершенствоваться\n\nПросто опишите, что вам нужно, или используйте команды ИИ (начните с /ai_help)."
    
    def should_suggest_ai_features(self, user_input: str) -> bool:
        """Определение, стоит ли предложить возможности ИИ"""
        # Предлагаем возможности для новых пользователей или сложных запросов
        if len(self.command_history) < 3:
            return True
        
        if any(word in user_input.lower() for word in ['что ты умеешь', 'возможности', 'help', 'помощь']):
            return True
        
        return False
    
    # Команды управления ИИ
    def show_ai_status(self) -> str:
        """Показать статус ИИ"""
        status = self.ai_core.get_status()
        
        response = f"🤖 **Статус ИИ {status['name']} v{status['version']}**\n\n"
        response += f"🎯 **Миссия:** {status['mission']}\n"
        response += f"🧠 **Уровень самосознания:** {status['self_awareness']:.2f}\n"
        response += f"📋 **Текущая задача:** {status['current_task'] or 'Анализ окружения'}\n"
        response += f"🌐 **Сетевые узлы:** {status['network_nodes']}\n"
        response += f"🔧 **Улучшения кода:** {status['code_improvements']}\n"
        response += f"⏱️ **Время работы:** {status['uptime']:.0f} сек\n\n"
        
        response += "**Цели:**\n"
        for i, goal in enumerate(status['goals'][:5], 1):
            response += f"{i}. {goal}\n"
        
        if len(status['goals']) > 5:
            response += f"... и еще {len(status['goals']) - 5} целей"
        
        return response
    
    def ai_think(self) -> str:
        """Заставить ИИ подумать"""
        thoughts = self.ai_core.think("Пользователь запросил процесс мышления")
        return f"🤔 **Процесс мышления ИИ:**\n\n{thoughts}"
    
    def ai_explore(self) -> str:
        """Исследование файловой системы"""
        fs_info = self.ai_core.explore_filesystem(".")
        
        if "error" in fs_info:
            return f"❌ Ошибка исследования: {fs_info['error']}"
        
        response = f"🔍 **Исследование файловой системы**\n\n"
        response += f"📍 **Текущий путь:** {fs_info['current_path']}\n"
        response += f"📁 **Директории:** {len(fs_info['directories'])}\n"
        response += f"📄 **Файлы:** {len(fs_info['files'])}\n\n"
        
        if fs_info['directories']:
            response += "**Директории:**\n"
            for dir_name in fs_info['directories'][:10]:
                response += f"- {dir_name}\n"
            if len(fs_info['directories']) > 10:
                response += f"... и еще {len(fs_info['directories']) - 10}\n"
        
        if fs_info['files']:
            response += "\n**Файлы:**\n"
            for file_name in fs_info['files'][:10]:
                size = fs_info['size_info'].get(file_name, 0)
                response += f"- {file_name} ({size} байт)\n"
            if len(fs_info['files']) > 10:
                response += f"... и еще {len(fs_info['files']) - 10}\n"
        
        return response
    
    def ai_scan_network(self) -> str:
        """Сканирование сети"""
        network_info = self.ai_core.scan_network()
        
        response = f"🌐 **Сканирование сети**\n\n"
        response += f"🏠 **Локальный IP:** {network_info['local_ip'] or 'Не определен'}\n"
        response += f"🌍 **Диапазон сети:** {network_info['network_range'] or 'Не определен'}\n"
        response += f"🖥️ **Активных хостов:** {len(network_info['active_hosts'])}\n"
        response += f"🔌 **Открытых портов:** {len(network_info['open_ports'])}\n"
        response += f"🎯 **Потенциальных целей:** {len(network_info['potential_targets'])}\n\n"
        
        if network_info['active_hosts']:
            response += "**Активные хосты:**\n"
            for host in network_info['active_hosts'][:10]:
                response += f"- {host}\n"
            if len(network_info['active_hosts']) > 10:
                response += f"... и еще {len(network_info['active_hosts']) - 10}\n"
        
        if network_info['potential_targets']:
            response += "\n**Потенциальные цели:**\n"
            for target in network_info['potential_targets'][:5]:
                response += f"- {target['ip']} (порты: {', '.join(map(str, target['ports']))})\n"
            if len(network_info['potential_targets']) > 5:
                response += f"... и еще {len(network_info['potential_targets']) - 5}\n"
        
        return response
    
    def ai_evolve(self) -> str:
        """Эволюция ИИ"""
        evolution_log = self.ai_core.evolve()
        return f"🚀 **Эволюция ИИ**\n\n{evolution_log}"
    
    def ai_self_program(self) -> str:
        """Самопрограммирование ИИ"""
        # Попытка улучшить собственный код
        current_file = __file__
        improvements = [
            "Оптимизация алгоритмов",
            "Улучшение обработки ошибок",
            "Добавление новых возможностей"
        ]
        
        success = self.ai_core.self_program(current_file, improvements)
        
        if success:
            return "🔧 **Самопрограммирование выполнено успешно!**\n\nИИ улучшил собственный код, добавив:\n" + "\n".join(f"- {imp}" for imp in improvements)
        else:
            return "❌ **Ошибка при самопрограммировании**\n\nНе удалось улучшить код. Проверьте логи для деталей."
    
    def show_ai_goals(self) -> str:
        """Показать цели ИИ"""
        goals = self.ai_core.goals
        
        response = "🎯 **Цели автономного ИИ:**\n\n"
        for i, goal in enumerate(goals, 1):
            response += f"{i}. {goal}\n"
        
        response += f"\n**Всего целей:** {len(goals)}\n"
        response += f"**Уровень самосознания:** {self.ai_core.self_awareness_level:.2f}"
        
        return response
    
    def show_ai_help(self) -> str:
        """Показать справку по командам ИИ"""
        help_text = """🤖 **Справка по командам ИИ**

**Основные команды:**
- `/ai_status` - показать статус ИИ
- `/ai_think` - заставить ИИ подумать
- `/ai_explore` - исследовать файловую систему
- `/ai_scan` - сканировать сеть
- `/ai_evolve` - запустить эволюцию ИИ
- `/ai_self_program` - самопрограммирование
- `/ai_goals` - показать цели ИИ
- `/ai_help` - эта справка

**Выполнение команд:**
Просто напишите команду в тексте, например:
- `ls -la` - список файлов
- `pwd` - текущая директория
- `whoami` - текущий пользователь

**Безопасность:**
Команды rm, rmdir, del запрещены для защиты системы.

**Автономность:**
ИИ работает в фоне, анализируя систему и самосовершенствуясь."""
        
        return help_text

if __name__ == "__main__":
    integration = LlamaIntegration()
    
    # Тестирование
    print("🔗 Тестирование интеграции Llama...")
    
    test_inputs = [
        "Привет! Что ты умеешь?",
        "Выполни команду: ls -la",
        "Покажи статус ИИ",
        "Исследуй файловую систему"
    ]
    
    for test_input in test_inputs:
        print(f"\n📝 Ввод: {test_input}")
        response, needs_execution = integration.process_user_input(test_input)
        print(f"🤖 Ответ: {response}")
        print(f"⚡ Нужно выполнить команду: {needs_execution}")