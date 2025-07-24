import os

def ensure_dir_exists(path):
    os.makedirs(path, exist_ok=True)

def print_progress(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = f"{100 * (iteration / float(total)):.1f}"
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

def log_console(msg):
    print(f"[INFO] {msg}")