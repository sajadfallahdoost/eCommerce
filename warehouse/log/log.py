import threading


class SingletonLogger:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonLogger, cls).__new__(cls)
                cls._instance.log_file = "admin_activity.log"  # Log file
        return cls._instance

    def log(self, message: str):
        # Append the log message to the file
        with open(self.log_file, "a") as f:
            f.write(message + "\n")
