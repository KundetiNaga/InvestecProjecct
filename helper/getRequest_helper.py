import json

from invest.coms.common_functions.common_functions import readJsonFile, find
from invest.coms.common_functions.path_configs import PathConfigs


class InvestecHelper:
    def verifyJsonResponseData(self,param1,param2):
        try:
            body = readJsonFile(PathConfigs.investec_json_rd_file_path)
            print(body)
            json_lst = json.loads(body)
            jsonResponseName = list(find(param1, json_lst))[2]
            jsonResponseColor = list(find(param2, json_lst))[2]
            print(jsonResponseName,jsonResponseColor)
            return str(jsonResponseName),str(jsonResponseColor)
        except Exception as e:
            print('exception message :', e)