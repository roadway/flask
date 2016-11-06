#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file : dbconn.py
class People:
    #++/C#
    Count = 0 
    def __init__(self,name,age):
        self.name = name  
        self.age = age 
        People.Count += 1  
    def query(self,sql):
        #
        self.rs.Open(sql,self.conn,1,1)
        #
        return self.rs
        #
    def execute(self,sql):
        #
        return self.conn.execute(sql)