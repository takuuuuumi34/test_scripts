from tqdm import tqdm
import time

for i in tqdm(range(100), leave=False):
    time.sleep(0.1)
