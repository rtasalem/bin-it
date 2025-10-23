#!/usr/bin/env bash
set -e

source venv/bin/activate
watchmedo auto-restart --pattern="*.py" --recursive python main.py

