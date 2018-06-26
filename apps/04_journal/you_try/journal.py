import os

def load(name):
    """
    This method creates and loads a new journal.

    :param - name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    file_name = get_full_pathname(name)

    if os.path.exists(file_name):
        with open(file_name) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    file_name = get_full_pathname(name)
    print('...saving file to {}'.format(file_name))

    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def get_full_pathname(name):
    file_name = os.path.abspath(os.path.join('.', 'journals', name + '.jrl' ))
    return file_name

def add_entry(text, journal_data):
    journal_data.append(text)
