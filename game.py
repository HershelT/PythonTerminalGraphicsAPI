from ChunkLoader import *
from gameSprites import *
import threading

#initialize the screen
if len(sys.argv) <= 1:
    clear()
    resizeWindow(2)
time.sleep(0.5)
SCENE_HEIGHT = 8
SCENE_WIDTH = 10
CHUNK_COUNT = 4

# def washScreen(screen):
#     screen = square(SCENE_HEIGHT*BLOCK_SIZE, SCENE_WIDTH*BLOCK_SIZE, BACKGROUND_COLOR)

Scene = screen(SCENE_HEIGHT * BLOCK_SIZE, SCENE_WIDTH * BLOCK_SIZE, BACKGROUND_COLOR)

#Creating Chunks
Chunk = ChunkLoader(SCENE_HEIGHT, SCENE_WIDTH, BLOCK_SIZE, BLOCK_SIZE, BACKGROUND_COLOR)
def generateSeed(Chunk : ChunkLoader, currentChunk = 0):
    for i in range(0, CHUNK_COUNT):
        Chunk.generateChunks()
        #place blocks randomly in the bounds of the chunk
        for y in range(0, SCENE_HEIGHT):
            for x in range(0, SCENE_WIDTH):
                if y != int(SCENE_HEIGHT/2) or x != int(SCENE_WIDTH/2):
                    #randomly place solid blocks
                    if random.randint(0, 1) == 1:
                        # randomly place solid blocks
                        random_key = random.choice(list(SPRITE_SHEET.keys()))
                        if random.randint(0, 1) == 1:
                            Sprite = SPRITE_SHEET["TNT"]
                            Chunk.setBlock(i, (x, y), Block(Sprite.getName(), Sprite.getSprite(), Sprite.getSolid(), Sprite.getMoveable(), Sprite.getBreakable()))
                        else:
                            Sprite = SPRITE_SHEET[random_key]
                            Chunk.setBlock(i, (x, y), Block(Sprite.getName(), Sprite.getSprite(), Sprite.getSolid(), Sprite.getMoveable(), Sprite.getBreakable()))
generateSeed(Chunk)
#Creating player sprite
sprite = square(BLOCK_SIZE-4, BLOCK_SIZE-4, BACKGROUND_COLOR)
drawDownTriangle(sprite, yellow, (6, 5), 4)
drawDownTriangle(sprite, yellow, (5, 5), 4)
drawUpTriangle(sprite, magenta, (6, 6), 4)
drawUpTriangle(sprite, magenta, (5, 6), 4)
playerSprite = addToScreen(square(BLOCK_SIZE, BLOCK_SIZE, BACKGROUND_COLOR ), sprite, 2, 2, True)
for i in range(0, 3):
    addToScreenWithColor(playerSprite, rotate(sprite, 270), BACKGROUND_COLOR, 2, 2, True)
addToScreenWithoutColor(playerSprite, square(4, 4, rgb(255, 175, 135)), BACKGROUND_COLOR, 6, 10, True)
drawLine(playerSprite, black, (5, 10), (4, 8))
drawLine(playerSprite, black, (10, 10), (11, 8))
drawRectangle(playerSprite, white, (4, 7), (6, 9))
drawSetSquare(playerSprite, black, (7, 12), 1)
drawSetSquare(playerSprite, black, (9, 12), 1)
# drawLine(sprite, green, (0, 0), (5, 5))
# drawPG(sprite, red, 6, 5, (2, 2))
PLAYER = Player("PLAYER", playerSprite, int(SCENE_WIDTH/2), int(SCENE_HEIGHT/2), Chunk.getBlock(0, (int(SCENE_WIDTH/2), int(SCENE_HEIGHT/2))))

Chunk.fillScreenWithChunk(Scene, PLAYER.getChunk())
# printScreen(Scene)

#initialize the keyboard listener
keys = MyKeyListener()
listener = keyboard.Listener(
    on_press=keys.on_press,
    on_release=keys.on_release
)
listener.start()

rotating = False
run = False
class RotateSpriteThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global rotating
        global run
        while run:
            rotating = True
            time.sleep(0.1)


rotatingThread = RotateSpriteThread()
rotatingThread.start()
# run = False


Chunk.changeBlockSprite(0, (PLAYER.getX(), PLAYER.getY()), PLAYER.getSprite())
triggerChange = True

while not keys.is_esc_pressed():
    #Screen is updated only when there is a change
    KEY_PRESSED = keys.get_pressed_key()
    if triggerChange:
        # Scene = screen(SCENE_HEIGHT * BLOCK_SIZE, SCENE_WIDTH * BLOCK_SIZE, BACKGROUND_COLOR)
        #Update the screen
        Chunk.fillScreenWithChunk(Scene, PLAYER.getChunk())
        printScreen(Scene)
        print(f"{black} X: {PLAYER.getX()} Y: {PLAYER.getY()} Chunk: {PLAYER.getChunk()} {reset}")
        time.sleep(0.05)
        triggerChange = False

    movement = keys.wasd()
    if (movement != False):
        #Update the player's last position
        PLAYER.setLastX(PLAYER.getX())
        PLAYER.setLastY(PLAYER.getY())
        #Which direction the player is facing
        PLAYER.setDirection(movement) 
        #Update PLAYER position
        if movement == "d": 
            if PLAYER.getX() < SCENE_WIDTH - 1:
                PLAYER.setX(PLAYER.getX() + 1)
        elif movement == "a":
            if PLAYER.getX() > 0:
                PLAYER.setX(PLAYER.getX() - 1)
        elif movement == "s":
            if PLAYER.getY() > 0:
                PLAYER.setY(PLAYER.getY() - 1)
        elif movement == "w": 
            if PLAYER.getY() < SCENE_HEIGHT - 1:
                PLAYER.setY(PLAYER.getY() + 1)
        #See if we can go over new block if it is  a solid block
        triggerChange = True
        BlockToCheck = Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()))
        if  BlockToCheck.getSolid() or (PLAYER.getX() == PLAYER.getLastX() and PLAYER.getY() == PLAYER.getLastY()):
            triggerChange = False
            #Push Block Forward
            if BlockToCheck.getMoveable():
                #get the position of block to be swapped
                toMove = PLAYER.calculateMovement()
                futureSwapPosition = (PLAYER.getX() + toMove[0], PLAYER.getY() + toMove[1])
                #Only swap blocks if next block is within bounds
                if futureSwapPosition[0] < SCENE_WIDTH and futureSwapPosition[0] >= 0 and futureSwapPosition[1] < SCENE_HEIGHT and futureSwapPosition[1] >= 0:
                    #Can only swap if next block is air
                    if Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX() + toMove[0], PLAYER.getY() + toMove[1])).getName() == "Air":
                        #Swap the block with the air block
                        Chunk.swapBlocks(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), (PLAYER.getX() + toMove[0], PLAYER.getY() + toMove[1]))
                        # Update trigger so player moves along with block
                        triggerChange = True   
            #If no interaction happens (i.e movement is blocked) then reset the player's position
            if not triggerChange:
                PLAYER.setX(PLAYER.getLastX())
                PLAYER.setY(PLAYER.getLastY())
                keys.keys_pressed.discard(all)
        if triggerChange:
            #Save the block that the player was stepping on
            oldPlayer = PLAYER.getBlockBehind().getBlockCopy()
            # save the block the player is about to step on
            currentChunkBlock = Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()))
            #Change the block that the player is on
            PLAYER.setBlockBehind(currentChunkBlock.getBlockCopy())
            #Set old position to what was overwritten
            Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getLastX(), PLAYER.getLastY()), oldPlayer)
            #Draw the player over the block we are about to step on
            chunkBlock = copy.deepcopy(Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY())).getSprite())
            chunkBlock = addToScreenWithoutColor(chunkBlock, PLAYER.getSprite(), BACKGROUND_COLOR, 0, 0, True)
            #Make the player step on the block
            Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), Block(PLAYER.getBlockBehind().getName(), chunkBlock))
    #Move between Chunks
    if keys.is_c_pressed() and PLAYER.getChunk() < Chunk.getChunkCount()-1:
        #set the block behind before moving to the next chunk
        Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), PLAYER.getBlockBehind().getBlockCopy())
        PLAYER.setChunk(PLAYER.getChunk() + 1)
        Chunk.changeBlockSprite(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), PLAYER.getSprite())
        triggerChange = True
    if keys.is_z_pressed() and PLAYER.getChunk() > 0:
        Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), PLAYER.getBlockBehind().getBlockCopy())
        PLAYER.setChunk(PLAYER.getChunk() - 1)
        Chunk.changeBlockSprite(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), PLAYER.getSprite())
        triggerChange = True
        
    if keys.is_x_pressed() or rotating:
        #Rotate the player sprite
        PLAYER.setSprite(rotate(PLAYER.getSprite(), 270))
        #GRab the block that the player is on  
        currentBlock = Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY())).getBlockCopy()
        #Rotate just the player sprite on block
        sprite = addToScreen(currentBlock.getSprite(), PLAYER.getBlockBehind().getSprite(), 0, 0, True)
        sprite = addToScreenWithoutColor(sprite, PLAYER.getSprite(), BACKGROUND_COLOR, 0, 0, True)
        #Update the block that the player is on
        Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), Block(currentBlock.getName(), sprite, currentBlock.getSolid(), currentBlock.getMoveable(), currentBlock.getBreakable()))
        #Update the screen
        triggerChange = True
        if rotating:
            rotating = False
    #erase the next block
    if keys.is_e_pressed():
        ToMove = PLAYER.calculateMovement()
        if PLAYER.getX() + ToMove[0] < SCENE_WIDTH and PLAYER.getX() + ToMove[0] >= 0 and PLAYER.getY() + ToMove[1] < SCENE_HEIGHT and PLAYER.getY() + ToMove[1] >= 0:
            #change block to air if block is breakable
            if Chunk.getBlock(PLAYER.getChunk(), (PLAYER.getX() + ToMove[0], PLAYER.getY() + ToMove[1])).getBreakable():
                Chunk.setBlock(PLAYER.getChunk(), (PLAYER.getX() + ToMove[0], PLAYER.getY() + ToMove[1]), Block("Air", square(BLOCK_SIZE, BLOCK_SIZE, BACKGROUND_COLOR), False, False, False))
                #update screen
                triggerChange = True

    if keys.is_r_pressed():
        # Scene = screen(SCENE_HEIGHT * BLOCK_SIZE, SCENE_WIDTH * BLOCK_SIZE, BACKGROUND_COLOR)
        #Regenerate the chunks to have nothing
        Chunk.clearChunks()
        #Regenerate the blocks into a new seed
        generateSeed(Chunk)
        #Place Player
        Chunk.changeBlockSprite(PLAYER.getChunk(), (PLAYER.getX(), PLAYER.getY()), PLAYER.getSprite())
        #Update the screen
        triggerChange = True

        
    keys.keys_pressed.discard(all)

run = False
rotatingThread.join()
sys.exit()    
