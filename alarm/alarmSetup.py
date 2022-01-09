#first run command "pip install python-crontab"

from crontab import CronTab
import datetime
import os

#running a command in shell might be easiest
#can be done with
#os.system('sox input.wav -b 24 output.aiff rate -v -L -b 90 48k')


with open('dateInfo.txt','a') as outFile:
    #format date and time arguments with date +"%m-%d-%y-%T"
    outFile.write('\n' + str(sys.argv[1]))

my_cron = CronTab(user='pi')
job = my_cron.new(command='python /home/jay/writeDate.py') # this folder is where the date and time will be written into

#can use something like this for loop to extract dates and stuff
#can use time delta to just add second minutes and hours to current date then setup cron job
while 1:
    date = datetime.datetime.now()
    if date.day == day_to_run and date.month == month_to_run:
        break # this breaks out of the while loop if it's the right day.
    else:
        sleep(60) #wait 60 seconds


#job.minute.on()

my_cron.write()

# can check with "crontab -l"
