"""Contains the character classes for the pathfinder 2e character tracker"""
from math import floor
import weakref

class Skills:
    """Base skills in the game
       Used for both proficiencies and skills
    """
    def __init__(self, parent_char):
        #Keep a reference to the parent character so that we can refer to the chars attributes without having to pass the char.
        #Use weakref.proxy to prevent garbage collection issues if one instance is deleted without the other.
        #Will raise a ReferenceError exception if the proxy is accessed after the proxied item is removed.
        self.parent_char = weakref.proxy(parent_char)
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
        return([var for var in vars(self) if not var == "parent_char"])

    def __str__(self):
        """Tells python print how to format these data"""
        return "\n".join("{:12} {}".format(k, v) for k, v in vars(self).items() if not k == "parent_char")

class CharSkills(Skills):
    """Child class of Skills - as skills is also used for proficiencies but should not have the update_skills function"""
    def update_skills(self):
        """Do the maths here to update the skills depending on attributes (ability scores) and proficiencies"""
        #if we had grouped skills by ability scores we could loop over them but I don't think it gains us much.
        for skill in self.skill_names():
            #strength skills
            if skill in ['athletics']:
                setattr(self, skill, self.parent_char.abilities.mod("strength")
                        + getattr(self.parent_char.proficiencies, skill))
            #dex skills
            elif skill in ['acrobatics', 'stealth', 'thievery']:
                setattr(self, skill, self.parent_char.abilities.mod("dexterity")
                        + getattr(self.parent_char.proficiencies, skill))
            #int skills - note we will need special case for lores
            elif skill in ['arcana', 'crafting', 'occultism', 'society']:
                setattr(self, skill, self.parent_char.abilities.mod("intelligence")
                        + getattr(self.parent_char.proficiencies, skill))
            #wis skills
            elif skill in ['medicine', 'nature', 'religion', 'survival']:
                setattr(self, skill, self.parent_char.abilities.mod("wisdom")
                        + getattr(self.parent_char.proficiencies, skill))
            #cha skills4
            elif skill in ['deception', 'diplomacy', 'intimidation', 'performance']:
                setattr(self, skill, self.parent_char.abilities.mod("charisma")
                        + getattr(self.parent_char.proficiencies, skill))
            else:
                print("How to handle {} has not been coded yet".format(skill))


class SavingThrows:
    """Stores a characters saving throws"""
    def __init__(self, parent_char):
        self.parent_char = weakref.proxy(parent_char)
        self.fortitude = 0
        self.reflex = 0
        self.will = 0

    def update_saves(self):
        """Recalculates the characters saving throws"""
        self.fortitude = self.parent_char.abilities.mod('constitution') + self.parent_char.proficiencies.fortitude
        self.reflex = self.parent_char.abilities.mod('dexterity') + self.parent_char.proficiencies.reflex
        self.will = self.parent_char.abilities.mod('wisdom') + self.parent_char.proficiencies.will

    def __str__(self):
        """Tells python print how to format these data"""
        return "\n".join("{:12} {}".format(k, v) for k, v in vars(self).items() if not k == "parent_char")


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
        return "\n".join("{:12} {}".format(k, v) for k, v in vars(self).items())

    def mod_calc(self, ability):
        """Calculates (and returns) the ability modifier"""
        return floor((ability - 10)/2)

    def mod(self, ability):
        """Returns ability modifier given input string"""
        #I'm sure there's a nicer way but it escapes me at present
        if ability == "strength":
            return self.mod_calc(self.strength)
        elif ability == "dexterity":
            return self.mod_calc(self.dexterity)
        elif ability == "constitution":
            return self.mod_calc(self.constitution)
        elif ability == "intelligence":
            return self.mod_calc(self.intelligence)
        elif ability == "wisdom":
            return self.mod_calc(self.wisdom)
        elif ability == "charisma":
            return self.mod_calc(self.charisma)
        return -1


class CharacterPathfinder2e:
    """ Base char class - all characters (PCs and NPCs/Monsters) have these traits:"""
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.hp = 0
        self.ac = 10
        self.fortitude = 0
        self.reflex = 0
        self.will = 0
        self.perception = 0
        self.speed = 0
        self.size = "medium"
        self.abilities = AbilityScores()  #move to playerClass?
        self.skills = CharSkills(self) #pass self so that the skills can ref back to attributes #should maybe move to the playerClass?
        self.saves = SavingThrows(self)
        self.proficiencies = Skills(self) #should maybe move to the playerClass?
        #need to add more to profs class is no problem:
        self.proficiencies.perception = 0
        self.proficiencies.fortitude = 0
        self.proficiencies.reflex = 0
        self.proficiencies.will = 0
        #ac
        #class dc?






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
print("dex mod", a_char.abilities.mod("dexterity"))
print("char mod", a_char.abilities.mod("charisma"))
a_char.skills.update_skills()
print(a_char.skills)
a_char.saves.update_saves()
print(a_char.saves)

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
#OB#    ancestry - grants skill training and ability boosts
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
