import logging


def csvlogger() -> logging.Logger:
    logger = logging.getLogger("csvlogger")
    logger.setLevel(logging.DEBUG)

    # Check existing logger for not duplicating handlers
    if logger.hasHandlers():
        return logger

    cmd_h = logging.StreamHandler()
    file_h = logging.FileHandler("csvlogger.csv", encoding="utf-8")
    fmt = logging.Formatter(
        fmt='{asctime},{levelname},"{message}"', datefmt="%d-%m-%Y-%H:%M", style="{"
    )

    cmd_h.setLevel(logging.INFO)
    cmd_h.setFormatter(fmt)
    file_h.setLevel(logging.DEBUG)
    file_h.setFormatter(fmt)

    logger.addHandler(cmd_h)
    logger.addHandler(file_h)

    return logger


log = csvlogger()
