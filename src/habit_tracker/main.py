import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

logger.debug("messaggio debug")
logger.info("messaggio info")
logger.warning("messaggio warning")