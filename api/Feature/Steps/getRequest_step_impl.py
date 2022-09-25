import json
import os

import requests
from behave import *

from invest.coms.common_functions.path_configs import PathConfigs
from invest.helper.getRequest_helper import InvestecHelper

responseobj = InvestecHelper()

@given('the environment is ready for testing')
def step_impl(context):
    print(" The build is ready for testing")

@when('the get request is send on the "{url}"')
def step_impl(context,url):
    global response
    urls = url
    response = requests.get(url)

@then('the request is successful with the 200 message in the response')
def step_impl(context):
    try:
        if response.status_code == 200:
            responseData = response.json()
            formatted_json_response = json.dumps(responseData, indent=4, sort_keys=True)
            # write the response into a file
            with open(os.path.join(PathConfigs.targetDataPath, 'investecApi.json'), "w") as text_file:
                print(formatted_json_response, file=text_file)
            assert True
        else:
            print('')
            assert False

    except Exception as e:
        print('exception msg', e)

@then('verify R2-D2 skin color is white and blue in the response')
def step_impl(context):
    param1 = 'name'
    param2 = 'skin_color'
    result = responseobj.verifyJsonResponseData(param1,param2)
    if result[0] == 'R2-D2':
        print('Expected R2-D2 skin_color is : ', result[1] )
        assert True
        if result[1] == 'white, blue':
            assert True
        else:
            assert False
    else:
        assert False
