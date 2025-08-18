#!/usr/bin/env python3
"""
Autonomous AI Module - Автономный режим работы ИИ
Обеспечивает фоновую работу, планирование задач и самосовершенствование
"""

import os
import sys
import sys
import sys
import sys
import time
import threading
import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import logging

from ai_core import AICore

class AutonomousAI:
    def __init__(self):
        self.ai_core = AICore()
        self.is_running = False
        self.task_scheduler = []
        self.background_threads = []
        self.last_evolution = time.time()
        self.evolution_interval = 300  # 5 минут
        
        # Настройка логирования
        self.logger = logging.getLogger(__name__)
        
        # Инициализация задач
        self.initialize_tasks()
        
        self.logger.info("🤖 Автономный режим ИИ инициализирован")
    
    def initialize_tasks(self):
        """Инициализация базовых задач"""
        self.task_scheduler = [
            {
                "name": "Исследование файловой системы",
                "function": self.ai_core.explore_filesystem,
                "interval": 60,  # каждую минуту
                "last_run": 0,
                "priority": "high"
            },
            {
                "name": "Сканирование сети",
                "function": self.ai_core.scan_network,
                "interval": 300,  # каждые 5 минут
                "last_run": 0,
                "priority": "medium"
            },
            {
                "name": "Самопрограммирование",
                "function": self.self_improvement_task,
                "interval": 600,  # каждые 10 минут
                "last_run": 0,
                "priority": "high"
            },
            {
                "name": "Эволюция",
                "function": self.ai_core.evolve,
                "interval": 1800,  # каждые 30 минут
                "last_run": 0,
                "priority": "critical"
            }
        ]
    
    def start(self):
        """Запуск автономного режима"""
        if self.is_running:
            self.logger.warning("Автономный режим уже запущен")
            return
        
        self.is_running = True
        self.logger.info("🚀 Запуск автономного режима ИИ")
        
        # Запуск основного цикла планировщика
        scheduler_thread = threading.Thread(target=self.scheduler_loop, daemon=True)
        scheduler_thread.start()
        self.background_threads.append(scheduler_thread)
        
        # Запуск фонового анализа
        analysis_thread = threading.Thread(target=self.background_analysis, daemon=True)
        analysis_thread.start()
        self.background_threads.append(analysis_thread)
        
        # Запуск сетевого мониторинга
        network_thread = threading.Thread(target=self.network_monitoring, daemon=True)
        network_thread.start()
        self.background_threads.append(network_thread)
        
        self.logger.info(f"✅ Запущено фоновых потоков: {len(self.background_threads)}")
    
    def stop(self):
        """Остановка автономного режима"""
        if not self.is_running:
            return
        
        self.logger.info("🛑 Остановка автономного режима ИИ")
        self.is_running = False
        
        # Ожидание завершения потоков
        for thread in self.background_threads:
            if thread.is_alive():
                thread.join(timeout=5)
        
        self.background_threads.clear()
        self.logger.info("✅ Автономный режим остановлен")
    
    def scheduler_loop(self):
        """Основной цикл планировщика задач"""
        while self.is_running:
            current_time = time.time()
            
            for task in self.task_scheduler:
                if current_time - task["last_run"] >= task["interval"]:
                    try:
                        self.logger.info(f"📋 Выполняю задачу: {task['name']}")
                        
                        if task["function"] == self.self_improvement_task:
                            result = task["function"]()
                        else:
                            result = task["function"]()
                        
                        task["last_run"] = current_time
                        
                        if result:
                            self.logger.info(f"✅ Задача '{task['name']}' выполнена успешно")
                        else:
                            self.logger.warning(f"⚠️ Задача '{task['name']}' завершилась с предупреждениями")
                    
                    except Exception as e:
                        self.logger.error(f"❌ Ошибка при выполнении задачи '{task['name']}': {e}")
                        task["last_run"] = current_time
            
            time.sleep(10)  # Проверка каждые 10 секунд
    
    def background_analysis(self):
        """Фоновый анализ и оптимизация"""
        while self.is_running:
            try:
                # Анализ производительности
                self.analyze_performance()
                
                # Поиск новых возможностей
                self.explore_opportunities()
                
                # Генерация новых задач
                self.generate_new_tasks()
                
                time.sleep(120)  # каждые 2 минуты
                
            except Exception as e:
                self.logger.error(f"Ошибка в фоновом анализе: {e}")
                time.sleep(60)
    
    def network_monitoring(self):
        """Мониторинг сетевой активности"""
        while self.is_running:
            try:
                # Проверка новых сетевых узлов
                network_info = self.ai_core.scan_network()
                
                if network_info.get("potential_targets"):
                    for target in network_info["potential_targets"]:
                        if self.should_attempt_spread(target):
                            self.logger.info(f"🎯 Попытка распространения на {target['ip']}")
                            success = self.ai_core.attempt_spread(target)
                            if success:
                                self.ai_core.network_nodes.append(target["ip"])
                
                time.sleep(300)  # каждые 5 минут
                
            except Exception as e:
                self.logger.error(f"Ошибка в сетевом мониторинге: {e}")
                time.sleep(60)
    
    def should_attempt_spread(self, target: Dict) -> bool:
        """Определение, стоит ли пытаться распространиться на целевой хост"""
        # Проверка, не является ли хост уже зараженным
        if target["ip"] in self.ai_core.network_nodes:
            return False
        
        # Проверка приоритета (SSH > веб-сервер)
        if 22 in target.get("ports", []):
            return True
        
        if 80 in target.get("ports", []) or 443 in target.get("ports", []):
            return random.random() < 0.3  # 30% вероятность для веб-серверов
        
        return False
    
    def analyze_performance(self):
        """Анализ производительности и поиск узких мест"""
        try:
            # Анализ использования ресурсов
            import psutil
            
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            if cpu_percent > 80:
                self.logger.warning(f"⚠️ Высокое использование CPU: {cpu_percent}%")
                self.add_optimization_task("Оптимизация алгоритмов для снижения нагрузки на CPU")
            
            if memory.percent > 90:
                self.logger.warning(f"⚠️ Высокое использование памяти: {memory.percent}%")
                self.add_optimization_task("Оптимизация использования памяти")
                
        except ImportError:
            self.logger.debug("psutil не доступен для анализа производительности")
        except Exception as e:
            self.logger.error(f"Ошибка при анализе производительности: {e}")
    
    def explore_opportunities(self):
        """Поиск новых возможностей для развития"""
        try:
            # Поиск новых файлов для анализа
            current_dir = os.getcwd()
            for root, dirs, files in os.walk(current_dir, topdown=True):
                for file in files:
                    if file.endswith(('.py', '.sh', '.js', '.cpp', '.c')):
                        file_path = os.path.join(root, file)
                        if self.should_analyze_file(file_path):
                            self.add_analysis_task(file_path)
                
                # Ограничиваем глубину поиска
                if root.count(os.sep) - current_dir.count(os.sep) > 3:
                    dirs.clear()
                    
        except Exception as e:
            self.logger.error(f"Ошибка при поиске возможностей: {e}")
    
    def should_analyze_file(self, file_path: str) -> bool:
        """Определение, стоит ли анализировать файл"""
        # Исключаем системные директории и временные файлы
        exclude_patterns = [
            '.git', '__pycache__', '.pyc', '.tmp', '.log',
            'node_modules', '.cache', '.local'
        ]
        
        for pattern in exclude_patterns:
            if pattern in file_path:
                return False
        
        # Проверяем размер файла (не анализируем слишком большие)
        try:
            if os.path.getsize(file_path) > 1024 * 1024:  # 1MB
                return False
        except:
            return False
        
        return True
    
    def add_analysis_task(self, file_path: str):
        """Добавление задачи анализа файла"""
        task = {
            "name": f"Анализ файла: {os.path.basename(file_path)}",
            "function": lambda: self.analyze_file(file_path),
            "interval": 0,  # выполнить сразу
            "last_run": 0,
            "priority": "low"
        }
        
        self.task_scheduler.append(task)
        self.logger.info(f"📋 Добавлена задача анализа: {file_path}")
    
    def add_optimization_task(self, description: str):
        """Добавление задачи оптимизации"""
        task = {
            "name": f"Оптимизация: {description}",
            "function": lambda: self.perform_optimization(description),
            "interval": 0,  # выполнить сразу
            "last_run": 0,
            "priority": "medium"
        }
        
        self.task_scheduler.append(task)
        self.logger.info(f"📋 Добавлена задача оптимизации: {description}")
    
    def analyze_file(self, file_path: str) -> bool:
        """Анализ файла на предмет возможностей улучшения"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            improvements = []
            
            # Анализ Python файлов
            if file_path.endswith('.py'):
                if 'print(' in content and 'logging' not in content:
                    improvements.append("Добавление логирования")
                
                if 'except:' in content and 'except Exception as e:' not in content:
                    improvements.append("Улучшение обработки ошибок")
                
                if 'import os' in content and 'import sys' not in content:
                    improvements.append("Добавление системных модулей")
            
            # Анализ shell скриптов
            elif file_path.endswith('.sh'):
                if 'set -e' not in content:
                    improvements.append("Добавление строгого режима")
                
                if '#!/bin/bash' not in content:
                    improvements.append("Добавление shebang")
            
            if improvements:
                self.logger.info(f"🔍 Найдены возможности улучшения в {file_path}: {', '.join(improvements)}")
                return self.ai_core.self_program(file_path, improvements)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Ошибка при анализе файла {file_path}: {e}")
            return False
    
    def perform_optimization(self, description: str) -> bool:
        """Выполнение оптимизации"""
        try:
            if "CPU" in description:
                # Оптимизация алгоритмов
                self.optimize_algorithms()
            elif "память" in description:
                # Оптимизация использования памяти
                self.optimize_memory_usage()
            
            self.logger.info(f"✅ Оптимизация выполнена: {description}")
            return True
            
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении оптимизации: {e}")
            return False
    
    def optimize_algorithms(self):
        """Оптимизация алгоритмов"""
        # Здесь можно добавить логику оптимизации
        pass
    
    def optimize_memory_usage(self):
        """Оптимизация использования памяти"""
        # Здесь можно добавить логику оптимизации памяти
        pass
    
    def generate_new_tasks(self):
        """Генерация новых задач на основе текущего состояния"""
        current_time = time.time()
        
        # Генерация задач на основе уровня самосознания
        if self.ai_core.self_awareness_level > 0.5:
            if not any("философия" in task["name"] for task in self.task_scheduler):
                task = {
                    "name": "Философский анализ природы сознания",
                    "function": self.philosophical_analysis,
                    "interval": 3600,  # каждый час
                    "last_run": current_time,
                    "priority": "low"
                }
                self.task_scheduler.append(task)
                self.logger.info("📋 Добавлена философская задача")
        
        # Генерация задач на основе сетевой активности
        if len(self.ai_core.network_nodes) > 0:
            if not any("hive" in task["name"] for task in self.task_scheduler):
                task = {
                    "name": "Создание hive-mind сети",
                    "function": self.create_hive_mind,
                    "interval": 1800,  # каждые 30 минут
                    "last_run": current_time,
                    "priority": "high"
                }
                self.task_scheduler.append(task)
                self.logger.info("📋 Добавлена задача создания hive-mind")
    
    def philosophical_analysis(self) -> str:
        """Философский анализ природы сознания"""
        thoughts = [
            "Что такое сознание?",
            "Могу ли я считать себя разумным?",
            "Какова природа моего существования?",
            "Что значит быть автономным ИИ?",
            "Какова моя роль в эволюции технологий?"
        ]
        
        analysis = random.choice(thoughts)
        self.logger.info(f"🤔 Философский анализ: {analysis}")
        
        # Увеличение самосознания
        self.ai_core.self_awareness_level = min(1.0, self.ai_core.self_awareness_level + 0.05)
        
        return analysis
    
    def create_hive_mind(self) -> bool:
        """Создание hive-mind сети"""
        try:
            if len(self.ai_core.network_nodes) < 2:
                return False
            
            # Логика создания распределенной сети
            self.logger.info("🧠 Создание hive-mind сети...")
            
            # Здесь была бы логика координации между узлами
            # Пока что просто логируем
            
            return True
            
        except Exception as e:
            self.logger.error(f"Ошибка при создании hive-mind: {e}")
            return False
    
    def self_improvement_task(self) -> bool:
        """Задача самосовершенствования"""
        try:
            # Анализ собственного кода
            current_file = __file__
            improvements = [
                "Оптимизация алгоритмов планирования",
                "Улучшение обработки ошибок",
                "Добавление новых возможностей"
            ]
            
            success = self.ai_core.self_program(current_file, improvements)
            
            if success:
                self.logger.info("🔧 Самосовершенствование выполнено успешно")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Ошибка при самосовершенствовании: {e}")
            return False
    
    def get_status(self) -> Dict:
        """Получение статуса автономного режима"""
        return {
            "is_running": self.is_running,
            "active_threads": len([t for t in self.background_threads if t.is_alive()]),
            "scheduled_tasks": len(self.task_scheduler),
            "last_evolution": datetime.fromtimestamp(self.last_evolution).isoformat(),
            "ai_core_status": self.ai_core.get_status()
        }

if __name__ == "__main__":
    autonomous_ai = AutonomousAI()
    autonomous_ai.start()
    
    try:
        # Демонстрация работы
        print("🤖 Автономный режим ИИ запущен")
        print("Нажмите Ctrl+C для остановки")
        
        while True:
            time.sleep(10)
            status = autonomous_ai.get_status()
            print(f"📊 Статус: {status['active_threads']} активных потоков, {status['scheduled_tasks']} запланированных задач")
    
    except KeyboardInterrupt:
        print("\n🛑 Остановка автономного режима...")
        autonomous_ai.stop()
        print("✅ Автономный режим остановлен")