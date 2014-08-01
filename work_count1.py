#-*-coding:utf-8-*-
import MySQLdb

class DB:
    def first_time(self):
	try:
            conn = MySQLdb.connect(host = "localhost", user = "wangyu",passwd = "I@tianpin",db = "pinphp_test",port = 3306)
	    cur = conn.cursor()
	    cur.execute("set names utf8")
	    dict_first = {}
            status0 = 0
#            status1 = 0
#            status2 = 0
#            list_id = []
#            cur.execute("select id,title from pin_album where global=1 or global=9")
#            first_result = cur.fetchall()
#            for i in first_result:
        #	print i[0],i[1]
        	cur.execute("select item_id from pin_album_item where album_id=%s",i[0])
            	first_result1 = cur.fetchall()
		print len(first_result1)
        	for j in first_result1:
       #		    print j[0],
                    list_id.append(j[0])
        	    count = cur.execute("select id,album_name,status from pin_item where  id=%s",j[0])	
       # 	    count1 = cur.execute("select count(id) from pin_item where status=2 and id=%s",j[0])	
        #	    count2 = cur.execute("select id,album_name,status from pin_item where status=0 and id=%s",j[0])	
        	    result2 = cur.fetchall()
        	    for a in result2:
        		if  a[2] == 0:
        		    status0 = status0 + 1
        	    	elif a[2] == 1:
        		    status1 = status1 + 1
        		elif a[2] == 2:
        		    status2 = status2 + 1
     
           	print i[1],status0,status1,status2
		dict_first[i[1]]=status0,status1,status2
    	    cur.close()
	    conn.close()
	    print "a" 
	except MySQLdb.Error,e:
	    print "Error"
	print len(list_id)
    	return first_result,first_result1,dict_first,list_id
	
    def end_time(self,first_time):
	try:
            conn = MySQLdb.connect(host = "localhost", user = "wangyu",passwd = "I@tianpin",db = "pinphp_test",port = 3306)
	    cur = conn.cursor()
	
	    cur.execute("set names utf8")
	    first_result,first_result1,dict_end,list_id = first_time	
	    print len(list_id)
            for oo in first_result:
		end_status0 = 0
                end_status1 = 0
                end_status2 = 0
		
                for pp in list_id:
		    end_status0 = 0
                    end_status1 = 0
                    end_status2 = 0
		

	            print end_status0,end_status1,end_status2
	            print pp,	
                    count = cur.execute("select id,album_name,status from pin_item where  id=%s",pp)	
                    result2 = cur.fetchall()
                    for a in result2:
                	if  a[2] == 0:
                	    end_status0 = end_status0 + 1
                        elif a[2] == 1:
                	    end_status1 = end_status1 + 1
                	elif a[2] == 2:
                	    end_status2 = end_status2 + 1

	            print end_status0,end_status1,end_status2
	        print end_status0,end_status1,end_status2
	    	dict_end[oo[1]]=end_status0,end_status1,end_status2
		   
    	    cur.close()
	    conn.close()
	except MySQLdb.Error,e:
	    print "Error"
#	print end_status0 - status0,end_status1 - status1,end_status2 - status2
    	return dict_end

    def day_time():
	try:
            conn = MySQLdb.connect(host = "localhost", user = "wangyu",passwd = "I@tianpin",db = "pinphp_test",port = 3306)
	    cur = conn.cursor()
	
	    cur.execute("set names utf8")
            end_status0 = 0
            end_status1 = 0
            end_status2 = 0
            cur.execute("select id,title from pin_album where global=1 or global=9")
            result = cur.fetchall()
            for i in first_result:
        	print i[0],i[1]
        	cur.execute("select item_id from pin_album_item where album_id=%s",i[0])
            	result1 = cur.fetchall()
        	for j in first_result1:
       	            print j[0]
        	    count = cur.execute("select id,album_name,status from pin_item where  id=%s",j[0])	
       # 	    count1 = cur.execute("select count(id) from pin_item where status=2 and id=%s",j[0])	
        #	    count2 = cur.execute("select id,album_name,status from pin_item where status=0 and id=%s",j[0])	
        	    result2 = cur.fetchall()
        	    for a in result2:
        		if  a[2] == 0:
        		    end_status0 = end_status0 + 1
        	    	elif a[2] == 1:
        		    end_status1 = end_status1 + 1
        		elif a[2] == 2:
        		    end_status2 = end_status2 + 1
     
   #        	print i[1],end_status0,end_status1,end_status2
		dict_end[i[1]]=end_status0,end_status1,end_status2
    	    cur.close()
	    conn.close()
 
	except MySQLdb.Error,e:
	    print "Error"
#	print end_status0 - status0,end_status1 - status1,end_status2 - status2
    	return dict_end




			

if __name__ == "__main__":
    db = DB()
    first_time = db.first_time()
    #print first_time[2]
    db.end_time(first_time)
   # print end_time


