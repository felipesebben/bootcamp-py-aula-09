from loguru import logger

# Exemplos de mensagens padrao que podemos desenvolver com logger do loguru.


logger.debug("Aviso para o desenvolvedor no futuro (no caso, eu)")
logger.info("Esta e' uma informacao importante no processo")
logger.warning("Informacao de que algo podera ser depreciado no futuro ou parar de funcionar!")
logger.error("Erro: aconteceu uma falha")
logger.critical("Ocorreu algo que aborta a aplicacao")