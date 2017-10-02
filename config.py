import configparser


class Config:
    parser = configparser.ConfigParser()

    @staticmethod
    def ready() -> bool:
        return len(Config.parser.sections()) > 0

    @staticmethod
    def get(section) -> dict:
        dict1 = {}
        options = Config.parser.options(section)
        for option in options:
            try:
                dict1[option] = Config.parser.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
