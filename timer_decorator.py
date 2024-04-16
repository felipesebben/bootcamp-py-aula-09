import time
from functools import wraps

# Decorador de medida de tempo
def time_measure_decorator(func):
    """
    Decorador de medida de tempo de execucao da funcao recebida.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funcao '{func.__name__}' executada em {end_time - start_time:.4f} segundos")
        return result
    return wrapper