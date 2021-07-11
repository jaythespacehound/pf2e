class Skills:
    """Base skills in the game"""
    def __init__(self):
        self.acrobatics = 0
        self.arcana = 0
        self.athletics = 0
        self.crafting = 0
        self.deception = 0
        self.diplomacy = 0
        self.intimidation = 0
        self.lores = {}
        self.medicine = 0
        self.nature = 0
        self.occultism = 0
        self.performance = 0
        self.religion = 0
        self.society = 0
        self.stealth = 0
        self.survival = 0
        self.thievery = 0
        
    def skill_names(self):
        """Returns all the names above (variables in this class)"""
        return(vars(self))
    
    def __str__(self):
        """Tells python print how to format these data"""
        return("\n".join("{:12} {}".format(k, v) for k, v in self.skill_names().items()))
    
    def update_skills(self, char):
        """Do the maths here to update the skills depending on attributes and proficiencies"""



class CharacterPathfinder2e:
    """ Base char class - all characters (PCs and NPCs/Monsters) have these traits:"""
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.hp = 0
        self.ac = 0
        self.fortitude = 0
        self.reflex = 0
        self.will = 0
        self.perception = 0
        self.speed = 0
        self.size = "medium"
        self.skills = Skills() #should maybe move to the playerClass
        

#This will move outside this file but for testing
aChar = CharacterPathfinder2e("Test Char")

print("Char name, willpower:")
print(aChar.name, aChar.will)
print()
print("Skills:")
print(aChar.skills.skill_names())
print(aChar.skills)


##not starting with a PLAYER character: better to have scalability than not
##class CharacterPathfinderSecondEdition - wow, 
##    - all characters (PCs and NPCs/Monsters) have these traits:
##    name
##    level - can be negative
##    hit points
##    AC
##    Fortitude
##    Reflex
##    Will
##    Perception
##    Speed
##    size
##    - not sure about this one - traits(humanoid, draconic, etc)
##    
##    class CharacterPlayer
##    - inherits everything from CharacterSecondEdition
##    - all player characters have:
##    ancestry - grants skill training and ability boosts
##    background- grants skill training and ability boosts
##    class - grants ability boost
##    d - aDventurer ability boost
##
##    proficiency from level
##    training in skills 
##    all skills:
##        Acrobatics
##        Arcana
##        Athletics
##        Crafting
##        Deception
##        Diplomacy
##        Intimidation
##        Lore
##        Medicine
##        Nature
##        Occultism
##        Performance
##        Religion
##        Society
##        Stealth
##        Survival
####        Thievery
##boolean dual-class
##boolean free archetype
##boolean ancestry paragon - actually relevant to level 1
##boolean starts at level 0
##boolean simplified ancestry
##boolean simplified skill feats
##boolean automatic bonus progression
##boolean proficiency without level - ugh, ruins balance
