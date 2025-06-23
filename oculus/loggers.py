import sys
from datetime import datetime
import inspect


def log_debug(context: str, message: str) -> None:
    """

    :param context: контекст сообщения (прим.: "вычисление вектора мнений")
    :param message: сообщение (прим.: "промежуточное значение 21")
    :return:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print(timestamp, '\t', 'DEBUG', '-', context, '-', message)


def log_info(context: str, message: str) -> None:
    """

    :param context: контекст сообщения (прим.: "вычисление вектора мнений")
    :param message: сообщение (прим.: "вычислено")
    :return:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print(timestamp, '\t', 'INFO', '-', context, '-', message, '-', 'CALLED BY:  ', str(inspect.stack()[1].function))
    # print(timestamp, '\t', 'INFO', '-', context, '-', message)


def log_warning(context: str, message: str) -> None:
    """

    :param context: контекст сообщения (прим.: "вычисление вектора мнений")
    :param message: сообщение (прим.: "уже выполнено 1000 итераций")
    :return:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print(timestamp, '\t', 'WARNING', '-', context, '-', message)


def log_error(context: str, message: str) -> None:
    """

    :param context: контекст сообщения (прим.: "вычисление вектора мнений")
    :param message: сообщение (прим.: "возникла непредвиденная ошибка")
    :return:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print(timestamp, '\t', 'ERROR', '-', context, '-', message, file=sys.stderr)


def log_fatal(context: str, message: str) -> None:
    """

    :param context: контекст сообщения (прим.: "вычисление вектора мнений")
    :param message: сообщение (прим.: "возникла непредвиденная ошибка")
    :return:
    """
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    print(timestamp, '\t', 'FATAL', '-', context, '-', message, file=sys.stderr)
