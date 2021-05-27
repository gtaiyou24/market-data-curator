from logging import getLogger, StreamHandler, DEBUG, Formatter

log = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(Formatter("[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s"))
log.setLevel(DEBUG)
log.addHandler(handler)
log.propagate = False
