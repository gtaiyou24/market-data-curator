from __future__ import annotations

from enum import Enum

from others import log, notice

LOG_FORMAT_WITHOUT_STACK_TRACE = "[Code] {} [Message] {} [Detail] {}"
LOG_FORMAT_WITH_STACK_TRACE = "[Code] {} [Message] {} [Detail] {} [Trace] {}"


class ErrorLevel(Enum):
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRIT = 'CRITICAL'

    def to_logger(self, error_code: ErrorCode, detail: str):
        msg = LOG_FORMAT_WITH_STACK_TRACE.format(error_code.name, error_code.message, detail)

        if self == ErrorLevel.WARN:
            log.warn(msg)
        elif self == ErrorLevel.ERROR:
            log.error(msg)
        elif self == ErrorLevel.CRIT:
            log.critical(msg)
            notice.post(msg)
        else:
            log.info(msg)


class ErrorCode(Enum):
    MARKET_1001 = ("500系エラーが発生しました。", ErrorLevel.CRIT)
    MARKET_1002 = ("400系エラーが発生しました。", ErrorLevel.CRIT)
    MARKET_2001 = ("タイムアウトが発生しました。", ErrorLevel.WARN)

    def __init__(self, message: str, error_level: ErrorLevel):
        self.message = message
        self.error_level = error_level

    def log(self, detail: str):
        self.error_level.to_logger(self, detail)
