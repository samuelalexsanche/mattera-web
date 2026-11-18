#!/bin/sh
# Instala los hooks de git del repo. Se corre una vez por clon.
set -e
raiz=$(git rev-parse --show-toplevel)
for h in "$raiz"/tools/hooks/*; do
  nombre=$(basename "$h")
  cp "$h" "$raiz/.git/hooks/$nombre"
  chmod +x "$raiz/.git/hooks/$nombre"
  echo "instalado: .git/hooks/$nombre"
done
