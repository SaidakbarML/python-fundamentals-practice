import os
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
commit_message = f"Auto-save on {now}"

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push origin main")
