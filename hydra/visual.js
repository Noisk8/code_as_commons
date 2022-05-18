//PARTE 1
s0.initVideo('https://media.giphy.com/media/9NNaCoXYcRtSTOIMgc/giphy.mp4') // initialize a webcam in source buffer s0

src(s0)
.rotate(.1,.1)
  .luma(() => a.fft[1]*.4)
  .scale(() => a.fft[0]*2)
.mask(gradient(),1,() => a.fft[0]*2)
.mult(voronoi(() => a.fft[0]*2,2,1))
  .out(o0)
