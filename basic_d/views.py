from django.shortcuts import render
from django.urls import reverse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import shutil
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect
#from scipy.misc import imread
import matplotlib.cbook as cbook
from django.http import HttpResponse

# Create your views here.


def index(request):
    entries = Entry.objects.all()
    return render(request,'index.html',{'entries':entries})

def FinCard(request):
    return render(request,'finland.html')

def Financial(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board/d_d/static/finance"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/finance")
        os.makedirs("/home/nitesh/Desktop/dash_board/d_d/static/finance")
        ds=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/rch_flexiable.csv")
        width = .35 # width of a bar
        m1_t = pd.DataFrame({
        'Allocation' : ds.iloc[:,1],
        'Relese' :ds.iloc[:,2],
        'Utilization' :ds.iloc[:,3],
        'bad_rate' : ds.iloc[:,1]})

        m1_t[['Allocation','Relese','Utilization']].plot(kind='bar', width = width)
        m1_t['bad_rate'].plot(secondary_y=True)

        ax = plt.gca()
        plt.xlim([-width, len(m1_t['Utilization'])-width])
        plt.xlabel("Year")
        plt.title("RCH Flexible Pool comparison (2010---2013)")
        ax.set_xticklabels(('2010-11', '2011-12', '2012-13'))
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/finance/finance.png",dpi=100,figsize = (5,5))
        #plt.show()
    return render(request,'financial.html')

def Financial_indicator_2(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind2"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind2")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind2")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[0]
        fig1, ax = plt.subplots(figsize=(9,10))
        #set background color
        #fig1.patch.set_facecolor('#33ccff')
        #datafile = cbook.get_sample_data('1.jpeg')
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 15
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:RCH Flexible Pool")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind2/Finance1.png', dpi=100)
    return render(request,'fin_ind2.html')

def Financial_indicator_3(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind3"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind3")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind3")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[1]
        fig1, ax = plt.subplots(figsize=(9,10))
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 15
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:Mission Flexible Pool")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind3/Finance2.png', dpi=100)
    return render(request,'fin_ind3.html')

def Financial_indicator_4(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind4"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind4")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind4")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[2]
        fig1, ax = plt.subplots(figsize=(9,10))
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 16
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:Routine Immunization")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        #fig1.savefig('Finance3.png', dpi=100)
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind4/Finance3.png', dpi=100)
    return render(request,'fin_ind4.html')

def Financial_indicator_5(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind5"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind5")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind5")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[3]
        fig1, ax = plt.subplots(figsize=(9,10))
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 16
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:Pulse Polio Immunisation")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        #fig1.savefig('Finance4.png', dpi=100)
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind5/Finance4.png', dpi=100)
    return render(request,'fin_ind5.html')

def Financial_indicator_6(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind6"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind6")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind6")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[4]
        fig1, ax = plt.subplots(figsize=(9,10))
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 15
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:National I.D.D. Control Programme")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        #fig1.savefig('Finance5.png', dpi=100)
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind6/Finance5.png', dpi=100)
    return render(request,'fin_ind6.html')

def Financial_indicator_7(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind7"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind7")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind7")
        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/pia1.csv",index_col="programme")
        print(piadf)
        y=list(piadf)

        x=piadf.iloc[5]
        fig1, ax = plt.subplots(figsize=(9,10))
        img = imread("/home/nitesh/Desktop/dash_board_final/d_d/static/image/1.jpeg")
        plt.imshow(img,zorder=0,  extent=[-7.0, 7.0, -7.0, 7.0])
        plt.rcParams['font.size'] = 14
        plt.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=0.75*3.14,colors=["#BC8F8F","#848484","#E3CF57"],radius=5)
        ax.axis('equal')
        ax.set_title("Programme Name:Infrastructure Maintenance")
        fig1=plt.gcf()
        plt.show()
        plt.draw()
        #fig1.savefig('Finance6.png', dpi=100)
        fig1.savefig('/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind7/Finance6.png', dpi=100)
    return render(request,'fin_ind7.html')

def department(request):
    return render(request,'department.html')


def KeyCard(request):
    return render(request,'kpiland.html')

def Keyperformance(request):

    if os.path.exists("/home/nitesh/Desktop/dash_board/d_d/static/graphs"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/graphs")
        os.makedirs("/home/nitesh/Desktop/dash_board/d_d/static/graphs")

        df = pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17.csv",index_col=['city'])

        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="Total _number_of_pregnant_women_Registered_for_ANC" )
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk1.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,2])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="Number of Pregnant women registered within first trimester")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk2.png",dpi=100,figsize = (5,5))

        s = pd.Series(df.ix[:,3])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="% 1st Trimester registration to Total ANC Registrations")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk3.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title='Number of pregnant women received 4 or more ANC check ups')
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk4.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="TT2 given to Pregnant women (numbers)")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk5.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="TT Booster given to Pregnant women (numbers)")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk6.png",dpi=100,figsize = (5,5))

        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="% Pregnant Woman received 4 ANC check ups to Total ANC Registrations")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk7.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="% Pregnant women received TT2+ TT Booster to Total ANC Registration")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk8.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="Number of Pregnant women given 180 IFA tablets")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk9.png",dpi=100,figsize = (5,5))


        s = pd.Series(df.ix[:,1])
        plt.figure(figsize=(20,10))
        s.plot(kind="bar",title="% Pregnant women given 180 IFA to Total ANC Registration")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/graphs/jk10.png",dpi=100,figsize = (5,5))


    if os.path.exists("/home/nitesh/Desktop/dash_board/d_d/static/family_health"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/family_health")
        os.makedirs("/home/nitesh/Desktop/dash_board/d_d/static/family_health")

        df2=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk18_new.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17_new.csv")

        fig, ax = plt.subplots()
        x =df2.iloc[:,0]
        y=df2.iloc[:,80]
        # multiple line pl
        plt.scatter(x, y,alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Male Sterlisation (Vasectomies) to Total sterilisation")
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/family_health/family_health1.png")

        x=df2.iloc[:,0]
        y=df2.iloc[:,81]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Female Serlisation (Tubectomies) to Total sterilisation")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/family_health/family_health2.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,88]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Sterilisation (Tubectomies & Vasectomies) conducted at Private Inst.")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/family_health/family_health3.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,89]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Sterilisation (Tubectomies & Vasectomies) conducted at Public Inst.")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/family_health/family_health4.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,90]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Laparoscopic sterlisations to Total Female Sterilisations")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/family_health/family_health5.png")

    if os.path.exists("/home/nitesh/Desktop/dash_board/d_d/static/child_health"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/child_health")
        os.makedirs("/home/nitesh/Desktop/dash_board/d_d/static/child_health")

        df2=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk18_new.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17_new.csv")


        # create data
        x = df2.iloc[:,0]
        y=df2.iloc[:,125]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y,alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Newborns given OPV0 at birth to Reported live birth")
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child1.png")

        x = df2.iloc[:,0]
        y=df2.iloc[:,126]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Newborns given BCG to Reported live birth")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child2.png")

        x = df2.iloc[:,0]
        y=df2.iloc[:,127]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Newborns given Hep-B0(Birth Dose)at birth to Reported live birth")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child3.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,136]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Infants 0 to 11 months old who received Measles+ MR vaccine to reported live births")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child4.png")


        x = df2.iloc[:,0]
        y=df2.iloc[:,138]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Drop Out between BCG & Measles/ MR")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child5.png")

        x = df2.iloc[:,0]
        y=df2.iloc[:,139]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Children given Vitamin A Dose 9 to Children given Vit A dose1")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child6.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,140]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Children given Vitamin A Dose 9 to Children given Vit A dose1")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child7.png")
    return render(request,'keyperf.html')
   # for maternal health ///////////////////////////////////////////////////
'''

    df2=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk18_new.csv")
    df1=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17_new.csv")

    x =df2.iloc[:,0]
    y=df2.iloc[:,3]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% 1st Trimester registration to Total ANC Registrations")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat1.png")

    x = df2.iloc[:,0]
    y=df2.iloc[:,12]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Pregnant women having severe anaemia (Hb<7) treated at institution to women having hb level<7")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat2.png")

    x = df2.iloc[:,0]
    y=df2.iloc[:,7]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Pregnant Woman received 4 ANC check ups to Total ANC Registrations")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat3.png")

    x =df2.iloc[:,0]
    y=df2.iloc[:,8]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Pregnant women received TT2+ TT Booster to Total ANC Registration")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat4.png")



    x =df2.iloc[:,0]
    y=df2.iloc[:,10]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Pregnant women given 180 IFA to Total ANC Registration")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat5.png")



    x = df2.iloc[:,0]
    y=df2.iloc[:,13]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Pregnant women having severe anaemia treated as hb level<7")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat6.png")



    x = df2.iloc[:,0]
    y=df2.iloc[:,14]
    # multiple line plot
    fig, ax = plt.subplots()
    plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=12)
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% New cases of Pregnant Women detected at inst. for hyper. to Total ANC Regis.")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/maternal_health/mat7.png")

    #for child health //////////////////////////////////////////////////////////

    df2=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk18_new.csv")
    df1=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17_new.csv")

    fig, ax = plt.subplots()
    # create data
    x = df2.iloc[:,0]
    y=df2.iloc[:,125]

    # multiple line pl
    plt.scatter(x, y,alpha=1,marker="o",s=200,c="orange")
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Newborns given OPV0 at birth to Reported live birth")
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child1.png")

    x = df2.iloc[:,0]
    y=df2.iloc[:,126]
    fig, ax = plt.subplots()
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Newborns given BCG to Reported live birth")
    plt.xticks(rotation=90)
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child2.png")

    x = df2.iloc[:,0]
    y=df2.iloc[:,127]
    fig, ax = plt.subplots()
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Newborns given Hep-B0(Birth Dose)at birth to Reported live birth")
    plt.xticks(rotation=90)
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child3.png")

    x =df2.iloc[:,0]
    y=df2.iloc[:,136]
    fig, ax = plt.subplots()
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Infants 0 to 11 months old who received Measles+ MR vaccine to reported live births")
    plt.xticks(rotation=90)
    fig.tight_layout()
    plt.grid()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child4.png")


    x = df2.iloc[:,0]
    y=df2.iloc[:,138]
    fig, ax = plt.subplots()
    # multiple line pl
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Drop Out between BCG & Measles/ MR")
    fig.tight_layout()
    plt.grid()
    fig.tight_layout()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child5.png")

    x = df2.iloc[:,0]
    y=df2.iloc[:,139]
    fig, ax = plt.subplots()
    # multiple line pl
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Children given Vitamin A Dose 9 to Children given Vit A dose1")
    fig.tight_layout()
    plt.grid()
    fig.tight_layout()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child6.png")

    x =df2.iloc[:,0]
    y=df2.iloc[:,140]
    fig, ax = plt.subplots()
    # multiple line pl
    plt.scatter(x, y, alpha=1,marker="o",s=200,c="orange")
    plt.xticks(rotation=90)
    ax.set_ylabel('Scores')
    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title("% Children given Vitamin A Dose 9 to Children given Vit A dose1")
    fig.tight_layout()
    plt.grid()
    fig.tight_layout()
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/child_health/child7.png")
'''
    #family ///////////////////////////////////////////////////////////////////

def Mat_Health(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health"):
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health")
        df=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk18join.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk17.csv")

        x = df.iloc[:,0]
        y=df.iloc[:, 3]
        # multiple line plot
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Maternal Health: % 1st Trimester registration # ANC Registrations",fontsize=25)
        plt.xticks(x)
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health1.png")

        x = df.iloc[:,0]
        y=df.iloc[:, 12]
        # multiple line plot
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(30,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:Pregnant women having severe anaemia (Hb<7) treated as level<7")
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health2.png")

        x = df.iloc[:,0]
        y=df.iloc[:, 7]
        # multiple line plot
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:  % Pregnant Woman received 4 ANC check ups to Total ANC Registrations")
        fig.tight_layout()
        plt.grid()
        plt.show()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health3.png")


        x = df.iloc[:,0]
        y=df.iloc[:, 8]
        # multiple line plot
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:  % Pregnant women received TT2+ TT Booster to Total ANC Registration")
        fig.tight_layout()
        plt.grid()
        plt.show()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health4.png")


        x = df.iloc[:,0]
        y=df.iloc[:, 10]
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:  % Pregnant women given 180 IFA to Total ANC Registration")
        fig.tight_layout()
        plt.grid()
        plt.show()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health5.png")

        x = df.iloc[:,0]
        y=df.iloc[:, 13]
        # multiple line plot
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:  % Pregnant women having severe anaemia treated as hb level<7")
        fig.tight_layout()
        plt.grid()
        plt.show()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health6.png")

        x = df.iloc[:,0]
        y=df.iloc[:, 14]
        plt.rc('font', size=25)
        fig,ax = plt.subplots(figsize=(20,10))
        plt.plot(x, y, marker='o',markerfacecolor = 'red',markersize=15,linewidth=7.0,c="#6A5ACD")
        plt.xticks(rotation=90)
        #plt.plot.bgcolor="#B7B7B7"
        ax.set_facecolor('#CAE1FF')
        fig.set_facecolor('#F0E68C')
        ax.set_ylabel('Scores',fontsize=25)
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        plt.xticks(x)
        ax.set_title("Maternal Health:  % New cases of Pregnant Women detected at inst. for hyper. to Total ANC Regis.")
        fig.tight_layout()
        plt.grid()
        plt.show()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/mat_health/Mat_health7.png")

    return render(request,'key_ind2.html')
'''
def Family_Health(request):

    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health")

        df2=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk18_new.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk17_new.csv")

        fig, ax = plt.subplots()
        x =df2.iloc[:,0]
        y=df2.iloc[:,80]
        # multiple line pl
        plt.scatter(x, y,alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Male Sterlisation (Vasectomies) to Total sterilisation")
        #fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health/family_health1.png")

        x=df2.iloc[:,0]
        y=df2.iloc[:,81]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Female Serlisation (Tubectomies) to Total sterilisation")
        plt.xticks(rotation=90)
        #fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health/family_health2.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,88]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Sterilisation (Tubectomies & Vasectomies) conducted at Private Inst.")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health/family_health3.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,89]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Sterilisation (Tubectomies & Vasectomies) conducted at Public Inst.")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health/family_health4.png")

        x =df2.iloc[:,0]
        y=df2.iloc[:,90]
        fig, ax = plt.subplots()
        # multiple line pl
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Laparoscopic sterlisations to Total Female Sterilisations")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health/family_health5.png")
        return render(request,'family_health_indicator.html')
'''
def Child_Health_Ind(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health"):
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health")

        df=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk18join.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk17.csv")

        x = df.iloc[:,0]
        y=df.iloc[:, 125]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Newborns given OPV0 at birth to Reported live birth")
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child1.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 126]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Newborns given BCG to Reported live birth")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child2.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 127]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Newborns given Hep-B0(Birth Dose)at birth to Reported live birth")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child3.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 136]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Infants 0 to 11 months old who received Measles+ MR vaccine to reported live births")
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child4.png")

        x = df.iloc[:,0]
        y=df.iloc[:, 138]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Drop Out between BCG & Measles/ MR")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child5.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 139]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health: % Children given Vitamin A Dose 9 to Children given Vit A dose1")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child6.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 140]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 23
        plt.scatter(x, y,alpha=1,marker='o',s=800,c="#E0FFFF")
        plt.xticks(rotation=90)
        ax.set_facecolor('#5B5B5B')
        fig.set_facecolor('#FFEC8B')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("Child Health:% Children given Vitamin A Dose 9 to Children given Vit A dose1")
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/chil_health/child7.png")
        #plt.show()
    return render(request,'key_ind4.html')


def Family_Health_Ind(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health"):
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health")
        df=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk18join.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk17.csv")

        x = df.iloc[:,0]
        y=df.iloc[:, 89]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 25
        plt.scatter(x, y,alpha=1,marker=r'$\clubsuit$',s=800,c="#006400")
        plt.xticks(rotation=90)
        ax.set_facecolor('#FFB90F')
        fig.set_facecolor('#00F5FF')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Family Planning: % Male Sterlisation (Vasectomies) to Total sterilisation",fontsize=25)
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health/Family1.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 81]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 25
        plt.scatter(x, y,alpha=1,marker=r'$\clubsuit$',s=800,c="#006400")
        plt.xticks(rotation=90)
        ax.set_facecolor('#FFB90F')
        fig.set_facecolor('#00F5FF')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Family Planning: % Female Serlisation (Tubectomies) to Total sterilisation",fontsize=25)
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health/Family2.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 88]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 25
        plt.scatter(x, y,alpha=1,marker=r'$\clubsuit$',s=800,c="#006400")
        plt.xticks(rotation=90)
        ax.set_facecolor('#FFB90F')
        fig.set_facecolor('#00F5FF')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Family Planning: % Sterilisation (Tubectomies & Vasectomies) conducted at Private Inst.",fontsize=25)
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health/Family3.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 89]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 25
        plt.scatter(x, y,alpha=1,marker=r'$\clubsuit$',s=800,c="#006400")
        plt.xticks(rotation=90)
        ax.set_facecolor('#FFB90F')
        fig.set_facecolor('#00F5FF')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Family Planning: % Sterilisation (Tubectomies & Vasectomies) conducted at Public Inst.",fontsize=25)
        plt.xticks(rotation=90)
        fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health/Family4.png")
        #plt.show()

        x = df.iloc[:,0]
        y=df.iloc[:, 90]
        z= df.iloc[:, 1]
        fig, ax = plt.subplots(figsize=(20,10))
        plt.rcParams['font.size'] = 25
        plt.scatter(x, y,alpha=1,marker=r'$\clubsuit$',s=800,c="#006400")
        plt.xticks(rotation=90)
        ax.set_facecolor('#FFB90F')
        fig.set_facecolor('#00F5FF')
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name',fontsize=25)
        ax.set_title("Family Planning:% Laparoscopic sterlisations to Total Female Sterilisations",fontsize=25)
        fig.tight_layout()
        plt.grid()
        fig.tight_layout()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fam_health/Family5.png")
    return render(request,'key_ind3.html')
        #plt.show()


    #pichart //////////////////////////////////////////////////////////////////
'''
def Pichart(request):

    if os.path.exists("/home/nitesh/Desktop/dash_board/d_d/static/pichart"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/pichart")
        os.makedirs("/home/nitesh/Desktop/dash_board/d_d/static/pichart")

        piadf=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/pia.csv",index_col="programme")
        #print(piadf)
        y=list(piadf)
        x=piadf.iloc[0]
        fig1, ax = plt.subplots()
        ax.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("RCH Flexible Pool")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial1")

        x=piadf.iloc[1]
        fig1, ax = plt.subplots()
        ax.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("Mission Flexible Pool")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial2")


        x=piadf.iloc[2]
        fig1, ax = plt.subplots()
        ax.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("Routine Immunization")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial3")

        x=piadf.iloc[3]
        fig1, ax = plt.subplots()
        colors = ['#ff7f0e','C0','C2']
        ax.pie(x, labels=y, autopct='%1.1f%%',colors=colors,shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("Pulse Polio Immunisation")
        ax.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial4")
        #plt.show()

        x=piadf.iloc[4]
        fig1, ax = plt.subplots()
        ax.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("National I.D.D. Control Programme")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial5")


        x=piadf.iloc[5]
        fig1, ax = plt.subplots()
        ax.pie(x, labels=y, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')
        ax.set_title("Infrastructure Maintenance")
        plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/pichart/Financial6")

        return render(request,'pichart_indicator.html')

'''

def Analysis(request):
    df=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk18.csv")
    df1=pd.read_csv("/home/nitesh/Desktop/dash_board/d_d/static/jk17.csv")
    df1.columns = df1.columns.str.strip()
    print(df1.columns)



    y=df1.iloc[:, 1]
    x = df.iloc[:,0]
    z= df.iloc[:, 1]
    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)
    width = 0.30
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')

    ax.set_ylabel('Scores')
    plt.xticks(rotation=90)

    ax.set_xlabel('Jammu Kashmir -District Name')
    ax.set_title('Total _number_of_pregnant_women_Registered_for_ANC')

    plt.tight_layout()

    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk12.png",dpi = 350)


    x = df.iloc[:,0]
    y=df1.iloc[:, 2]
    z= df.iloc[:, 2]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Number of Pregnant women registered within first trimester')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk13.png",dpi = 350)


    x = df.iloc[:,0]
    y=df1.iloc[:, 3]
    z= df.iloc[:, 3]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('% 1st Trimester registration to Total ANC Registrations')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk14.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 4]
    z= df.iloc[:, 4]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Number of pregnant women received 4 or more ANC check ups')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk15.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 5]
    z= df.iloc[:, 5]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('TT2 given to Pregnant women (numbers)')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk16.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 6]
    z= df.iloc[:, 6]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('TT Booster given to Pregnant women (numbers)')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk17.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 7]
    z= df.iloc[:, 7]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Pregnant Woman received 4 ANC check ups to Total ANC Registrations"')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk18.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 8]
    z= df.iloc[:, 8]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Number of Pregnant women registered within first trimester')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk19.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 9]
    z= df.iloc[:, 9]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('% Pregnant women received TT2+ TT Booster to Total ANC Registration')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk20.png",dpi = 350)



    x = df.iloc[:,0]
    y=df1.iloc[:, 10]
    z= df.iloc[:, 10]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Number of Pregnant women given 180 IFA tablets')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk21.png",dpi = 350)


    x = df.iloc[:,0]
    y=df1.iloc[:, 10]
    z= df.iloc[:, 10]
    p1 = ax.bar(x, y, width, color="red")
    p2 = ax.bar(x, z, width, color='blue')
    ax.set_title('Number of Pregnant women given 180 IFA tablets')
    plt.savefig("/home/nitesh/Desktop/dash_board/d_d/static/3d/jk21.png",dpi = 350)
    return render(request,'analysis.html')



def Health_Portal(request):
    return render(request,'health_portal.html')


def Program(request):
    return render(request,'progr_scheme.html')

def district(request):
    return render(request,'district_report.html')

def Report_Year(request):
    return render(request,'report.html')

def State_Report(request):
    return render(request,'state_report.html')

def Help_Cont(request):
    return render(request,'help_cont.html')

def Calendar(request):
    entries = Entry.objects.all()
    return render(request,'calendar_index.html',{'entries':entries})

def Calendar_Details(request,pk):
    entry = Entry.objects.get(id=pk)
    return render(request,'calendar_detail.html',{'entry':entry})

def Calendar_Add(request):
    entries = Entry.objects.all()
    if request.method == 'POST':

        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description,
            ).save()

            return render(request,'calendar_index.html',{'entries':entries})


    else:
        form = EntryForm()

    return render(request,'calendar_form.html',{'form': form})


def Chat_Report(request):
    return render(request,'chat.html')

def Sterilisation(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/family_health"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/sterilisation")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/sterilisation")

        df2=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk18_new.csv")
        df1=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/jk17_new.csv")

        fig, ax = plt.subplots()
        x =df2.iloc[:,0]
        y=df2.iloc[:,80]
        # multiple line pl
        plt.scatter(x, y,alpha=1,marker="o",s=200,c="orange")
        plt.xticks(rotation=90)
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Male Sterilisation (Vasectomies) to Total sterilisation")
        #fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/sterilisation/family_health1.png")

        x=df2.iloc[:,0]
        y=df2.iloc[:,81]
        fig, ax = plt.subplots()
        plt.scatter(x, y, alpha=1,marker=r'$\clubsuit$',s=200,c="red")
        ax.set_ylabel('Scores')
        ax.set_xlabel('Jammu Kashmir -District Name')
        ax.set_title("% Female Sterilisation (Tubectomies) to Total sterilisation")
        plt.xticks(rotation=90)
        #fig.tight_layout()
        plt.grid()
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/sterilisation/family_health2.png")
    return render(request,'key_ind1.html')

def Financial_indicator_1(request):
    if os.path.exists("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind1"):
        #os.rmdir("/home/nitesh/Desktop/dash_board/d_d/static/my")
        #shutil.rmtree("/home/nitesh/Desktop/dash_board/d_d/static/my", ignore_errors=False, onerror=None)
        shutil.rmtree("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind1")
        os.makedirs("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind1")
        ds=pd.read_csv("/home/nitesh/Desktop/dash_board_final/d_d/static/rch_flexiable.csv")
        width = .35 # width of a bar
        m1_t = pd.DataFrame({
        'Allocation' : ds.iloc[:,1],
        'Release' :ds.iloc[:,2],
        'Utilization' :ds.iloc[:,3],
        'bad_rate' : ds.iloc[:,1]})

        m1_t[['Allocation','Release','Utilization']].plot(kind='bar', width = width)
        m1_t['bad_rate'].plot(secondary_y=True)

        ax = plt.gca()
        plt.xlim([-width, len(m1_t['Utilization'])-width])
        plt.xlabel("Year")
        plt.title("RCH Flexible Pool comparison (2010---2013)")
        ax.set_xticklabels(('2010-11', '2011-12', '2012-13'))
        plt.savefig("/home/nitesh/Desktop/dash_board_final/d_d/static/fin_ind1/finance.png",dpi=100,figsize = (5,5))
        #plt.show()
    return render(request,'fin_ind1.html')

def Login(request):
    return render(request,"login.html")
def chart(request):
    return render(request,"chart.html")

def Role(request):
    if request.POST:
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']


        if (role =="Secretary - Health"):
            message = request.POST['role']
            return render(request,"finland.html")
        elif(role =="NHM - Director"):
            message = request.POST['role']
            return render(request,"kpiland.html")
        elif(role =="Program - Manager"):
            message = request.POST['role']
            return render(request,"index.html")
        else:
            message = 'You submitted an empty form.'
