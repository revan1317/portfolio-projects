import time
import schedule

def biep():
    print("Biep!")

schedule.every().minute.at(":00").do(biep)

while True:
    schedule.run_pending()
    time.sleep(1)
    