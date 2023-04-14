from youtube_client import YoutubeCliente
import os
from Manipulating_Thumbnail import generateClock, generateThumb, cropRoundBg


def run():
    os.system("node Manipulating_Thumbnail/generateSub.js")
    cropRoundBg.removeBackGround()
    generateClock.buildClock()
    generateThumb.buildThumbnail()
    
    yt = YoutubeCliente()

    video_id = 'dO0GfRWQTT4'
    final_imag = 'images/thumb/final_thumbnail.png'

    yt.set_thumbnail(video_id, final_imag)
    print('Thumbnail updated!')

run()