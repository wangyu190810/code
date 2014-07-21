#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: pinan.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-07-20
#Description: 
import csv
import sqlite3
import MySQLdb
def train():
    with open("train_target_first.csv","r") as ttf:
        tt = csv.DictReader(ttf)
        a = [(i["id"],
            i["target"]) for i in tt]
    return a
def data():
    with open("data_first.csv","r") as dt:
        af = csv.DictReader(dt)       
        a = [(i["id"],i["feature_1"],i["feature_2"],i["feature_3"],i["feature_4"],i["feature_5"],i["feature_6"],i["feature_7"],i["feature_8"],i["feature_9"],i["feature_10"],i["feature_11"],i["feature_12"],i["feature_13"],i["feature_14"],i["feature_15"],i["feature_16"],i["feature_17"],i["feature_18"],i["feature_19"],i["feature_20"],i["feature_21"],i["feature_22"],i["feature_23"],i["feature_24"],i["feature_25"],i["feature_26"],i["feature_27"],i["feature_28"],i["feature_29"],i["feature_30"],i["feature_31"],i["feature_32"],i["feature_33"],i["feature_34"],i["feature_35"],i["feature_36"],i["feature_37"],i["feature_38"],i["feature_39"],i["feature_40"],i["feature_41"],i["feature_42"],i["feature_43"],i["feature_44"],i["feature_45"],i["feature_46"],i["feature_47"],i["feature_48"],i["feature_49"],i["feature_50"],i["feature_51"],i["feature_52"],i["feature_53"],i["feature_54"],i["feature_55"],i["feature_56"],i["feature_57"],i["feature_58"],i["feature_59"],i["feature_60"],i["feature_61"],i["feature_62"],i["feature_63"],i["feature_64"],i["feature_65"],i["feature_66"],i["feature_67"],i["feature_68"],i["feature_69"],i["feature_70"],i["feature_71"],i["feature_72"],i["feature_73"],i["feature_74"],i["feature_75"],i["feature_76"],i["feature_77"],i["feature_78"],i["feature_79"],i["feature_80"],i["feature_81"],i["feature_82"],i["feature_83"],i["feature_84"],i["feature_85"],i["feature_86"],i["feature_87"],i["feature_88"],i["feature_89"],i["feature_90"],i["feature_91"],i["feature_92"],i["feature_93"],i["feature_94"],i["feature_95"],i["feature_96"],i["feature_97"],i["feature_98"],i["feature_99"],i["feature_100"],i["feature_101"],i["feature_102"],i["feature_103"],i["feature_104"],i["feature_105"],i["feature_106"],i["feature_107"],i["feature_108"],i["feature_109"],i["feature_110"],i["feature_111"],i["feature_112"],i["feature_113"],i["feature_114"],i["feature_115"],i["feature_116"],i["feature_117"],i["feature_118"],i["feature_119"],i["feature_120"],i["feature_121"],i["feature_122"],i["feature_123"],i["feature_124"],       i["feature_125"],i["feature_126"],i["feature_127"],i["feature_128"],i["feature_129"],i["feature_130"],i["feature_131"],i["feature_132"],i["feature_133"],i["feature_134"],i["feature_135"],i["feature_136"],i["feature_137"],i["feature_138"],i["feature_139"],i["feature_140"],i["feature_141"],i["feature_142"],i["feature_143"],i["feature_144"],i["feature_145"],i["feature_146"],i["feature_147"],i["feature_148"]) for i in af]
    return a


#a = train()

conn = sqlite3.connect("first.db")
cur = conn.cursor()

sql = "insert into data(id,feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10,feature_11,feature_12,feature_13,feature_14,feature_15,feature_16,feature_17,feature_18,feature_19,feature_20,feature_21,feature_22,feature_23,feature_24,feature_25,feature_26,feature_27,feature_28,feature_29,feature_30,feature_31,feature_32,feature_33,feature_34,feature_35,feature_36,feature_37,feature_38,feature_39,feature_40,feature_41,feature_42,feature_43,feature_44,feature_45,feature_46,feature_47,feature_48,feature_49,feature_50,feature_51,feature_52,feature_53,feature_54,feature_55,feature_56,feature_57,feature_58,feature_59,feature_60,feature_61,feature_62,feature_63,feature_64,feature_65,feature_66,feature_67,feature_68,feature_69,feature_70,feature_71,feature_72,feature_73,feature_74,feature_75,feature_76,feature_77,feature_78,feature_79,feature_80,feature_81,feature_82,feature_83,feature_84,feature_85,feature_86,feature_87,feature_88,feature_89,feature_90,feature_91,feature_92,feature_93,feature_94,feature_95,feature_96,feature_97,feature_98,feature_99,feature_100,feature_101,feature_102,feature_103,    feature_104,feature_105,feature_106,feature_107,feature_108,feature_109,feature_110,            feature_111,feature_112,feature_113,feature_114,feature_115,feature_116,feature_117,        feature_118,feature_119,feature_120,feature_121,feature_122,feature_123,feature_124,            feature_125,feature_126,feature_127,feature_128,feature_129,feature_130,feature_131,            feature_132,feature_133,feature_134,feature_135,feature_136,feature_137,feature_138,            feature_139,feature_140,feature_141,feature_142,feature_143,feature_144,feature_145,            feature_146,feature_147,feature_148) values ("

aaa = ",?"*149

sql = sql+aaa[1:]
sql = sql+');"'
a=data()
print "start"
cur.executemany(sql,a)
cur.close()
conn.close()

#print a[1][0]

#print data()


