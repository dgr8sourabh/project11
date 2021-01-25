from django.shortcuts import render


def homepage(request):
    return render(request,'app11/index.html')


def hindiMovies(request):
    return render(request, 'app11/hindimovie.html')


def englishMovies(request):
    return render(request,'app11/englishmovie.html')


def southMovies(request):
    return render(request, 'app11/southmovie.html')


def trailor(request):
    id = request.GET.get('id')
    print(id)
    if id == '10':
        data = {'link':"https://www.youtube.com/embed/MJyKN-8UncM"}
        return render(request, 'app11/trailor.html', data)

