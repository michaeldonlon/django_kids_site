# customuser/views.py

from django.shortcuts import render
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, mail_admins
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView



from .forms import CustomUserCreateForm, LoginForm
from .token import account_activation_token



class MyLoginView(LoginView):


    form_class = LoginForm
    template_name = 'registration/login.html'



class UserCreateView(CreateView):


    model = get_user_model()
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def usersignup(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            token = PasswordResetTokenGenerator()
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user=user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            admin_message = f'{user.first_name} {user.last_name} has requested access to kidsite. Please login to the admin dashboard to grant access.'
            mail_admins('kidsite access request', admin_message)
            return render(request, 'registration/please_confirm.html')
    else:
        form = CustomUserCreateForm()

    return render(request, 'registration/signup.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'registration/confirmation.html')
    else:
        return HttpResponse('Activation link invalid.')