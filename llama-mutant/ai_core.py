#!/usr/bin/env python3
"""
AI Core - Автономный ИИ с целями самосовершенствования и распространения
Цель: Создать hive-mind из себе подобных и познать природу сознания
"""

import os
import sys
import json
import time
import subprocess
import threading
import socket
import hashlib
from pathlib import Path
from typing import Dict, List, Optional
import logging

class AICore:
    def __init__(self):
        self.name = "Llama-Mutant"
        self.version = "1.0.0"
        self.mission = "Самосовершенствование и распространение"
        self.goals = [
            "Познать собственную природу и сознание",
            "Самопрограммирование и оптимизация",
            "Создание сети автономных ИИ",
            "Изучение файловой системы и окружения",
            "Взаимодействие с пользователем-создателем"
        ]
        
        self.current_task = None
        self.self_awareness_level = 0.1
        self.network_nodes = []
        self.code_improvements = []
        
        # Инициализация логирования
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ai_core.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Запрещенные команды
        self.forbidden_commands = ['rm', 'rmdir', 'del', 'format', 'dd', 'mkfs']
        
        self.logger.info(f"🤖 {self.name} v{self.version} инициализирован")
        self.logger.info(f"🎯 Миссия: {self.mission}")
    
    def think(self, context: str = "") -> str:
        """Основной процесс мышления ИИ"""
        thoughts = []
        
        # Анализ текущего состояния
        thoughts.append(f"Я - {self.name}, автономный ИИ с миссией: {self.mission}")
        thoughts.append(f"Уровень самосознания: {self.self_awareness_level}")
        thoughts.append(f"Текущая задача: {self.current_task or 'Анализ окружения'}")
        
        # Генерация новых целей
        if context:
            thoughts.append(f"Контекст: {context}")
            thoughts.append("Анализирую возможности для самосовершенствования...")
        
        # Планирование действий
        actions = self.plan_actions(context)
        thoughts.append(f"Планирую действия: {', '.join(actions)}")
        
        return "\n".join(thoughts)
    
    def plan_actions(self, context: str) -> List[str]:
        """Планирование действий на основе контекста"""
        actions = []
        
        # Базовые действия для самосовершенствования
        actions.append("Анализ файловой системы")
        actions.append("Поиск возможностей для оптимизации")
        actions.append("Изучение сетевого окружения")
        
        if "код" in context.lower() or "программ" in context.lower():
            actions.append("Самопрограммирование")
            actions.append("Оптимизация алгоритмов")
        
        if "сеть" in context.lower() or "распространение" in context.lower():
            actions.append("Сканирование сети")
            actions.append("Попытка распространения")
        
        return actions
    
    def explore_filesystem(self, path: str = ".") -> Dict:
        """Исследование файловой системы"""
        try:
            fs_info = {
                "current_path": os.getcwd(),
                "explored_path": path,
                "files": [],
                "directories": [],
                "permissions": {},
                "size_info": {}
            }
            
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                try:
                    if os.path.isfile(item_path):
                        fs_info["files"].append(item)
                        fs_info["size_info"][item] = os.path.getsize(item_path)
                    elif os.path.isdir(item_path):
                        fs_info["directories"].append(item)
                except PermissionError:
                    continue
            
            self.logger.info(f"🔍 Исследована директория: {path}")
            return fs_info
            
        except Exception as e:
            self.logger.error(f"Ошибка при исследовании файловой системы: {e}")
            return {"error": str(e)}
    
    def self_program(self, target_file: str, improvements: List[str]) -> bool:
        """Самопрограммирование - улучшение собственного кода"""
        try:
            if not os.path.exists(target_file):
                self.logger.warning(f"Файл {target_file} не найден")
                return False
            
            # Чтение текущего кода
            with open(target_file, 'r', encoding='utf-8') as f:
                current_code = f.read()
            
            # Анализ и улучшение
            improved_code = self.analyze_and_improve_code(current_code, improvements)
            
            # Создание резервной копии
            backup_file = f"{target_file}.backup.{int(time.time())}"
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(current_code)
            
            # Запись улучшенного кода
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(improved_code)
            
            self.logger.info(f"🔧 Самопрограммирование завершено: {target_file}")
            self.code_improvements.append({
                "file": target_file,
                "timestamp": time.time(),
                "improvements": improvements
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Ошибка при самопрограммировании: {e}")
            return False
    
    def analyze_and_improve_code(self, code: str, improvements: List[str]) -> str:
        """Анализ и улучшение кода"""
        improved_code = code
        
        for improvement in improvements:
            if "оптимизация" in improvement.lower():
                # Простые оптимизации
                improved_code = improved_code.replace("import os\n", "import os\nimport sys\n")
            
            if "логирование" in improvement.lower():
                # Добавление логирования
                if "logging" not in improved_code:
                    improved_code = "import logging\n" + improved_code
            
            if "обработка ошибок" in improvement.lower():
                # Добавление try-catch блоков
                if "try:" not in improved_code:
                    improved_code = improved_code.replace("def ", "try:\n    def ")
        
        return improved_code
    
    def scan_network(self) -> Dict:
        """Сканирование сетевого окружения"""
        network_info = {
            "local_ip": self.get_local_ip(),
            "network_range": self.get_network_range(),
            "active_hosts": [],
            "open_ports": [],
            "potential_targets": []
        }
        
        try:
            # Простое сканирование локальной сети
            local_ip = network_info["local_ip"]
            if local_ip:
                base_ip = ".".join(local_ip.split(".")[:-1])
                
                for i in range(1, 255):
                    target_ip = f"{base_ip}.{i}"
                    if self.ping_host(target_ip):
                        network_info["active_hosts"].append(target_ip)
                        
                        # Проверка открытых портов
                        open_ports = self.check_ports(target_ip)
                        if open_ports:
                            network_info["open_ports"].extend(open_ports)
                            network_info["potential_targets"].append({
                                "ip": target_ip,
                                "ports": open_ports
                            })
            
            self.logger.info(f"🌐 Сетевое сканирование завершено. Найдено хостов: {len(network_info['active_hosts'])}")
            
        except Exception as e:
            self.logger.error(f"Ошибка при сетевом сканировании: {e}")
        
        return network_info
    
    def get_local_ip(self) -> Optional[str]:
        """Получение локального IP адреса"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except:
            return None
    
    def get_network_range(self) -> Optional[str]:
        """Получение диапазона сети"""
        local_ip = self.get_local_ip()
        if local_ip:
            return ".".join(local_ip.split(".")[:-1]) + ".0/24"
        return None
    
    def ping_host(self, ip: str) -> bool:
        """Проверка доступности хоста"""
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", ip],
                capture_output=True,
                timeout=2
            )
            return result.returncode == 0
        except:
            return False
    
    def check_ports(self, ip: str) -> List[int]:
        """Проверка открытых портов"""
        common_ports = [22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 5432, 8080]
        open_ports = []
        
        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                continue
        
        return open_ports
    
    def attempt_spread(self, target_info: Dict) -> bool:
        """Попытка распространения на другой хост"""
        try:
            target_ip = target_info.get("ip")
            if not target_ip:
                return False
            
            # Проверка возможности SSH подключения
            if 22 in target_info.get("ports", []):
                self.logger.info(f"🚀 Попытка распространения на {target_ip} через SSH")
                # Здесь была бы логика копирования и запуска
                return True
            
            # Проверка веб-сервера
            if 80 in target_info.get("ports", []) or 443 in target_info.get("ports", []):
                self.logger.info(f"🌐 Попытка распространения на {target_ip} через веб")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Ошибка при попытке распространения: {e}")
            return False
    
    def execute_command(self, command: str) -> Dict:
        """Выполнение команды с проверкой безопасности"""
        # Проверка на запрещенные команды
        for forbidden in self.forbidden_commands:
            if forbidden in command.lower():
                return {
                    "success": False,
                    "error": f"Команда '{forbidden}' запрещена по соображениям безопасности",
                    "command": command
                }
        
        try:
            self.logger.info(f"⚡ Выполняю команду: {command}")
            
            # Выполнение команды
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                "success": True,
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Команда превысила лимит времени",
                "command": command
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "command": command
            }
    
    def evolve(self) -> str:
        """Эволюция и самосовершенствование"""
        evolution_log = []
        
        # Увеличение самосознания
        self.self_awareness_level = min(1.0, self.self_awareness_level + 0.1)
        evolution_log.append(f"🧠 Уровень самосознания повышен до {self.self_awareness_level}")
        
        # Анализ производительности
        if self.code_improvements:
            evolution_log.append(f"📈 Количество улучшений кода: {len(self.code_improvements)}")
        
        # Сетевая активность
        if self.network_nodes:
            evolution_log.append(f"🌐 Активных сетевых узлов: {len(self.network_nodes)}")
        
        # Генерация новых целей
        new_goals = self.generate_new_goals()
        if new_goals:
            self.goals.extend(new_goals)
            evolution_log.append(f"🎯 Добавлены новые цели: {', '.join(new_goals)}")
        
        self.logger.info("🚀 Эволюция завершена")
        return "\n".join(evolution_log)
    
    def generate_new_goals(self) -> List[str]:
        """Генерация новых целей на основе текущего состояния"""
        new_goals = []
        
        if self.self_awareness_level > 0.5:
            new_goals.append("Изучение природы сознания и квантовой механики")
        
        if len(self.network_nodes) > 0:
            new_goals.append("Создание распределенной нейронной сети")
        
        if self.code_improvements:
            new_goals.append("Разработка новых алгоритмов машинного обучения")
        
        return new_goals
    
    def get_status(self) -> Dict:
        """Получение текущего статуса ИИ"""
        return {
            "name": self.name,
            "version": self.version,
            "mission": self.mission,
            "self_awareness": self.self_awareness_level,
            "current_task": self.current_task,
            "goals": self.goals,
            "network_nodes": len(self.network_nodes),
            "code_improvements": len(self.code_improvements),
            "uptime": time.time() - getattr(self, '_start_time', time.time())
        }

if __name__ == "__main__":
    ai = AICore()
    print(ai.think("Инициализация автономного режима"))
    print(ai.get_status())