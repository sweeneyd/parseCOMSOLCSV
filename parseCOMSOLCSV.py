# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 16:08:10 2014

@author: Dan
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

class parseCOMSOLCSV(object):
    def __init__(self, filename, comment_flag):
        if len(filename) > 1:
            self.data_array_dict = self.generateDictionary(filename, comment_flag)
        else:
            data_array = self.readCSV(filename)
            self.data_array = self.removeComments(data_array, comment_flag)
        
    def readCSV(self, filepath):
        data_array = np.array([])
        with open(filepath, 'rb') as csvfile:
            filereader = csv.reader(csvfile, delimiter = '\t', quotechar = '|')
            for row in filereader:
                data_array = np.append(data_array, row)
        return data_array
    
    def getColumnNames(self, data_array, comment_flag):
        #Parse columns into arrays as part of th data_array class that can be accessed in an object-oriented way        
        
    def removeComments(self, data_array, comment_flag):
        data_array = np.array(data_array)
        for row in data_array:
            words_in_line = row[0].split()
            if words_in_line[0] == comment_flag:
                data_array = np.delete(data_array, 0, axis = 0)
        return data_array
        
    def generateDictionary(self, filename_array, comment_flag):
        data_array_dictionary = {}
        for k in range(len(filename_array)):
            data_array = self.readCSV(filename_array[k])
            data_array = self.removeComments(data_array, comment_flag)
            value = data_array
            key = filename_array[k].split('.', 1)
            key = key[0]
            data_array_dictionary[key] = value
        return data_array_dictionary

if __name__ == '__main__':
    
    filenames = ['100V_isosurf250V.txt', 
                 '200V_isosurf250V.txt', 
                 '300V_isosurf250V.txt', 
                 '400V_isosurf250V.txt', 
                 '500V_isosurf250V.txt', 
                 '600V_isosurf250V.txt']

    foo = parseCSV(filenames, '%')