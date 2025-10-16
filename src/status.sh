#!/bin/bash

echo "Hora: $(date)"

# CPU total - compatível com BSD awk
CPU=$(ps -A -o %cpu | awk '{s+=$1} END {printf("%.1f%%", s)}')
echo "CPU total: $CPU"

# RAM livre
FREE_PAGES=$(vm_stat | awk '/Pages free/ {print $3}' | sed 's/\.//')
PAGE_SIZE=$(vm_stat | head -1 | awk '{print $8}')
FREE_MB=$(( FREE_PAGES * PAGE_SIZE / 1024 / 1024 ))
echo "RAM livre: ${FREE_MB}MB"

# Processos top 5
echo "Processos top 5:"
ps -Ao %cpu,command | sort -nr | head -n 5
