import logging

# logging settings
logging.basicConfig(            # overwrite each time
    level=logging.DEBUG,          # capture all levels from DEBUG and up
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # fixed "message"
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('arthimeticApp')

def add(a,b):
    result = a+b
    logger.debug(f'adding {a} and {b} {result}')
    return result

def substract(a,b):
    result = a-b
    logger.debug(f'substracting is happening')
    return result

def multiply(a,b):
    result = a*b
    logger.debug('multiplication is happening ')
    return result

def divider(a,b):
    try:
        result = a/b
        logger.debug(' divifing is happening')
        return result
    except ZeroDivisionError:
        logger.error('zerp divivsoon error')
        return None
    

add(10,14)
substract(10,12)
multiply(23,23)
divider(20,0)
