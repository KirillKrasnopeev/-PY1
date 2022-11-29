import json
INPUT_FILE = "output.csv"
def csv_to_list_dict(file):
    with open(file, 'r') as f:
        output = []
        lines = f.read().splitlines()
        column_names = lines[0].split(',')
        for index_line, line in enumerate(lines):
            a = dict()
            if index_line == 0:
                continue
            entries = line.split(',')
            for index_r, column_name in enumerate(column_names):
                a[column_name] = entries[index_r]
            output.append(a)
    return output
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
