def debug_log(path, name='logger', log=True, CRITICAL=False, ERROR=False, WARNING=False, INFO=False, NOTSET=False):
    import logging
    # CRITICAL   ERROR   WARNING   INFO   DEBUG  NOTSET
    logger = logging.getLogger('LogForTest')
    log_formatter = logging.Formatter(
        "[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s][%(lineno)d][%(message)s]")

    file_handl = logging.FileHandler(path + '/' + name)
    file_handl.setFormatter(log_formatter)
    logger.addHandler(file_handl)

    if log:
        # 是否在控制台打印
        control_handle = logging.StreamHandler()
        control_handle.setFormatter(log_formatter)
        logger.addHandler(control_handle)

    if NOTSET:
        logger.setLevel(logging.NOTSET)

    elif INFO:
        logger.setLevel(logging.INFO)

    elif WARNING:
        logger.setLevel(logging.WARNING)

    elif ERROR:
        logger.setLevel(logging.ERROR)

    elif CRITICAL:
        logger.setLevel(logging.CRITICAL)

    else:
        logger.setLevel(logging.DEBUG)

    return logger
