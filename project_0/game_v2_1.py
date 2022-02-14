#from itertools import count
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    """Интервал поиска делаем на переменных, чтобы ссужать его
    в зависимости от условий сравнения больше-меньше"""
    first_val = 1 #первая переменная интервала поиска
    second_val = 101 #вторая переменная интервала поиска
            
    while True:
        count += 1
        predict_number = np.random.randint(first_val, second_val)
        
        if predict_number < number:
            first_val = predict_number #сдвигаем левую границу интервала поиска
            
            
        elif predict_number > number:
            second_val = predict_number #сдвигаем правую границу интервала поиска
            
        else:
            break
    
    return count

print(f'Количество попыток {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 10000 подходов угадывает наш алгоритм

    Args:
        random_predict([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    """загадали список из 1000 чисел, которые будем угадывать"""
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000))
    
    """перебираем список и каждое число из списка подаем в первую функцию,
        количество попыток, за которое угадали записываем в пустой список"""
    for number in random_array:
        count_ls.append(random_predict(number))
        
        """вычисляем среднее значение по массиву count_ls"""
        score = int(np.mean(count_ls))
        
        print(f'Алгоритм угадывает число в среднем за: {score} попыток')
                
        return score
    
    if __name__ == '__main__':
    score_game(random_predict)
    