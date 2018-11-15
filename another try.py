# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:42:24 2018

@author: Administrator
"""

#the information of the stalls in each canteen
#Keys --> canteen names
#values --> lists of lists of lists,the most nested is a list of food categories,
             #the upper nest is the information for each stall(index 0 is name, 1 is food, 2 is price),
             #the outer most nest is the list of stalls
stall_info = {'Koufu': [['Western', ['Western','Salad'], '5'],
                        ['Bento', ['Healthy', 'Salad'], '6'],
                        ['Salad', ['Healthy', 'Salad'],'6'],
                        ['Pasta', ['Western'], '6']],
              'North Spine': [['Mcdonalds', ['Fast food', 'Western'], '7'],
                               ['Subway', ['Healthy', 'Fast Food'], '6'],
                               ['Long John Silver\'s', ['Fast Food', 'Western'], '6'],
                               ['Each-a-Cup', ['Drinks'], '4'],
                               ['North Spine Plaza', ['Snacks'], '3'],
                               ['Mr Bean', ['Drinks', 'Snacks'],'3'],
                               ['North Spine Food Court', ['Western', 'Chinese','Korean', 'Japanese'],'5'],
                               ['Pen & Inc', ['Western', 'Bar'], '15'],
                               ['Peach Garden Chinese Restaurant', ['Chinese'], '18'],
                               ['Starbucks Coffee', ['Drinks'], '6'],
                               ['The Sandwich Guys', ['Snacks', 'Western'], '5'],
                               ['KFC', ['Fast food', 'Western'], '7'],
                               ['The House Steam Boat Restaurant', ['Chinese'], '15'],
                               ['The Soup Spoon Union', ['Western'], '10']],
             'Food Court 1': [['Western', ['Western', 'Salad'], '5'],
                              ['Korean', ['Korean'], '4'],
                              ['Drinks', ['Drinks'], '2'],
                              ['Chinese', ['Chinese', 'Snacks'], '3']],
             'Food Court 2': [['Western', ['Western', 'Salad'], '7'], 
                              ['Drinks', ['Drinks'], '2'],
                              ['Chinese', ['Chinese', 'Snacks'], '6']],
             'Food Court 9': [['Western', ['Western', 'Salad'], '4'],
                              ['Ramen', ['Japanese'], '5'],
                              ['Drinks', ['Drinks'], '2'],
                              ['Chinese', ['Chinese', 'Snacks'], '5']],
             'Food Court 11': [['Western', ['Western', 'Salad'], '6'], 
                               ['Drinks', ['Drinks'], '2'],
                               ['Chinese', ['Chinese', 'Snacks'], '5']],
             'Food Court 13': [['Western', ['Western', 'Salad'], '5'], 
                               ['Drinks', ['Drinks'], '2'],
                               ['Chinese', ['Chinese', 'Snacks'], '6']],
             'Food Court 14': [['Western', ['Western', 'Salad'], '5'],
                               ['Drinks', ['Drinks'], '2'],
                               ['Chinese', ['Chinese', 'Snacks'], '5']],
             'Food Court 16': [['Western', ['Western', 'Salad'], '6'], 
                               ['Drinks', ['Drinks'], '2'],
                               ['Chinese', ['Chinese', 'Snacks'], '4']],
             'Foodgle Food Court': [['Western', ['Western', 'Salad'], '4'],
                                    ['Mala', ['Chinese'], '6'],
                                    ['Chinese', ['Chinese', 'Snacks'], '6']],
             'North Hill Food Court': [['Western', ['Western', 'Salad'], '5'],
                                       ['Chinese', ['Chinese', 'Snacks'], '4']],
             'Pioneer Food Court': [['Western', ['Western', 'Salad'], '6'], 
                                    ['Korean', ['Korean'], '4'],
                                    ['Chinese', ['Chinese', 'Snacks'], '6']]}
             
#the details of each canteen, irregarding the stalls
canteen_info = [["Food Court 1", "600PAX",  "7AM-11PM", 5], ["Food Court 2" , "400PAX", "6AM-11PM", 2],
                ["Food Court 9", "300PAX"," 7AM-10PM", 3], ["Food Court 11","550PAX","8AM-12AM", 4],
                ["Food Court 13","650PAX","7AM-10PM", 1], ["Food Court 14","450PAX","7AM-10PM", 6],
                ["Food Court 16", "600PAX","7AM-11PM", 7], 
                ["Foodgle Food Court","600PAX","9AM-11PM", 9], ["North Hill Food Court", "700PAX", "10AM-11PM", 10],
                ["Pioneer Food Court", "600PAX", "7AM-11PM", 11],
                ["North Spine Plaza", "800PAX", "7AM-11PM", 13], ["Each-A-Cup", "30PAX","7AM-11PM", 14],
                ["Grande Cibo" ,"200PAX", "7AM-11PM", 16], ["KFC", "500PAX", "7AM-11PM", 17],
                ["Long John Silver's", "600PAX","7AM-11PM", 19], ["McDonald's", "300PAX"," 7AM-11PM", 18],
                ["Mr Bean", "50PAX" ,"7AM-11PM", 20], ["North Spine Food Court", "400PAX","7AM-11PM", 8],
                ["Paik's Bibim", "300PAX", "7AM-11PM", 22], ["Peach Garden Chinese Restaurant" ,"600PAX" ,"7AM-11PM", 23],
                ["PEN & INC", "400PAX", "7AM-11PM", 24], ["Pizza Hut Express", "600PAX" ,"7AM-11PM", 25],
                ["Starbucks Coffee" ,"300PAX", "7AM-11PM", 26], ["Subway", "500PAX", "7AM-11PM", 27],
                ["The Sandwich Guys", "50PAX", "7AM-11PM", 15], ["The House Steam Boat Restaurant", "400PAX", "7AM-11PM", 28],
                ["The Soup Spoon Union", "600PAX", "7AM-11PM", 12], ["Koufu @ South Spine" ,"300PAX", "7AM-11PM", 21]]

#the co-ordinates of all the canteens
canteen_coords= {"Food Court 1": (372, 386),"Food Court 2": (351, 322),"Food Court 9": (351, 188),\
                 "Food Court 11": (388, 93), "Food Court 13" : (200, 205), "Food Court 14" : (241, 173),\
                 "Food Court 16" : (204, 257), "Foodgle Food Court":(340, 100), "North Hill Food Court":(446, 119),\
                 "Pioneer Food Court":(462, 400), "Koufu" : (244, 530), "North Spine" :(204, 390)}

#pointdict needs to be updated
PointDictionary = {"Point1": (157,232), "Point2": (108, 365), "Point3": (232, 305), "Point4": (263, 133),
                   "Point5": (437, 89), "Point6": (368, 187), "Point7": (336, 283), "Point8": (500, 244),
                   "Point9": (454, 441), "Point10": (210, 465), "Point11": (294, 504), "Point12": (137, 586)}

#all the bus stops in the red loop and their co-ords
BusStopRed = {"Bus Stop 1" : (367, 484) ,"Bus Stop 2" :  (434, 416) ,"Bus Stop 3" : (357, 302),
                  "Bus Stop 4" : (365, 213),"Bus Stop 5" : (416, 104),"Bus Stop 6" :  (408, 67),
                  "Bus Stop 7" : (299, 104),"Bus Stop 8" : (184, 200),"Bus Stop 9" :  (193, 330),
                  "Bus Stop 10" :  (113, 438),"Bus Stop 11" :  (136, 546),"Bus Stop 12" :  (171, 613),
                  "Bus Stop 13" :  (291, 519)}

#all the stops in the blue loop and thier co-ords
BusStopBlue = {"Bus Stop 1" : (399, 482),"Bus Stop 2" : (293, 519), "Bus Stop 3" : (201, 546),
               "Bus Stop 4" : (134, 546),"Bus Stop 5" : (109, 398),"Bus Stop 6" : (190, 330),
               "Bus Stop 7" : (201, 275),"Bus Stop 8" : (233, 151),"Bus Stop 9" : (301, 101),
               "Bus Stop 10" : (419, 104),"Bus Stop 11" : (364, 208),"Bus Stop 12" : (390, 341)}


import pygame, sys , os, time

#1
#--creates a window to choose the type of food, and passes the choice to a search function--
def display_food():
    introScreenImage = pygame.image.load("food.png")
    pygame.display.set_caption("Food Categories")
    screen = pygame.display.set_mode((450, 636))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    chi = pygame.Rect(60,203, 145, 40) #defining the areas where the mousepress is detected
    western = pygame.Rect(255,203, 145, 40)
    korean = pygame.Rect(60,262, 145, 40)
    japanese = pygame.Rect(255,262, 145, 40)
    healthy = pygame.Rect(60,325, 145, 40)
    salad = pygame.Rect(255,325, 145, 40)
    fast = pygame.Rect(60,387, 145, 40)
    snacks = pygame.Rect(255,387, 145, 40)
    bar = pygame.Rect(60,448, 145, 40)
    drinks = pygame.Rect(255,448, 145, 40)
    back = pygame.Rect(158,524,145,40)
    done = True 
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#quitting the programme using the exit button
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:#detecting mousepress within the hitboxes
                pos = pygame.mouse.get_pos()
                if chi.collidepoint(pos):
                    food = "Chinese"
                elif western.collidepoint(pos):
                    food = "Western"
                elif korean.collidepoint(pos):
                    food = "Korean"
                elif japanese.collidepoint(pos):
                    food = "Japanese"
                elif healthy.collidepoint(pos):
                    food = "Healthy"
                elif salad.collidepoint(pos):
                    food = "Salad"
                elif fast.collidepoint(pos):
                    food = "Fast Food"
                elif snacks.collidepoint(pos):
                    food = "Snacks"
                elif bar.collidepoint(pos):
                    food = "Bar"
                elif drinks.collidepoint(pos):
                    food = "Drinks"
                elif back.collidepoint(pos):
                    main()
                    break
                else:
                    continue
                search_by_food(food,stall_info)#calls another function if a hitbox was clicked
    pygame.quit()
                
#--searches the canteens for the chosen food--
def search_by_food(food,canteens):#canteens is a dictionary
    canteen_list = []
    results_array = []
    for key,val in canteens.items():  #checking each key and value pair
        for i in val:     
            if food in i[1]:   #checking if food is in index one of each element 
                if key not in canteen_list:
                    canteen_list.append(key)
                stall_list = []
                stall_list.append(key)
                stall_list.append(i[0])
                stall_list.append(i[2])
                results_array.append(stall_list)  #creating a list of lists to be printed
    print("")
    print ("You can find " + food + " in these canteens: " + ', '.join(canteen_list))
    print("")
    print ("--Canteen Name-----Stall Name-----Price--" )
    for x in results_array:
        print(x)  #prints each stall in a new line
        
    
#2        
#--creates a window to choose the max budget--
def display_price():
    introScreenImage = pygame.image.load("price.png")
    pygame.display.set_caption("Prices")
    screen = pygame.display.set_mode((450, 636))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    one= pygame.Rect(60,203,145, 45) #defining the areas where the mousepress is detected
    two = pygame.Rect(255,203, 145, 45)
    three = pygame.Rect(60, 262, 145, 45)
    four = pygame.Rect(255, 262, 145, 45)
    five = pygame.Rect(60, 325, 145, 45)
    six = pygame.Rect(255, 325, 145, 45)
    seven = pygame.Rect(60, 387, 145, 45)
    eight = pygame.Rect(255, 387, 145, 45)
    nine = pygame.Rect(60, 450, 145, 45)
    ten = pygame.Rect(255, 450, 145, 45)
    more = pygame.Rect(158, 507, 145, 45)
    back = pygame.Rect(158, 564, 145, 45)
    done = True 
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if one.collidepoint(pos):
                    price = 1
                elif two.collidepoint(pos):
                    price = 2
                elif three.collidepoint(pos):
                    price = 3
                elif four.collidepoint(pos):
                    price = 4
                elif five.collidepoint(pos):
                    price = 5
                elif six.collidepoint(pos):
                    price = 6
                elif seven.collidepoint(pos):
                    price = 7
                elif eight.collidepoint(pos):
                    price= 8
                elif nine.collidepoint(pos):
                    price = 9
                elif ten.collidepoint(pos):
                    price = 10
                elif more.collidepoint(pos):
                    price = 20
                elif back.collidepoint(pos):
                    main()
                    break
                else: 
                    continue
                print("You can patronise these stalls which are within your budget:")
                search_by_prices(price)  #calling another function using the value selected
    pygame.quit()

#--searching for all stalls that has an average price lower than the stated budget
def search_by_prices(price_input):
    results_array = [] 
    for key, val in stall_info.items(): #iterating over each key and value pair
        for x in val:
            if int(x[2]) <= price_input:
                results = []
                results.append(key)
                results.append(x[0])
                results.append(x[2])
                results_array.append(results) #creating a list of lists to be printed
    if len(results_array) == 0:
        print("no results")
    for num in range(len(results_array)-1):  #first modification of bubblesort
        swapped = False
        for i in range(len(results_array)-num-1):
            if int(results_array[i][2])>int(results_array[i+1][2]):  #sorting the sublists using their 3rd element
                temp = results_array[i]
                results_array[i] = results_array[i+1]
                results_array[i+1] = temp
                swapped = True
                if not swapped:
                    break
    else:
        for x in results_array:
            print(x)

#3    
#--sorts the list of canteen information according to the rank of the canteens--
#no display function is necessary here as there is no userinput required upon choosing rank
def sort_by_rank(list_):
    for num in range(len(list_)-1):
        swapped = False
        for i in range(len(list_)-num-1): #second modification of bubblesort
            if list_[i][3]>list_[i+1][3]:  #sorting the list of lists using their fourth element
                temp = list_[i]
                list_[i] = list_[i+1]
                list_[i+1] = temp
                swapped = True
        if not swapped:
            break
    results_array = []
    for x in list_:
        results=[]
        results.append(x[3])
        results.append(x[0])
        results_array.append(results)  #similar to search_by_price/food
    for i in results_array:
        print (i)

#4
#--creates a window to indicate current location--
#output: nearest canteen and a sorted list of canteens by distance 
def display_distance():
    introScreenImage = pygame.image.load("NTU campus.png")
    pygame.display.set_caption("Map of NTU")
    screen = pygame.display.set_mode((545,648))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    back = pygame.Rect(20,590,87,35)
    done = True 
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                Coordinates = pos
                if back.collidepoint(pos):
                    main()
                    pygame.quit()
                pygame.draw.circle(screen, (255,255, 255), Coordinates, 4)  #draws a pointer to indicate current location
                pygame.display.update()
                to_sort = get_elementDist(Coordinates, canteen_coords)
                print("The nearest canteen is " + str(sort_by_distance(to_sort)[0][0]))
                print ("---Canteens sorted by distance---")            #sorted by linear distance, not walking distance to simplify things
                for i in sort_by_distance(to_sort):
                    print(i[0]+': '  + str(round(i[1]* 3.2767 )) + " metres")
                done = False
                pos1= canteen_coords[sort_by_distance(to_sort)[0][0]]
                pygame.draw.circle(screen, (0,255,0) , pos1, 15, 3)  #highlights the location of the nearest canteen
                pygame.display.update()
            else:
                continue
    y = input("Do you wish to go to the nearest canteen?(Y/N)")      #normally, the nearest canteen is close enough that bus is not possible
    print("")
    if y.lower() == "y":                                            #but in case of an abnormally deserted situation
        getting_there(Coordinates, pos1)
    main()
    pygame.quit()
    
    
def bubblesort(list_):      #default version of bubblesort
    for num in range(len(list_)-1):
        swapped = False
        for i in range(len(list_)-num-1):
            if list_[i]>list_[i+1]:     #sorting elements of a list based on their own values
                temp = list_[i]
                list_[i] = list_[i+1]
                list_[i+1] = temp
                swapped = True
        if not swapped:
            break
    return list_

#sorting a dictionary based on the distance values 
def sort_by_distance(canteen_dist):
    dist_list = []
    for distance in canteen_dist.values(): #creating a list of the values of canteen_dist
        dist_list.append(distance)
    dist_list = bubblesort(dist_list)       #calling the default version of bubblesort on the list
    sorted_list = []
    for dist in dist_list:
        for i in canteen_dist.keys():
            if canteen_dist[i] == dist:     #checking for the corresponding key from the associated value 
                sorted_list.append([i,canteen_dist[i]]) #adding in order both the key, value into a new list 
    return (sorted_list)
                
#getting the distance from given coordinates from all points in a co-ordinate dictionary
#used to get distance from current location from all canteens
#returns another dictionary (keys-->canteens, values-->distance)
def get_elementDist(Coordinates, coord_list):
    dist = {}
    for element in coord_list.keys():
        Xlength = Coordinates[0] - coord_list[element][0]
        X2 = Xlength ** 2
        Ylength = Coordinates[1] - coord_list[element][1]
        Y2 = Ylength ** 2
        Distance2 = float(X2 + Y2)
        Distance = Distance2 ** 0.5
        dist[element]= Distance
    return (dist)

#5
#--creating a window to indicate both the start and end points of a journey--
def display_map():
    introScreenImage = pygame.image.load("NTU campus.png")
    pygame.display.set_caption("Map of NTU")
    screen = pygame.display.set_mode((545,648))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    back = pygame.Rect(20,590,87,35)
    done = True 
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if back.collidepoint(pos):
                    main()
                    pygame.quit()
                CurrentCoordinates = pos
                pygame.draw.circle(screen, (255,255, 255), CurrentCoordinates, 4)
                pygame.display.update()   #creating a pointer to indicate current and end co-ordinates
                DestiCoordinates = mouseclick()
                pygame.draw.circle(screen, (255,255, 255), DestiCoordinates, 4)
                pygame.display.update()
                done = False
            else:
                continue
    getting_there(CurrentCoordinates, DestiCoordinates)  #calling another function to advice method of transport
    main()

#--outputs both walking distance and bus stop routes to get to a location
def getting_there(CurrentCoordinates, DestiCoordinates):
    StraightDistance = get_distance(CurrentCoordinates, DestiCoordinates)
    print("---If you prefer walking ---")
    if StraightDistance < 100:  #when distance is short enough, able to approximate in a straight line
        print("The walking distance is", round(StraightDistance * 3.2767) , " metres.") #converting pixel distance into scaled distance
    else:
        Point1 = Nearestpoint(CurrentCoordinates)    
        Point2 = Nearestpoint(DestiCoordinates)
        PointDistance = pointdistance(Point1, Point2)
        Distance1 = get_distance(PointDictionary[Point1], CurrentCoordinates)
        Distance2 = get_distance(PointDictionary[Point2], DestiCoordinates)
        TotalDistance = Distance1 + Distance2 + PointDistance
        print("The shortest walking distance is", round(TotalDistance* 3.2767)," metres." )#converting pixel distance into scaled distance
    print ("---If you prefer taking a bus---")
    busstop(CurrentCoordinates, DestiCoordinates)
    
    

def Nearestpoint(Coordinates):
    list1 = []
    for key in PointDictionary.keys():
        distance = get_distance(Coordinates, PointDictionary[key])
        list1.append(distance)
    minimumdistance = min(list1)
    for key in PointDictionary.keys():
        distance = get_distance(Coordinates, PointDictionary[key])
        if distance == minimumdistance:
            return key



def DistanceCal(PreviousStop, stop, List):
    OldX = PointDictionary[PreviousStop][0]
    OldY = PointDictionary[PreviousStop][1]
    NewX = PointDictionary[stop][0]
    NewY = PointDictionary[stop][1]
    Xlength = NewX - OldX
    X2 = Xlength ** 2
    Ylength = NewY - OldY
    Y2 = Ylength ** 2
    Distance2 = float(X2 + Y2)
    Distance = Distance2 ** 0.5
    List.append(Distance)

def LoopDistance(Point1, Point2, Loop):
    Index1 = Loop.index(Point1)
    Index2 = Loop.index(Point2)
    if Index1 < Index2:
        NewList1 = Loop[Index1:Index2+1]
        NewList2 = Loop[Index1::-1]+Loop[-1:Index2-1:-1]
    elif Index2 < Index1:
        NewList1 = Loop[Index1:] + Loop[:Index2+1]
        if Index2 > 0:
            NewList2 = Loop[Index1:Index2-1:-1]
        elif Index2 == 0:
            NewList2 = Loop[Index1::-1] #NewList1 goes from left to right; NewList2 opposite direction
    elif Index1 == Index2:
        return 0
    list1 = []
    list2 = []
    Sum1 = 0
    Sum2 = 0
    NewList1Index1 = NewList1.index(Point1)
    NewList1Index2 = NewList1.index(Point2)
    NewList2Index1 = NewList2.index(Point1)
    NewList2Index2 = NewList2.index(Point2)
    for stop in NewList1[NewList1Index1+1:NewList1Index2+1]:
        StopIndex = NewList1.index(stop)
        PreviousStop = NewList1[StopIndex-1]
        DistanceCal(PreviousStop, stop, list1)
    for distance in list1:
        Sum1 += distance
    for stop in NewList2[NewList2Index1+1:NewList2Index2+1]:
        StopIndex = NewList2.index(stop)
        PreviousStop = NewList2[StopIndex-1]
        DistanceCal(PreviousStop, stop, list2)
    for distance in list2:
        Sum2 += distance
    if Sum1 < Sum2:
        return Sum1
    else:
        return Sum2

def findconnection(list1, list2):
    List1 = []
    List2 = []
    Commonlist = []
    for lists in list1:
        for point in lists:
            if point in List1:
                continue
            else:
                List1.append(point)
    for lists in list2:
        for point in lists:
            if point in List2:
                continue
            else:
                List2.append(point)
    for point in List1:
        if point in List2:
            Commonlist.append(point)
    return Commonlist

def pointdistance(Point1, Point2):
    Loop1 = ("Point1", "Point2", "Point3")
    Loop2 = ("Point1", "Point3", "Point7", "Point6", "Point5", "Point4")
    Loop3 = ("Point2", "Point12", "Point11", "Point10", "Point7", "Point3")
    Loop4 = ("Point7", "Point10", "Point11", "Point9")
    Loop5 = ("Point7", "Point9", "Point8", "Point5", "Point6")
    list1 = []
    list2 = []
    for loop in [Loop1, Loop2, Loop3, Loop4, Loop5]:
        if Point1 in loop:
            list1.append(loop)
        if Point2 in loop:
            list2.append(loop)
    Same = any(x in list1 and x in list2 for x in [Loop1, Loop2, Loop3, Loop4, Loop5])
    if Same == True:
        for loop in list1:
            if loop in list2:
                loopdistance = LoopDistance(Point1, Point2, loop)
                return loopdistance
    elif Same == False:
        Connection = findconnection(list1, list2)
        commonlist = []
        for point in Connection:
            for loop in [Loop1, Loop2, Loop3, Loop4, Loop5]:
                if point in loop and Point1 in loop:
                    loopdistance1 = LoopDistance(Point1, point, loop)
            for loop in [Loop1, Loop2, Loop3, Loop4, Loop5]:
                if point in loop and Point2 in loop:
                    loopdistance2 = LoopDistance(Point2, point, loop)
            totaldistance = loopdistance1 + loopdistance2
            commonlist.append(totaldistance)
        return min(commonlist)

def get_distance(CurrentCoordinates, DestiCoordinates):
    Xlength = CurrentCoordinates[0] - DestiCoordinates[0]
    X2 = Xlength ** 2
    Ylength = CurrentCoordinates[1] - DestiCoordinates[1]
    Y2 = Ylength ** 2
    Distance2 = float(X2 + Y2)
    Distance = Distance2 ** 0.5
    return Distance 

#advices the bus route from current point to destination point
def busstop(CurrentCoordinates, DestiCoordinates):
    BlueList = ("Bus Stop 1", "Bus Stop 2", "Bus Stop 3", "Bus Stop 4", "Bus Stop 5",\
                "Bus Stop 6", "Bus Stop 7", "Bus Stop 8", "Bus Stop 9", "Bus Stop 10", "Bus Stop 11", "Bus Stop 12")
    RedList = ("Bus Stop 1", "Bus Stop 2", "Bus Stop 3", "Bus Stop 4", "Bus Stop 5",\
                "Bus Stop 6", "Bus Stop 7", "Bus Stop 8", "Bus Stop 9", "Bus Stop 10", "Bus Stop 11", "Bus Stop 12", "Bus Stop 13")
    back1= pygame.Rect(428, 568,102,50)
    back2 = pygame.Rect(423,569,110,50)
    #----finding the shortest distance between the current location and the nearest red/blue bus stops---
    distDict1_R= get_elementDist(CurrentCoordinates, BusStopRed)     #returns list of lists of all the bus stops and their distances
    shortest_dist1_R = sort_by_distance(distDict1_R)[0]          #calling the nearest red stop+ distance from current point
    distDict1_B= get_elementDist(CurrentCoordinates, BusStopBlue)
    shortest_dist1_B = sort_by_distance(distDict1_B)[0]         #calling the nearest blue stop+dist  from current point
    #----finding the shortest distance between the destination location and the nearest red/blue bus stops---
    distDict2_R= get_elementDist(DestiCoordinates, BusStopRed)      #returns list of lists of all the bus stops and their distances
    shortest_dist2_R = sort_by_distance(distDict2_R)[0]         #calling the nearest red stop + dist from end point
    distDict2_B= get_elementDist(DestiCoordinates, BusStopBlue)
    shortest_dist2_B = sort_by_distance(distDict2_B)[0]         #calling the nearest blue stop + dist from end point
    #---Two sets of current bus stops and destination bus stops---
    #calling only the names of the four bus stops
    CurrentR = shortest_dist1_R [0]
    CurrentB = shortest_dist1_B [0]
    DestinationR = shortest_dist2_R[0]
    DestinationB = shortest_dist2_B[0]
    #splicing the ordered bus stop lists based on the current location 
    BlueIndex = BlueList.index(CurrentB)
    NewBIndex = BlueIndex + 1
    RedIndex = RedList.index(CurrentR)
    NewRIndex = RedIndex + 1
    NewRList = RedList[NewRIndex:] + RedList[0:RedIndex]
    NewBList = BlueList[NewBIndex:] + BlueList[0:BlueIndex]
    if CurrentB == DestinationB or CurrentR == DestinationR:
        print("The distance is too short to take a bus! Please walk instead :-) ")
    elif NewRList.index(DestinationR) > NewBList.index(DestinationB):  #comparing the differences in bus stops between red and blue lin e
        print ("Walk " + str(round(shortest_dist1_B[1]* 3.2767 )) + " metres to " + CurrentB +\
               ". Take the blue line to " + DestinationB + " then walk "+ str(round(shortest_dist2_B[1]* 3.2767 )) + " metres.")
        introScreenImage = pygame.image.load("NTU blue loop.png")
        pygame.display.set_caption("Blue Line")         #creates a map of the blue loop
        screen = pygame.display.set_mode((545,648))
        screen.blit(introScreenImage,(0,0))
        color = (0, 255, 0)
        pos1 = BusStopBlue[CurrentB]
        pos2 = BusStopBlue[DestinationB]
        pygame.draw.circle(screen, color , pos1, 15, 3)     #indicates the start and ending bus stops
        pygame.draw.circle(screen, color, pos2, 15, 3)
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back2.collidepoint(pos):
                        main()
                        pygame.quit()
    elif NewRList.index(DestinationR) < NewBList.index(DestinationB):
        print ("Walk " + str(round(shortest_dist1_R[1]* 3.2767 )) + " metres to " + CurrentR +\
               ". Take the red line to "+ DestinationR + " then walk "+ str(round(shortest_dist2_R[1]* 3.2767 )) + " metres.")
        introScreenImage = pygame.image.load("NTU red loop.png")
        pygame.display.set_caption("Red Line")          #creates a map of the red loop
        screen = pygame.display.set_mode((545,648))
        screen.blit(introScreenImage,(0,0))
        color = (0, 255, 0)
        pos1 = BusStopRed[CurrentR]
        pos2 = BusStopRed[DestinationR]
        pygame.draw.circle(screen, color , pos1, 15, 3)    #indicates the start and ending bus stops
        pygame.draw.circle(screen, color, pos2, 15, 3)
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back1.collidepoint(pos):
                        main()
                        pygame.quit()
    elif NewRList.index(DestinationR) == NewBList.index(DestinationB):#exception when it takes the same bus stops to reach destination from both red and blue line
        print ("Take either the red or blue line.")
        print ("To take the red line, walk " + str(round(shortest_dist1_R[1]* 3.2767 )) + " metres to " + CurrentR +\
               " then take to " + DestinationR + " and walk " + str(round(shortest_dist2_R[1]* 3.2767 )) + " metres.")
        print ("To take the blue line, walk " + str(round(shortest_dist1_B[1]* 3.2767 )) + " metres to " + CurrentB +\
               " then take to " + DestinationB + " and walk " + str(round(shortest_dist2_B[1]* 3.2767 )) + " metres.")
        while True:
            choice = input("Do you want to display BLUE or RED loop?:(B/R): ")  #asks the user to choose to display either the red or blue loop
            if choice.lower()== "b":
                choice1 = CurrentB
                choice2 = DestinationB
                list1 = BusStopBlue
                map1 = "NTU blue loop.png"
                break
            elif choice.lower() == "r":
                choice1 = CurrentR
                choice2 = DestinationR
                list1 = BusStopRed
                map1 = "NTU red loop.png"
                break
            else: 
                print ("Invalid input! Please retry!:")
                continue
        introScreenImage = pygame.image.load(map1) #creates a map of the chosen loop
        screen = pygame.display.set_mode((545,648))
        screen.blit(introScreenImage,(0,0))
        color = (0, 255, 0)
        pos1 = list1[choice1]   #the list that is accessed depends on the user input
        pos2 = list1[choice2]
        pygame.draw.circle(screen, color , pos1, 15, 3)    #indicates the start and ending bus stops
        pygame.draw.circle(screen, color, pos2, 15, 3)
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if back1.collidepoint(pos):
                        main()
                        pygame.quit()
        
#function to get the coordinates from a mouseclick   
def mouseclick():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = event.pos
                return coordinates

#--opening up a menu of the list of all canteens for the user to select the canteen of choice--
def display_canteenlist():
    introScreenImage = pygame.image.load("canteens.png")
    pygame.display.set_caption("List of canteens")
    screen = pygame.display.set_mode((450,636))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    fc1 = pygame.Rect(60,145, 145, 45)
    fc2 = pygame.Rect(255,145, 145, 45)
    fc9 = pygame.Rect(60, 205, 145, 45)
    fc11 = pygame.Rect(255, 205, 145, 45)
    fc13 = pygame.Rect(60, 260, 145, 45)
    fc14 = pygame.Rect(255, 260, 145, 45)
    fc16 = pygame.Rect(60, 325, 145, 45)
    foodgle = pygame.Rect(255, 325, 145, 45)
    north_hill = pygame.Rect(60, 385, 145, 45)
    pioneer = pygame.Rect(255, 385, 145, 45)
    koufu = pygame.Rect(60, 450, 145, 45)
    north_spine = pygame.Rect(225, 450, 145, 45)
    back = pygame.Rect(158, 523, 145, 45)
    done = True 
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if fc1.collidepoint(pos):
                    canteen = "Food Court 1"
                elif fc2.collidepoint(pos):
                    canteen = "Food Court 2"
                elif fc9.collidepoint(pos):
                    canteen = "Food Court 9"
                elif fc11.collidepoint(pos):
                    canteen = "Food Court 11"
                elif fc13.collidepoint(pos):
                    canteen = "Food Court 13"
                elif fc14.collidepoint(pos):
                    canteen = "Food Court 14"
                elif fc16.collidepoint(pos):
                    canteen = "Food Court 16"
                elif foodgle.collidepoint(pos):
                    canteen = "Foodgle Food Court"
                elif north_hill.collidepoint(pos):
                    canteen = "North Hill Food Court"
                elif pioneer.collidepoint(pos):
                    canteen = "Pioneer Food Court"
                elif koufu.collidepoint(pos):
                    canteen = "Koufu"
                elif north_spine.collidepoint(pos):
                    canteen = "North Spine"
                elif back.collidepoint(pos):
                    main()
                    break
                else:
                    continue
                done = False
    pygame.quit()
    return canteen
                
#intermediate function that combines the UI function and the algorithmic function
def display_updateinfo():
    x = display_canteenlist()
    update_info(x)


#--updating the information stored in the main dictionary--
#three choices: to add a new stall, add new food, or change price
def update_info(cant):
    introScreenImage = pygame.image.load("update.png")
    pygame.display.set_caption("Update menu")
    screen = pygame.display.set_mode((450,600))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    stall = pygame.Rect(93, 140, 287, 50)  ##defining the areas to detect mousepress
    food = pygame.Rect(93, 205, 287, 50)
    price = pygame.Rect(93, 272, 287, 50)
    back = pygame.Rect(159, 355, 145, 45)
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if stall.collidepoint(pos):
                    input_stall = input("What is the name of the stall?:").title()
                    temp = input("What does this store sell? You can enter multiple categories, separated by commas:").title()
                    input_category = list(temp.split(','))
                    while True:
                        try:
                            input_price = input("What is the average price of this stall?:")
                            input_price = int(input_price)
                            break
                        except ValueError:
                            print("Only numbers allowed! Try again!")
                    stall_info[cant].append([input_stall, input_category, input_price]) #adding a new dictionary entry in stall_info
                elif food.collidepoint(pos):
                    list1= []
                    for x in stall_info[cant]:
                        list1.append(x[0])
                    print ("Current stalls in "+ cant + ": " , str(list1))   #prints out a list of the current stalls in the canteen
                    while True:                                 #checking for validity of user-input
                        input_stall = input("Select the name of the stall?:").title()
                        if input_stall not in list1:
                            print("Invalid response! Try again!")
                        elif input_stall in list1:
                            break
                    temp = input("What does this store sell? You can enter multiple categories, separated by commas:").title()
                    input_category = temp.split(',')            #splits the input into a list separated by commas
                    for stalls in stall_info[cant]:
                        if stalls[0] == input_stall:
                            i = stall_info[cant].index(stalls)
                            for x in input_category:
                                stall_info[cant][i][1].append(x)    #appending the new food category into the existing list of food cat
                elif price.collidepoint(pos):
                    add= []
                    names = []
                    for stall in stall_info[cant]:          #creating iists of lists to print 
                        to_add= []
                        to_add = [stall[0],stall[2]]
                        add.append(to_add)
                        names.append(stall[0])
                    print ("Current stalls in ", cant, " and their respective prices:")  
                    for x in add:           #printing each stall and their prices
                        print(x)
                    while True:             #checking for validity of name
                        input_stall = input("Select the name of the name of the stall?:").title()
                        if input_stall not in names:
                            print("Invalid response! Try again!")
                        else:
                            break
                    while True:             #checking for validity and range of price input
                        input_price = input("What is the new average price of the stall?:")
                        try: 
                            val = int(input_price)
                            if val > 20:
                                print ("Maximum price is 20!")
                            else:
                                break   
                        except ValueError:
                            print ("Only integer prices!")     
                    for stalls in stall_info[cant]:
                        if stalls[0] == input_stall:
                            i = stall_info[cant].index(stalls)
                            stall_info[cant][i][2]= input_price    #replacing the old price with the new price data
                elif back.collidepoint(pos):
                    pygame.quit()
                    main()
                else: 
                    continue
                done = False 
    temp = stall_info[cant]
    print (cant, " :")
    for x in temp:
        print (x)           #prints the changed canteen list
    main()
    return stall_info

#7
#--creates a window to select which information to show--
def display_all():
    pygame.init()
    introScreenImage = pygame.image.load("all.png")
    pygame.display.set_caption("Showing all canteens")
    screen = pygame.display.set_mode((450,530))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    info = pygame.Rect(95, 140, 287, 50)
    all_stalls = pygame.Rect(93, 205, 287, 50)
    single_stall = pygame.Rect(93, 272, 287, 50)
    back = pygame.Rect(159, 355, 145, 45)
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if info.collidepoint(pos):      #shows all the canteens with their corresponding information(irregarding the stalls)
                    print ("--Canteen Name--Capacity--Opening Hours--Rank--")
                    for num in range(len(canteen_info)-1):
                        swapped = False
                        for i in range(len(canteen_info)-num-1):   #third modified bubblesort
                            if canteen_info[i][0]>canteen_info[i+1][0]: #sorting the lists of lists based on the first element
                                temp = canteen_info[i]                  #arranging in alphabetical order
                                canteen_info[i] = canteen_info[i+1]
                                canteen_info[i+1] = temp
                                swapped = True
                        if not swapped:
                            break
                    for x in canteen_info:
                        print(x)
                elif all_stalls.collidepoint(pos):  #shows all the stalls arranged by canteens
                    print ("--Stall Name--Food Type--Average Price--")
                    for cant in stall_info.keys():
                        print("")
                        print(cant, ":")
                        for x in stall_info[cant]:
                            print (x)
                elif single_stall.collidepoint(pos):   #shows all the stalls of a single canteen
                    canteen = display_canteenlist()
                    print ("--Stall Name--Food Type--Average Price--")
                    print (canteen, ":")
                    for x in stall_info[canteen]:
                        print (x)
                    display_all()
                elif back.collidepoint(pos):
                    main()
                    break
                else: 
                    continue
    pygame.quit()
    sys.exit()
    
#------------------------------------------------------
#--main menu that links all the seven functions together--
def main():
    introScreenImage = pygame.image.load("menu.png")
    pygame.display.set_caption("Main Menu")
    screen = pygame.display.set_mode((450,636))
    screen.blit(introScreenImage,(0,0))
    pygame.display.flip()
    food = pygame.Rect(185, 210, 145, 45)
    price = pygame.Rect(185, 270, 145, 45)
    rank = pygame.Rect(185, 330, 145, 45)
    near_you = pygame.Rect(185, 393, 145, 45)
    getting_around = pygame.Rect(185, 455, 145, 45)
    update_info= pygame.Rect(185, 515, 145, 45)
    show_all = pygame.Rect(185, 575, 145, 45)
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if food.collidepoint(pos):
                    display_food()
                elif price.collidepoint(pos):
                    display_price()
                elif rank.collidepoint(pos):
                    print ("In our opinion, the canteens in NTU ranked in order are as follows:")
                    sort_by_rank(canteen_info)
                elif near_you.collidepoint(pos):
                    display_distance()
                elif getting_around.collidepoint(pos):
                    display_map()
                elif update_info.collidepoint(pos):
                    display_updateinfo()
                elif show_all.collidepoint(pos):
                    display_all()
                else:
                    break
            if event.type == pygame.QUIT:
                done = False
    pygame.quit()
    sys.exit()
    
#arranges the pygame windows to the top to maximise screen real estate
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,30)
#initialises pygame and starts main function
pygame.init()
main()