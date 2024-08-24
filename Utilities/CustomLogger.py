import logging
import datetime

def logger():
    timestamp = datetime.datetime.now().strftime("%d_%m_%y-%H_%M_%S")
    file_path=r"../Logs/log_"+timestamp+".txt"
    logging.basicConfig(handlers=[logging.FileHandler(filename=file_path, mode="w"),
                                  logging.StreamHandler()],
                        level=logging.INFO,
                        format="%(asctime)s::%(levelname)s::%(message)s",
                        force=True)
    return logging

