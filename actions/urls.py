from django.conf.urls import include, url, patterns

urlpatterns = patterns('actions.views',
                       # Home page with card number form
                       url('^$', 'login_page', name='login_page'),
                       # Selection operation balance/withdrawal
                       url('^operations/$', 'operations', name='operations'),
                       # Balance
                       url('^balance/$', 'balance', name='balance'),
                       # Withdrawal money
                       url('^withdrawal/$', 'withdrawal',
                           name='withdrawal'),
                       # Logout
                       url('^exit/$', 'exit', name='exit'),

                       )

