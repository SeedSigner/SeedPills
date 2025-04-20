#!/usr/bin/env python3
"""
BIP39 Word Grid Generator for OpenSCAD

This script generates OpenSCAD code to create a grid of "pills" with BIP39 words
on either side. The pills are arranged in a grid pattern with customizable dimensions.
Each pill contains a truncated BIP39 word on each side.
"""

import argparse
from typing import List, Tuple

# BIP39 word list (2048 words)
BIP_39_LIST = ["padding_string","ABANDON","ABILITY","ABLE","ABOUT","ABOVE","ABSENT","ABSORB","ABSTRACT","ABSURD","ABUSE","ACCESS","ACCIDENT","ACCOUNT","ACCUSE","ACHIEVE","ACID","ACOUSTIC","ACQUIRE","ACROSS","ACT","ACTION","ACTOR","ACTRESS","ACTUAL","ADAPT","ADD","ADDICT","ADDRESS","ADJUST","ADMIT","ADULT","ADVANCE","ADVICE","AEROBIC","AFFAIR","AFFORD","AFRAID","AGAIN","AGE","AGENT","AGREE","AHEAD","AIM","AIR","AIRPORT","AISLE","ALARM","ALBUM","ALCOHOL","ALERT","ALIEN","ALL","ALLEY","ALLOW","ALMOST","ALONE","ALPHA","ALREADY","ALSO","ALTER","ALWAYS","AMATEUR","AMAZING","AMONG","AMOUNT","AMUSED","ANALYST","ANCHOR","ANCIENT","ANGER","ANGLE","ANGRY","ANIMAL","ANKLE","ANNOUNCE","ANNUAL","ANOTHER","ANSWER","ANTENNA","ANTIQUE","ANXIETY","ANY","APART","APOLOGY","APPEAR","APPLE","APPROVE","APRIL","ARCH","ARCTIC","AREA","ARENA","ARGUE","ARM","ARMED","ARMOR","ARMY","AROUND","ARRANGE","ARREST","ARRIVE","ARROW","ART","ARTEFACT","ARTIST","ARTWORK","ASK","ASPECT","ASSAULT","ASSET","ASSIST","ASSUME","ASTHMA","ATHLETE","ATOM","ATTACK","ATTEND","ATTITUDE","ATTRACT","AUCTION","AUDIT","AUGUST","AUNT","AUTHOR","AUTO","AUTUMN","AVERAGE","AVOCADO","AVOID","AWAKE","AWARE","AWAY","AWESOME","AWFUL","AWKWARD","AXIS","BABY","BACHELOR","BACON","BADGE","BAG","BALANCE","BALCONY","BALL","BAMBOO","BANANA","BANNER","BAR","BARELY","BARGAIN","BARREL","BASE","BASIC","BASKET","BATTLE","BEACH","BEAN","BEAUTY","BECAUSE","BECOME","BEEF","BEFORE","BEGIN","BEHAVE","BEHIND","BELIEVE","BELOW","BELT","BENCH","BENEFIT","BEST","BETRAY","BETTER","BETWEEN","BEYOND","BICYCLE","BID","BIKE","BIND","BIOLOGY","BIRD","BIRTH","BITTER","BLACK","BLADE","BLAME","BLANKET","BLAST","BLEAK","BLESS","BLIND","BLOOD","BLOSSOM","BLOUSE","BLUE","BLUR","BLUSH","BOARD","BOAT","BODY","BOIL","BOMB","BONE","BONUS","BOOK","BOOST","BORDER","BORING","BORROW","BOSS","BOTTOM","BOUNCE","BOX","BOY","BRACKET","BRAIN","BRAND","BRASS","BRAVE","BREAD","BREEZE","BRICK","BRIDGE","BRIEF","BRIGHT","BRING","BRISK","BROCCOLI","BROKEN","BRONZE","BROOM","BROTHER","BROWN","BRUSH","BUBBLE","BUDDY","BUDGET","BUFFALO","BUILD","BULB","BULK","BULLET","BUNDLE","BUNKER","BURDEN","BURGER","BURST","BUS","BUSINESS","BUSY","BUTTER","BUYER","BUZZ","CABBAGE","CABIN","CABLE","CACTUS","CAGE","CAKE","CALL","CALM","CAMERA","CAMP","CAN","CANAL","CANCEL","CANDY","CANNON","CANOE","CANVAS","CANYON","CAPABLE","CAPITAL","CAPTAIN","CAR","CARBON","CARD","CARGO","CARPET","CARRY","CART","CASE","CASH","CASINO","CASTLE","CASUAL","CAT","CATALOG","CATCH","CATEGORY","CATTLE","CAUGHT","CAUSE","CAUTION","CAVE","CEILING","CELERY","CEMENT","CENSUS","CENTURY","CEREAL","CERTAIN","CHAIR","CHALK","CHAMPION","CHANGE","CHAOS","CHAPTER","CHARGE","CHASE","CHAT","CHEAP","CHECK","CHEESE","CHEF","CHERRY","CHEST","CHICKEN","CHIEF","CHILD","CHIMNEY","CHOICE","CHOOSE","CHRONIC","CHUCKLE","CHUNK","CHURN","CIGAR","CINNAMON","CIRCLE","CITIZEN","CITY","CIVIL","CLAIM","CLAP","CLARIFY","CLAW","CLAY","CLEAN","CLERK","CLEVER","CLICK","CLIENT","CLIFF","CLIMB","CLINIC","CLIP","CLOCK","CLOG","CLOSE","CLOTH","CLOUD","CLOWN","CLUB","CLUMP","CLUSTER","CLUTCH","COACH","COAST","COCONUT","CODE","COFFEE","COIL","COIN","COLLECT","COLOR","COLUMN","COMBINE","COME","COMFORT","COMIC","COMMON","COMPANY","CONCERT","CONDUCT","CONFIRM","CONGRESS","CONNECT","CONSIDER","CONTROL","CONVINCE","COOK","COOL","COPPER","COPY","CORAL","CORE","CORN","CORRECT","COST","COTTON","COUCH","COUNTRY","COUPLE","COURSE","COUSIN","COVER","COYOTE","CRACK","CRADLE","CRAFT","CRAM","CRANE","CRASH","CRATER","CRAWL","CRAZY","CREAM","CREDIT","CREEK","CREW","CRICKET","CRIME","CRISP","CRITIC","CROP","CROSS","CROUCH","CROWD","CRUCIAL","CRUEL","CRUISE","CRUMBLE","CRUNCH","CRUSH","CRY","CRYSTAL","CUBE","CULTURE","CUP","CUPBOARD","CURIOUS","CURRENT","CURTAIN","CURVE","CUSHION","CUSTOM","CUTE","CYCLE","DAD","DAMAGE","DAMP","DANCE","DANGER","DARING","DASH","DAUGHTER","DAWN","DAY","DEAL","DEBATE","DEBRIS","DECADE","DECEMBER","DECIDE","DECLINE","DECORATE","DECREASE","DEER","DEFENSE","DEFINE","DEFY","DEGREE","DELAY","DELIVER","DEMAND","DEMISE","DENIAL","DENTIST","DENY","DEPART","DEPEND","DEPOSIT","DEPTH","DEPUTY","DERIVE","DESCRIBE","DESERT","DESIGN","DESK","DESPAIR","DESTROY","DETAIL","DETECT","DEVELOP","DEVICE","DEVOTE","DIAGRAM","DIAL","DIAMOND","DIARY","DICE","DIESEL","DIET","DIFFER","DIGITAL","DIGNITY","DILEMMA","DINNER","DINOSAUR","DIRECT","DIRT","DISAGREE","DISCOVER","DISEASE","DISH","DISMISS","DISORDER","DISPLAY","DISTANCE","DIVERT","DIVIDE","DIVORCE","DIZZY","DOCTOR","DOCUMENT","DOG","DOLL","DOLPHIN","DOMAIN","DONATE","DONKEY","DONOR","DOOR","DOSE","DOUBLE","DOVE","DRAFT","DRAGON","DRAMA","DRASTIC","DRAW","DREAM","DRESS","DRIFT","DRILL","DRINK","DRIP","DRIVE","DROP","DRUM","DRY","DUCK","DUMB","DUNE","DURING","DUST","DUTCH","DUTY","DWARF","DYNAMIC","EAGER","EAGLE","EARLY","EARN","EARTH","EASILY","EAST","EASY","ECHO","ECOLOGY","ECONOMY","EDGE","EDIT","EDUCATE","EFFORT","EGG","EIGHT","EITHER","ELBOW","ELDER","ELECTRIC","ELEGANT","ELEMENT","ELEPHANT","ELEVATOR","ELITE","ELSE","EMBARK","EMBODY","EMBRACE","EMERGE","EMOTION","EMPLOY","EMPOWER","EMPTY","ENABLE","ENACT","END","ENDLESS","ENDORSE","ENEMY","ENERGY","ENFORCE","ENGAGE","ENGINE","ENHANCE","ENJOY","ENLIST","ENOUGH","ENRICH","ENROLL","ENSURE","ENTER","ENTIRE","ENTRY","ENVELOPE","EPISODE","EQUAL","EQUIP","ERA","ERASE","ERODE","EROSION","ERROR","ERUPT","ESCAPE","ESSAY","ESSENCE","ESTATE","ETERNAL","ETHICS","EVIDENCE","EVIL","EVOKE","EVOLVE","EXACT","EXAMPLE","EXCESS","EXCHANGE","EXCITE","EXCLUDE","EXCUSE","EXECUTE","EXERCISE","EXHAUST","EXHIBIT","EXILE","EXIST","EXIT","EXOTIC","EXPAND","EXPECT","EXPIRE","EXPLAIN","EXPOSE","EXPRESS","EXTEND","EXTRA","EYE","EYEBROW","FABRIC","FACE","FACULTY","FADE","FAINT","FAITH","FALL","FALSE","FAME","FAMILY","FAMOUS","FAN","FANCY","FANTASY","FARM","FASHION","FAT","FATAL","FATHER","FATIGUE","FAULT","FAVORITE","FEATURE","FEBRUARY","FEDERAL","FEE","FEED","FEEL","FEMALE","FENCE","FESTIVAL","FETCH","FEVER","FEW","FIBER","FICTION","FIELD","FIGURE","FILE","FILM","FILTER","FINAL","FIND","FINE","FINGER","FINISH","FIRE","FIRM","FIRST","FISCAL","FISH","FIT","FITNESS","FIX","FLAG","FLAME","FLASH","FLAT","FLAVOR","FLEE","FLIGHT","FLIP","FLOAT","FLOCK","FLOOR","FLOWER","FLUID","FLUSH","FLY","FOAM","FOCUS","FOG","FOIL","FOLD","FOLLOW","FOOD","FOOT","FORCE","FOREST","FORGET","FORK","FORTUNE","FORUM","FORWARD","FOSSIL","FOSTER","FOUND","FOX","FRAGILE","FRAME","FREQUENT","FRESH","FRIEND","FRINGE","FROG","FRONT","FROST","FROWN","FROZEN","FRUIT","FUEL","FUN","FUNNY","FURNACE","FURY","FUTURE","GADGET","GAIN","GALAXY","GALLERY","GAME","GAP","GARAGE","GARBAGE","GARDEN","GARLIC","GARMENT","GAS","GASP","GATE","GATHER","GAUGE","GAZE","GENERAL","GENIUS","GENRE","GENTLE","GENUINE","GESTURE","GHOST","GIANT","GIFT","GIGGLE","GINGER","GIRAFFE","GIRL","GIVE","GLAD","GLANCE","GLARE","GLASS","GLIDE","GLIMPSE","GLOBE","GLOOM","GLORY","GLOVE","GLOW","GLUE","GOAT","GODDESS","GOLD","GOOD","GOOSE","GORILLA","GOSPEL","GOSSIP","GOVERN","GOWN","GRAB","GRACE","GRAIN","GRANT","GRAPE","GRASS","GRAVITY","GREAT","GREEN","GRID","GRIEF","GRIT","GROCERY","GROUP","GROW","GRUNT","GUARD","GUESS","GUIDE","GUILT","GUITAR","GUN","GYM","HABIT","HAIR","HALF","HAMMER","HAMSTER","HAND","HAPPY","HARBOR","HARD","HARSH","HARVEST","HAT","HAVE","HAWK","HAZARD","HEAD","HEALTH","HEART","HEAVY","HEDGEHOG","HEIGHT","HELLO","HELMET","HELP","HEN","HERO","HIDDEN","HIGH","HILL","HINT","HIP","HIRE","HISTORY","HOBBY","HOCKEY","HOLD","HOLE","HOLIDAY","HOLLOW","HOME","HONEY","HOOD","HOPE","HORN","HORROR","HORSE","HOSPITAL","HOST","HOTEL","HOUR","HOVER","HUB","HUGE","HUMAN","HUMBLE","HUMOR","HUNDRED","HUNGRY","HUNT","HURDLE","HURRY","HURT","HUSBAND","HYBRID","ICE","ICON","IDEA","IDENTIFY","IDLE","IGNORE","ILL","ILLEGAL","ILLNESS","IMAGE","IMITATE","IMMENSE","IMMUNE","IMPACT","IMPOSE","IMPROVE","IMPULSE","INCH","INCLUDE","INCOME","INCREASE","INDEX","INDICATE","INDOOR","INDUSTRY","INFANT","INFLICT","INFORM","INHALE","INHERIT","INITIAL","INJECT","INJURY","INMATE","INNER","INNOCENT","INPUT","INQUIRY","INSANE","INSECT","INSIDE","INSPIRE","INSTALL","INTACT","INTEREST","INTO","INVEST","INVITE","INVOLVE","IRON","ISLAND","ISOLATE","ISSUE","ITEM","IVORY","JACKET","JAGUAR","JAR","JAZZ","JEALOUS","JEANS","JELLY","JEWEL","JOB","JOIN","JOKE","JOURNEY","JOY","JUDGE","JUICE","JUMP","JUNGLE","JUNIOR","JUNK","JUST","KANGAROO","KEEN","KEEP","KETCHUP","KEY","KICK","KID","KIDNEY","KIND","KINGDOM","KISS","KIT","KITCHEN","KITE","KITTEN","KIWI","KNEE","KNIFE","KNOCK","KNOW","LAB","LABEL","LABOR","LADDER","LADY","LAKE","LAMP","LANGUAGE","LAPTOP","LARGE","LATER","LATIN","LAUGH","LAUNDRY","LAVA","LAW","LAWN","LAWSUIT","LAYER","LAZY","LEADER","LEAF","LEARN","LEAVE","LECTURE","LEFT","LEG","LEGAL","LEGEND","LEISURE","LEMON","LEND","LENGTH","LENS","LEOPARD","LESSON","LETTER","LEVEL","LIAR","LIBERTY","LIBRARY","LICENSE","LIFE","LIFT","LIGHT","LIKE","LIMB","LIMIT","LINK","LION","LIQUID","LIST","LITTLE","LIVE","LIZARD","LOAD","LOAN","LOBSTER","LOCAL","LOCK","LOGIC","LONELY","LONG","LOOP","LOTTERY","LOUD","LOUNGE","LOVE","LOYAL","LUCKY","LUGGAGE","LUMBER","LUNAR","LUNCH","LUXURY","LYRICS","MACHINE","MAD","MAGIC","MAGNET","MAID","MAIL","MAIN","MAJOR","MAKE","MAMMAL","MAN","MANAGE","MANDATE","MANGO","MANSION","MANUAL","MAPLE","MARBLE","MARCH","MARGIN","MARINE","MARKET","MARRIAGE","MASK","MASS","MASTER","MATCH","MATERIAL","MATH","MATRIX","MATTER","MAXIMUM","MAZE","MEADOW","MEAN","MEASURE","MEAT","MECHANIC","MEDAL","MEDIA","MELODY","MELT","MEMBER","MEMORY","MENTION","MENU","MERCY","MERGE","MERIT","MERRY","MESH","MESSAGE","METAL","METHOD","MIDDLE","MIDNIGHT","MILK","MILLION","MIMIC","MIND","MINIMUM","MINOR","MINUTE","MIRACLE","MIRROR","MISERY","MISS","MISTAKE","MIX","MIXED","MIXTURE","MOBILE","MODEL","MODIFY","MOM","MOMENT","MONITOR","MONKEY","MONSTER","MONTH","MOON","MORAL","MORE","MORNING","MOSQUITO","MOTHER","MOTION","MOTOR","MOUNTAIN","MOUSE","MOVE","MOVIE","MUCH","MUFFIN","MULE","MULTIPLY","MUSCLE","MUSEUM","MUSHROOM","MUSIC","MUST","MUTUAL","MYSELF","MYSTERY","MYTH","NAIVE","NAME","NAPKIN","NARROW","NASTY","NATION","NATURE","NEAR","NECK","NEED","NEGATIVE","NEGLECT","NEITHER","NEPHEW","NERVE","NEST","NET","NETWORK","NEUTRAL","NEVER","NEWS","NEXT","NICE","NIGHT","NOBLE","NOISE","NOMINEE","NOODLE","NORMAL","NORTH","NOSE","NOTABLE","NOTE","NOTHING","NOTICE","NOVEL","NOW","NUCLEAR","NUMBER","NURSE","NUT","OAK","OBEY","OBJECT","OBLIGE","OBSCURE","OBSERVE","OBTAIN","OBVIOUS","OCCUR","OCEAN","OCTOBER","ODOR","OFF","OFFER","OFFICE","OFTEN","OIL","OKAY","OLD","OLIVE","OLYMPIC","OMIT","ONCE","ONE","ONION","ONLINE","ONLY","OPEN","OPERA","OPINION","OPPOSE","OPTION","ORANGE","ORBIT","ORCHARD","ORDER","ORDINARY","ORGAN","ORIENT","ORIGINAL","ORPHAN","OSTRICH","OTHER","OUTDOOR","OUTER","OUTPUT","OUTSIDE","OVAL","OVEN","OVER","OWN","OWNER","OXYGEN","OYSTER","OZONE","PACT","PADDLE","PAGE","PAIR","PALACE","PALM","PANDA","PANEL","PANIC","PANTHER","PAPER","PARADE","PARENT","PARK","PARROT","PARTY","PASS","PATCH","PATH","PATIENT","PATROL","PATTERN","PAUSE","PAVE","PAYMENT","PEACE","PEANUT","PEAR","PEASANT","PELICAN","PEN","PENALTY","PENCIL","PEOPLE","PEPPER","PERFECT","PERMIT","PERSON","PET","PHONE","PHOTO","PHRASE","PHYSICAL","PIANO","PICNIC","PICTURE","PIECE","PIG","PIGEON","PILL","PILOT","PINK","PIONEER","PIPE","PISTOL","PITCH","PIZZA","PLACE","PLANET","PLASTIC","PLATE","PLAY","PLEASE","PLEDGE","PLUCK","PLUG","PLUNGE","POEM","POET","POINT","POLAR","POLE","POLICE","POND","PONY","POOL","POPULAR","PORTION","POSITION","POSSIBLE","POST","POTATO","POTTERY","POVERTY","POWDER","POWER","PRACTICE","PRAISE","PREDICT","PREFER","PREPARE","PRESENT","PRETTY","PREVENT","PRICE","PRIDE","PRIMARY","PRINT","PRIORITY","PRISON","PRIVATE","PRIZE","PROBLEM","PROCESS","PRODUCE","PROFIT","PROGRAM","PROJECT","PROMOTE","PROOF","PROPERTY","PROSPER","PROTECT","PROUD","PROVIDE","PUBLIC","PUDDING","PULL","PULP","PULSE","PUMPKIN","PUNCH","PUPIL","PUPPY","PURCHASE","PURITY","PURPOSE","PURSE","PUSH","PUT","PUZZLE","PYRAMID","QUALITY","QUANTUM","QUARTER","QUESTION","QUICK","QUIT","QUIZ","QUOTE","RABBIT","RACCOON","RACE","RACK","RADAR","RADIO","RAIL","RAIN","RAISE","RALLY","RAMP","RANCH","RANDOM","RANGE","RAPID","RARE","RATE","RATHER","RAVEN","RAW","RAZOR","READY","REAL","REASON","REBEL","REBUILD","RECALL","RECEIVE","RECIPE","RECORD","RECYCLE","REDUCE","REFLECT","REFORM","REFUSE","REGION","REGRET","REGULAR","REJECT","RELAX","RELEASE","RELIEF","RELY","REMAIN","REMEMBER","REMIND","REMOVE","RENDER","RENEW","RENT","REOPEN","REPAIR","REPEAT","REPLACE","REPORT","REQUIRE","RESCUE","RESEMBLE","RESIST","RESOURCE","RESPONSE","RESULT","RETIRE","RETREAT","RETURN","REUNION","REVEAL","REVIEW","REWARD","RHYTHM","RIB","RIBBON","RICE","RICH","RIDE","RIDGE","RIFLE","RIGHT","RIGID","RING","RIOT","RIPPLE","RISK","RITUAL","RIVAL","RIVER","ROAD","ROAST","ROBOT","ROBUST","ROCKET","ROMANCE","ROOF","ROOKIE","ROOM","ROSE","ROTATE","ROUGH","ROUND","ROUTE","ROYAL","RUBBER","RUDE","RUG","RULE","RUN","RUNWAY","RURAL","SAD","SADDLE","SADNESS","SAFE","SAIL","SALAD","SALMON","SALON","SALT","SALUTE","SAME","SAMPLE","SAND","SATISFY","SATOSHI","SAUCE","SAUSAGE","SAVE","SAY","SCALE","SCAN","SCARE","SCATTER","SCENE","SCHEME","SCHOOL","SCIENCE","SCISSORS","SCORPION","SCOUT","SCRAP","SCREEN","SCRIPT","SCRUB","SEA","SEARCH","SEASON","SEAT","SECOND","SECRET","SECTION","SECURITY","SEED","SEEK","SEGMENT","SELECT","SELL","SEMINAR","SENIOR","SENSE","SENTENCE","SERIES","SERVICE","SESSION","SETTLE","SETUP","SEVEN","SHADOW","SHAFT","SHALLOW","SHARE","SHED","SHELL","SHERIFF","SHIELD","SHIFT","SHINE","SHIP","SHIVER","SHOCK","SHOE","SHOOT","SHOP","SHORT","SHOULDER","SHOVE","SHRIMP","SHRUG","SHUFFLE","SHY","SIBLING","SICK","SIDE","SIEGE","SIGHT","SIGN","SILENT","SILK","SILLY","SILVER","SIMILAR","SIMPLE","SINCE","SING","SIREN","SISTER","SITUATE","SIX","SIZE","SKATE","SKETCH","SKI","SKILL","SKIN","SKIRT","SKULL","SLAB","SLAM","SLEEP","SLENDER","SLICE","SLIDE","SLIGHT","SLIM","SLOGAN","SLOT","SLOW","SLUSH","SMALL","SMART","SMILE","SMOKE","SMOOTH","SNACK","SNAKE","SNAP","SNIFF","SNOW","SOAP","SOCCER","SOCIAL","SOCK","SODA","SOFT","SOLAR","SOLDIER","SOLID","SOLUTION","SOLVE","SOMEONE","SONG","SOON","SORRY","SORT","SOUL","SOUND","SOUP","SOURCE","SOUTH","SPACE","SPARE","SPATIAL","SPAWN","SPEAK","SPECIAL","SPEED","SPELL","SPEND","SPHERE","SPICE","SPIDER","SPIKE","SPIN","SPIRIT","SPLIT","SPOIL","SPONSOR","SPOON","SPORT","SPOT","SPRAY","SPREAD","SPRING","SPY","SQUARE","SQUEEZE","SQUIRREL","STABLE","STADIUM","STAFF","STAGE","STAIRS","STAMP","STAND","START","STATE","STAY","STEAK","STEEL","STEM","STEP","STEREO","STICK","STILL","STING","STOCK","STOMACH","STONE","STOOL","STORY","STOVE","STRATEGY","STREET","STRIKE","STRONG","STRUGGLE","STUDENT","STUFF","STUMBLE","STYLE","SUBJECT","SUBMIT","SUBWAY","SUCCESS","SUCH","SUDDEN","SUFFER","SUGAR","SUGGEST","SUIT","SUMMER","SUN","SUNNY","SUNSET","SUPER","SUPPLY","SUPREME","SURE","SURFACE","SURGE","SURPRISE","SURROUND","SURVEY","SUSPECT","SUSTAIN","SWALLOW","SWAMP","SWAP","SWARM","SWEAR","SWEET","SWIFT","SWIM","SWING","SWITCH","SWORD","SYMBOL","SYMPTOM","SYRUP","SYSTEM","TABLE","TACKLE","TAG","TAIL","TALENT","TALK","TANK","TAPE","TARGET","TASK","TASTE","TATTOO","TAXI","TEACH","TEAM","TELL","TEN","TENANT","TENNIS","TENT","TERM","TEST","TEXT","THANK","THAT","THEME","THEN","THEORY","THERE","THEY","THING","THIS","THOUGHT","THREE","THRIVE","THROW","THUMB","THUNDER","TICKET","TIDE","TIGER","TILT","TIMBER","TIME","TINY","TIP","TIRED","TISSUE","TITLE","TOAST","TOBACCO","TODAY","TODDLER","TOE","TOGETHER","TOILET","TOKEN","TOMATO","TOMORROW","TONE","TONGUE","TONIGHT","TOOL","TOOTH","TOP","TOPIC","TOPPLE","TORCH","TORNADO","TORTOISE","TOSS","TOTAL","TOURIST","TOWARD","TOWER","TOWN","TOY","TRACK","TRADE","TRAFFIC","TRAGIC","TRAIN","TRANSFER","TRAP","TRASH","TRAVEL","TRAY","TREAT","TREE","TREND","TRIAL","TRIBE","TRICK","TRIGGER","TRIM","TRIP","TROPHY","TROUBLE","TRUCK","TRUE","TRULY","TRUMPET","TRUST","TRUTH","TRY","TUBE","TUITION","TUMBLE","TUNA","TUNNEL","TURKEY","TURN","TURTLE","TWELVE","TWENTY","TWICE","TWIN","TWIST","TWO","TYPE","TYPICAL","UGLY","UMBRELLA","UNABLE","UNAWARE","UNCLE","UNCOVER","UNDER","UNDO","UNFAIR","UNFOLD","UNHAPPY","UNIFORM","UNIQUE","UNIT","UNIVERSE","UNKNOWN","UNLOCK","UNTIL","UNUSUAL","UNVEIL","UPDATE","UPGRADE","UPHOLD","UPON","UPPER","UPSET","URBAN","URGE","USAGE","USE","USED","USEFUL","USELESS","USUAL","UTILITY","VACANT","VACUUM","VAGUE","VALID","VALLEY","VALVE","VAN","VANISH","VAPOR","VARIOUS","VAST","VAULT","VEHICLE","VELVET","VENDOR","VENTURE","VENUE","VERB","VERIFY","VERSION","VERY","VESSEL","VETERAN","VIABLE","VIBRANT","VICIOUS","VICTORY","VIDEO","VIEW","VILLAGE","VINTAGE","VIOLIN","VIRTUAL","VIRUS","VISA","VISIT","VISUAL","VITAL","VIVID","VOCAL","VOICE","VOID","VOLCANO","VOLUME","VOTE","VOYAGE","WAGE","WAGON","WAIT","WALK","WALL","WALNUT","WANT","WARFARE","WARM","WARRIOR","WASH","WASP","WASTE","WATER","WAVE","WAY","WEALTH","WEAPON","WEAR","WEASEL","WEATHER","WEB","WEDDING","WEEKEND","WEIRD","WELCOME","WEST","WET","WHALE","WHAT","WHEAT","WHEEL","WHEN","WHERE","WHIP","WHISPER","WIDE","WIDTH","WIFE","WILD","WILL","WIN","WINDOW","WINE","WING","WINK","WINNER","WINTER","WIRE","WISDOM","WISE","WISH","WITNESS","WOLF","WOMAN","WONDER","WOOD","WOOL","WORD","WORK","WORLD","WORRY","WORTH","WRAP","WRECK","WRESTLE","WRIST","WRITE","WRONG","YARD","YEAR","YELLOW","YOU","YOUNG","YOUTH","ZEBRA","ZERO","ZONE","ZOO"]

# Constants for pill dimensions and layout
PILL_WIDTH_CORE = 11.0
PILL_HEIGHT = 7.5
PILL_THICKNESS = 3.0
PILL_CIRCLE_RADIUS = 3.75
PILL_RELIEF_RADIUS = 2.75
PILL_RELIEF_HEIGHT = 2.0
PILL_RELIEF_WIDTH = 5.5

HORIZONTAL_SPACING = 18.75
VERTICAL_SPACING = 7.75
LINK_THICKNESS = 0.3
HORIZONTAL_LINK_WIDTH = 1.2
VERTICAL_LINK_WIDTH = 0.5
LINK_HEIGHT = 0.5
LINK_Z_OFFSET = -0.825

TEXT_SIZE = 3.5
TEXT_HEIGHT = 0.51
TEXT_Z_OFFSET = 0.99
WORD_TRUNCATE_LENGTH = 4

class PillGridGenerator:
    """Generator for creating OpenSCAD code for a grid of BIP39 word pills."""
    
    def __init__(self, first_word: int, num_cols: int, num_rows: int, word_list: List[str], 
                 font: str = "Fredoka", word_length: int = 4, color: str = None):
        """
        Initialize the generator with grid dimensions and starting word.
        
        Args:
            first_word: Index of the first BIP39 word to use
            num_cols: Number of columns in the grid
            num_rows: Number of rows in the grid
            word_list: List of BIP39 words
            font: Font to use for text
            word_length: How many characters of each word to show
            color: Optional color for the pills (e.g., "orange")
        """
        self.first_word = first_word
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.word_list = word_list
        self.font = font
        self.word_length = word_length
        self.color = color
        
        self.total_pills = num_cols * num_rows
        self.rear_first_word = first_word + self.total_pills + (num_cols - 1)
    
    def generate_openscad_header(self) -> str:
        """Generate the OpenSCAD header with configuration variables."""
        header = f"""// BIP39 Word Grid Generator
// Configuration:
//   - Starting Word: {self.first_word} ({self.word_list[self.first_word]})
//   - Grid Size: {self.num_cols}x{self.num_rows} ({self.total_pills} pills)
//   - Font: {self.font}
//   - Word display length: {self.word_length} characters

// OpenSCAD render quality settings
$fa = 1;  // minimum angle (smaller is better quality)
$fs = 0.5;  // minimum size (smaller is better quality)
"""
        if self.color:
            header += f"\ncolor(\"{self.color}\")\n"
        
        return header
    
    def generate_pill(self, x: float, y: float, top_word: str, bottom_word: str) -> str:
        """Generate OpenSCAD code for a single pill at position (x,y)."""
        return f"""
// Pill at position [{x}, {y}]
translate([{x}, {y}, 0])
union() {{
    // Create the pill shape with raised lettering on both sides
    union() {{
        // Pill body with relief cutouts
        difference() {{
            union() {{
                // Pill Core
                cube([{PILL_WIDTH_CORE}, {PILL_HEIGHT}, {PILL_THICKNESS}], center=true);
                // Left Pill circle
                translate([-{PILL_WIDTH_CORE/2}, 0, 0])
                    cylinder(h={PILL_THICKNESS}, r={PILL_CIRCLE_RADIUS}, center=true);
                // Right Pill circle
                translate([{PILL_WIDTH_CORE/2}, 0, 0])
                    cylinder(h={PILL_THICKNESS}, r={PILL_CIRCLE_RADIUS}, center=true);
            }}
            union() {{
                // Top relief cutout
                translate([0, 0, {PILL_THICKNESS/2 - PILL_RELIEF_HEIGHT/2}])
                union() {{
                    cube([{PILL_WIDTH_CORE}, {PILL_RELIEF_WIDTH}, {PILL_RELIEF_HEIGHT}], center=true);
                    translate([-{PILL_WIDTH_CORE/2}, 0, 0])
                        cylinder(h={PILL_RELIEF_HEIGHT}, r={PILL_RELIEF_RADIUS}, center=true);
                    translate([{PILL_WIDTH_CORE/2}, 0, 0])
                        cylinder(h={PILL_RELIEF_HEIGHT}, r={PILL_RELIEF_RADIUS}, center=true);
                }}
                
                // Bottom relief cutout
                translate([0, 0, -{PILL_THICKNESS/2 + PILL_RELIEF_HEIGHT/2}])
                union() {{
                    cube([{PILL_WIDTH_CORE}, {PILL_RELIEF_WIDTH}, {PILL_RELIEF_HEIGHT}], center=true);
                    translate([-{PILL_WIDTH_CORE/2}, 0, 0])
                        cylinder(h={PILL_RELIEF_HEIGHT}, r={PILL_RELIEF_RADIUS}, center=true);
                    translate([{PILL_WIDTH_CORE/2}, 0, 0])
                        cylinder(h={PILL_RELIEF_HEIGHT}, r={PILL_RELIEF_RADIUS}, center=true);
                }}
            }}
        }}
        
        // Top text
        translate([0, 0, {TEXT_Z_OFFSET}])
            linear_extrude({TEXT_HEIGHT})
                text("{top_word}", size={TEXT_SIZE}, font="{self.font}", halign="center", valign="center");
        
        // Bottom text
        rotate([0, 180, 0])
            translate([0, 0, {TEXT_Z_OFFSET}])
                linear_extrude({TEXT_HEIGHT})
                    text("{bottom_word}", size={TEXT_SIZE}, font="{self.font}", halign="center", valign="center");
    }}
}}
"""

    def generate_link(self, x1: float, y1: float, x2: float, y2: float, is_horizontal: bool) -> str:
        """Generate OpenSCAD code for a link between two pills."""
        width = HORIZONTAL_LINK_WIDTH if is_horizontal else VERTICAL_LINK_WIDTH
        
        return f"""
// Link between [{x1}, {y1}] and [{x2}, {y2}]
translate([{(x1+x2)/2}, {(y1+y2)/2}, {LINK_Z_OFFSET}])
    cube([{abs(x2-x1) + width}, {abs(y2-y1) + width}, {LINK_HEIGHT}], center=true);
"""

    def generate_pill_grid(self) -> str:
        """Generate OpenSCAD code for the complete grid of pills and links."""
        code = ["union() {"]
        
        # Generate pills
        word_index = self.first_word
        rear_word_index = self.rear_first_word
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = col * HORIZONTAL_SPACING
                y = row * VERTICAL_SPACING
                
                front_word = self.word_list[word_index][:self.word_length]
                rear_word = self.word_list[rear_word_index][:self.word_length]
                
                code.append(self.generate_pill(x, y, front_word, rear_word))
                
                word_index += 1
                rear_word_index += 1
        
        # Generate horizontal links
        for row in range(self.num_rows):
            for col in range(self.num_cols - 1):
                x1 = col * HORIZONTAL_SPACING + PILL_WIDTH_CORE/2 + PILL_CIRCLE_RADIUS
                y1 = row * VERTICAL_SPACING
                x2 = (col + 1) * HORIZONTAL_SPACING - PILL_WIDTH_CORE/2 - PILL_CIRCLE_RADIUS
                y2 = y1
                
                code.append(self.generate_link(x1, y1, x2, y2, True))
        
        # Generate vertical links
        for row in range(self.num_rows - 1):
            for col in range(self.num_cols):
                x1 = col * HORIZONTAL_SPACING
                y1 = row * VERTICAL_SPACING + PILL_HEIGHT/2
                x2 = x1
                y2 = (row + 1) * VERTICAL_SPACING - PILL_HEIGHT/2
                
                code.append(self.generate_link(x1, y1, x2, y2, False))
        
        code.append("}")
        return "\n".join(code)
    
    def generate_full_code(self) -> str:
        """Generate the complete OpenSCAD code."""
        header = self.generate_openscad_header()
        grid = self.generate_pill_grid()
        
        return header + "\n" + grid


def main():
    """Parse command line arguments and generate OpenSCAD code."""
    parser = argparse.ArgumentParser(description="Generate OpenSCAD code for BIP39 word grid.")
    parser.add_argument("--start", type=int, default=1, help="Index of the first word (1-2048)")
    parser.add_argument("--cols", type=int, default=6, help="Number of columns in the grid")
    parser.add_argument("--rows", type=int, default=4, help="Number of rows in the grid")
    parser.add_argument("--font", type=str, default="Fredoka", help="Font to use for text")
    parser.add_argument("--length", type=int, default=4, help="Number of characters to show for each word")
    parser.add_argument("--color", type=str, help="Color for the pills (e.g., 'orange')")
    parser.add_argument("--output", type=str, help="Output file (defaults to stdout)")
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.start < 1 or args.start > 2048:
        parser.error("Start word index must be between 1 and 2048")
    
    if args.length < 1:
        parser.error("Word length must be at least 1")
    
    # Create the generator
    generator = PillGridGenerator(
        first_word=args.start,
        num_cols=args.cols,
        num_rows=args.rows,
        word_list=BIP_39_LIST,
        font=args.font,
        word_length=args.length,
        color=args.color
    )
    
    # Generate the code
    scad_code = generator.generate_full_code()
    
    # Output the code
    if args.output:
        with open(args.output, 'w') as file:
            file.write(scad_code)
        print(f"OpenSCAD code written to {args.output}")
    else:
        print(scad_code)


if __name__ == "__main__":
    main()
