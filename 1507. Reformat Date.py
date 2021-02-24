class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        #print(day, month, year)
        month2num = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05",\
        "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11",\
        "Dec":"12"}
        #print(month2num[month])
        #print(day[:-2])
        day_ = day[:-2] if len(day[:-2])>=2 else "0"+day[:-2]
        ret = "{}-{}-{}".format(year, month2num[month], day_)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #date = "20th Oct 2052"
    #date = "6th Jun 1933"
    date = "26th May 1960"
    ret = sol.reformatDate(date)
    print(ret)