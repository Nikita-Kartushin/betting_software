import logging


def configure_logger(app_name="app", logs_path="logs/log.txt"):
    file_handler = logging.FileHandler(logs_path)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, logging.StreamHandler()],
        format='%(asctime)s [%(levelname)s] %(filename)s %(message)s'
    )

    _logger = logging.getLogger(app_name)
    return _logger


def redirect_logs(func):
    def wrapper(_logger):
        try:
            logger.info('Start service')
            result = func()
            return result
        except KeyboardInterrupt as e:
            logger.warning('Stop Service')
        except Exception:
            logger.error('Fatal error', exc_info=True)

    return wrapper


logger = configure_logger()
