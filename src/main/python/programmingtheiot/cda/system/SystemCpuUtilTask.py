#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil

from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemCpuUtilTask(BaseSystemUtilTask):
    """
    Implementation of CPU utilization monitoring task.
    """

    def __init__(self):
        super(SystemCpuUtilTask, self).__init__()

    def getTelemetryValue(self) -> float:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)  # Mide la CPU en un intervalo de 1 segundo
            return cpu_usage
        except Exception as e:
            logging.error("Error getting CPU utilization: %s", str(e))
            return None

		