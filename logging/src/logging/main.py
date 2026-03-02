import logging


def logger_beauty():
    # ========== CONFIG ============

    # ---------- init --------------
    logger = logging.getLogger("beauty")
    cmd_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("beauty.log", encoding="utf-8")
    fmt = logging.Formatter(
        fmt="{asctime} : {levelname} : {message}", datefmt="%d-%m-%Y-%H:%M", style="{"
    )

    # ---------- set -------------
    cmd_handler.setFormatter(fmt)
    file_handler.setFormatter(fmt)
    logger.addHandler(cmd_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger


if __name__ == "__main__":
    log = logger_beauty()
    log.info("Logger setted")
