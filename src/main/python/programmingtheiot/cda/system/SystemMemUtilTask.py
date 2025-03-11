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

class SystemMemUtilTask(BaseSystemUtilTask):
    """
    Implementation of memory utilization monitoring task.
    """

    def __init__(self):
        super(SystemMemUtilTask, self).__init__()

    def getTelemetryValue(self) -> float:
        try:
            mem = psutil.virtual_memory()
            return mem.percent  # Retorna el porcentaje de uso de memoria
        except Exception as e:
            logging.error("Error getting memory utilization: %s", str(e))
            return None
		