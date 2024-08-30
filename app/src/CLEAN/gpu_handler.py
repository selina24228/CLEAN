import subprocess
import re

def get_free_gpus():
    result = subprocess.run(['nvidia-smi', '--query-gpu=index,memory.free', '--format=csv,noheader,nounits'],
                            stdout=subprocess.PIPE, text=True)
    gpu_info = result.stdout.strip().split('\n')
    gpu_info = [tuple(map(int, re.split(r',\s+', gpu.strip()))) for gpu in gpu_info]
    gpu_info.sort(key=lambda x: x[1], reverse=True)  # Sort by free memory in descending order
    
    for gpu in gpu_info:
        print(f"GPU {gpu[0]}: {gpu[1]} MB free")
    
    return gpu_info

def get_best_gpu():
    free_gpus = get_free_gpus()
    best_gpu = free_gpus[0][0] if free_gpus else None
    return best_gpu
