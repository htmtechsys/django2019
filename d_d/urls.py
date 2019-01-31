"""d_d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basic_d import views

app_name ='basic_d'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
    path('keyperformance',views.Keyperformance,name='keyperformance'),  # indicator 2 & KPI Link
    path('financial',views.Financial,name='financial'),
    path('analysis',views.Analysis,name='analysis'),
    path('key_indicators/',views.KeyCard,name='Keycards'),
    path('finance_indicators/',views.FinCard,name='fincards'),
    path('RCH_3_year_comparison/',views.Financial_indicator_1,name='fincards1'),
    path('RCH_flixible_pool/',views.Financial_indicator_2,name='fincards2'),
    path('Mission_flixible_pool/',views.Financial_indicator_3,name='fincards3'),
    path('Routine_Immunisation/',views.Financial_indicator_4,name='fincards4'),
    path('Pulsepolio_Immunisation/',views.Financial_indicator_5,name='fincards5'),
    path('IDD_control_program/',views.Financial_indicator_6,name='fincards6'),
    path('Infrastructure_maintanance/',views.Financial_indicator_7,name='fincards7'),
    #path('portfolio/',views.Portfolio,name='portfolio'),
    path('programme/',views.Program,name='program'),
    path('department/',views.department,name='department'),
    path('district/',views.district,name='district'),
    path('year_report/',views.Report_Year,name='report'),
    path('state_report/',views.State_Report,name='state_report'),
    path('help/',views.Help_Cont,name='help'),
    #path('indicator_1/',views.Family_Health,name='indicator_1'),   #indicator 1 not used
    #path('indicator_9/',views.Pichart,name='indicator_9'),   #indicator 3 not used
    path('calendar/',views.Calendar,name='calendar'),
    path('add/',views.Calendar_Add,name='add'),
    path('entry/<int:pk>',views.Calendar_Details,name='details'),
    path('chatapp/',views.Chat_Report,name='chat'),
    path('health_portal/',views.Health_Portal,name='health_portal'),
    path('mat_ind_2/',views.Mat_Health,name='mat_ind_2'),
    path('family_indicators/',views.Family_Health_Ind,name='health_ind_3'),
    path('child_indicators/',views.Child_Health_Ind,name='child_ind_3'),
    path('sterilisation/',views.Sterilisation,name='key_ind1'),
    path('',views.Login,name='login'),
    path('index/',views.Role,name='role'),
    path('chart/',views.chart,name='chart'),

]
