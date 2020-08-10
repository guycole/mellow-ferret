#
# Title:ferret.py
# Description: 
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging

class Ferret:
	def __init__(self, logger_level: int, configuration: dict):
		logging.basicConfig(format="%(asctime)s %(message)s", level=logger_level)

		self.logger = logging.getLogger()
		self.logger.debug("debug level message")
		self.logger.info("info level message")
		self.logger.warning("warning level message")
		self.logger.error("error level message")
		self.logger.critical("critical level message")

	def execute(self):
		print("run run")

print("start")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "config.yaml"

    logging_level = logging.DEBUG

    with open(file_name, "r") as infile:
        try:
            ferret = Ferret(logging_level, yaml.load(infile, Loader=yaml.FullLoader))
            ferret.execute()
        except yaml.YAMLError as exception:
            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
