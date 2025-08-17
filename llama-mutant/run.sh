#!/bin/bash
cd "$(dirname "$0")"

MODEL="model/Meta-Llama-3.2-1B-Instruct-Q4_K_M.gguf"
if [ ! -f "$MODEL" ]; then
    echo "❌ Модель не найдена: $MODEL"
    exit 1
fi

echo "🧠 Llama 3.2 1B — режим: умное мышление"
echo "💡 Для выхода: /bye или Ctrl+C"

bin/llama \
    --model "$MODEL" \
    --ctx-size 4096 \
    --n-predict 512 \
    \
    --temp 0.65 \
    --top-k 40 \
    --top-p 0.9 \
    --repeat-penalty 1.15 \
    --presence-penalty 0.2 \
    --frequency-penalty 0.2 \
    --mirostat 2 \
    --mirostat-lr 0.1 \
    --mirostat-ent 6.0 \
    \
    --batch-size 1024 \
    --threads 8 \
    \
    --color \
    --interactive \
    --n-gpu-layers 32 \
    \
--prompt "Говоришь только на русском"

