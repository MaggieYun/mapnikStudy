#coding=utf-8
#以下逻辑用于从数据库中取出数据后存储为geojson格式的文本
# from sqlalchemy import create_engine
# import json

# def encodeAttr(val):
#     import datetime
#     from decimal import Decimal
#     if val is None:
#         return ""
#     elif isinstance(val,datetime.datetime):
#         return val.strftime("%Y-%m-%d %H:%M:%S")
#     elif isinstance(val,Decimal):
#         return float(str(val))
#     else:
#         return val 


# db = 'oracle://gis:gis@172.16.60.35:1521/yhte'
# sql = "SELECT TASK_POINT_LONGITUDE,TASK_POINT_LATITUDE from V_TASK_POINT"
# engine = create_engine(db)
# conn = engine.connect()
# results = conn.execute(sql)
# records = results.fetchall()#获取数据所有记录
# conn.close()
# # print records
# xys = map(lambda vals:map(encodeAttr,vals),records)
# MultiPoint = { "type": "MultiPoint",
#   "coordinates": xys
#   }
# f = file(r"G:\mapnik\geojson\data.geojson",'w+')
# f.write(str(MultiPoint))
# f.close()


from mapnik import Ogr,Layer
import mapnik
datasource = Ogr(base='G:/mapnik/geojson',file='data.geojson',layer='OGRGeoJSON') 

lyr = Layer('OGR Layer from GeoJSON file')
lyr.datasource = datasource

m = mapnik.Map(800, 800)

m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
point_symbolizer = mapnik.PointSymbolizer(mapnik.PathExpression("../point.png"))

# point_symbolizer = mapnik.PointSymbolizer("../point.png", "png", 16, 16) #为何这样用会报错？

point_symbolizer.allow_overlap = True
point_symbolizer.opacity = 0.8


r.symbols.append(point_symbolizer)
s.rules.append(r)
m.append_style('point_style',s)


lyr.styles.append('point_style')




m.layers.append(lyr)
m.zoom_all() 
mapnik.render_to_file(m,'geojson.png', 'png')