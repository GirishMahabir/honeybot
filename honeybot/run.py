import logging
import sys

from honeybot.main import Bot_core

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    # logger.debug("debug message")
    # logger.info("info message")
    # logger.warning("warn message")
    # logger.error("error message")
    # logger.critical("critical message")
    try:
        x = Bot_core()
        x.unregistered_run()
    except KeyboardInterrupt:
        print('interrupted')
        sys.exit()