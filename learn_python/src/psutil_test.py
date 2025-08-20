import psutil

cpu_percent = psutil.cpu_percent()
mem_used = psutil.virtual_memory().percent

print(f"系统负载：{cpu_percent} {mem_used}")

