render(o0)



//@ferdoropeza
s0.initImage('/home/noisk8/FONDO2.png') // initialize a webcam in source buffer s0


src(o0)
voronoi(7,1,.5)
.hue(0.4)
.modulate(s0,0.8)
.scale(1)
.luma([0.15,0.25])

.out()
