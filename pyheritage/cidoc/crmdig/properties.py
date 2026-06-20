# -*- coding: utf-8 -*-

"""CRMDig property models;

(Mixin classes for entity models);

CRMDig v5.0

------------------------------------------------
Properties
------------------------------------------------
L1  digitized                          D2  -> E18
L2  used as source                     D10 -> D1
L10 had input                          D7  -> D1
L11 had output                         D7  -> D1
L12 happened on device                 D7  -> D8
L13 used parameters                    D10 -> D1
L14 transferred                        D12 -> D1
L15 has sender                         D12 -> D8
L16 has receiver                       D12 -> D8
L18 has modified                       D7  -> D13
L19 stores                             D13 -> D1
L20 has created                        D11 -> D9
L21 used as derivation source          D3  -> D1
L22 created derivative                 D3  -> D1
L23 used software or firmware          D7  -> D14
L24 created logfile                    D10 -> D1
L43 annotates                          D29 -> E1
L48 created annotation                 D30 -> D29
L49 is primary area of                 D35 -> D1
L50 is propagated area                 D35 -> D1
L54 is same as                         E1  -> E1
L61 contains value set of              D9  -> E54

"""
