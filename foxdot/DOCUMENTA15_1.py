
Clock.bpm=130


vf >> pulse(amp=1, dur=1, oct=5, delay=.2, room=2, mix=2)


b1 >> bass(dur=1/4, formant=PRand(5)[:8], rate=PRand(2,10)[:8], pan=PWhite(-1,1), amp=1.3)


b2 >> sawbass(var([0,5,2,[3,6]],[3,3,1,1]), dur=PDur(8,8), amp=0).spread()

ko >> play ("|x4| ", amp=1)


ji >> play (" |~3|", dur=1/2, amp=0)

lk >> play (" |o4|", dur=2/2, amp=0)

bm >> play ("[--]", amp=1, sample=0)

vf.stop()


b1.stop()

b2.stop()

ko.stop()
bm.stop()
ji.stop()

b1 >> dbass(dur=PDur(3,8), sus=2, chop=0, shape=PWhite(0,1/2),amp=1, pan=PWhite(-1,1)).sometimes("offadd", 4) + var([0,2],4)
c1 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5)
p1 >> space([7,6,4,P*(2,1),0], dur=8, pan=(-1,1), amp=0, chop=4, oct=4.9)
p2 >> pads([0,2,4,6], dur=4, spin=4, oct=4,amp=2.0, chop=[8,16], hpf=linvar([500,2000],16), hpr=0.2).every(8, "shuffle")



c2.stop()

b1.stop()


var.switch = var([1,1],[32])

ko >> play ("|x4| ", amp=.7)

ji >> play (" |~3|", dur=1/2, amp=0)

lk >> play (" |o4|", dur=2/2, amp=.6)

bm >> play ("[--]", amp=0, sample=3)

Scale.default="minor"; Clock.bpm=126; Root.default=var([0,3],32)

b1 >> dirt([0,0,0.5], dur=PDur(3,8), sus=1, amp=.9, chop=2, drive=0.5, formant=1, oct=(5), room=0.2).spread()


p3 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=2, amplify=var([0,var.switch],64), room=0.5)

p1 >> pasha(var([0,2,0.5],[3,1/2,1/2]), dur=PDur(5,8), amp=1, oct=7, sus=2, pan=PWhite(-1,1)).every(4, "dur.shuffle")





ko.stop()


love =[0,6,0,6,3,]

ju >> play ("|X2| ", amp=.6)

hu >> dirt (love,dur=PDur(5,8), root=var([0,.5]),vib=0, amp=1)

il >> play (" |=1|", amp=2, chop=0)



jp >> play (" |o3|",  room=.2, mix=.4, dur=2/2, amp=1 )

kn >> play ("[::]", amp=1,  sample=1, dur=[.5,.5,.5])

hs >> dbass ( amp=1, dur=PDur(7,8).stutter(3),root=var([2,1]), formant=0)



gc >> pads (amp=.6,dur=PDur(1,32), oct=4, root=var([0,1]), shape=1)

hf >> play (" e ", dur=PDur(7,8), sample=PRand(1), amp=3.5)
np >> play (" *[**]*", amp=0, sample=3)

hz >> play ("tt",   sample=0, amp=0)
jm >> play (" |n2|", amp=3)

hz.stop()


ju >> play ("|X2| ", amp=1)

var.fuck = var ([0,4,3,5], 8)


Clock.bpm


yt >> sawbass (amp=1, dur=PDur(3,8).stutter(3),root=var([0,.5]), oct=6, formant=linvar([1,2]))


ly >> sitar  (oct=8, dur=PDur(3,8), vib=1,root=var([0,.1]))

jp >> play (" |o3|",  room=.1, mix=.1, dur=2/2, amp=1.5 )


gv >> sinepad (amp=2, oct=var([4,5]), dur=PDur(5,8), silde=var([1,0]))


h1 >> creep (var.fuck + (0,4,7), dur=8, mix =.6, chop =32, amp=1 )

rr >> play ("|Z0| ", dur=PDur(3,8), amp=1, chop=0,
    root=var([0,9]),shape=var([.1,.1],4))




no >> play ("|V2| ", mix=.1, room=0, amp=.7)


kk >>  play (" |n2|", amp=0)

jp >> play (" |=1|", amp=1, chop=0, dur=1/2)

nh >> play (" [::]", amp=1)

nl >> play (" |o2|", dur=8/2, amp=1.2, mix=0, room=0)

nm >> play ("treeeee", dur=PDur(6,8), amp=3)


dd >> feel (dur=PDur(8,8), chop=1, shape=.6,
    oct=(5,3),amp=1.5, lpf=0 )


Clock.bpm=128

#En Varios momentos
g2 >> arpy (amp=linvar([1,2]), oct=6, dur=PDur(7,8),
    sus=var([10,50]),
     chop=0, hpf=var([22, 4000]))




vf >> play (" |o3|", dur=8/2, amp=0, mix=.5, room=0)

be >> sawbass ( dur=PDur(5,8), root=var([0,1]), amp=0)



k8 >>  play("|X3| ", amp=1.5)
c1 >> play (" |o2|", dur=2/2, amp=.8)

b8 >> play ("[--]", amp=2)

var.switch= var ([1,1], [32])

vy >> dirt(dur=PDur(5,8), amp=1.2)

v1 >> sitar (dur=1/4, rate =PWhite(40), pan=PWhite(-1,1), amplifity=var.switch, amp=0, room=8, formant=0, oct=5 )

v2 >> glass (oct=6, rate=linvar([-2,2],16), shape=0.5, amp=5, ammplifity=var([1, var.switch],64), room=0.5)

v3 >> play ("e", amp=var([3, 5], [PRand(9,16)/2,16]), dur=PRand([1/2,1/4]), pan=var([-1,1],2))

r5 >> orient (oct=3, dur=P[1/2,1/2,1/2,2/2,2/2,1/2,], amp=1.7, vib=2, root=0)
