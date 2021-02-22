class Solution:
    def alertNames(self, keyName, keyTime):
        name2time = {}
        for name, time in zip(keyName, keyTime):
            if name not in name2time:
                name2time[name] = []
            name2time[name].append(time)
        #print(name2time)
        ret = []
        for name in name2time:
            if len(name2time[name]) < 3:
                continue
            name2time[name] = sorted(name2time[name])
            #print(name, name2time[name])
            alerttimes = 0
            for idx, time in enumerate(name2time[name][:-2]):
                #print(idx, time)
                preH = int(name2time[name][idx][:2])
                preM = int(name2time[name][idx][3:5])
                postH = int(name2time[name][idx+2][:2])
                postM = int(name2time[name][idx+2][3:5])
                #print(preH, preM, postH, postM)
                if preH == postH:
                    ret.append(name)
                    break
                elif postH - preH == 1 and postM <= preM:
                    ret.append(name)
                    break
        ret = sorted(ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    #keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    #keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    #keyName = ["alice","alice","alice","bob","bob","bob","bob"]
    #keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
    #keyName = ["john","john","john"]
    #keyTime = ["23:58","23:59","00:01"]
    #keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
    #keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
    #keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
    #keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
    #keyName = ["a","a","a","a","a","b","b","b","b","b","b"]
    #keyTime = ["23:20","11:09","23:30","23:02","15:28","22:57","23:40","03:43","21:55","20:38","00:19"]
    keyName = ["a","a","a","a","b","b","b","b","b","b","c","c","c","c"]
    keyTime = ["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]
    ret = sol.alertNames(keyName, keyTime)
    print(ret)