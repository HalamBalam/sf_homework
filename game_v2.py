import numpy as np

def random_predict(number:int = 1) -> int:
    """ Guess random number

    Args:
        number (int, optional): Random number. Defaults to 1.

    Returns:
        int: number of tries
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count

def score_game(random_predict) -> int:
    """ Average tries

    Args:
        random_predict (_type_): guess function

    Returns:
        int: average number of tries
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your function guess a number average in {score} tryes')
    
    return score
    

score_game(random_predict)