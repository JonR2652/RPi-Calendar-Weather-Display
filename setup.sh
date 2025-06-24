#!/bin/bash

echo "🔧 Updating system packages..."
sudo apt update

echo "📦 Installing system dependencies..."
sudo apt install -y python3-pip python3-venv python3-pil python3-numpy python3-dev python3-gpiozero git nodejs npm

echo "🖧 Enabling SPI interface (required for Waveshare display)..."
sudo raspi-config nonint do_spi 0

# Setup Python virtual environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "✅ Python virtual environment already exists. Skipping creation."
fi

echo "📂 Activating Python virtual environment..."
source venv/bin/activate

echo "📜 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Setup Node.js dependencies
if [ -f "package.json" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
else
    echo "⚠️ No package.json found. Skipping npm install."
fi

echo "✅ All setup complete."
echo "👉 To activate your Python venv later, run:"
echo "   source venv/bin/activate"
