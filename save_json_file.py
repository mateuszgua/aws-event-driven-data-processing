def save_json_file(json_object):
    with open("./data/sample.json", "w") as outfile:
        outfile.write(json_object)
