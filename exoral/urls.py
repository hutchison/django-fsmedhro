from django.conf.urls import url
from . import views

app_name = 'exoral'
urlpatterns = [
    url(r'^$', views.moduswahl, name='moduswahl'),
    url(r'^(?P<modus>[lp])/$', views.testatwahl, name='testatwahl'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/$', views.prueferwahl, name='prueferwahl'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/$', views.fragenliste,
        name='fragenliste'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/kommentare$', views.kommentarliste,
        name='kommentarliste'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/protokolle$', views.protokollliste,
        name='protokollliste'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/Frageneingabe/$', views.frage_neu,
        name='frage_neu'),
    url(r'^frage_score/(?P<frage_id>[0-9]+)/$', views.frage_score, name='frage_score'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/Protokolleingabe/$', views.protokoll_neu,
        name='protokoll_neu'),
    url(r'^(?P<modus>[lp])/(?P<testat_id>[0-9]+)/(?P<pruefer_id>[0-9]+)/Kommentareingabe/$', views.kommentar_neu,
        name='kommentar_neu'),
]
