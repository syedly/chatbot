from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from app.forms import CustomUserCreationForm
from app.preferences import PREFERENCES
from app.models import Preferences

User = get_user_model()

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/preferences/'

class PreferencesView(View):
    template_name = 'preferences.html'

    def get(self, request):
        if request.user.is_authenticated:
            preferences_obj = Preferences.objects.filter(user=request.user).first()
            user_pref = preferences_obj.preferences if preferences_obj else None

            return render(request, self.template_name, {
                'preference_choices': PREFERENCES,
                'user_pref': user_pref
            })
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            selected_pref = request.POST.get('preferences')
            preferences_obj, created = Preferences.objects.get_or_create(user=request.user)
            preferences_obj.preferences = selected_pref
            preferences_obj.save()

            return redirect('preferences')
        else:
            return redirect('login')

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        identifier = request.POST['identifier'] 
        password = request.POST['password']
        user = authenticate(request, username=identifier, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})
        
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('index')
    
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return redirect('index')