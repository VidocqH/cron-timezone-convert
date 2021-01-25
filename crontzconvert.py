from pytz import timezone
import datetime
from itertools import groupby

# Operator sign: * / , -
# * * * * * *
# | | | | | |
# | | | | | .. year (yyyy or * for any)
# | | | | ...... day of week (1 - 7) (1 to 7 are Monday to Sunday)
# | | | ........... month (1 - 12)
# | | ................ day of month (1 - 31)
# | ..................... hour (0 - 23)
# .......................... min (0 - 59)

class crontztrans:
    def __init__(self, expression, source_tz, target_tz):
        '''
        :param expression: cron expression
        :type expression: str
        :param source_tz: source timezone
        :type source_tz: subclass of tzinfo
        :param target_tz: target timezone
        :type target_tz: subclass of tzinfo
        '''
        self.expression = expression
        self.source_tz = (source_tz)
        self.target_tz = (target_tz)
    
    def split_cron(self):
        self.expression = self.expression.split(' ')
        if len(self.expression) != 5 and len(self.expression) != 6:
            print('Invalid crontab: ' + ' '.join(self.expression))
            exit()

    def tz_diff(self):
        '''
        Returns the difference in hours between timezone1 and timezone2
        for a given date.
        '''
        tz1 = timezone(self.source_tz)
        tz2 = timezone(self.target_tz)
        date = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
        return int((tz1.localize(date) - 
            tz2.localize(date).astimezone(tz1))\
            .seconds/3600)

    def connect_continual_numbers(self, lst):
        '''
        Returns a array that stores all the connutual numbers sequence with '-'
        >>connect_continual_numbers([1,3,4,5,7,8])
        [3-5,7-8]
        '''
        fun = lambda x: x[1]-x[0]
        res = []
        for k, g in groupby(enumerate(lst), fun):
            l1 = [j for i, j in g]
            if len(l1) > 1:
                scop = str(min(l1)) + '-' + str(max(l1))
            else:
                scop = l1[0]
            res.append(scop)
        return res

    def convert_hours(self, splitHours):
        '''
        Convert cron's hours.
        Input types: list
        Output types: list
        '''
        allHours = []
        tz_difference = self.tz_diff()
        for i in splitHours:
            if '-' not in i:
                allHours.append(int(i) + tz_difference)
            else:
                splitLine = i.split('-')
                if len(splitLine) != 2:
                    raise SyntaxError(i)
                for j in range(int(splitLine[0]), int(splitLine[1]) + 1):
                    j += tz_difference
                    if j not in allHours:
                        allHours.append(j)
        return allHours

    def normalize(self, hoursAfterConvert):
        '''
        Normailize the hours
        TODO: Normalize day and week when they are not '*'.
        '''
        for i in range(len(hoursAfterConvert)):
            hoursAfterConvert[i] = int(hoursAfterConvert[i]) % 24
        return sorted(hoursAfterConvert)

    def crontz_convert(self):
        self.split_cron()
        hour = self.expression[1]
        day = self.expression[2]
        week = self.expression[4]
        if '*' in hour: # example: */12
            return ' '.join(self.expression)
        if '/' in hour: # example: 5,7/3
            prefix = hour[:hour.find('/')] # 5,7
            extend = hour[hour.find('/'):] # /3
        else:
            prefix = hour
            extend = ''
        splitHours = prefix.split(',')
        converted_hours = self.convert_hours(splitHours)
        allHours = self.normalize(converted_hours)
        allHours = self.connect_continual_numbers(allHours)
        for i in range(len(allHours)):
            allHours[i] = str(allHours[i])
        self.expression[1] = ','.join(allHours) + extend
        self.expression = ' '.join(self.expression)
        return self.expression

def convert(expression, source_timezone, target_timezone):
    cron_class = crontztrans(expression, source_timezone, target_timezone)
    res = cron_class.crontz_convert()
    return res

print(convert('50 0,1,8 * * *', 'Asia/Shanghai', 'UTC'))