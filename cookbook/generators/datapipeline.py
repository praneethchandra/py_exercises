import configparser

CONFIG_FILE_NAME = "/home/pgone/py/py_exercises/config/project_env.cfg"

def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_NAME)
    file_name = config['DEFAULT']['DATA_SET_FILE_NAME']

    # generator 1
    lines = (line for line in open(file_name, 'r'))
    # generator 2
    list_line = (s.rstrip().split(",") for s in lines)
    # call generator next to fetch first row which is column names
    cols = next(list_line)
    # create dictionary
    company_dicts = (dict(zip(cols, data)) for data in list_line)

    # generator 3
    funding = (
        int(company_dict["raisedAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )

    '''
    you aren't iterating through all these at once in the generator expression. In fact you aren't iterating through anything
    until you actually use for loop or a function that works on iterables like sum(). Calling sum would iterate through generators
    '''
    total_series_a = sum(funding)
    print(f"Total series A fundraising: ${total_series_a}")

if __name__ == '__main__':
    main()