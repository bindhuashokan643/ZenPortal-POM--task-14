import logging
import os

class LogGenerator:

     @staticmethod
     def loggen():

         os.makedirs("reports", exist_ok=True)

         logging.basicConfig(filename="reports\automation.log",
             format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
             datefmt="%d-%m-%Y %I:%M:%S %p",
             level=logging.INFO)
         return logging.getLogger()

