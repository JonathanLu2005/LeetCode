class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        # round every 15 min
        # start at 00:00
        # given login and logout
        # if logout < login, mean played a whole day
        # return number of chess rounds played

        # if 1 hour apart, then we need to really consider mintues
        # e.g 60 - 31 = 29 // 15 = 1
        # else hour between iscalm

        loginHour, loginMinute = loginTime.split(":")
        logoutHour, logoutMinute = logoutTime.split(":")
        loginHour = int(loginHour)
        loginMinute = int(loginMinute)
        logoutHour = int(logoutHour)
        logoutMinute = int(logoutMinute)
        rounds = 0
        hours = 0

        if loginHour > logoutHour:
            hours = (24-loginHour) + logoutHour - 1
        elif logoutHour > loginHour:
            hours = logoutHour - loginHour - 1
        elif logoutMinute < loginMinute:
            hours = 23

        rounds += (hours * 4)

        if loginHour != logoutHour or logoutMinute < loginMinute:
            print("her1e")
            rounds += (60 - loginMinute) // 15
            rounds += (logoutMinute) // 15
        else:
            print("here")
            loginRemainder = loginMinute % 15
            if loginRemainder != 0:
                loginMinute += (15 - loginRemainder)

            logoutMinute -= (logoutMinute % 15)

            print(loginMinute)
            print(logoutMinute)

            rounds += max((logoutMinute - loginMinute) // 15,0)

        return rounds
        

    