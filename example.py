from random import randint, random
# import


def function_with_noise():
    '''função y = 2x'''
    noise_value_x = random()
    noise_value_y = random()
    x = randint(0, 7) + noise_value_x
    y = 2*x + noise_value_y
    return x, y


def createDataset(number_of_examples):
    examples_X = []
    examples_Y = []
    for i in range(number_of_examples):
        x, y = function_with_noise()
        examples_X.append(x)
        examples_Y.append(y)
    return examples_X, examples_Y


print(createDataset(5))
