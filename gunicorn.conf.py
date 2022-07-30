# -*- coding: utf-8 -*-
"""
Gunicorn with Uvicorn config to launch in Digital Ocean's App Platform.
"""
bind = "0.0.0.0:8000"
workers = 2
# Uvicorn's Gunicorn worker class
worker_class = "uvicorn.workers.UvicornWorker"
pythonpath = "./src"
