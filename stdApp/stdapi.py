from flask import Blueprint, jsonify,request,json
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource

stdapi=Blueprint('stdapi',__name__)
mysql=MySQL()


class Query(Resource):

  @stdapi.route('/std',methods=['POST','GET','PUT','DELETE'])
  def std():
    if request.method=="POST":
        jdata=json.loads(request.data)
        cur=mysql.connection.cursor()
        cur.execute('insert into std_data(std_name,std_phoneNo,std_address) values(%s,%s,%s)',(jdata['std_name'],jdata['std_phoneNo'],jdata['std_address']))
        mysql.connection.commit()
        return 'data is saved'

    if request.method=="GET":
      # headers = request.headers
      # auth = headers.get("X-Api-Key")
      # if auth == 'asoidewfoef':
        try:
          jdata=json.loads(request.data)
          for key in jdata:
              if (key == 'std_id'):
                cur=mysql.connection.cursor()
                cur.execute('select * from std_data where std_id=%s',[jdata['std_id']])

              if (key == 'std_name'):
                cur=mysql.connection.cursor()
                cur.execute('select * from std_data where std_name=%s',[jdata['std_name']])

              elif (key == 'std_phoneNo'):
                cur=mysql.connection.cursor()
                cur.execute('select * from std_data where std_phoneNo=%s',[jdata['std_phoneNo']])

              # elif (key == 'std_address'):
              #   cur=mysql.connection.cursor()
              #   cur.execute('select * from std_data where std_address=%s',[jdata['std_address']])
              ver=cur.fetchall()
              data={}
              data1=[]
              for i in ver:          
                  data={
                      'std_id':i[0],
                      'std_name':i[1],
                      'std_phoneNo':i[2],
                      'std_address':i[3]
                  }
                  data1.append(data)
              mysql.connection.commit()
              return jsonify(data1)
         
        except:
          cur=mysql.connection.cursor()
          cur.execute('select * from std_data ')
          ver=cur.fetchall()
          data={}
          data2=[]
          for i in ver:          
              data={
                  'std_id':i[0],
                  'std_name':i[1],
                  'std_phoneNo':i[2],
                  'std_address':i[3]
                }
              data2.append(data)
          mysql.connection.commit()
          return jsonify(data2)
        else:
          return jsonify({"message": "ERROR: Unauthorized"}), 401


    if request.method=="PUT":
      jdata=json.loads(request.data)
      cur=mysql.connection.cursor()
      cur.execute('UPDATE std_data SET std_name=%s,std_phoneNo=%s,std_address=%s WHERE std_id=%s',[jdata['std_name'],jdata['std_phoneNo'],jdata['std_address'],jdata['std_id']])
      mysql.connection.commit()
      return 'data is updated'

    if request.method=="DELETE":
      jdata=json.loads(request.data)
      cur=mysql.connection.cursor()
      cur.execute('DELETE from std_data WHERE std_id=%s',[jdata['std_id']])
      mysql.connection.commit()
      return 'data is deleted'
      


  

        