# -*- coding: utf-8 -*-

"""CRMtex property models;

(Mixin classes for entity models);

CRMtex v2.0 (June 2023)
https://cidoc-crm.org/extensions/crmtex

-------------------------------------------------
Properties
-------------------------------------------------
TXP1  used writing system                  TX2  -> TX3
TXP2  includes                             TX4  -> TX1
TXP4  has segment                          TX1  -> TX7
TXP5  wrote                                TX2  -> TX1
TXP6  encodes                              TX3  -> E56
TXP7  has item                             TX13 -> TX8
TXP8  has component                        TX1  -> TX9
TXP9  is encoded using                     TX1  -> TX3
TXP10 deciphered text                      TX5  -> E24
TXP11 transcribed                          TX6  -> TX12
TXP12 has style                            TX1  -> TX10
TXP13 deciphered via the representation    TX5  -> E36
TXP14 used copy or representation of       TX5  -> TX1
TXP15 recorded correspondence              TX5  -> TX12
TXP16 employs script                       TX3  -> TX13
TXP17 has part                             TX12 -> TX12
TXP18 read                                 TX14 -> TX1

"""
