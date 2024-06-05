# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):

    def __init__(self):
        # initialises new graph object with empty adjacency matrix to represent the graph structure
        self.matrix = {}



    def addVertex(self, label:Coordinates):
        # new vertex with the label is added to the graph
        # this initialises a dictionary to represent the
        self.matrix[label] = {}



    def addVertices(self, vertLabels:List[Coordinates]):
        # now for each label in the list, we add it
        for label in vertLabels:
            self.addVertex(label)
            # we access vertLabel again, and make an edge in a 2d form that is defaulted to False
            for nextlabel in vertLabels:
                self.matrix[label][nextlabel] = False



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        """ we check if two vertices are adjacent and add the edge accordingly
            depending on the bool value stored in addWall. Returns true if operation
            was successful and false otherwise """
        if vert1.isAdjacent(vert2):
            self.matrix[vert1][vert2] = addWall
            self.matrix[vert2][vert1] = addWall
            return True
        return False



    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        """ we check if two vertices are adjacent and add update the wall accordingly
            depending on the bool value stored in wallStatus. Returns true if operation
            was successful and false otherwise """
        if vert1 in self.matrix[vert2] and vert2 in self.matrix[vert1]:
            if vert1.isAdjacent(vert2):
                self.matrix[vert1][vert2] = wallStatus
                self.matrix[vert2][vert1] = wallStatus
                return True
        return False



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # we check if the vertices are adjacent and remove an edge accordingly
        # returns true if operation was successful and false otherwise
        if vert1.isAdjacent(vert2):
            self.matrix[vert1][vert2] = False
            self.matrix[vert2][vert1] = False
            return True
        return False




    def hasVertex(self, label:Coordinates)->bool:
        # we check if the vertex is present in matrix and return values accordingly
        # returns true if operation was successful and false otherwise
        if label in self.matrix:
            return True
        return False



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        """ we check if there is an edge in the matrix by checking
            if the vert1 is there in vert2 and return value accordingly. Returns true if
            operation was successful and false otherwise """
        if vert1 in self.matrix[vert2]:
            return True
        return False



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # check the status of the relationship between vert1 and vert2 and return if there exists one
        # returns true if operation was successful and false otherwise
        if self.matrix[vert1][vert2]:
            return True
        return False



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        # a list for neighbours is created
        neighbours = []
        for i in self.matrix[label]:
            # now for each element in the label, we check if they are neighbours and add to the neighbours list
            if self.matrix[label][i]:
                neighbours.append(i)
        return neighbours

