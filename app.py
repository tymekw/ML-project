import os

# dataset_path = "C:\\Users\\P1\\Desktop\\githubRepos\\OIDv4_ToolKit\\OID\\Dataset\\validation"
#
# directory_contents = os.listdir(dataset_path)
#
# for subdirectory in directory_contents:

google = """Adhesive  tape  Aircraft  Airplane  Alarm clock  Alpaca  Ambulance  Apple  Armadillo  Artichoke  Axe  Backpack  Bagel  Balance beam  Ball  Balloon  Banana  Band-aid  Barge  Barrel  Baseball bat  Baseball glove  Bat (Animal)  Beaker  Bear  Beer  Bell pepper  Belt  Bicycle wheel  Billiard table  Binoculars  Bird  Blue jay  Bomb  Book  Boot  Bottle  Bottle opener  Bowl  Box  Boy  Bread  Briefcase  Broccoli  Bronze sculpture  Brown bear  Bull  Burrito  Bus  Bust  Cabbage  Cake  Calculator  Camel  Camera  Canary  Candle  Canoe  Cantaloupe  Car  Carnivore  Carrot  Cat  Cattle  Cello  Cheese  Cheetah  Chest of drawers  Chicken  Chisel  Chopsticks  Christmas tree  Clock  Clothing  Cocktail  Cocktail shaker  Coffee  Coffee cup  Coin  Common fig  Common sunflower  Computer keyboard  Computer mouse  Cookie  Cooking spray  Corded phone  Couch  Cowboy hat  Cricket ball  Crocodile  Croissant  Cucumber  Dagger  Diaper  Dice  Digital clock  Dog  Dog bed  Dolphin  Door handle  Doughnut  Dress  Drill (Tool)  Drink  Drinking straw  Duck  Dumbbell  Eagle  Elephant  Envelope  Eraser  Facial tissue holder  Falcon  Fedora  Filing cabinet  Fire hydrant  Fish  Flag  Flashlight  Flower  Flowerpot  Flute  Flying disc  Food processor  Football  Fox  Frog  Frying pan  Garden Asparagus  Giraffe  Girl  Glove  Goat  Goldfish  Golf ball  Goose  Grape  Grapefruit  Guacamole  Guitar  Hair dryer  Hair spray  Hamburger  Hammer  Hamster  Hand dryer  Handbag  Handgun  Harbor seal  Harmonica  Harpsichord  Hat  Heater  Hedgehog  High heels  Hippopotamus  Horse  Hot dog  Human body  Human ear  Human mouth  Ipod  Jaguar (Animal)  Jeans  Jet ski  Jug  Juice  Kangaroo  Kettle  Kitchen knife  Kite  Knife  Koala  Ladle  Laptop  Lemon  Leopard  Light switch  Lighthouse  Limousine  Lion  Lipstick  Lizard  Loveseat  Luggage and bags  Lynx  Magpie  Man  Mango  Maracas  Measuring cup  Microwave oven  Milk  Miniskirt  Missile  Mixing bowl  Mobile phone  Monkey  Motorcycle  Mouse  Muffin  Mug  Mule  Mushroom  Nail (Construction)  Orange  Ostrich  Otter  Oven  Owl  Oyster  Pancake  Panda  Paper cutter  Paper towel  Parrot  Pastry  Peach  Pear  Pen  Pencil case  Penguin  Person  Piano  Picture frame  Pig  Pillow  Pitcher (Container)  Pizza  Pizza cutter  Plastic bag  Platter  Polar bear  Pomegranate  Popcorn  Potato  Power plugs and sockets  Pressure cooker  Pretzel  Printer  Pumpkin  Punching bag  Rabbit  Raccoon  Racket  Radish  Raven  Red panda  Remote control  Reptile  Rhinoceros  Rocket  Roller skates  Rose  Rugby ball  Ruler  Sandwich  Saucer  Saxophone  Scarf  Scissors  Screwdriver  Sculpture  Sea lion  Sea turtle  Seat belt  Segway  Shark  Sheep  Shirt  Shorts  Shower  Skateboard  Skirt  Skull  Skunk  Skyscraper  Slow cooker  Snake  Snowmobile  Soap dispenser  Sock  Sofa bed  Sombrero  Sparrow  Spatula  Spoon  Squash (Plant)  Squirrel  Stapler  Starfish  Stop sign  Strawberry  Studio couch  Submarine sandwich  Suit  Suitcase  Sun hat  Surfboard  Swan  Swim cap  Swimwear  Sword  Table tennis racket  Tablet computer  Tank  Tap  Tart  Taxi  Tea  Teapot  Teddy bear  Tennis ball  Tennis racket  Tie  Tiger  Toaster  Toilet  Toilet paper  Tomato  Torch  Tortoise  Towel  Toy  Traffic light  Traffic sign  Train  Trousers  Truck  Turkey  Turtle  Van  Vase  Vehicle registration plate  Volleyball (Ball)  Waffle  Washing machine  Waste container  Watch  Watermelon  Whale  Wheel  Whiteboard  Wine  Winter melon  Wok  Woman  Woodpecker  Wrench  Zebra  Zucchini"""
coco = """person
bicycle
car
motorcycle
airplane
bus
train
truck
boat
traffic light
fire hydrant
street sign
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
hat
backpack
umbrella
shoe
eye glasses
handbag
tie
suitcase
frisbee
skis
snowboard
sports ball
kite
baseball bat
baseball glove
skateboard
surfboard
tennis racket
bottle
plate
wine glass
cup
fork
knife
spoon
bowl
banana
apple
sandwich
orange
broccoli
carrot
hot dog
pizza
donut
cake
chair
couch
potted plant
bed
mirror
dining table
window
desk
toilet
door
tv
laptop
mouse
remote
keyboard
cell phone
microwave
oven
toaster
sink
refrigerator
blender
book
clock
vase
scissors
teddy bear
hair drier
toothbrush
hair brush """

for line in coco.splitlines():
    if line.strip().lower() not in google.lower():
        print("couldnt find coco : ", line, "  in google")
