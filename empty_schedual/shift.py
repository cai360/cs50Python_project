

class Shift():
    def __init__(self, start = 8, end = 16):
        self.start = start
        self.end = end

    def generate(self, start, end, interval = 1):
        working_hr = self.end - self.start
        w_hour = []
        for i in range(working_hr):
            colume_string = f"{self.start + i:02} - {self.start + i + 1:02}"
            #None is for temparary, it should be who will work in this time 
            w_hour.append({colume_string: None})
        return(w_hour)
        




def main():
    shift = Shift()
    print(shift.generate(8, 16))

if __name__ == "__main__":
    main()