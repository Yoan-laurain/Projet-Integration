import typing
import xml.etree.ElementTree as ET
from abc import abstractclassmethod, abstractmethod

tree = ET.parse('data.xml')
root = tree.getroot()
#####Classe sans clés étrangères####

class Effect : 
    repeated = bool
    good_type = str
    row_movement = int
    column_movement = int

    def __init__(self, repeated, good_type, row_movement, column_movement) :
        self.repeated = repeated
        self.good_type = good_type
        self.row_movement = row_movement
        self.column_movement = column_movement

class sector :
    valueSector = int

    def __init__(self, valueSector) :
        self.valueSector = valueSector

    #AddBuilding() : void

    #UpdateManche() : void

class Cost():
    number=int
    def __init__(self, number) :
        self.number = number 

class Ressource() :
    print("aaa")




#########################################################################

class Player : 

    points = int
    hasPlayed = bool
    buldinglist = []
    goodList = {}


    @abstractmethod
    def __init__(self, Points, HasPlayed,BuldingList, GoodList):
        self.points = Points
        self.hasPlayed = HasPlayed
        self.buldinglist = BuldingList
        self.goodList = GoodList

    #def Update()

    #def Sell()





class Good(Ressource): 

    name = str
    color = str

    def __init__(self, name, color):
        self.name = name
        self.color = color
    #isFood() : boolean


class building : 
    round = int
    name = str
    value = int
    function = str
    isOnBoard = bool
    player = Player
    effects = [] 
    cost = Cost

    def __init__(self, round, name,value,function,isOnBoard, player,effects,cost):
        self.round = round
        self.name = name
        self.value=value
        self.function=function
        self.isOnBoard=isOnBoard
        self.player = player
        self.effects = effects
        self.cost = cost

    def importBuilding() :
        for building in root.iter('building'):
            round = int(building.get('round'))
            name = building.get('name')
            value = int(building.get('value'))
            function = building.get('function')
            isOnBoard = False
            building(round, name, value, function, isOnBoard)
            print(name)
            print( )


class Warehouse :
    warehouse=[[]]
    warehouse = [[0 for i in range (6)] for j in range (6)]
    positionX = int
    positionY = int
    quantity = int 
    
    def __init__(self, warehouse, positionX, positionY) :
        self.warehouse=warehouse
        self.positionX = positionX
        self.positionY = positionY

    quantity=3*positionY + positionX

    
class IA(Player):
    print("aaa")



class Basic(IA):
    print("aaa")
    #search()
    #play()

class Advanced(IA):
    print("aaa")
    #searchWithIQ()
    #playWithIQ()

class Human(Player):
    name=str
    def __init__(self, name,Points, HasPlayed,BuldingList, GoodList) :
        self.name = name
        super().__init__(Points, HasPlayed,BuldingList, GoodList)


class Action():
    print("aaa")

    #Use() : boolean
    #BuyWithCash():boolean
    #BuyWithMaterials():boolean





class GameLogic():
    warehouseGraph=Warehouse.warehouse
    def afficher(warehouseGraph):
        for i in range (len(warehouseGraph)):
            for j in range (len(warehouseGraph[0])):
                print(warehouseGraph[i][j])





    

