import logging
import os

class LogGen:

    @staticmethod
    def loggen():

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d/%m/%Y %I:%M:%S %p",
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()

        return logger