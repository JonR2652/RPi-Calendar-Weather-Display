#run by ./setup.sh


#!/bin/bash

echo "Updating system packages..."
sudo apt update

echo "Installing system dependencies..."
sudo apt install -y python3-pip python3-venv python3-pil python3-numpy python3-dev python3-gpiozero git

echo "Enabling SPI interface (required for e-ink display)..."
sudo raspi-config nonint do_spi 0

echo "Setting up Python virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python packages from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete."
echo "To activate the virtual environment later, run:"
echo "source venv/bin/activate"