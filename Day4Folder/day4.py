# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
# print("hello from day4")

########################################################################
# Task 1:
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1

counter = 5
while counter < 33:
    print(counter)
    counter+= 1



########################################################################
# Task 2:
def Teleport():
    agent.teleport_to_player()

player.on_chat("come", Teleport)

def Forward(steps):
    agent.move(FORWARD, steps)

player.on_chat("fw", Forward)

def Back(steps):
    agent.move(BACK, steps)

player.on_chat("bk", Back)

def Up(steps):
    agent.move(UP, steps)

player.on_chat("up", Up)

def Down(steps):
    agent.move(DOWN, steps)

player.on_chat("down", Down)

def TurnLeft():
    agent.turn(LEFT)

player.on_chat("tl", TurnLeft)

def TurnRight():
    agent.turn(RIGHT)

player.on_chat("tr", TurnRight)

def PlaceBlock(grass):
    agent.place(FORWARD)

player.on_chat("place", PlaceBlock)

def ObstacleCourse():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.turn(LEFT)
    agent.turn(LEFT)
    agent.turn(LEFT)
    agent.turn(LEFT)

player.on_chat("oc", ObstacleCourse)

def Spin():
    agent.turn(LEFT)
    agent.turn(LEFT)
    agent.turn(LEFT)
    agent.turn(LEFT)

player.on_chat("spin", Spin)

def Chat():
    for count in range(5):
        agent.move(FORWARD, 1)

player.on_chat("say", Chat)

def Chop():
    for i in range(6):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, 6)
    agent.collect_all()
    
player.on_chat("chop", Chop)

def ChopAll(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.turn(LEFT)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.turn(LEFT)
        agent.destroy(FORWARD)
        agent.move(FORWARD,1)
        agent.turn(LEFT)
        agent.move(FORWARD, 1)
        agent.turn(LEFT)
        agent.move(BACK, 1)
        agent.move(UP, 1)
    agent.move(DOWN,24)
    agent.collect_all()

player.on_chat("chopall", ChopAll)

def mining(length):
    for i in range(length):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

player.on_chat("mine", mining)

def TeleportMe():
    player.teleport(pos(453, 160, -1998))

player.on_chat("tm", TeleportMe)

def BuildWall(height, width):
    for j in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(RIGHT, 1)
        agent.move(DOWN, height)

player.on_chat("wall", BuildWall)

def BuildRoof(height, width):
    for j in range(width):
        for i in range(height):
            agent.place(DOWN)
            agent.move(FORWARD, 1)
        agent.move(RIGHT, 1)
        agent.move(BACK, height)

player.on_chat("roof", BuildRoof)

def DigDown():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.collect_all()

player.on_chat("dig", DigDown)

def Bridge(length):
    for i in range(length):
        agent.move(FORWARD, 1)
        agent.place(DOWN)
        
player.on_chat("bridge", Bridge)



########################################################################
# Additional exercises: