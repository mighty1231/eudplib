from eudtrg import LICENSE  # @UnusedImport

UnitNameDict = {
    "Terran Marine": 0,
    "Terran Ghost": 1,
    "Terran Vulture": 2,
    "Terran Goliath": 3,
    "Goliath Turret": 4,
    "Terran Siege Tank (Tank Mode)": 5,
    "Siege Tank Turret (Tank Mode)": 6,
    "Terran SCV": 7,
    "Terran Wraith": 8,
    "Terran Science Vessel": 9,
    "Gui Montag (Firebat)": 10,
    "Terran Dropship": 11,
    "Terran Battlecruiser": 12,
    "Spider Mine": 13,
    "Nuclear Missile": 14,
    "Terran Civilian": 15,
    "Sarah Kerrigan (Ghost)": 16,
    "Alan Schezar (Goliath)": 17,
    "Alan Schezar Turret": 18,
    "Jim Raynor (Vulture)": 19,
    "Jim Raynor (Marine)": 20,
    "Tom Kazansky (Wraith)": 21,
    "Magellan (Science Vessel)": 22,
    "Edmund Duke (Tank Mode)": 23,
    "Edmund Duke Turret (Tank Mode)": 24,
    "Edmund Duke (Siege Mode)": 25,
    "Edmund Duke Turret (Siege Mode)": 26,
    "Arcturus Mengsk (Battlecruiser)": 27,
    "Hyperion (Battlecruiser)": 28,
    "Norad II (Battlecruiser)": 29,
    "Terran Siege Tank (Siege Mode)": 30,
    "Siege Tank Turret (Siege Mode)": 31,
    "Terran Firebat": 32,
    "Scanner Sweep": 33,
    "Terran Medic": 34,
    "Zerg Larva": 35,
    "Zerg Egg": 36,
    "Zerg Zergling": 37,
    "Zerg Hydralisk": 38,
    "Zerg Ultralisk": 39,
    "Zerg Broodling": 40,
    "Zerg Drone": 41,
    "Zerg Overlord": 42,
    "Zerg Mutalisk": 43,
    "Zerg Guardian": 44,
    "Zerg Queen": 45,
    "Zerg Defiler": 46,
    "Zerg Scourge": 47,
    "Torrasque (Ultralisk)": 48,
    "Matriarch (Queen)": 49,
    "Infested Terran": 50,
    "Infested Kerrigan (Infested Terran)": 51,
    "Unclean One (Defiler)": 52,
    "Hunter Killer (Hydralisk)": 53,
    "Devouring One (Zergling)": 54,
    "Kukulza (Mutalisk)": 55,
    "Kukulza (Guardian)": 56,
    "Yggdrasill (Overlord)": 57,
    "Terran Valkyrie": 58,
    "Mutalisk Cocoon": 59,
    "Protoss Corsair": 60,
    "Protoss Dark Templar (Unit)": 61,
    "Zerg Devourer": 62,
    "Protoss Dark Archon": 63,
    "Protoss Probe": 64,
    "Protoss Zealot": 65,
    "Protoss Dragoon": 66,
    "Protoss High Templar": 67,
    "Protoss Archon": 68,
    "Protoss Shuttle": 69,
    "Protoss Scout": 70,
    "Protoss Arbiter": 71,
    "Protoss Carrier": 72,
    "Protoss Interceptor": 73,
    "Protoss Dark Templar (Hero)": 74,
    "Zeratul (Dark Templar)": 75,
    "Tassadar/Zeratul (Archon)": 76,
    "Fenix (Zealot)": 77,
    "Fenix (Dragoon)": 78,
    "Tassadar (Templar)": 79,
    "Mojo (Scout)": 80,
    "Warbringer (Reaver)": 81,
    "Gantrithor (Carrier)": 82,
    "Protoss Reaver": 83,
    "Protoss Observer": 84,
    "Protoss Scarab": 85,
    "Danimoth (Arbiter)": 86,
    "Aldaris (Templar)": 87,
    "Artanis (Scout)": 88,
    "Rhynadon (Badlands Critter)": 89,
    "Bengalaas (Jungle Critter)": 90,
    "Cargo Ship (Unused)": 91,
    "Mercenary Gunship (Unused)": 92,
    "Scantid (Desert Critter)": 93,
    "Kakaru (Twilight Critter)": 94,
    "Ragnasaur (Ashworld Critter)": 95,
    "Ursadon (Ice World Critter)": 96,
    "Lurker Egg": 97,
    "Raszagal (Corsair)": 98,
    "Samir Duran (Ghost)": 99,
    "Alexei Stukov (Ghost)": 100,
    "Map Revealer": 101,
    "Gerard DuGalle (BattleCruiser)": 102,
    "Zerg Lurker": 103,
    "Infested Duran (Infested Terran)": 104,
    "Disruption Web": 105,
    "Terran Command Center": 106,
    "Terran Comsat Station": 107,
    "Terran Nuclear Silo": 108,
    "Terran Supply Depot": 109,
    "Terran Refinery": 110,
    "Terran Barracks": 111,
    "Terran Academy": 112,
    "Terran Factory": 113,
    "Terran Starport": 114,
    "Terran Control Tower": 115,
    "Terran Science Facility": 116,
    "Terran Covert Ops": 117,
    "Terran Physics Lab": 118,
    "Starbase (Unused)": 119,
    "Terran Machine Shop": 120,
    "Repair Bay (Unused)": 121,
    "Terran Engineering Bay": 122,
    "Terran Armory": 123,
    "Terran Missile Turret": 124,
    "Terran Bunker": 125,
    "Norad II (Crashed)": 126,
    "Ion Cannon": 127,
    "Uraj Crystal": 128,
    "Khalis Crystal": 129,
    "Infested Command Center": 130,
    "Zerg Hatchery": 131,
    "Zerg Lair": 132,
    "Zerg Hive": 133,
    "Zerg Nydus Canal": 134,
    "Zerg Hydralisk Den": 135,
    "Zerg Defiler Mound": 136,
    "Zerg Greater Spire": 137,
    "Zerg Queen's Nest": 138,
    "Zerg Evolution Chamber": 139,
    "Zerg Ultralisk Cavern": 140,
    "Zerg Spire": 141,
    "Zerg Spawning Pool": 142,
    "Zerg Creep Colony": 143,
    "Zerg Spore Colony": 144,
    "Unused Zerg Building1": 145,
    "Zerg Sunken Colony": 146,
    "Zerg Overmind (With Shell)": 147,
    "Zerg Overmind": 148,
    "Zerg Extractor": 149,
    "Mature Chrysalis": 150,
    "Zerg Cerebrate": 151,
    "Zerg Cerebrate Daggoth": 152,
    "Unused Zerg Building2": 153,
    "Protoss Nexus": 154,
    "Protoss Robotics Facility": 155,
    "Protoss Pylon": 156,
    "Protoss Assimilator": 157,
    "Unused Protoss Building1": 158,
    "Protoss Observatory": 159,
    "Protoss Gateway": 160,
    "Unused Protoss Building2": 161,
    "Protoss Photon Cannon": 162,
    "Protoss Citadel of Adun": 163,
    "Protoss Cybernetics Core": 164,
    "Protoss Templar Archives": 165,
    "Protoss Forge": 166,
    "Protoss Stargate": 167,
    "Stasis Cell/Prison": 168,
    "Protoss Fleet Beacon": 169,
    "Protoss Arbiter Tribunal": 170,
    "Protoss Robotics Support Bay": 171,
    "Protoss Shield Battery": 172,
    "Khaydarin Crystal Formation": 173,
    "Protoss Temple": 174,
    "Xel'Naga Temple": 175,
    "Mineral Field (Type 1)": 176,
    "Mineral Field (Type 2)": 177,
    "Mineral Field (Type 3)": 178,
    "Cave (Unused)": 179,
    "Cave-in (Unused)": 180,
    "Cantina (Unused)": 181,
    "Mining Platform (Unused)": 182,
    "Independent Command Center (Unused)": 183,
    "Independent Starport (Unused)": 184,
    "Independent Jump Gate (Unused)": 185,
    "Ruins (Unused)": 186,
    "Khaydarin Crystal Formation (Unused)": 187,
    "Vespene Geyser": 188,
    "Warp Gate": 189,
    "Psi Disrupter": 190,
    "Zerg Marker": 191,
    "Terran Marker": 192,
    "Protoss Marker": 193,
    "Zerg Beacon": 194,
    "Terran Beacon": 195,
    "Protoss Beacon": 196,
    "Zerg Flag Beacon": 197,
    "Terran Flag Beacon": 198,
    "Protoss Flag Beacon": 199,
    "Power Generator": 200,
    "Overmind Cocoon": 201,
    "Dark Swarm": 202,
    "Floor Missile Trap": 203,
    "Floor Hatch (Unused)": 204,
    "Left Upper Level Door": 205,
    "Right Upper Level Door": 206,
    "Left Pit Door": 207,
    "Right Pit Door": 208,
    "Floor Gun Trap": 209,
    "Left Wall Missile Trap": 210,
    "Left Wall Flame Trap": 211,
    "Right Wall Missile Trap": 212,
    "Right Wall Flame Trap": 213,
    "Start Location": 214,
    "Flag": 215,
    "Young Chrysalis": 216,
    "Psi Emitter": 217,
    "Data Disc": 218,
    "Khaydarin Crystal": 219,
    "Mineral Cluster Type 1": 220,
    "Mineral Cluster Type 2": 221,
    "Protoss Vespene Gas Orb Type 1": 222,
    "Protoss Vespene Gas Orb Type 2": 223,
    "Zerg Vespene Gas Sac Type 1": 224,
    "Zerg Vespene Gas Sac Type 2": 225,
    "Terran Vespene Gas Tank Type 1": 226,
    "Terran Vespene Gas Tank Type 2": 227,
    "(any unit)": 229,
    "(men)": 230,
    "(buildings)": 231,
    "(factories)": 232
}


# Data from http://cafe.daum.net/rpgguild/6cWR/158
# Original data from ScAIEdit
AIScriptDict = {
    # Custom AI Scripts
    'Terran Custom Level': b'TMCu',
    'Zerg Custom Level': b'ZMCu',
    'Protoss Custom Level': b'PMCu',
    'Terran Expansion Custom Level': b'TMCx',
    'Zerg Expansion Custom Level': b'ZMCx',
    'Protoss Expansion Custom Level': b'PMCx',
    'Terran Campaign Easy': b'TLOf',
    'Terran Campaign Medium': b'TMED',
    'Terran Campaign Difficult': b'THIf',
    'Terran Campaign Insane': b'TSUP',
    'Terran Campaign Area Town': b'TARE',
    'Zerg Campaign Easy': b'ZLOf',
    'Zerg Campaign Medium': b'ZMED',
    'Zerg Campaign Difficult': b'ZHIf',
    'Zerg Campaign Insane': b'ZSUP',
    'Zerg Campaign Area Town': b'ZARE',
    'Protoss Campaign Easy': b'PLOf',
    'Protoss Campaign Medium': b'PMED',
    'Protoss Campaign Difficult': b'PHIf',
    'Protoss Campaign Insane': b'PSUP',
    'Protoss Campaign Area Town': b'PARE',
    'Expansion Terran Campaign Easy': b'TLOx',
    'Expansion Terran Campaign Medium': b'TMEx',
    'Expansion Terran Campaign Difficult': b'THIx',
    'Expansion Terran Campaign Insane': b'TSUx',
    'Expansion Terran Campaign Area Town': b'TARx',
    'Expansion Zerg Campaign Easy': b'ZLOx',
    'Expansion Zerg Campaign Medium': b'ZMEx',
    'Expansion Zerg Campaign Difficult': b'ZHIx',
    'Expansion Zerg Campaign Insane': b'ZSUx',
    'Expansion Zerg Campaign Area Town': b'ZARx',
    'Expansion Protoss Campaign Easy': b'PLOx',
    'Expansion Protoss Campaign Medium': b'PMEx',
    'Expansion Protoss Campaign Difficult': b'PHIx',
    'Expansion Protoss Campaign Insane': b'PSUx',
    'Expansion Protoss Campaign Area Town': b'PARx',
    'Send All Units on Strategic Suicide Missions': b'Suic',
    'Send All Units on Random Suicide Missions': b'SuiR',
    'Switch Computer Player to Rescue Passive': b'Rscu',
    'Turn ON Shared Vision for Player 1': b'+Vi0',
    'Turn ON Shared Vision for Player 2': b'+Vi1',
    'Turn ON Shared Vision for Player 3': b'+Vi2',
    'Turn ON Shared Vision for Player 4': b'+Vi3',
    'Turn ON Shared Vision for Player 5': b'+Vi4',
    'Turn ON Shared Vision for Player 6': b'+Vi5',
    'Turn ON Shared Vision for Player 7': b'+Vi6',
    'Turn ON Shared Vision for Player 8': b'+Vi7',
    'Turn OFF Shared Vision for Player 1': b'-Vi0',
    'Turn OFF Shared Vision for Player 2': b'-Vi1',
    'Turn OFF Shared Vision for Player 3': b'-Vi2',
    'Turn OFF Shared Vision for Player 4': b'-Vi3',
    'Turn OFF Shared Vision for Player 5': b'-Vi4',
    'Turn OFF Shared Vision for Player 6': b'-Vi5',
    'Turn OFF Shared Vision for Player 7': b'-Vi6',
    'Turn OFF Shared Vision for Player 8': b'-Vi7',
    'Move Dark Templars to Region': b'MvTe',
    'Clear Previous Combat Data': b'ClrC',
    'Set Player to Enemy': b'Enmy',
    'Set Player to Ally  ': b'y   ',
    'Value This Area Higher': b'VluA',
    'Enter Closest Bunker': b'EnBk',
    'Set Generic Command Target': b'StTg',
    'Make These Units Patrol': b'StPt',
    'Enter Transport': b'EnTr',
    'Exit Transport': b'ExTr',
    'AI Nuke Here': b'NuHe',
    'AI Harass Here': b'HaHe',
    'Set Unit Order To: Junk Yard Dog': b'JYDg',
    'Disruption Web Here': b'DWHe',
    'Recall Here': b'ReHe',

    # StarCraft AI Scripts
    'Terran 3 - Zerg Town': b'Ter3',
    'Terran 5 - Terran Main Town': b'Ter5',
    'Terran 5 - Terran Harvest Town': b'Te5H',
    'Terran 6 - Air Attack Zerg': b'Ter6',
    'Terran 6 - Ground Attack Zerg': b'Te6b',
    'Terran 6 - Zerg Support Town': b'Te6c',
    'Terran 7 - Bottom Zerg Town': b'Ter7',
    'Terran 7 - Right Zerg Town': b'Te7s',
    'Terran 7 - Middle Zerg Town': b'Te7m',
    'Terran 8 - Confederate Town': b'Ter8',
    'Terran 9 - Light Attack': b'Tr9L',
    'Terran 9 - Heavy Attack': b'Tr9H',
    'Terran 10 - Confederate Towns': b'Te10',
    'Terran 11 - Zerg Town': b'T11z',
    'Terran 11 - Lower Protoss Town': b'T11a',
    'Terran 11 - Upper Protoss Town': b'T11b',
    'Terran 12 - Nuke Town': b'T12N',
    'Terran 12 - Phoenix Town': b'T12P',
    'Terran 12 - Tank Town': b'T12T',
    'Terran 1 - Electronic Distribution': b'TED1',
    'Terran 2 - Electronic Distribution': b'TED2',
    'Terran 3 - Electronic Distribution': b'TED3',
    'Terran 1 - Shareware': b'TSW1',
    'Terran 2 - Shareware': b'TSW2',
    'Terran 3 - Shareware': b'TSW3',
    'Terran 4 - Shareware': b'TSW4',
    'Terran 5 - Shareware': b'TSW5',
    'Zerg 1 - Terran Town': b'Zer1',
    'Zerg 2 - Protoss Town': b'Zer2',
    'Zerg 3 - Terran Town': b'Zer3',
    'Zerg 4 - Right Terran Town': b'Zer4',
    'Zerg 4 - Lower Terran Town': b'Ze4S',
    'Zerg 6 - Protoss Town': b'Zer6',
    'Zerg 7 - Air Town': b'Zr7a',
    'Zerg 7 - Ground Town': b'Zr7g',
    'Zerg 7 - Support Town': b'Zr7s',
    'Zerg 8 - Scout Town': b'Zer8',
    'Zerg 8 - Templar Town': b'Ze8T',
    'Zerg 9 - Teal Protoss': b'Zer9',
    'Zerg 9 - Left Yellow Protoss': b'Z9ly',
    'Zerg 9 - Right Yellow Protoss': b'Z9ry',
    'Zerg 9 - Left Orange Protoss': b'Z9lo',
    'Zerg 9 - Right Orange Protoss': b'Z9ro',
    'Zerg 10 - Left Teal (Attack': b'Z10a',
    'Zerg 10 - Right Teal (Support': b'Z10b',
    'Zerg 10 - Left Yellow (Support': b'Z10c',
    'Zerg 10 - Right Yellow (Attack': b'Z10d',
    'Zerg 10 - Red Protoss': b'Z10e',
    'Protoss 1 - Zerg Town': b'Pro1',
    'Protoss 2 - Zerg Town': b'Pro2',
    'Protoss 3 - Air Zerg Town': b'Pr3R',
    'Protoss 3 - Ground Zerg Town': b'Pr3G',
    'Protoss 4 - Zerg Town': b'Pro4',
    'Protoss 5 - Zerg Town Island': b'Pr5I',
    'Protoss 5 - Zerg Town Base': b'Pr5B',
    'Protoss 7 - Left Protoss Town': b'Pro7',
    'Protoss 7 - Right Protoss Town': b'Pr7B',
    'Protoss 7 - Shrine Protoss': b'Pr7S',
    'Protoss 8 - Left Protoss Town': b'Pro8',
    'Protoss 8 - Right Protoss Town': b'Pr8B',
    'Protoss 8 - Protoss Defenders': b'Pr8D',
    'Protoss 9 - Ground Zerg': b'Pro9',
    'Protoss 9 - Air Zerg': b'Pr9W',
    'Protoss 9 - Spell Zerg': b'Pr9Y',
    'Protoss 10 - Mini-Towns': b'Pr10',
    'Protoss 10 - Mini-Town Master': b'P10C',
    'Protoss 10 - Overmind Defenders': b'P10o',

    # Brood Wars AI Scripts
    'Brood Wars Protoss 1 - Town A': b'PB1A',
    'Brood Wars Protoss 1 - Town B': b'PB1B',
    'Brood Wars Protoss 1 - Town C': b'PB1C',
    'Brood Wars Protoss 1 - Town D': b'PB1D',
    'Brood Wars Protoss 1 - Town E': b'PB1E',
    'Brood Wars Protoss 1 - Town F': b'PB1F',
    'Brood Wars Protoss 2 - Town A': b'PB2A',
    'Brood Wars Protoss 2 - Town B': b'PB2B',
    'Brood Wars Protoss 2 - Town C': b'PB2C',
    'Brood Wars Protoss 2 - Town D': b'PB2D',
    'Brood Wars Protoss 2 - Town E': b'PB2E',
    'Brood Wars Protoss 2 - Town F': b'PB2F',
    'Brood Wars Protoss 3 - Town A': b'PB3A',
    'Brood Wars Protoss 3 - Town B': b'PB3B',
    'Brood Wars Protoss 3 - Town C': b'PB3C',
    'Brood Wars Protoss 3 - Town D': b'PB3D',
    'Brood Wars Protoss 3 - Town E': b'PB3E',
    'Brood Wars Protoss 3 - Town F': b'PB3F',
    'Brood Wars Protoss 4 - Town A': b'PB4A',
    'Brood Wars Protoss 4 - Town B': b'PB4B',
    'Brood Wars Protoss 4 - Town C': b'PB4C',
    'Brood Wars Protoss 4 - Town D': b'PB4D',
    'Brood Wars Protoss 4 - Town E': b'PB4E',
    'Brood Wars Protoss 4 - Town F': b'PB4F',
    'Brood Wars Protoss 5 - Town A': b'PB5A',
    'Brood Wars Protoss 5 - Town B': b'PB5B',
    'Brood Wars Protoss 5 - Town C': b'PB5C',
    'Brood Wars Protoss 5 - Town D': b'PB5D',
    'Brood Wars Protoss 5 - Town E': b'PB5E',
    'Brood Wars Protoss 5 - Town F': b'PB5F',
    'Brood Wars Protoss 6 - Town A': b'PB6A',
    'Brood Wars Protoss 6 - Town B': b'PB6B',
    'Brood Wars Protoss 6 - Town C': b'PB6C',
    'Brood Wars Protoss 6 - Town D': b'PB6D',
    'Brood Wars Protoss 6 - Town E': b'PB6E',
    'Brood Wars Protoss 6 - Town F': b'PB6F',
    'Brood Wars Protoss 7 - Town A': b'PB7A',
    'Brood Wars Protoss 7 - Town B': b'PB7B',
    'Brood Wars Protoss 7 - Town C': b'PB7C',
    'Brood Wars Protoss 7 - Town D': b'PB7D',
    'Brood Wars Protoss 7 - Town E': b'PB7E',
    'Brood Wars Protoss 7 - Town F': b'PB7F',
    'Brood Wars Protoss 8 - Town A': b'PB8A',
    'Brood Wars Protoss 8 - Town B': b'PB8B',
    'Brood Wars Protoss 8 - Town C': b'PB8C',
    'Brood Wars Protoss 8 - Town D': b'PB8D',
    'Brood Wars Protoss 8 - Town E': b'PB8E',
    'Brood Wars Protoss 8 - Town F': b'PB8F',
    'Brood Wars Terran 1 - Town A': b'TB1A',
    'Brood Wars Terran 1 - Town B': b'TB1B',
    'Brood Wars Terran 1 - Town C': b'TB1C',
    'Brood Wars Terran 1 - Town D': b'TB1D',
    'Brood Wars Terran 1 - Town E': b'TB1E',
    'Brood Wars Terran 1 - Town F': b'TB1F',
    'Brood Wars Terran 2 - Town A': b'TB2A',
    'Brood Wars Terran 2 - Town B': b'TB2B',
    'Brood Wars Terran 2 - Town C': b'TB2C',
    'Brood Wars Terran 2 - Town D': b'TB2D',
    'Brood Wars Terran 2 - Town E': b'TB2E',
    'Brood Wars Terran 2 - Town F': b'TB2F',
    'Brood Wars Terran 3 - Town A': b'TB3A',
    'Brood Wars Terran 3 - Town B': b'TB3B',
    'Brood Wars Terran 3 - Town C': b'TB3C',
    'Brood Wars Terran 3 - Town D': b'TB3D',
    'Brood Wars Terran 3 - Town E': b'TB3E',
    'Brood Wars Terran 3 - Town F': b'TB3F',
    'Brood Wars Terran 4 - Town A': b'TB4A',
    'Brood Wars Terran 4 - Town B': b'TB4B',
    'Brood Wars Terran 4 - Town C': b'TB4C',
    'Brood Wars Terran 4 - Town D': b'TB4D',
    'Brood Wars Terran 4 - Town E': b'TB4E',
    'Brood Wars Terran 4 - Town F': b'TB4F',
    'Brood Wars Terran 5 - Town A': b'TB5A',
    'Brood Wars Terran 5 - Town B': b'TB5B',
    'Brood Wars Terran 5 - Town C': b'TB5C',
    'Brood Wars Terran 5 - Town D': b'TB5D',
    'Brood Wars Terran 5 - Town E': b'TB5E',
    'Brood Wars Terran 5 - Town F': b'TB5F',
    'Brood Wars Terran 6 - Town A': b'TB6A',
    'Brood Wars Terran 6 - Town B': b'TB6B',
    'Brood Wars Terran 6 - Town C': b'TB6C',
    'Brood Wars Terran 6 - Town D': b'TB6D',
    'Brood Wars Terran 6 - Town E': b'TB6E',
    'Brood Wars Terran 6 - Town F': b'TB6F',
    'Brood Wars Terran 7 - Town A': b'TB7A',
    'Brood Wars Terran 7 - Town B': b'TB7B',
    'Brood Wars Terran 7 - Town C': b'TB7C',
    'Brood Wars Terran 7 - Town D': b'TB7D',
    'Brood Wars Terran 7 - Town E': b'TB7E',
    'Brood Wars Terran 7 - Town F': b'TB7F',
    'Brood Wars Terran 8 - Town A': b'TB8A',
    'Brood Wars Terran 8 - Town B': b'TB8B',
    'Brood Wars Terran 8 - Town C': b'TB8C',
    'Brood Wars Terran 8 - Town D': b'TB8D',
    'Brood Wars Terran 8 - Town E': b'TB8E',
    'Brood Wars Terran 8 - Town F': b'TB8F',
    'Brood Wars Zerg 1 - Town A': b'ZB1A',
    'Brood Wars Zerg 1 - Town B': b'ZB1B',
    'Brood Wars Zerg 1 - Town C': b'ZB1C',
    'Brood Wars Zerg 1 - Town D': b'ZB1D',
    'Brood Wars Zerg 1 - Town E': b'ZB1E',
    'Brood Wars Zerg 1 - Town F': b'ZB1F',
    'Brood Wars Zerg 2 - Town A': b'ZB2A',
    'Brood Wars Zerg 2 - Town B': b'ZB2B',
    'Brood Wars Zerg 2 - Town C': b'ZB2C',
    'Brood Wars Zerg 2 - Town D': b'ZB2D',
    'Brood Wars Zerg 2 - Town E': b'ZB2E',
    'Brood Wars Zerg 2 - Town F': b'ZB2F',
    'Brood Wars Zerg 3 - Town A': b'ZB3A',
    'Brood Wars Zerg 3 - Town B': b'ZB3B',
    'Brood Wars Zerg 3 - Town C': b'ZB3C',
    'Brood Wars Zerg 3 - Town D': b'ZB3D',
    'Brood Wars Zerg 3 - Town E': b'ZB3E',
    'Brood Wars Zerg 3 - Town F': b'ZB3F',
    'Brood Wars Zerg 4 - Town A': b'ZB4A',
    'Brood Wars Zerg 4 - Town B': b'ZB4B',
    'Brood Wars Zerg 4 - Town C': b'ZB4C',
    'Brood Wars Zerg 4 - Town D': b'ZB4D',
    'Brood Wars Zerg 4 - Town E': b'ZB4E',
    'Brood Wars Zerg 4 - Town F': b'ZB4F',
    'Brood Wars Zerg 5 - Town A': b'ZB5A',
    'Brood Wars Zerg 5 - Town B': b'ZB5B',
    'Brood Wars Zerg 5 - Town C': b'ZB5C',
    'Brood Wars Zerg 5 - Town D': b'ZB5D',
    'Brood Wars Zerg 5 - Town E': b'ZB5E',
    'Brood Wars Zerg 5 - Town F': b'ZB5F',
    'Brood Wars Zerg 6 - Town A': b'ZB6A',
    'Brood Wars Zerg 6 - Town B': b'ZB6B',
    'Brood Wars Zerg 6 - Town C': b'ZB6C',
    'Brood Wars Zerg 6 - Town D': b'ZB6D',
    'Brood Wars Zerg 6 - Town E': b'ZB6E',
    'Brood Wars Zerg 6 - Town F': b'ZB6F',
    'Brood Wars Zerg 7 - Town A': b'ZB7A',
    'Brood Wars Zerg 7 - Town B': b'ZB7B',
    'Brood Wars Zerg 7 - Town C': b'ZB7C',
    'Brood Wars Zerg 7 - Town D': b'ZB7D',
    'Brood Wars Zerg 7 - Town E': b'ZB7E',
    'Brood Wars Zerg 7 - Town F': b'ZB7F',
    'Brood Wars Zerg 8 - Town A': b'ZB8A',
    'Brood Wars Zerg 8 - Town B': b'ZB8B',
    'Brood Wars Zerg 8 - Town C': b'ZB8C',
    'Brood Wars Zerg 8 - Town D': b'ZB8D',
    'Brood Wars Zerg 8 - Town E': b'ZB8E',
    'Brood Wars Zerg 8 - Town F': b'ZB8F',
    'Brood Wars Zerg 9 - Town A': b'ZB9A',
    'Brood Wars Zerg 9 - Town B': b'ZB9B',
    'Brood Wars Zerg 9 - Town C': b'ZB9C',
    'Brood Wars Zerg 9 - Town D': b'ZB9D',
    'Brood Wars Zerg 9 - Town E': b'ZB9E',
    'Brood Wars Zerg 9 - Town F': b'ZB9F',
    'Brood Wars Zerg 10 - Town A': b'ZB0A',
    'Brood Wars Zerg 10 - Town B': b'ZB0B',
    'Brood Wars Zerg 10 - Town C': b'ZB0C',
    'Brood Wars Zerg 10 - Town D': b'ZB0D',
    'Brood Wars Zerg 10 - Town E': b'ZB0E',
    'Brood Wars Zerg 10 - Town F': b'ZB0F',
}
