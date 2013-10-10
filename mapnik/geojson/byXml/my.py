#coding = utf-8
import mapnik
stylesheet = 'my.xml'
image = 'fromxml.png'
m = mapnik.Map(600, 600)
mapnik.load_map(m, stylesheet)
m.zoom_all() 
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image