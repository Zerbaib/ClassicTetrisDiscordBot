from src.build.creator import Creator
from src.data.var import init_time
from datetime import datetime
from src.utils.logger import Log

class main:
    def __init__(self):
        init_time(datetime.now())
        Creator()

if __name__ == '__main__':
    main()