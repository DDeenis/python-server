import logging;
logging.basicConfig(
    filename="debug.log", 
    level=logging.INFO, 
    format="%(asctime)s %(levelname)s [%(filename)s::%(lineno)d] %(message)s %(args)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

import _10_module

def main():
    logging.info('logger info')
    logging.error('Query error', {'query': 'select *', 'err': 'syntax error'})

if __name__ == "__main__": 
    main()