import P_Logger
import P_Person as person


def start():
    P_Logger.logger.info("test")
    test = person.P_Person("test", 1)
    test.getPerson()


if __name__ == '__main__':
    start()
