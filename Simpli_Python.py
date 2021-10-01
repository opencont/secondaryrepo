pace_length = 0.714285714

class Person():
    def __init__ (self, name, age, sex, weight, height):
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.weight, self.unit_weight = weight.split(' ')
        self.height, self.unit_height = height.split(' ')
        self.weight = float(self.weight)
        self.height = float(self.height)

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getsex(self):
        return self.sex

    def getweight(self):
        return self.weight

    def getheight(self):
        return self.height

    def getBMI(self):
        if self.unit_weight.lower() == "kg":
            BMI =  self.weight/((self.height/100) ** 2)
        else:
            BMI = (self.weight/(self.height ** 2))*703

        print("Your BMI is {0:.2f}".format(BMI))
        if BMI > 25:
            print("You should lose some weight.")
        elif BMI < 18.5:
            print("You should put on some weight.")
        else:
            print("Congrats on your hardwork, you are fit !!")

def get_time(time):
    hour, min, sec = time.split(':')
    time_in_hour = int(hour)+(int(min)/60)+(int(sec)/3600)
    return time_in_hour
    

def gen_stats(days, steps, time):
    
    max_distance = 0.0
    max_speed = 0.0
    
    min_distance = float("inf")
    min_speed = float("inf")
    
    avg_distance = 0.0
    avg_speed = 0.0
    
    weeks = []
    months = []
    
    missed_week = []
    missed_days = 0
    
    for i in range(len(days)):
        if steps[i] > 0 :
            distance = (steps[i]/1000) * pace_length
            max_distance = max(distance, max_distance)
            min_distance = min(distance, min_distance)
            avg_distance += distance

            time_current = get_time(time[i])

            speed = distance/time_current
            
            max_speed = max(speed, max_speed)
            min_speed = min(speed, min_speed)
            avg_speed += speed

        else:
            missed_days = missed_days + 1
        
        if days[i] == 7:
            weeks.append(1)
            if missed_days > 0:
                missed_week.append(1)
            else:
                missed_week.append(0)
            missed_days = 0             

        weekly_reward = 0
       
    for i in range(len(weeks)):
        if weeks[i] == 1 and missed_week[i] != 1:
            weekly_reward += 1

    count_missed_week = 0
    
    for i in range(len(weeks)):
        if missed_week[i] == 1:
            count_missed_week += 1
        if (i+1)%4 == 0: 
            if count_missed_week == 0:
                months.append(1)
            count_missed_week = 0
            
    
    avg_distance /= len(weeks)
    avg_speed /= len(days)

    if len(months) > 0:
        print("Congrats! You have got a {} M/M award for this month".format(len(months)))
    elif weekly_reward > 0:
        if(len(days) > 7):
            print("Congrats! You have got a {} 7/7 award".format(weekly_reward))
        else:
            print("Your weekly achievements are as follows:")
            print("No Breakout in Session! You have got a 7/7 award")
    else:
        print("No awards as there were breaks in the schedule")

    print("Your Fastest Speed is : {0:.2f} Km/hr".format(max_speed))
    print("Your Slowest Speed is : {0:.2f} Km/hr".format(min_speed))
    print("Your Longest Distance is : {0:.2f} Km".format(max_distance))
    print("Your Shortest Distance is : {0:.2f} Km".format(min_distance))
    print("Your Average Weekly Speed is : {0:.2f} Km/hr".format(avg_speed))
    print("Your Average Weekly Distance is : {0:.2f} Km".format(avg_distance))


def main():

    name = input("Enter name : ")
    age = input("Enter age (yrs) : ")
    sex = input("Enter sex : ")
    weight = input("Enter weight (in lbs/kg) : ")
    height = input("Enter height (in in/cm) : ")

    person = Person(name, age, sex, weight, height)
    
    days = []
    steps_all = []
    time_all = []

    check = True
    print("Enter data (Press ENTER when finished)")
    print("Enter weekday, numer of steps and time taken (HH:MM:SS) : ")
    while check:
        key_input = input()
        if key_input == '':
            check = False
        else:
            day, steps, time = key_input.split(', ')
            days.append(int(day))
            steps_all.append(int(steps))
            time_all.append(time)

    if person.getsex().lower() == "male":
        desg = "Mr."
    else:
        desg = "Ms."

    print("Hi", desg, person.getname())
    person.getBMI()

    gen_stats(days, steps_all, time_all)


if __name__ == "__main__":
    main()
