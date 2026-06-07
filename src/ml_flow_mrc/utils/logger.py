
import logging
import time
from colorama import Fore, Style, init

# Initialize colorama (needed for Windows)
init(autoreset=True)

# New level
NOTICE_LEVEL = 25
logging.addLevelName(NOTICE_LEVEL, "NOTICE")
class Logger:

    """
    A simple logging utility with colorized console output.

    Provides convenience methods for logging messages at different
    severity levels, with optional color formatting for readability.
    """

    def __init__(self) -> None:
        """
        Initialize the Logger instance.

        Sets up a console handler with a custom formatter and attaches
        it to the root logger.
        """
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Custom formatter
        formatter = logging.Formatter("%(asctime)s | %(levelname)-6s | %(message)s")
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def debug(self, msg: str) -> None:
        """
        Log a debug-level message.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.debug(Fore.WHITE + msg + Style.RESET_ALL)

    def info(self, msg: str) -> None:
        """
        Log an info-level message in white.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.info(Fore.WHITE + msg + Style.RESET_ALL)

    def info_color(self, msg: str) -> None:
        """
        Log an info-level message in cyan.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.info(Fore.CYAN + msg + Style.RESET_ALL)

    def header(self, msg: str) -> None:
        """
        Log a header-style message surrounded by green hash lines.

        Parameters
        ----------
        msg : str
            The header text to log.

        """
        self.logger.info(Fore.GREEN + "#" * 30 + Style.RESET_ALL)
        self.logger.info(Fore.GREEN + msg + Style.RESET_ALL)
        self.logger.info(Fore.GREEN + "#" * 30 + Style.RESET_ALL)

    def notice(self, msg: str) -> None:
        """
        Log a custom notice-level message in yellow.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.log(NOTICE_LEVEL, Fore.YELLOW + msg)

    def warning(self, msg: str) -> None:
        """
        Log a warning-level message in yellow.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.warning(Fore.YELLOW + msg + Style.RESET_ALL)

    def error(self, msg: str) -> None:
        """
        Log an error-level message in red.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.error(Fore.RED + msg + Style.RESET_ALL)

    def critical(self, msg: str) -> None:
        """
        Log a critical-level message in magenta.

        Parameters
        ----------
        msg : str
            The message to log.

        """
        self.logger.critical(Fore.MAGENTA + msg + Style.RESET_ALL)


def log_run_time(start: float) -> float:
    """Calculate and log the elapsed runtime since a given start timestamp."""
    running_time = time.time() - start
    logg.info(f"Running time: {running_time:.2f} seconds")
    return running_time


logg = Logger()
