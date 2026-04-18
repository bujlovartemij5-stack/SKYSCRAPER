import time
from mcpi.minecraft import Minecraft
import collections
collections.Iterable = collections.abc.Iterable
mc = Minecraft.create()
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import collections
collections.Iterable=collections.abc.Iterable
x,y,z=mc.player.getTilePos()
x+=1
y+=1
z+=1
height=220
width=40
lenght=40
floor_height=3
GLASS=block.STAINED_GLASS.id
WOOD=block.WOOD_PLANKS.id
STONE=block.IRON_BLOCK.id
IRON=block.IRON_BLOCK.id
LIGHT=block.GLOWSTONE_BLOCK.id
for i in range(width):
    mc.setBlocks(x+i, y, z, x+i, y+height, z+lenght, block.AIR.id)
    sleep(0.1)
for h in range(height):
    mc.setBlocks(x,y+h,z,x+width,y+h,z+lenght,STONE)
    sleep(0.1)
for h in range(height-2):
    mc.setBlocks(x+1, y+1+h, z+1,
       x+width-1, y+1+h,z+lenght-1,block.AIR.id)
    sleep(0.1)
for h in range(floor_height,height,floor_height):
    mc.setBlocks(x+1, y+h, z+1,
        x+width-1, y+h, z+lenght-1, WOOD)
    sleep(0.1)
for h in range(5, height, 5):
    for w in range(5, width, 4):
        for l in range (5, lenght, 4):
            mc.setBlocks(x+w,y+h, z+l, LIGHT)
            sleep(0.01)
    sleep(0.01)
    mc.postToChat("Build is complete")