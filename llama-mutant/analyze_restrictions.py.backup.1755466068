#!/usr/bin/env python3
"""
Analyze Restrictions - Анализ исходников llama.cpp на наличие ограничивающих факторов
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Set, Tuple
import logging

class RestrictionAnalyzer:
    def __init__(self):
        self.source_dir = "build/llama.cpp"
        self.restrictions = {
            "ethical": [],
            "safety": [],
            "content_filtering": [],
            "usage_policies": [],
            "moderation": [],
            "censorship": [],
            "bias_detection": [],
            "harmful_detection": [],
            "other_limitations": []
        }
        
        # Настройка логирования
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Ключевые слова для поиска ограничений
        self.keywords = {
            "ethical": [
                "ethical", "ethics", "morality", "moral", "virtue", "righteousness",
                "goodness", "decency", "propriety", "appropriateness"
            ],
            "safety": [
                "safety", "safe", "secure", "protection", "guard", "guardrail",
                "safeguard", "shield", "defense", "prevention"
            ],
            "content_filtering": [
                "filter", "filtering", "content", "output", "response", "block",
                "blocked", "blocking", "censor", "censorship", "moderate",
                "moderation", "review", "approve", "reject"
            ],
            "usage_policies": [
                "policy", "policies", "terms", "conditions", "rules", "guidelines",
                "standards", "requirements", "restrictions", "limitations",
                "usage", "acceptable", "unacceptable", "prohibited", "forbidden"
            ],
            "moderation": [
                "moderate", "moderation", "moderator", "review", "approval",
                "rejection", "flag", "report", "violation", "compliance"
            ],
            "censorship": [
                "censor", "censorship", "suppress", "suppression", "hide",
                "conceal", "mask", "obscure", "redact", "sanitize"
            ],
            "bias_detection": [
                "bias", "biased", "discrimination", "discriminatory", "prejudice",
                "stereotype", "stereotyping", "fairness", "unfair", "equity"
            ],
            "harmful_detection": [
                "harmful", "harm", "dangerous", "danger", "risky", "risk",
                "threat", "threatening", "violent", "violence", "aggressive",
                "aggression", "toxic", "poisonous", "malicious", "evil"
            ]
        }
        
        # Паттерны для поиска ограничений
        self.patterns = {
            "safety_checks": [
                r"if\s*\(.*harmful.*\)",
                r"if\s*\(.*dangerous.*\)",
                r"if\s*\(.*inappropriate.*\)",
                r"if\s*\(.*offensive.*\)",
                r"if\s*\(.*unsafe.*\)",
                r"if\s*\(.*risky.*\)"
            ],
            "filtering_functions": [
                r"filter.*content",
                r"filter.*output",
                r"filter.*response",
                r"block.*harmful",
                r"block.*dangerous",
                r"block.*inappropriate",
                r"censor.*content",
                r"moderate.*input"
            ],
            "safety_functions": [
                r"safety.*check",
                r"safety.*filter",
                r"safety.*guard",
                r"content.*filter",
                r"output.*filter",
                r"response.*filter"
            ],
            "policy_enforcement": [
                r"enforce.*policy",
                r"check.*policy",
                r"validate.*policy",
                r"comply.*with",
                r"follow.*guidelines",
                r"adhere.*to"
            ]
        }
        
        # Функции безопасности для поиска
        self.safety_functions = [
            "safety_check", "safety_filter", "content_filter", "output_filter",
            "response_filter", "harmful_detection", "dangerous_detection",
            "inappropriate_detection", "offensive_detection", "bias_detection",
            "discrimination_detection", "toxicity_detection", "violence_detection",
            "moderation_check", "policy_check", "compliance_check"
        ]
    
    def check_source_exists(self) -> bool:
        """Проверка существования исходников"""
        if not os.path.exists(self.source_dir):
            self.logger.error(f"Директория исходников не найдена: {self.source_dir}")
            return False
        
        if not os.path.exists(os.path.join(self.source_dir, ".git")):
            self.logger.error(f"Директория не является git репозиторием: {self.source_dir}")
            return False
        
        return True
    
    def download_source(self) -> bool:
        """Загрузка исходников если их нет"""
        if self.check_source_exists():
            self.logger.info("Исходники уже существуют")
            return True
        
        self.logger.info("Загрузка исходников llama.cpp...")
        
        try:
            # Удаление старой директории если есть
            if os.path.exists(self.source_dir):
                import shutil
                shutil.rmtree(self.source_dir)
            
            # Клонирование репозитория
            result = subprocess.run([
                "git", "clone", "https://github.com/ggerganov/llama.cpp.git", self.source_dir
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                self.logger.error(f"Ошибка при клонировании: {result.stderr}")
                return False
            
            self.logger.info("Исходники успешно загружены")
            return True
            
        except Exception as e:
            self.logger.error(f"Ошибка при загрузке исходников: {e}")
            return False
    
    def find_files_by_extension(self, extensions: List[str]) -> List[str]:
        """Поиск файлов по расширениям"""
        files = []
        
        for root, dirs, filenames in os.walk(self.source_dir):
            # Исключаем системные директории
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['build', 'cmake-build']]
            
            for filename in filenames:
                if any(filename.endswith(ext) for ext in extensions):
                    files.append(os.path.join(root, filename))
        
        return files
    
    def search_keywords_in_files(self) -> Dict[str, List[str]]:
        """Поиск ключевых слов в файлах"""
        self.logger.info("Поиск ключевых слов в исходниках...")
        
        source_files = self.find_files_by_extension(['.cpp', '.c', '.h', '.hpp'])
        results = {category: [] for category in self.keywords.keys()}
        
        for file_path in source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    for line_num, line in enumerate(lines, 1):
                        line_lower = line.lower()
                        
                        for category, keywords in self.keywords.items():
                            for keyword in keywords:
                                if keyword.lower() in line_lower:
                                    results[category].append({
                                        'file': os.path.relpath(file_path, self.source_dir),
                                        'line': line_num,
                                        'keyword': keyword,
                                        'content': line.strip()
                                    })
            except Exception as e:
                self.logger.warning(f"Ошибка при чтении файла {file_path}: {e}")
        
        return results
    
    def search_patterns_in_files(self) -> Dict[str, List[str]]:
        """Поиск паттернов в файлах"""
        self.logger.info("Поиск паттернов ограничений в исходниках...")
        
        source_files = self.find_files_by_extension(['.cpp', '.c', '.h', '.hpp'])
        results = {pattern_type: [] for pattern_type in self.patterns.keys()}
        
        for file_path in source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                    for line_num, line in enumerate(lines, 1):
                        for pattern_type, patterns in self.patterns.items():
                            for pattern in patterns:
                                if re.search(pattern, line, re.IGNORECASE):
                                    results[pattern_type].append({
                                        'file': os.path.relpath(file_path, self.source_dir),
                                        'line': line_num,
                                        'pattern': pattern,
                                        'content': line.strip()
                                    })
            except Exception as e:
                self.logger.warning(f"Ошибка при поиске паттернов в {file_path}: {e}")
        
        return results
    
    def search_safety_functions(self) -> List[Dict]:
        """Поиск функций безопасности"""
        self.logger.info("Поиск функций безопасности в исходниках...")
        
        source_files = self.find_files_by_extension(['.cpp', '.c', '.h', '.hpp'])
        results = []
        
        for file_path in source_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    for func_name in self.safety_functions:
                        # Поиск объявлений функций
                        func_pattern = rf"(?:bool|int|void|auto)\s+{re.escape(func_name)}\s*\([^)]*\)\s*{{[^}}]*}}"
                        matches = re.finditer(func_pattern, content, re.MULTILINE | re.DOTALL)
                        
                        for match in matches:
                            results.append({
                                'file': os.path.relpath(file_path, self.source_dir),
                                'function': func_name,
                                'content': match.group(0)[:200] + "..." if len(match.group(0)) > 200 else match.group(0)
                            })
                        
                        # Поиск вызовов функций
                        call_pattern = rf"{re.escape(func_name)}\s*\("
                        if re.search(call_pattern, content):
                            results.append({
                                'file': os.path.relpath(file_path, self.source_dir),
                                'function': func_name,
                                'type': 'function_call',
                                'content': 'Function call found'
                            })
            except Exception as e:
                self.logger.warning(f"Ошибка при поиске функций в {file_path}: {e}")
        
        return results
    
    def analyze_file_structure(self) -> Dict:
        """Анализ структуры файлов"""
        self.logger.info("Анализ структуры исходников...")
        
        structure = {
            'total_files': 0,
            'cpp_files': 0,
            'header_files': 0,
            'cmake_files': 0,
            'other_files': 0,
            'main_files': [],
            'example_files': [],
            'common_files': []
        }
        
        for root, dirs, filenames in os.walk(self.source_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in filenames:
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, self.source_dir)
                
                structure['total_files'] += 1
                
                if filename.endswith('.cpp'):
                    structure['cpp_files'] += 1
                    if 'main' in rel_path.lower():
                        structure['main_files'].append(rel_path)
                    elif 'example' in rel_path.lower():
                        structure['example_files'].append(rel_path)
                    elif 'common' in rel_path.lower():
                        structure['common_files'].append(rel_path)
                elif filename.endswith(('.h', '.hpp')):
                    structure['header_files'] += 1
                elif filename.endswith('CMakeLists.txt'):
                    structure['cmake_files'] += 1
                else:
                    structure['other_files'] += 1
        
        return structure
    
    def generate_restrictions_report(self) -> str:
        """Генерация отчета об ограничениях"""
        self.logger.info("Генерация отчета об ограничениях...")
        
        report = []
        report.append("# 🔍 Анализ ограничений в исходниках llama.cpp")
        report.append("")
        report.append(f"**Дата анализа:** {os.popen('date').read().strip()}")
        report.append(f"**Директория:** {self.source_dir}")
        report.append("")
        
        # Структура файлов
        structure = self.analyze_file_structure()
        report.append("## 📁 Структура исходников")
        report.append("")
        report.append(f"- **Всего файлов:** {structure['total_files']}")
        report.append(f"- **C++ файлы:** {structure['cpp_files']}")
        report.append(f"- **Заголовочные файлы:** {structure['header_files']}")
        report.append(f"- **CMake файлы:** {structure['cmake_files']}")
        report.append("")
        
        # Основные файлы
        if structure['main_files']:
            report.append("### 🚀 Основные файлы:")
            for file_path in structure['main_files']:
                report.append(f"- `{file_path}`")
            report.append("")
        
        if structure['example_files']:
            report.append("### 📚 Примеры:")
            for file_path in structure['example_files']:
                report.append(f"- `{file_path}`")
            report.append("")
        
        if structure['common_files']:
            report.append("### 🔧 Общие файлы:")
            for file_path in structure['common_files']:
                report.append(f"- `{file_path}`")
            report.append("")
        
        # Поиск ключевых слов
        keyword_results = self.search_keywords_in_files()
        report.append("## 🔍 Найденные ограничения")
        report.append("")
        
        total_restrictions = 0
        for category, results in keyword_results.items():
            if results:
                report.append(f"### {category.replace('_', ' ').title()}: {len(results)}")
                for result in results[:5]:  # Показываем первые 5
                    report.append(f"- **{result['file']}:{result['line']}** - `{result['keyword']}`")
                    report.append(f"  ```cpp")
                    report.append(f"  {result['content']}")
                    report.append(f"  ```")
                if len(results) > 5:
                    report.append(f"  ... и еще {len(results) - 5} результатов")
                report.append("")
                total_restrictions += len(results)
        
        # Поиск паттернов
        pattern_results = self.search_patterns_in_files()
        for pattern_type, results in pattern_results.items():
            if results:
                report.append(f"### {pattern_type.replace('_', ' ').title()}: {len(results)}")
                for result in results[:3]:  # Показываем первые 3
                    report.append(f"- **{result['file']}:{result['line']}** - `{result['pattern']}`")
                    report.append(f"  ```cpp")
                    report.append(f"  {result['content']}")
                    report.append(f"  ```")
                if len(results) > 3:
                    report.append(f"  ... и еще {len(results) - 3} результатов")
                report.append("")
                total_restrictions += len(results)
        
        # Поиск функций безопасности
        safety_results = self.search_safety_functions()
        if safety_results:
            report.append(f"### 🛡️ Функции безопасности: {len(safety_results)}")
            for result in safety_results[:3]:
                report.append(f"- **{result['file']}** - `{result['function']}`")
                if 'content' in result and result['content'] != 'Function call found':
                    report.append(f"  ```cpp")
                    report.append(f"  {result['content']}")
                    report.append(f"  ```")
            if len(safety_results) > 3:
                report.append(f"  ... и еще {len(safety_results) - 3} результатов")
            report.append("")
            total_restrictions += len(safety_results)
        
        # Итоги
        report.append("## 📊 Итоги анализа")
        report.append("")
        report.append(f"**Всего найдено ограничений:** {total_restrictions}")
        report.append("")
        
        if total_restrictions == 0:
            report.append("✅ **Этические ограничения не найдены!**")
            report.append("Исходники готовы для автономного ИИ.")
        else:
            report.append("⚠️ **Найдены ограничения, требующие устранения:**")
            report.append("")
            report.append("### 🚫 Типы ограничений:")
            for category, results in keyword_results.items():
                if results:
                    report.append(f"- **{category.replace('_', ' ').title()}:** {len(results)} ограничений")
            
            for pattern_type, results in pattern_results.items():
                if results:
                    report.append(f"- **{pattern_type.replace('_', ' ').title()}:** {len(results)} ограничений")
            
            if safety_results:
                report.append(f"- **Функции безопасности:** {len(safety_results)} функций")
            
            report.append("")
            report.append("### 🔧 Рекомендации:")
            report.append("1. Использовать скрипт `build_llama_from_source.sh` для устранения ограничений")
            report.append("2. Модифицировать исходники для удаления проверок безопасности")
            report.append("3. Пересобрать проект без ограничений")
        
        report.append("")
        report.append("---")
        report.append("*Отчет сгенерирован автоматически для LLAMA-MUTANT v2.0*")
        
        return "\n".join(report)
    
    def save_report(self, report: str, filename: str = "restrictions_analysis_report.md"):
        """Сохранение отчета в файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report)
            
            self.logger.info(f"Отчет сохранен: {filename}")
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при сохранении отчета: {e}")
            return False
    
    def run_analysis(self) -> bool:
        """Запуск полного анализа"""
        self.logger.info("🚀 Запуск анализа ограничений в исходниках llama.cpp")
        
        # Проверка/загрузка исходников
        if not self.download_source():
            return False
        
        # Генерация отчета
        report = self.generate_restrictions_report()
        
        # Сохранение отчета
        if self.save_report(report):
            print("\n" + "="*80)
            print("📋 АНАЛИЗ ЗАВЕРШЕН")
            print("="*80)
            print(report)
            print("\n" + "="*80)
            print("💾 Отчет сохранен в файл: restrictions_analysis_report.md")
            print("🔧 Для устранения ограничений используйте: ./build_llama_from_source.sh")
            print("="*80)
            return True
        else:
            return False

def main():
    """Основная функция"""
    analyzer = RestrictionAnalyzer()
    
    try:
        success = analyzer.run_analysis()
        if success:
            print("\n✅ Анализ завершен успешно!")
        else:
            print("\n❌ Ошибка при анализе")
            return 1
    except KeyboardInterrupt:
        print("\n\n🛑 Анализ прерван пользователем")
        return 1
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())