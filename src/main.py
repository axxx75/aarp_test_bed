# src/main.py
import sys
import json
# import inesistente per test
from non_existent_module import magic_function

from utils import format_message, compute_sum
from database import Database

def load_config(path="config.yaml"):
    import yaml
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    cfg = load_config("../config.yaml")
    # bug logico: controllo errato su chiave mancante (usa 'environment' ma config la rimuove)
    if cfg.get("app").get("environment") == "production":
        print("Running in production mode")
    else:
        print("Running in non-production mode")

    db = Database()
    # bug logico: compute_sum ritorna stringa in alcuni casi, qui ci aspettiamo int
    result = compute_sum([1, 2, 3])
    message = format_message("Sum result is: " + result)
    print(message)

if __name__ == "__main__":
    main()

