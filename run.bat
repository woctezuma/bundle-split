@echo off
CALL .venv\Scripts\activate
python run_workflow.py --bundle %1
CALL deactivate
