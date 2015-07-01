#! /usr/bin/env python

import random
class Door:
	def __init__(self, source, dest):
		self.source = source
		self.dest = dest
class Room:
	def __init__(self, i):
		self.iden = i
		self.visited = False

def IsExitPossible(room, doorSet, destRoom):
	room.visited = True
	if room.iden == destRoom.iden:
		return True
	for door in doorSet:
		if door.source.iden == room.iden and door.dest.visited == False:
			exit = IsExitPossible(door.dest, doorSet, destRoom)
			if exit == True:
				return exit
	return False

def main():
	Rooms = []
	Doors = []
	numRooms = 5
	numDoors = 6
	for i in range(numRooms):
		Rooms.append(Room(i))
	for i in range(numDoors):
		Doors.append(Door(Rooms[random.randint(0, numRooms -1)], Rooms[random.randint(0,
		numRooms-1)]))
		print "Door %s source=%s dest=%s" %(i, Doors[i].source.iden,
		Doors[i].dest.iden)
	print IsExitPossible(Rooms[0], Doors, Rooms[numRooms - 1])

if __name__ == "__main__":
	main()
