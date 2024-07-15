from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print()
print('ft_tqdm')
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
print('tqdm1')
for elem in tqdm(range(333)):
    sleep(0.005)
print()
print('tqdm2')
for elem in tqdm(range(333)):
    sleep(0.005)
print()
