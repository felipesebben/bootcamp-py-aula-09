from loguru import logger
from sys import stderr
from functools import wraps

# logger.remove()
# Criar logs especificos para cada saida da aplicacao
logger.add(

    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(

    "meu_arquivo_de_logs.log",
    format="{time} {level} {message} {file}",
    level="INFO"
)

logger.add(

    "meu_arquivo_de_logs_critical.log",
    format="{time} {level} {message} {file}",
    level="CRITICAL"
)
logger.add(

    "meu_arquivo_de_logs_error.log",
    format="{time} {level} {message} {file}",
    level="ERROR"
)

def log_decorator(func):
    """
    Decorador para ser usado para retornar logs nas funcoes.
    
    Args:
    `func` - funcao a ser usada
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando funcao '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Funcao '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Excecao capturada em '{func.__name__}' : {e}")
            raise # Re-lancar a excecao para nao alterar o comportamento da funcao decorada
    return wrapper
