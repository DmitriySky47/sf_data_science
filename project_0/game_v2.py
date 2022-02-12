from itertools import count
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #Предполагаемое число
        if number == predict_number:
            break
    return count
print(f'Количество попыток {random_predict()}')
