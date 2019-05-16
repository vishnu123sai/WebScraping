import requests
import bs4

def alphabetical_order(college_details):
    list  = college_details.keys()
    list = sorted(list)

    for i in list:
        print("\n================================================")
        print("College Name                 :" ,i)
        print("Tution Cost in Range($-$$$$) :", college_details[i][0])
        print("Avg Retention Rate           :", college_details[i][1])
        print("Programs Available           :", college_details[i][2])
        print("Student Faculity Ration      :", college_details[i][3])
        print("Facilities in College        :", college_details[i][4])
        print("Placement Services           :", college_details[i][5])
        print("On Campus Housing            :", college_details[i][6])
        print("================================================\n")

def plaments_services(college_details):
    for i in college_details:
        if college_details[i][5]=='Yes':
            print("\n================================================")
            print("College Name                 :" ,i)
            print("Tution Cost in Range($-$$$$) :", college_details[i][0])
            print("Avg Retention Rate           :", college_details[i][1])
            print("Programs Available           :", college_details[i][2])
            print("Student Faculity Ration      :", college_details[i][3])
            print("Facilities in College        :", college_details[i][4])
            print("Placement Services           :", college_details[i][5])
            print("On Campus Housing            :", college_details[i][6])
            print("================================================\n")

def based_on_student_faculity_ratio(college_details):   
    list = []
    for i in college_details:
        list.append(college_details[i][3])
    list = sorted(list)
    list = list[::-1]
    temp = []

    for r in list:
        for i in college_details:
            if college_details[i][3]==r and i not in temp:
                temp.append(i)
                print("\n================================================")
                print("College Name                 :" ,i)
                print("Tution Cost in Range($-$$$$) :", college_details[i][0])
                print("Avg Retention Rate           :", college_details[i][1])
                print("Programs Available           :", college_details[i][2])
                print("Student Faculity Ration      :", college_details[i][3])
                print("Facilities in College        :", college_details[i][4])
                print("Placement Services           :", college_details[i][5])
                print("On Campus Housing            :", college_details[i][6])
                print("================================================\n")


def tution_cost_range(college_details):
    for r in range(1,5):
        for i in college_details:
            if len(college_details[i][0])==r:
                print("\n================================================")
                print("College Name                 :" ,i)
                print("Tution Cost in Range($-$$$$) :", college_details[i][0])
                print("Avg Retention Rate           :", college_details[i][1])
                print("Programs Available           :", college_details[i][2])
                print("Student Faculity Ration      :", college_details[i][3])
                print("Facilities in College        :", college_details[i][4])
                print("Placement Services           :", college_details[i][5])
                print("On Campus Housing            :", college_details[i][6])
                print("================================================\n")


def avg_retention_ratios(college_details):
    list = []
    for i in college_details:
        list.append(float(college_details[i][1]))
    list = sorted(list)
    list = list[::-1]
    temp = []

    for r in list:
        for i in college_details:
            if float(college_details[i][1])==r and i not in temp:
                temp.append(i)
                print("\n================================================")
                print("College Name                 :" ,i)
                print("Tution Cost in Range($-$$$$) :", college_details[i][0])
                print("Avg Retention Rate           :", college_details[i][1])
                print("Programs Available           :", college_details[i][2])
                print("Student Faculity Ration      :", college_details[i][3])
                print("Facilities in College        :", college_details[i][4])
                print("Placement Services           :", college_details[i][5])
                print("On Campus Housing            :", college_details[i][6])
                print("================================================\n")

def colleges(college_details):
    for i in college_details:
        print("\n================================================")
        print("College Name                 :" ,i)
        print("Tution Cost in Range($-$$$$) :", college_details[i][0])
        print("Avg Retention Rate           :", college_details[i][1])
        print("Programs Available           :", college_details[i][2])
        print("Student Faculity Ration      :", college_details[i][3])
        print("Facilities in College        :", college_details[i][4])
        print("Placement Services           :", college_details[i][5])
        print("On Campus Housing            :", college_details[i][6])
        print("================================================\n")

def main():
    print("\n=========  Welcome To WebScraping of indiaeducation.net site  ========\n")
    res = requests.get("http://www.indiaeducation.net/studyabroad/listing/")

    soup  = bs4.BeautifulSoup(res.content,'html.parser')
    college_details = {}
    college_name_tag = soup.find_all('div', attrs={'class': 'college_div'})

    for i in college_name_tag:
        college_name = i.find('span', class_= 'college_name2')
        college_name = (college_name.text).strip()
        college_details[college_name]=[]
        tution_range = i.find(class_='tuition_cost')
        tution_range = tution_range.find('font', class_='bluefont')
        tution_range=tution_range.text
        college_details[college_name].append(tution_range)
        avg_retention_rate = i.find(class_="distance_edu_value")
        avg_retention_rate=avg_retention_rate.text
        college_details[college_name].append(avg_retention_rate)
        programs_avail = i.find(class_="percent_transfer_value")
        programs_avail=programs_avail.text
        college_details[college_name].append(programs_avail)
        student_faculity_ratio = i.find(class_="sa_studentToFacultyRatio")
        student_faculity_ratio = student_faculity_ratio.find('span',class_="bluefont")
        student_faculity_ratio = student_faculity_ratio.text
        college_details[college_name].append(student_faculity_ratio)
        features = i.find(class_="listing_sa_ss_text_sizesetting")
        if features:
            features = features.text
            college_details[college_name].append(features)
        else:
            college_details[college_name].append("None")
        placements = i.find(class_='sa_placementServices')
        if placements:
            placements= placements.find('span',class_="bluefont")
            placements = placements.text
            college_details[college_name].append(placements)
        else:
            college_details[college_name].append("No")

        on_campus_housing = i.find(class_='sa_onCampusHousing')
        if on_campus_housing:
            on_campus_housing = on_campus_housing.find('span',class_="bluefont")
            on_campus_housing = on_campus_housing.text
            college_details[college_name].append(on_campus_housing)
        else:
            college_details[college_name].append("No")

    
    count = 0;
    while True:
        print("Sort Colleges Based on Options:")
        print("===============================")
        print("\n 1. Top 20 colleges \n 2. Colleges in Alphabetical order \n 3. Colleges Based on Student to Faculity Ratio \n 4. Colleges Based on Avg Retention Ration \n 5. Colleges Based on Tution Cost Range (\"$\"(Low)-\"$$$$\"(High) \n 6. Colleges Based on Placement Services\n 7. Exit")
        print("\n================================================\n")
        option = input("Enter Option from 1 to 7   :  ")
        if option=="1":
            colleges(college_details)
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()

        elif option=="2":
            alphabetical_order(college_details);
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()
        elif option=="3":
            based_on_student_faculity_ratio(college_details);
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()
        elif option=="4":
            avg_retention_ratios(college_details);
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()
        elif option=="5":
            tution_cost_range(college_details)
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()
        elif option=="6":
            plaments_services(college_details);
            count=0
            print("If you Wish To Close Enter Y/y or Press any key")
            options = input()
            if options =='Y' or options =='y':
                print("============== Thank You ============")
                exit()
        elif option=="7":
            print("============== Thank You ============")
            exit()
        else:
            count = count+1;
            if count == 3:
                print("\n======You have Entered Wrong Option Multiple Times Please Try Again======\n")
                exit()
            print("Please Enter Numeric value Between 1-7\n\n You have %d Chances to Choose Correct Option\n" %(3-count))

if __name__ == "__main__":
    main()