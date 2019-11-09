import csv

print('school info. :p')


class School(object):
    def __init__(self, name, num_of_sat_test_takers, 
                 sat_critical_reading_avg_score, 
                 sat_math_avg_score,
                 sat_writing_avg_score):
        self.name = name
        if ('s' != num_of_sat_test_takers):
            self.num_of_sat_test_takers = int(num_of_sat_test_takers)
            self.sat_critical_reading_avg_score = int(sat_critical_reading_avg_score)
            self.sat_math_avg_score = int(sat_math_avg_score)
            self.sat_writing_avg_score = int(sat_writing_avg_score)
            self.sum_score = self.sat_critical_reading_avg_score + self.sat_math_avg_score + self.sat_writing_avg_score
            if self.sat_critical_reading_avg_score > self.sat_writing_avg_score:
                self.math_mind_score = self.sat_math_avg_score / self.sat_critical_reading_avg_score
            else:
                self.math_mind_score = self.sat_math_avg_score / self.sat_writing_avg_score
        else:
            self.num_of_sat_test_takers = 0
            self.sat_critical_reading_avg_score = 0
            self.sat_math_avg_score = 0
            self.sat_writing_avg_score = 0
            self.sum_score = 0
            self.math_mind_score = 0

    def __lt__(self, other):
        if self.math_mind_score < other.math_mind_score:
            return True
        return False

    def __str__(self) -> str:
        return super().__str__()

    # def get_math_mind_score(self):
    #     if self.sat_critical_reading_avg_score > self.sat_writing_avg_score:
    #         return self.sat_math_avg_score / self.sat_critical_reading_avg_score
    #     else:
    #         return self.sat_math_avg_score / self.sat_writing_avg_score

    def print(self):
        print("school name: " + self.name)
        print("\tnum_of_sat_test_takers:         ", self.num_of_sat_test_takers)
        print("\tsat_critical_reading_avg_score: ", self.sat_critical_reading_avg_score)
        print("\tsat_math_avg_score:             ", self.sat_math_avg_score)
        print("\tsat_writing_avg_score:          ", self.sat_writing_avg_score)
        print("\tsum_score:                      ", self.sum_score)
        print("\tmath_mind_score:                ", self.math_mind_score)


# function: read scv
def read_csv(file_name):
    dict_reader = csv.DictReader(open(file_name, "r"))
    cols = dict_reader.fieldnames

    list = []
    for row in dict_reader:
        list.append(School(row[cols[1]], row[cols[2]], row[cols[3]], row[cols[4]], row[cols[5]]))
    return list


if __name__ == '__main__':
    school_list = read_csv("2012_SAT_Results.csv")
    minimum = school_list[0]
    maximum = school_list[0]

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    

    for school in school_list:
        if school.sum_score == 0:
            continue
        if school.sum_score > maximum.sum_score:
            maximum = school
        if school.sum_score < minimum.sum_score:
            minimum = school

        if school.num_of_sat_test_takers <= 100:
            num1 += 1
            sum1 += school.sum_score 
            
        elif school.num_of_sat_test_takers <= 200:
            num2 += 1
            sum2 += school.sum_score 
            
        elif school.num_of_sat_test_takers <= 500:
            num3 += 1
            sum3 += school.sum_score 
            
        elif school.num_of_sat_test_takers <= 1000:
            num4 += 1
            sum4 += school.sum_score 
            
        else:
            num5 += 1
            sum5 += school.sum_score 
           


    print(minimum.print())
    print(maximum.print())
    print("Test taker size from 0 to 100:    ",sum1/num1)
    print("Test taker size from 1000 to 200: ",sum2/num2)
    print("Test taker size from 200 to 500:  ",sum3/num3) 
    print("Test taker size from 500 to 1000: ",sum4/num4) 
    print("Test taker size from 1000:        ",sum5/num5)

    school_list_new = sorted(school_list, reverse=True)
    print(school_list_new[0].print())
    print(school_list_new[1].print())
    print(school_list_new[2].print())
    print(school_list_new[3].print())
    print(school_list_new[4].print())
    
cor_score = [sum1/num1,sum2/num2,sum3/num3,sum4/num4,sum5/num5]
cor_taker = [1,2,3,4,5]

import matplotlib.pyplot as plt
plt.plot(cor_score)