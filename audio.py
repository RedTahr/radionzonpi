import pyglet
song = pyglet.media.load('Rabbit.mp3')
# avbin.dll can't open remote file :-(
#song = pyglet.media.load('http://on-demand.radionz.co.nz/natmusic/natmusic-20140405-1405-under_the_influence_nirvana-128.mp3')
song.play()
pyglet.app.run()