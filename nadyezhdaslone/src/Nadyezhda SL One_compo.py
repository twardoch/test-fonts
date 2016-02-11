for g in fl.font.glyphs: 
	w = 1233
	if g.mark == 1: 
		print g.name
		g.width = 2466
		g.components[0].delta = Point(1100*0.0+100, 0)
		g.components[1].delta = Point(1100*0.5+100, 0)
		g.components[2].delta = Point(1100*1.0+100, 0)
		g.components[3].delta = Point(1100*1.5+100, 0)
fl.UpdateFont(-1)
print "OK"
