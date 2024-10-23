import csv
import schedual2

def main():

    s = schedual2.Schedual()
    s.get_key()
    s.get_colume()
    s.create_a_dic_hour_and_worker()
    with open("shift.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(s.make_a_list())
        
        # writer = csv.DictWriter(file, fieldnames = s.get_colume())
        # s.create_a_dic_hour_and_worker()
        # writer.writerow(s.make_a_list)

main()                               

