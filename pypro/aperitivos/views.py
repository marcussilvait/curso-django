from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 406390835},
        'console-interativo': {'titulo': 'Console Interativo', 'vimeo_id': 406805399},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
