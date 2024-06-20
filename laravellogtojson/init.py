# IMPORTING REQUIRED MODULES
import os
import re
import sys
import json

# INITITALIZING REQUIRED VARIABLES
output_json_path = 'output.json'
log_pattern      = re.compile(r'^\[(.*?)] (production|local)\.(.*?): (.*?)(\n|\r\n)')
log_data         = dict()
log_file_path    = sys.argv[1]
this_script_path = os.getcwd()

# CHECKIG IF THE FILEPATH, PASSED IN THE ARGUMENT, IS VALID OR NOT
if os.path.exists(log_file_path):
    # output_json_path = os.path.basename(log_file_path)+'.json'
    output_json_path = log_file_path+'.json'
    print (os.path.basename(log_file_path))
else:
    exit(f"Specified file not found -> {log_file_path}")
# print(output_json_path)
# raise Exception(output_json_path)
# FUNCTION TO CHECK SPECIFIC PATTERNS
def check_message(message):
    data_dict = dict({
        "SQLSTATE\[HY000] \[2002] Connection refused" : 'SQLSTATE[HY000] [2002] Connection refused',
        "Allowed memory size of" : 'Allowed memory size of ... bytes exhausted',
        "Argument 1 passed to Illuminate\\\\Database\\\\Connection::prepared\(\) must be an instance of PDOStatement" : "Argument 1 passed to Illuminate\\Database\\Connection::prepared() must be an instance of PDOStatement"
    })
    for reg,reply in data_dict.items():
        x = re.search(reg, message)
        if x:
            message = reply
            break

    return message

# READ THE LOG FILE LINE AFTER LINE AND COLLECT THE DATA AS DICTIONARY
with open(log_file_path, 'r') as log_file:
    for line in log_file: # Loop for each line in the file
        for match in log_pattern.finditer(line): # Loop for each match in the search
            message = match.group(4)
            message = check_message(message)
            test    = dict()
            test['type'] = match.group(3)

            if message in log_data:
                if 'timestamp' in log_data[message]:
                    # log_data[message]['timestamp'].append(match.group(1))
                    log_data[message]['timestamp'] = f"{log_data[message]['timestamp']}, {match.group(1)}"
            else:
                log_data[message] = test
                # test['timestamp'] = [match.group(1)]
                test['timestamp'] = match.group(1)

# DUMP THE DATA DICTIONARY TO JSON FILE AND WRITE IN THE SAME FOLDER
with open(output_json_path, 'w') as json_file:
    json.dump(log_data, json_file, indent=4)

print(f"Loge collected as JSON and stored in -> {this_script_path}/{output_json_path}")


# OPUTPUT JSON STRUCTURE
# {
#     '<error_msg>':{
#         '<type>': 'ERROR/WARNING',
#         '<timestamp>':[
#             "2023-08-22 10:44:01",
#             "2023-08-22 10:44:02",
#         ]
#     }
# }