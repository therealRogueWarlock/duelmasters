import pygame

card_dict = {
    "Darkness": {
        "BlackFeatherShadowofRage": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, destroy one of your creatures.",
            "Illustrator": "Soushi Hirose",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 3000,
            "Race": "Ghost",
            "Rarity": "Common",
        },
        "BloodySquito": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the "
                         "attack. Then the two creatures battle.) This creature can't attack. When this creature wins "
                         "a battle, destroy it.",
            "Illustrator": "Atsushi Kawasaki",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 4000,
            "Race": "Brain Jacker",
            "Rarity": "Common"
        },
        "BoneAssassintheRipper": {
            "Card Type": "Creature",
            "Card Text": "Slayer (When this creature loses a battle, destroy the other creature.)",
            "Illustrator": "Nottsuo",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 4000,
            "Race": "Living Dead",
            "Rarity": "Common"
        },
        "BoneSpider": {
            "Card Type": "Creature",
            "Card Text": "When this creature wins a battle, destroy it.",
            "Illustrator": "Dai",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 5000,
            "Race": "Living Dead",
            "Rarity": "Uncommon"
        },
        "CreepingPlague": {
            "Card Type": "Spell",
            "Card Text": "Whenever any of your creatures becomes blocked this turn, it gets \"slayer\" until the end "
                         "of the turn. (When a creature that has \"slayer\" loses a battle, destroy the other "
                         "creature.)",
            "Illustrator": "Ryoya Yuki",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": "None",
            "Race": "None",
            "Rarity": "Rare"
        },
        "DarkClown": {
            "Card Type": "Creature",
            "Card Text": "Blocker Blocker (When an opponent's creature attacks, you may tap this creature to stop the "
                         "attack. Then the two creatures battle.) This creature can't attack. When this creature wins "
                         "a battle, destroy it.",
            "Illustrator": "Jason",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 6000,
            "Race": "Brain Jacker",
            "Rarity": "Rare"
        },
        "DarkRavenShadowofGrief": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. "
                         "Then the two creatures battle.)",
            "Illustrator": "Norikatsu Miyoshi",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 1000,
            "Race": "Ghost",
            "Rarity": "Uncommon"
        },
        "DarkReversal": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger (When this spell is put into your hand from your shield zone, you may cast "
                         "it for no cost.)Return a creature from your graveyard to your hand.",
            "Illustrator": "Nottsuo",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": "None",
            "Race": "None",
            "Rarity": "Uncommon"
        },
        "DeathSmoke": {
            "Card Type": "Spell",
            "Card Text": "Destroy one of your opponent's untapped creatures.",
            "Illustrator": "Dustmoss",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": "None",
            "Race": "None",
            "Rarity": "Common"
        },
        "GhostTouch": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger (When this spell is put into your hand from your shield zone, you may cast "
                         "it for no cost.)Your opponent discards a card at random from his hand.",
            "Illustrator": "Soushi Hirose",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": "None",
            "Race": "None",
            "Rarity": "Common"
        },
        "Gigaberos": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, destroy 2 of your creatures or destroy "
                         "this creature.Double breaker (This creature breaks 2 shields.)",
            "Illustrator": "Katsuya",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 8000,
            "Race": "Chimera",
            "Rarity": "Rare"
        },
        "Gigagiele": {
            "Card Type": "Creature",
            "Card Text": "Slayer (When this creature loses a battle, destroy the other creature.)",
            "Illustrator": "Hisashi Momose",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 3000,
            "Race": "Chimera",
            "Rarity": "Rare"
        },
        "Gigargon": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, return up to 2 creatures from your "
                         "graveyard to your hand.",
            "Illustrator": "Tsutomu Kawade",
            "Mana": 1,
            "Mana Cost": 8,
            "Power": 3000,
            "Race": "Chimera",
            "Rarity": "Very Rare"
        },
        "MaskedHorrorShadowofScorn": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, your opponent discards a card at random "
                         "from his hand.",
            "Illustrator": "Gyokan",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 1000,
            "Race": "Ghost",
            "Rarity": "Uncommon"
        },
        "NightMasterShadowofDecay": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. "
                         "Then the two creatures battle.)",
            "Illustrator": "Hideaki Takamura",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 3000,
            "Race": "Ghost",
            "Rarity": "Rare"
        },
        "SkeletonSoldiertheDefiled": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Katsuya",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Living Dead",
            "Rarity": "Common"
        },
        "StingerWorm": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, destroy one of your creatures.",
            "Illustrator": "Norikatsu Miyoshi",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 5000,
            "Race": "Parasite Worm",
            "Rarity": "Uncommon"
        },
        "SwampWorm": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, your opponent chooses one of his creatures "
                         "and destroys it",
            "Illustrator": "\tYouichi Kai",
            "Mana": 1,
            "Mana Cost": 7,
            "Power": 2000,
            "Race": "Parasite Worm",
            "Rarity": "Uncommon"
        },
        "TerrorPit": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger (When this spell is put into your hand from your shield zone, you may cast "
                         "it for no cost.)Destroy one of your opponent's creatures.",
            "Illustrator": "Yusaku Nakaaki",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": "None",
            "Race": "None",
            "Rarity": "Rare"
        },
        "VampireSilphy": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, destroy all creatures that have power 3000 "
                         "or less.",
            "Illustrator": "Masaki Hirooka",
            "Mana": 1,
            "Mana Cost": 8,
            "Power": 4000,
            "Race": "Dark Lord",
            "Rarity": "Vary Rare"
        },
        "WanderingBraineater": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. "
                         "Then the two creatures battle.)This creature can't attack.",
            "Illustrator": "Youichi Kai",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 2000,
            "Race": "Living Dead",
            "Rarity": "Common"
        },
        "WrithingBoneGhoul": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Eiji Kaneda",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 2000,
            "Race": "Living Dead",
            "Rarity": "Common"
        },
        "ZagaanKnightofDarkness": {
            "Card Type": "Creature",
            "Card Text": "Double breaker",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 7000,
            "Race": "Demon command",
            "Rarity": "Super rare"
        }
    },
    "Light": {
        "ChiliasTheOracle": {
            "Card Type": "Creature",
            "Card Text": "When this creature would be destroyed, put it into your hand instead.",
            "Illustrator": "Akira Hamada",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 2500,
            "Race": "Light Bringer",
            "Rarity": "Rare"
        },
        "DiaNorkMoonlightGuardian": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. "
                         "Then the two creatures battle.)This creature can't attack players.",
            "Illustrator": "Tomofumi Ogasawara",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 5000,
            "Race": "Guardian",
            "Rarity": "Rare"
        },
        "EmeraldGrass": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)This creature can't attack players.",
            "Illustrator": "Daisuke Izuka",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 3000,
            "Race": "Starlight Tree",
            "Rarity": "Common"
        },
        "FreiVizierofAir": {
            "Card Type": "Creature",
            "Card Text": "At the end of each of your turns, you may untap this creature.",
            "Illustrator": "Yusaku Nakaaki",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Initiate",
            "Rarity": "Uncommon"
        },
        "GranGureSpaceGuardian": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)This creature can't attack players.",
            "Illustrator": "D-Suzuki",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 9000,
            "Race": "Guardian",
            "Rarity": "Very Rare"
        },
        "HolyAwe": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger (When this spell is put into your hand from your shield zone, you may cast it for no cost.)Tap all your opponent's creatures in the battle zone.",
            "Illustrator": "Naoki Saito",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": "None",
            "Race": "None",
            "Rarity": "Rare"
        },
        "IereVizierofBullets": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Daisuke Izuka",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 3000,
            "Race": "Initiate",
            "Rarity": "Common"
        },
        "IocanttheOracle": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)\n■ While you have at least 1 Angel Command in the battle zone, this creature gets +2000 power.\n\n■ This creature can't attack players.",
            "Illustrator": "Naoki Saito",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 2000,
            "Race": "Light Bringer",
            "Rarity": "Uncommon"
        },
        "LaUraGigaSkyGuardian": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)\n■ This creature can't attack players.",
            "Illustrator": "Kou1",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 2000,
            "Race": "Guardian",
            "Rarity": "Common"
        },
        "LahPurificationEnforcer": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Hideaki Takamura",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 5500,
            "Race": "Berserker",
            "Rarity": "Rare"
        },
        "LaserWing": {
            "Card Type": "Spell",
            "Card Text": "Choose up to 2 of your creatures in the battle zone. They can't be blocked this turn.",
            "Illustrator": "Gyokan",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": "None",
            "Race": "None",
            "Rarity": "Rare"
        },
        "LokVizierofHunting": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Hisanobu Kometani",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 4000,
            "Race": "Initiate",
            "Rarity": "Uncommon"
        },
        "MieleVizierofLightning": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, you may choose one of your opponent's creatures in the battle zone and tap it.",
            "Illustrator": "Dai",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 1000,
            "Race": "Initiate",
            "Rarity": "Common"
        },
        "MoonlightFlash": {
            "Card Type": "Spell",
            "Card Text": "Choose up to 2 of your opponent's creatures in the battle zone and tap them.",
            "Illustrator": "Hisanobu Kometani",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": "None",
            "Race": "None",
            "Rarity": "Uncommon"
        },
        "RaylaTruthEnforcer": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, search your deck. You may take a spell from your deck, show that spell to your opponent, and put it into your hand. Then shuffle your deck.",
            "Illustrator": "Dai",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 3000,
            "Race": "Berserker",
            "Rarity": "Very Rare"
        },
        "Reusol,TheOracle": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "Soushi Hirose",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 2000,
            "Race": "Light Bringer",
            "Rarity": "Common"
        },
        "RubyGrass": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)\n■ This creature can't attack players.\n\n■ At the end of each of your turns, you may untap this creature.",
            "Illustrator": "Naoki Saito",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 3000,
            "Race": "Starlight tree",
            "Rarity": "Uncommon"
        },
        "SenatineJadeTree": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)\n■ This creature can't attack players.",
            "Illustrator": "Norikatsu Miyoshi",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 4000,
            "Race": "Starlight Tree",
            "Rarity": "Common"
        },
        "SolarRay": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger (When this spell is put into your hand from your shield zone, you may cast it for no cost.)\n■ Choose one of your opponent's creatures in the battle zone and tap it.",
            "Illustrator": "Jason",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": "None",
            "Race": "None",
            "Rarity": "Common"
        },
        "SonicWing": {
            "Card Type": "Spell",
            "Card Text": "Choose one of your creatures in the battle zone. It can't be blocked this turn.",
            "Illustrator": "Masaki Hirooka",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": "None",
            "Race": "None",
            "Rarity": "Common"
        },
        "SzubsKinTwilightGuardian": {
            "Card Type": "Creature",
            "Card Text": "Blocker (When an opponent's creature attacks, you may tap this creature to stop the attack. Then the two creatures battle.)\n■ This creature can't attack players.",
            "Illustrator": "Ittoku",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 6000,
            "Race": "Guardian",
            "Rarity": "Rare"
        },
        "ToelVizierofHope": {
            "Card Type": "Creature",
            "Card Text": "At the end of each of your turns, you may untap all your creatures in the battle zone.",
            "Illustrator": "Masaki Hirooka",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 2000,
            "Race": "Initiate",
            "Rarity": "Uncommon"
        },
        "UrthPurifyingElemental": {
            "Card Type": "Creature",
            "Card Text": "Double Breaker\n At the end of each of your turn, you may untap this creature.",
            "Illustrator": "Masaki Hirooka",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 6000,
            "Race": "Angel command",
            "Rarity": "Super rare"
        }
    },
    "Fire": {
        "ArmoredWalkerUrherion": {
            "Card Type": "Creature",
            "Card Text": "While you have at least 1 human in the battle zone, "
                         "this creature gets +2000 power during its attacks.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Armorloid",
            "Rarity": "Uncommon"
        },
        "ArtisanPicora": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone, "
                         "put 1 card from your mana zone into your graveyard.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 2000,
            "Race": "Machine eater",
            "Rarity": "Common"
        },
        "AstrocometDragon": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +4000\n Double breaker",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 7,
            "Power": 6000,
            "Race": "Amored dragon",
            "Rarity": "Super rare"
        },
        "BolshackDragon": {
            "Card Type": "Creature",
            "Card Text": "While attacking, this creature gets +1000 power\n"
                         "for each fire card in you graveyard.\n Double breaker",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 6000,
            "Race": "Amored dragon",
            "Rarity": "Super rare"
        },
        "BrawlerZyler": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 1000,
            "Race": "Human",
            "Rarity": "Common"
        },
        "BurningPower": {
            "Card Type": "Spell",
            "Card Text": """One of your creatures gets "power attacker +2000" until the end of the turn.""",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 0,
            "Race": "None",
            "Rarity": "Common"
        },
        "ChaosStrike": {
            "Card Type": "Spell",
            "Card Text": "Choose 1 of your opponents's untapped creatures\nin the battle zone. "
                         "Your creatures can attack it this\nturn as though it were tapped.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 0,
            "Race": "None",
            "Rarity": "rare"
        },
        "DeadlyFighterBraidClaw": {
            "Card Type": "Creature",
            "Card Text": "This creature attacks each turn if able.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 1000,
            "Race": "Dragonoid",
            "Rarity": "common"
        },
        "Draglide": {
            "Card Type": "Creature",
            "Card Text": "This creature attacks each turn if able.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 5000,
            "Race": "Armored wyvern",
            "Rarity": "Rare"
        },
        "ExplosiveFighterUvarn": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone,\n"
                         "put 2 cards from you mana zone into your\ngraveyard.\n"
                         "Double breaker",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 9000,
            "Race": "Dragonoid",
            "Rarity": "Rare"
        },
        "FatalAttackerHorvath": {
            "Card Type": "Creature",
            "Card Text": "While you have at least 1 armorloid in the battle\n zone, this creature gets"
                         "+2000 power during its attacks.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 2000,
            "Race": "Human",
            "Rarity": "common"
        },
        "FireSweeperBurningHellion": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Dragonoid",
            "Rarity": "common"
        },
        "GatlingSkyterror": {
            "Card Type": "creature",
            "Card Text": "This creature can attack untapped creatures.\n Double breaker.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 7,
            "Power": 7000,
            "Race": "Armored wyvern",
            "Rarity": "Super rare"
        },
        "ImmortalBaronVorg": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 2000,
            "Race": "Human",
            "Rarity": "common"
        },
        "Meteosaur": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone\n"
                         "you may destroy 1 of your opponents's ceatures\nthat has power 2000 or less",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 2000,
            "Race": "Rock beast",
            "Rarity": "Rare"
        },
        "NomadHeroGigio": {
            "Card Type": "Creature",
            "Card Text": "This creature can attack untapped creatures",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 3000,
            "Race": "Machine eater",
            "Rarity": "Rare"
        },
        "OnslaughterTriceps": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle\n"
                         "zone, put 1 card from you manazone into your\ngraveyard.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 5000,
            "Race": "Dragonoid",
            "Rarity": "Rare"
        },
        "RothusTheTraveler": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle\nzone, "
                         "destroy one of your creatures. then your\nopponent chooses one of "
                         "his creatures and destroys is.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 4000,
            "Race": "Armorloid",
            "Rarity": "Rare"
        },
        "ScarletSkyterror": {
            "Card Type": "Spell",
            "Card Text": """When you put this creature into the battle zone,\n
                            destroy all creatures that have "blocker".""",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 8,
            "Power": 3000,
            "Race": "Armored wyvern",
            "Rarity": "Super Rare"
        },
        "Stonesaur": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 4000,
            "Race": "Rock beast",
            "Rarity": "Uncommon"
        },
        "SuperExplosiveVolcanodon": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +4000",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 2000,
            "Race": "Dragonoid",
            "Rarity": "Uncommon"
        },
        "Tornado_Flame": {
            "Card Type": "Creature",
            "Card Text": "Shield trigger\n"
                         "Destroy 1 of your opponent's creature that has power 4000 or less.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 0,
            "Race": "None",
            "Rarity": "Uncommon"
        }
    },
    "Nature": {
        "AuraBlast": {
            "Card Type": "Spell",
            "Card Text": """Each of your creatures in the battle zone gets 
                            "power attacker +200" until the end of the turn.""",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 0,
            "Race": "None",
            "Rarity": "Rare"
        },
        "BurningMane": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 0,
            "Race": "Beast folk ",
            "Rarity": "common"
        },
        "CoilingVines": {
            "Card Type": "Creature",
            "Card Text": "When this creature would be destoyed, put it into your mana zone instead.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Tree folk ",
            "Rarity": "uncommon"
        },
        "DeathbladeBeetle": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +4000\n"
                         "Double breaker.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 3000,
            "Race": "Giant insect",
            "Rarity": "Super rare"
        },
        "DimensionGate": {
            "Card Type": "spell",
            "Card Text": "Shield trigger\n"
                         "Search you deck. You may take a creature\nfrom you deck, "
                         "show the creature to your opponent, and put it into your\n"
                         "hand. then shuffle your deck.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 0,
            "Race": "None",
            "Rarity": "common"
        },
        "BronzeArmTribe": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone,\n "
                         "put the top card of your deck into your mana zone.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 1000,
            "Race": "Beast folk ",
            "Rarity": "common"
        },
        "DomeShell": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 3000,
            "Race": "Colony beetle",
            "Rarity": "uncommon"
        },
        "FearFang": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 3000,
            "Race": "Beast folk",
            "Rarity": "common"
        },
        "ForestHornet": {
            "Card Type": "Creature",
            "Card Text": "",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 4000,
            "Race": "Giant insect",
            "Rarity": "uncommon"
        },
        "GoldenWingStriker": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 2000,
            "Race": "Beast folk",
            "Rarity": "common"
        },
        "MightyShouter": {
            "Card Type": "Creature",
            "Card Text": "When this creature would be destroyed, put it into your mana zone instead.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 3,
            "Power": 2000,
            "Race": "Beast folk",
            "Rarity": "common"
        },
        "NaturalSnare": {
            "Card Type": "Spell",
            "Card Text": "Shield trigger\n"
                         "Choose one of your opponent's creatures in the\n"
                         "battle zone and put it into his mana zone.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 6,
            "Power": 0,
            "Race": "None",
            "Rarity": "Rare"
        },
        "PangaesSong": {
            "Card Type": "Spell",
            "Card Text": "Put 1 of your creatures from the battle zone into your mana zone.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 1,
            "Power": 0,
            "Race": "None",
            "Rarity": "uncommon"
        },
        "PoisonousDahlia": {
            "Card Type": "Creature",
            "Card Text": "This creature can't attack players.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 4,
            "Power": 5000,
            "Race": "Tree folk",
            "Rarity": "Uncommon"
        },
        "PoisonousMushroom": {
            "Card Type": "Creature",
            "Card Text": "When you put this creature into the battle zone,\n "
                         "you may put 1 card from your hand into your mana zone.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 1000,
            "Race": "Balloon mushroom",
            "Rarity": "Uncommon"
        },
        "RedEyeScorpion": {
            "Card Type": "Creature",
            "Card Text": "When this creature would be destroyed,\n put it into your mana zone instead.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 4000,
            "Race": "Giant insect",
            "Rarity": "Rare"
        },
        "RoaringGreatHorn": {
            "Card Type": "Creature",
            "Card Text": "Power attacker +2000\n"
                         "Double breaker",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 7,
            "Power": 8000,
            "Race": "Horned beast",
            "Rarity": "Super rare"
        },
        "StampedingLonghorn": {
            "Card Type": "Creature",
            "Card Text": "This creature can't be blocked by any creature\n that has power 3000 or less.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 5,
            "Power": 4000,
            "Race": "Horned beast",
            "Rarity": "Rare"
        },
        "SteelSmasher": {
            "Card Type": "Creature",
            "Card Text": "This creature can't attack players.",
            "Illustrator": "someone",
            "Mana": 1,
            "Mana Cost": 2,
            "Power": 3000,
            "Race": "Beast Folk",
            "Rarity": "common"
        },
    }
}
