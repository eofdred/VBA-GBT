#!/bin/bash
# Move to the project root directory where package.json lives
cd "$(dirname "$0")/.."
echo "Senkronizasyon başlatılıyor (npx quartz sync)..."
npx quartz sync
echo ""
echo "Senkronizasyon işlemi bitti!"
echo "Çıkmak için Enter tuşuna basın..."
read
