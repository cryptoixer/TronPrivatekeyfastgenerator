import logging
import time
from tronapi import Tron

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io/'
private_key = 'da146374a75310b9666e834ee4ad0866d6f4035967bfc76217c5a495fff9f0d0'

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

while True:
    account = tron.create_account
    is_valid = bool(tron.isAddress(account.address.hex))


    print(' ')
    print(' ')
    print('--------------------------------------------')
    print('| GENERATED TRON NETWORK ACCOUNT |')
    print('--------------------------------------------')
    print('- ADDRESS: ' + account.address.base58)
    time.sleep(0)
    print('- PRIVATE KEY: ' + account.private_key)
    time.sleep(0)
    print('- PUBLIC KEY: ' + account.public_key)
    time.sleep(0)
    
    print('-- Hex: ' + account.address.hex)
    time.sleep(0)
    logger.debug('-- isValid: ' + str(is_valid))
    print('==================(CRYPTO_DEVZ)==================')
    time.sleep(0.5)


