#audio 1 

Clock.bpm=10 

a1 >> loop ('Agua',amp=8, bpm=120 )

p1 >> sitar (dur=40, rate=PWhite(40), pan=PWhite(-1,1), amplify=var.switch, amp=0, room=.8, formant=1)
#audio 2 

a2 >> loop("antena1", amp=8, bpm=120, dur=8)

#audio 3

a3 >> loop("bosque", amp=8, bpm=120)

a4 >> loop ("lago", dur=10, bpm=120)

a5 >> loop ("vaso1", dur=20, bpm=120, amp=2)

a6 >> loop ("vaso2", dur=20, bpm=120, amp=2 )


a1.stop()
a2.stop()
a3.stop()
a4.stop()
a5.stop()
a6.stop()

#audio 4

s1.stop()

#audio 5


#audio 6

#audio 7 


zp >> zap(
    -1,
    dur=0.15,
    oct=[5, [5, var([5, 5.25, 5.5, 6], [[64, 32], [32, 64], 32])], 5, var([5, 4.85, 4.5], 128)],
    pan=PWhite(-0.5, 0.5),
    bend=[0, expvar([0, 0, -0.15, -0.15], [64, 64, 64, 0]), 0, 0],
    room=P[1, 0.5, 0, 1] * expvar([0, 1], [128, 0]), mix=0.25,
    formant=[0.5, [0.5, 0.25, 0.75, 1, 0], [0.5, var([0, 0.5], 8), var([0, 0.5], [64, 32])], [[0.25, var([0.25, 0], 64)], 0.5]],
    lpf=[var([500, 250, 750, 1000], 128), var([850, 400, 900, 200], 16), var([1000, 10], [[128, 32], [64, 32]]), [250, 900],  [300, 1000], 400, var([500, 300, 100], 8), 600],
    lpr=expvar([0.75, 1], 64),
    drive=[var([0, 0.02], [[128, 64], 64]), var([0, 0.04], [[256, 128], [128, 64]]), 0.01, var([0, 0.025], 64)],
    sus=P[0.25, var([0.25, 1, 0.25, 2, 0.25, 0.25, 4], [64, 32]), 0.25, var([0.25, 1], 128)],
    amp=[1, var([0.25, 1], [64, 128]), 1, var([0.5, 1], [128, 256])]
) + (expvar([5, 4, 3, 2, 0, 0], 32), sinvar([0, -1, -2, -3], 64))



zp.stop()




var.switch = var([1,1],[32])


p3 >> glass(oct=7, rate=linvar([-2,2],16), shape=0.5, amp=2, amplify=var([1,var.switch],64), room=0.5)

p4 >> noise(dur=20, amp=.6)
#MAX .5

p3.stop()


p4.stop()
