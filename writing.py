from calendar import Calendar
"""
this is for writing
"""
class Writing:
    def __init__(self, year=2024, month=11):
        self.year = year
        self.month = month
        self.row = []
        self.colume = []
        self.start = 8
        self.end = 16
        self.hour_worker = {}
        self.shift = {}
        self.list = []


    def get_key(self, year=2024, month=11):
        c = Calendar()
        empty_calendar = c.monthdays2calendar(self.year, self.month)

        #delete day 0
        new_calendar = []
        for i in range(len(empty_calendar)):
            for j in range(7):
                if empty_calendar[i][j][0]  != (0):
                        new_calendar.append(empty_calendar[i][j])
            
         #use for write the row on the file
        key_title = []
        for i in range(len(new_calendar)):
           key_title.append(new_calendar[i][0])
        key_title.insert(0, "time")
        self.row = key_title

        return self.row
    
    #colume == hours interval
    def get_colume(self, start=8, end=16):
        working_hr = self.end - self.start
        w_hour = []
        for i in range(working_hr):
            w_hour.append(f"{self.start + i:02} - {self.start + i + 1:02}")
        self.colume = w_hour
        return self.colume
 
    #a dic of {key=hour: value=worker}
    def create_a_dic_hour_and_worker(self):
        hour_and_worker = {}
        for i in range(len(self.colume)):
            colume_string = f"{self.start + i:02} - {self.start + i + 1:02}"
            #None is for temparary, it should be who will work in this time 
            hour_and_worker.update({colume_string: None})
        self.hour_worker = hour_and_worker
        return self.hour_worker

  
    #make a list including dictionary
    def make_a_shift(self):
        shift = {}
        #how many dic in shift[]
        shift.update({self.row[0] : None})
        for i in range(len(self.row)-1):
            #add key in dictionary shift[i]
            shift.update({self.row[1+i] : self.hour_worker})
        self.shift = shift
        return shift

    def make_a_list(self):
        list = []
        for i in range(len(self.row)):
            list.append(self.hour_worker)
        self.list = list
        return self.list
    

def main():
    shift = Writing()
    shift.get_key(2024, 11)
    shift.get_key()
    shift.get_colume()
    shift.create_a_dic_hour_and_worker()
    print(shift.make_a_list())

    #print(shift.make_a_shift())


if __name__ == "__main__":
    main()


