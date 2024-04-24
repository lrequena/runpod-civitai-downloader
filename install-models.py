#!/usr/bin/env python3
from pathlib import Path

# Define the path for the token file
TOKEN_FILE = Path.home() / '.civitai' / 'config'

# Define your API token
api_token = "e84a2551ef9fbe85b9ff8ba958ba7987"

# Function to store the token
def store_token(token: str):
    TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(TOKEN_FILE, 'w') as file:
        file.write(token)

# Call the function to store the token
store_token(api_token)

import subprocess

download_script_url = "https://raw.githubusercontent.com/lrequena/runpod-civitai-downloader/main/download.py"

# Define the commands as a list of lists
commands = [
    ["wget", download_script_url],
    ["mv", "download.py", "/usr/local/bin/download-model"],
    ["chmod", "+x", "/usr/local/bin/download-model"],
    ["download-model", "https://civitai.com/api/download/models/399640", "/workspace/stable-diffusion-webui/models/Stable-diffusion"],
    ["download-model", "https://civitai.com/api/download/models/370979", "/workspace/stable-diffusion-webui/models/Stable-diffusion"],
    ["download-model", "https://civitai.com/api/download/models/290640", "/workspace/stable-diffusion-webui/models/Stable-diffusion"],
    ["download-model", "https://civitai.com/api/download/models/244808", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/152309", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/31515", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/323936", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/16657", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/10976", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/131364", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/447878", "/workspace/stable-diffusion-webui/models/Lora"],
    ["download-model", "https://civitai.com/api/download/models/422554", "/workspace/stable-diffusion-webui/models/Lora"]
]

# Execute each command
for cmd in commands:
    result = subprocess.run(cmd, check=True, text=True, capture_output=True)
    print("Command executed:", ' '.join(cmd))
    print("Output:", result.stdout)
    print("Errors:", result.stderr)
    print("-" * 60)
