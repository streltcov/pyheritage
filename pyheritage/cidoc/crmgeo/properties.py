# -*- coding: utf-8 -*-

"""CRMgeo property models;

(Mixin classes for entity models);

CRMgeo v1.2 (original 2015)

------------------------------------------------
Properties
------------------------------------------------
Q1  occupied                         E4  -> SP1
Q2  occupied                         E18 -> SP1
Q3  has temporal projection          SP1 -> SP13
Q4  has spatial projection           SP1 -> SP2
Q5  defined in                       E53 -> SP3
Q6  is at rest in relation to        SP3 -> E18
Q7  describes                        SP4 -> SP3
Q8  is fixed on                      SP4 -> E26
Q9  is expressed in terms of         SP5 -> SP4
Q10 defines place                    SP5 -> SP6
Q11 approximates                     SP6 -> SP2
Q12 approximates                     SP7 -> SP1
Q13 approximates                     SP10 -> SP13
Q14 defines time                     SP14 -> SP10
Q15 is expressed in terms of         SP14 -> SP11
Q16 defines spacetime volume         SP12 -> SP7
Q17 is expressed in terms of         SP12 -> SP11
Q18 is expressed in terms of         SP12 -> SP4
Q19 has reference event              SP11 -> E5

"""
