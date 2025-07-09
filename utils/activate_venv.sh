#!/bin/bash

# BlueFort ACM 2025 Virtual Environment Activation Script
# This script activates the virtual environment and shows the (venv) prefix

echo "🐍 Activating BlueFort ACM 2025 virtual environment..."

# Change to project directory
cd /home/upgautam/CLionProjects/BlueFortACM2025

# Activate virtual environment
source venv/bin/activate

# Show project info
echo "✅ Virtual environment activated"
echo "📁 Project: BlueFort ACM 2025"
echo "🐍 Python: $(python --version)"
echo "📦 Packages: $(pip list | wc -l) installed"
echo ""
echo "💡 Available commands:"
echo "   make python-figures  # Generate all figures"
echo "   make                 # Build LaTeX document"
echo "   make help            # Show all available commands"
echo ""

# Start bash with virtual environment active
export PS1="(venv) $PS1"
exec bash 