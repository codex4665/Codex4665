#!/bin/bash

echo "🔧 إعداد بيئة CODEX v3..."

# إنشاء البيئة الافتراضية
python3 -m venv codexenv

# تفعيل البيئة وتثبيت المكتبات
source codexenv/bin/activate
pip install --upgrade pip
pip install InquirerPy termcolor distro psutil

echo ""
echo "✅ تم تثبيت كل المكتبات المطلوبة بنجاح!"
echo ""
echo "📌 لتشغيل أداة CODEX، انسخ السطور التالية 👇"

echo ""
echo "-----------------------------------------"
echo "source codexenv/bin/activate"
echo "sudo ./codexenv/bin/python3 Codex.py"
echo "-----------------------------------------"
echo ""

echo "🎉 كل حاجة جاهزة! شغّل الأداة واستمتع يا بطل 💪"
