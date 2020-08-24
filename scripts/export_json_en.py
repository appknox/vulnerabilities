import json
import os


def generate_translation_json():
    os.chdir('vulnerabilities')
    folder_names = sorted(os.listdir('.'))
    vulnerabilities = []
    file_names = os.listdir(folder_names[0])
    for folder_name in folder_names:
        vulnerability = {}
        vulnerability['vulnerability_id'] = int(folder_name.split('_')[0])
        for file_name in file_names:
            file_handle = open(os.path.join(folder_name, file_name), 'r')
            field_name = file_name.split('.')[0]
            vulnerability[field_name] = file_handle.read()
            file_handle.close()
        vulnerabilities.append(vulnerability)
    with open('../appknox_vulnerabilities_en.json', 'w') as f:
        json.dump(vulnerabilities, f)


if __name__ == '__main__':
    generate_translation_json()
