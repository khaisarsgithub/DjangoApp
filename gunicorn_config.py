# gunicorn_config.py

bind = "0.0.0.0:8000"  # Address to bind to
workers = 3  # Number of worker processes (adjust based on your CPU cores)
accesslog = "-"  # Log access to stdout
errorlog = "-"   # Log errors to stdout
timeout = 120  # Increase this if your app takes longer to start
