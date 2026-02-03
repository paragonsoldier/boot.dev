from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)


def get_csv_status(status, data):
    match (status):
        case (CSVExportStatus.PENDING):
            converted_data = list(map(lambda x: list(map(lambda y: str(y), x)), data))
            return ("Pending...", converted_data)
        case (CSVExportStatus.PROCESSING):
            converted_data = "\n".join(list(map(lambda x: ",".join(x), data)))
            return ("Processing...", converted_data)
        case (CSVExportStatus.SUCCESS):
            return ("Success!", data)
        case (CSVExportStatus.FAILURE):
            converted_data = list(map(lambda x: list(map(lambda y: str(y), x)), data))
            converted_data = "\n".join(list(map(lambda x: ",".join(x), converted_data)))
            return ("Unknown error, retrying...", converted_data)
        case _:
            raise Exception("unknown export status")

