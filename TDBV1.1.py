# The Dark Below v0.1
# Re-writing with a data-centric approach
game_title = "The Dark Below"
game_version = "0.1"

# Creating the character
class Player(object):
    
    def __init__(self):
        self.inventory = []
        self.level = 0
        self.exp = 0
        self.exptolevel = 50
        self.str = 5
        self.dex = 5
        self.con = 5
        self.int = 5
        self.hp = 20
        self.hp_now = 20
        self.gold = 0
        self.updatestats()

    def newgame(self):
        self.item_permanence_element = Element('itempermanence')
        self.enemy_permanence_element = Element('enemypermanence')
        self.container_permanence_element = Element('containerpermanence')

    def updatestats(self):
        items_element = map_element.find('items')
        defbonus = 0


# Items
worldItems = {
    'Knife': {
        DESC: ,
        ATKBONUS: ,
        EQUIPTO: },
    'Cleaver': {
        DESC: ,
        ATKBONUS: ,
        EQUIPTO: False },
    'Health Potion': {
        DESC: ,
        EFFECT: ,
        EQUIPTO: False },
    'Key': {
        DESC: ,
        EFFECT: ,
        EQUIPTO: False },
}

# Rooms
worldRooms = { 
    'Entry': {
        DESC: 'The portal spits you out into a large, dark room, lit only by a single torch. It looks like you could pry the torch off the wall. Dim flickers of light come from two different passages, one to your left and one to your right.',
        NORTH: 'Altar',
        EAST: ,
        SOUTH: 'Dwelling',
        WEST: ,
        GROUND: ['Torch']},
    'Altar':{
        DESC: 'There is an altar of bones standing before you, with crude pewter icons. There is painting on the walls, in what looks like blood. Something shiny gleams on top of the rough surface. The path continues forward, into the dark, and back the way you came.',
        NORTH: ,
        EAST: ,
        SOUTH: 'Entry',
        WEST: ,
        GROUND: ['Knife', 'Health Potion']},
    'Dwelling':{
        DESC: ,
        NORTH: ,
        EAST: ,
        SOUTH: ,
        WEST: ,
        GROUND: []},
    'Kitchen':{
        DESC: ,
        NORTH: ,
        EAST: ,
        SOUTH: ,
        WEST: ,
        GROUND: ['Cleaver']},
    'Large Hall':{
        DESC: ,
        NORTH: ,
        EAST: ,
        SOUTH: ,
        WEST: ,
        GROUND: []},
    ''
    }
}