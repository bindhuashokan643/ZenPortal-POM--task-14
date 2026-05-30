import os
import json

class ReadJson:


    @staticmethod
    def get_config():
        project_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        json_path = os.path.join(
            project_path,
            "config",
            "config.json"
        )
        with open(json_path, "r") as file:
            return json.load(file)

