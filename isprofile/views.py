import mimetypes
import os

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    current_user = request.user
    context = {
        'firstname': current_user.first_name,
        'lastname': current_user.last_name,
        'email': current_user.email,
    }

    return render(request, 'index.html', context=context)

@permission_required('isprofile.can_see_db')
def dbinfo(request):
    current_user = request.user
    context = {
        'dbname': current_user.employee.dbname,
        'flag': current_user.employee.flag,
    }

    return render(request, 'dbinfo.html', context=context)


def docs(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/isprofile/static/docs/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'docs.html')