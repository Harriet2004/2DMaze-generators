# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Harriet Mathew', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):

    def __init__(self):
        # initialises new graph object with empty adjacency list to represent the graph structure
        self.list = {}


    def addVertex(self, label:Coordinates):
        # new vertex with the label is added to the graph
        # this initialises a dictionary to represent the adjacency list of this vertex
        self.list[label] = {}

    def addVertices(self, vertLabels:List[Coordinates]):
        # for each vertex in the list, we are calling the addVertex function to add them as a new node
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        """ we check if two vertices are adjacent and add the edge accordingly
            depending on the bool value stored in addWall. Returns true if operation
            was successful and false otherwise """
        if vert1.isAdjacent(vert2):
            self.list[vert1][vert2] = addWall
            self.list[vert2][vert1] = addWall
            return True
        return False


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        # checking if the vertices are present each other's list of vertices
        if vert1 in self.list[vert2] and vert2 in self.list[vert1]:
            # if they are present, we proceed to update the status of the wall
            # returns true if operation was successful and false otherwise
            self.list[vert1][vert2] = wallStatus
            self.list[vert2][vert1] = wallStatus
            return True
        return False


    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # we check if the vertices are adjacent and remove an edge accordingly
        # returns true if operation was successful and false otherwise
        if vert1.isAdjacent(vert2):
            self.list[vert1].remove(vert2)
            self.list[vert2].remove(vert1)
            return True
        return False

    def hasVertex(self, label:Coordinates)->bool:
        # checking if the vertex is in the list
        # returns true if operation was successful and false otherwise
        if label in self.list:
            return True
        else:
            return False


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # check if an edge exists between the two vertices
        # returns true if operation was successful and false otherwise
        if vert1 in self.list[vert2]:
            return True
        return False

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # first checking if the vertices are there in the list
        if vert1 in self.list[vert2] and vert2 in self.list[vert1]:
            # then return the status of wall
            return self.list[vert1][vert2]
        return False


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        # just return the list of neighbours from the particular of node
        return self.list[label]