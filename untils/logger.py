from loguru import logger

logger.add(
    "logs/framework.log",
    rotation="10 MB"
)