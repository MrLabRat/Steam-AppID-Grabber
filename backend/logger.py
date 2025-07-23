import logging

# Create a simple logger that outputs to console
class SimpleLogger:
    def log(self, message):
        print(f"[SteamAppID] {message}")
        
    def error(self, message):
        print(f"[SteamAppID] ERROR: {message}")

# Create a singleton instance of the logger
logger = SimpleLogger()
