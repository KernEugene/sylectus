import time
import sylectus
import os

counter = 0
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cms.csv')


while counter != 4:
    sylectus.main()
    time.sleep(20)
    counter += 1
    if counter == 4:
        sylectus.send_test_mail()
        counter = 0
        os.remove(path)
        print('sss')