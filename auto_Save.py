import os
import datetime

message = f"Auto-commit on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
os.system("git add .")
os.system(f'git commit -m "{message}"')
os.system("git push")
