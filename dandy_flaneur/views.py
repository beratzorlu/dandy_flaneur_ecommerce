from django.shortcuts import render


def handler_500(request):
    """
    Error Handler for 500 Page Not Found Error
    """
    return render(request, "errors/500.html", status=500)


def handler_404(request, exception):
    """
    Error Handler for 404 Page Not Found Error
    """
    return render(request, "errors/404.html", status=404)


def handler_403(request):
    """
    Error Handler for 403 Page Not Found Error
    """
    return render(request, "errors/403.html", status=403)
