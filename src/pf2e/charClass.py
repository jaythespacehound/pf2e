from math import floor

#This entire class can go die
# class Skills:
#     """Base skills in the game"""
#     #we may want to split this into two classes one inheriting the other with the functions so we can use the base list as a proficiency list also..
#     def __init__(self):
#         self.
#         self.acrobatics = 0
#         self.arcana = 0
#         self.athletics = 0
#         self.crafting = 0
#         self.deception = 0
#         self.diplomacy = 0
#         self.intimidation = 0
#         self.lores = {}
#         self.medicine = 0
#         self.nature = 0
#         self.occultism = 0
#         self.performance = 0
#         self.religion = 0
#         self.society = 0
#         self.stealth = 0
#         self.survival = 0
#         self.thievery = 0
        
#     def skill_names(self):
#         """Returns all the names above (variables in this class)"""
#         return(vars(self))
    
#     def __str__(self):
#         """Tells python print how to format these data"""
#         return("\n".join("{:12} {}".format(k, v) for k, v in self.skill_names().items()))
    
#     def update_skills(self, char): #This will never work because I am dumb - we could make it work but it would be dumb. We could make it work smarter but it would go against all coding practices. Just use a dict jay
#         """Do the maths here to update the skills depending on attributes (ability scores) and proficiencies"""
#         #if we had grouped skills by ability scores we could loop over them but I don't think it gains us much.
#         for skill, value in self.skill_names().items():
#             #haven't touched proficiencies yet
            
#             #strength skills
#             if skill in ['athletics']:
#                 value = char.abilities.mod("strength")
#             #dex skills
#             elif skill in ['acrobatics', 'stealth', 'thievery']:
#                 value = char.abilities.mod("dexterity")
#             #int skills - note we will need special case for lores
#             elif skill in ['arcana', 'crafting', 'occultism', 'society']:
#                 value = char.abilities.mod("intelligence")
#             #wis skills 
#             elif skill in ['medicine', 'nature', 'religion', 'survival']:
#                 value = char.abilities.mod("wisdom")
#             #cha skills 
#             elif skill in ['deception', 'diplomacy', 'intimidation', 'performance']:
#                 value = char.abilities.mod("charisma")
#             else:
#                 print("How to handle {} has not been coded yet".format(skill))


class AbilityScores:
    """Stores a characters ability scores and calculates the modifier"""
    def __init__(self):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def __str__(self):
        """Tells python print how to format these data"""
        return("\n".join("{:12} {}".format(k, v) for k, v in vars(self).items()))
    
    def mod_calc(self, ability):
        return(floor((ability - 10)/2))
    
    def mod(self, ability):
        #I'm sure there's a nicer way but it escapes me at present
        if ability == "strength":
            return(self.mod_calc(self.strength))
        elif ability == "dexterity":
            return(self.mod_calc(self.dexterity))
        elif ability == "constitution":
            return(self.mod_calc(self.constitution))
        elif ability == "intelligence":
            return(self.mod_calc(self.intelligence))
        elif ability == "wisdom":
            return(self.mod_calc(self.wisdom))
        elif ability == "charisma":
            return(self.mod_calc(self.charisma))
        else:
            return(-1)
        


        
            
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
        self.abilities = AbilityScores() #move to playerClass?
        self.skills = {
            "acrobatics" : 0,
            "arcana" : 0,
            "athletics" : 0,
            "crafting" : 0,
            "deception" : 0,
            "diplomacy" : 0,
            "intimidation" : 0,
            "lores" : {},
            "medicine" : 0,
            "nature" : 0,
            "occultism" : 0,
            "performance" : 0,
            "religion" : 0,
            "society" : 0,
            "stealth" : 0,
            "survival" : 0,
            "thievery" : 0
            }
        #I dislike the copy paste here but a skills class seemed really stupid given the advantages dicts have.
        #We could make a skills class holding the dict though but maybe overkill...
        self.proficiencies = {
            "acrobatics" : 0,
            "arcana" : 0,
            "athletics" : 0,
            "crafting" : 0,
            "deception" : 0,
            "diplomacy" : 0,
            "intimidation" : 0,
            "lores" : {},
            "medicine" : 0,
            "nature" : 0,
            "occultism" : 0,
            "performance" : 0,
            "religion" : 0,
            "society" : 0,
            "stealth" : 0,
            "survival" : 0,
            "thievery" : 0
            }

            
        #deprecated:
        # self.skills = Skills() #should maybe move to the playerClass

    def update_skills(self):
        """Do the maths here to update the skills depending on attributes (ability scores) and proficiencies"""
        #if we had grouped skills by ability scores we could loop over them but I don't think it gains us much.
        for skill in self.skills.keys():
            #strength skills
            if skill in ['athletics']:
                self.skills[skill] = self.abilities.mod("strength") + self.proficiencies[skill]
            #dex skills
            elif skill in ['acrobatics', 'stealth', 'thievery']:
                self.skills[skill] = self.abilities.mod("dexterity") + self.proficiencies[skill]
            #int skills - note we will need special case for lores
            elif skill in ['arcana', 'crafting', 'occultism', 'society']:
                self.skills[skill] = self.abilities.mod("intelligence") + self.proficiencies[skill]
            #wis skills 
            elif skill in ['medicine', 'nature', 'religion', 'survival']:
                self.skills[skill] = self.abilities.mod("wisdom") + self.proficiencies[skill]
            #cha skills 
            elif skill in ['deception', 'diplomacy', 'intimidation', 'performance']:
                self.skills[skill] = self.abilities.mod("charisma") + self.proficiencies[skill]
            else:
                print("How to handle {} has not been coded yet".format(skill))





#This will move outside this file but for testing
a_char = CharacterPathfinder2e("Test Char")

print("Char name, willpower:")
print(a_char.name, a_char.will)
print()
print("Skills:")
print(a_char.skills)
print()
print(a_char.abilities)
a_char.abilities.dexterity = 18
a_char.abilities.constitution = 14
a_char.abilities.intelligence = 12
a_char.abilities.charisma = 3
print(a_char.abilities)
print("str mod", a_char.abilities.mod("strength"))
print("dex mod",a_char.abilities.mod("dexterity"))
print("char mod",a_char.abilities.mod("charisma"))
a_char.update_skills()
print(a_char.skills)

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
