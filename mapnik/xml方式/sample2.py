#coding = utf-8
import mapnik
stylesheet = 'sample2.xml'
image = 'world_style.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all() 
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image