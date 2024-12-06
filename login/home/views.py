from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib import messages 

@never_cache
def loginn(request):
    if request.session.get('is_logged_in'):  
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check for hardcoded credentials
        if username == 'jerin' and password == 'login':
            request.session['is_logged_in'] = True  # Set session variable
            return redirect('home')  # Redirect to home page
        else:
            #Error message on the login page
            messages.error(request, 'Entered Username or Password is wrong!!!')
            return redirect('login')  # Redirect back to login

    # Render login page for GET requests
    return render(request, 'login.html')

@never_cache
def home(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')  # Redirect to login if not authenticated
    return render(request, 'home.html')  # Render the home page for authenticated users

def signout(request):
    request.session.flush()  # Clear all session data
    return redirect('login')  # Redirect to login after signing out
