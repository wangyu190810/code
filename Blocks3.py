#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: importsql.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-06-30
#Description: 

import csv
import datetime
import tornado.ioloop
import tornado.web

def LocationFile():    
    with open("GeoLite2-City-Locations.csv","r") as fin:
        dr = csv.DictReader(fin)
        to_Locations = [(i["geoname_id"],
            i["continent_code"],
            i["continent_name"],
            i["country_iso_code"],
            i["country_name"],
            i["subdivision_iso_code"],
            i["subdivision_name"],
            i["city_name"],
            i["metro_code"],
            i["time_zone"]) for i in dr]
    return to_Locations
    
def BlockFile():
    with open("GeoLite2-City-Blocks.csv","r") as fin:
        dr = csv.DictReader(fin)
    
        to_db = [(i["network_start_ip"],
        i["network_mask_length"],
        i["geoname_id"],
        i["registered_country_geoname_id"],
        i["represented_country_geoname_id"],
        i["postal_code"],
        i["latitude"],
        i["longitude"],
        i["is_anonymous_proxy"],
        i["is_satellite_provider"]) for i in dr]
    return to_db
    
def set_Block_dict(to_db = {}):
    Blocks_dict = {}
    for ip_tuple in to_db:
        ip_list = list(ip_tuple)
        Blocks_dict[ip_list[0]] = ip_list[2]
    return Blocks_dict

def set_Locations_dict(to_Locations={}):
    Locations_dict = {}
    
    for Location in to_Locations:
        Location_id = list(Location)
        Locations_dict[Location_id[0]] = Location_id[1]+Location_id[4]+Location_id[8]+Location_id[9]

    return Locations_dict
class Index(tornado.web.RequestHandler):
    to_Locations = LocationFile()
    to_db = BlockFile()
    Blocks_dict = set_Block_dict(to_db)
    Locations_dict = set_Locations_dict(to_Locations)
    geoname_id=""
    def get(self):
        self.render("index.html",geoname_id=self.geoname_id)

    def post(self):

        print self.get_argument("ip")
        ip = self.get_argument("ip")
        str_ip_split = str(ip)
        str_ip1 = str_ip_split.split(".")
        str_ip = str_ip1[0]+"."+str_ip1[1]+"."+str_ip1[2]+".0"
        print str_ip
        answer = self.Blocks_dict[str_ip]
        self.geoname_id= self.Locations_dict[answer]
        print self.geoname_id
        print answer
        self.render("index.html",geoname_id=self.geoname_id)



application = tornado.web.Application([
    (r"/",Index),
    ])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


