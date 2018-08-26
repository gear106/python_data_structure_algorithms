# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:28:32 2018

@author: GEAR
"""
'''
采用hash表实现字典
'''
class HashTable(object):
    def __init__(self):
        self.size = 11  # hash 表初始大小最好为质数，可使得冲突解决算法可以尽可能高效
        self.slots = [None] * self.size
        self.value = [None] * self.size
        
    
    def hashfunction(self, key, size):  # 采用求余法实现hash函数
        return key % size
    
    def rehash(self, oldhash, size):    # 采用加1法解决冲突问题
        return (oldhash + 1) % size
    
    def put(self, key, value):
        '''
        向字典中添加一个新的键-值对，如果已经在字典中，则用新值替代旧值
        '''
        hashValue = self.hashfunction(key, len(self.slots))
        
        if self.slots[hashValue] == None:   #如不存在新键，则添加新键-值对
            self.slots[hashValue] = key
            self.value[hashValue] = value
        else:
            if self.slots[hashValue] == key: # 若键存在，用新值替换旧值
                self.value[hashValue] = value
            else:
                nextslot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:  # 寻找空槽位
                    nextslot = self.rehash(nextslot, len(self.slots)) # 空槽位加1
                if self.slots[nextslot] == None:
                    self.slots[nextslot]  = key
                    self.value[nextslot] = value
                else:
                    self.value[nextslot] = data
            
    def get(self, key):
        '''
        寻找字典中键值对应的值
        '''
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and not found and not stop:            
            if self.slots[position] == key:
                found = True
                data = self.value[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot: # 若回到初始槽的位置，说明已经找完所有位置
                    stop = True    #停止搜索
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
        
if __name__ == '__main__':
    
    H = HashTable()
    H[54] = 'cat'    # 将键-值放入字典中
    H[26] = 'dog'
    H[93] = 'lion'
    H[17] = 'tiger'
    H[77] = 'bird'
    H[31] = 'cow'
    H[44] = 'goat'
    H[55] = 'pig'
    H[20] = 'chicken'
    print(H.slots)
    print(H.value)
    print(H[99]) # 查找键99对应的值
        