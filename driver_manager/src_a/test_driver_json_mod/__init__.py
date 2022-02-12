import json


# this is the function `test_driver_json_mod.format`
# this function is exported by file `setup.cfg` as the name `json` within the registry `plugin_test_driver`
def format(s):
    return json.dumps(s)
