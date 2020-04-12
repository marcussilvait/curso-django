from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 406390835},
    {'slug': 'console-interativo', 'titulo': 'Console Interativo', 'vimeo_id': 406805399},
]
# Dict Comprehensions
videos_dct = {
    dct['slug']: dct for dct in videos
}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
