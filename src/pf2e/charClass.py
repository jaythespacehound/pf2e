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
