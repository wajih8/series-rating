#v1.0
from pickle import load,dump
from numpy import array
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
def confirmer():
    if len(ff.let.text())!=8:
        QMessageBox.warning(ff,"erreur","le numero doit etre de 8 chiffres")
    elif ff.brf.isChecked()==False and ff.brh.isChecked()==False:
        QMessageBox.warning(ff,"erreur","choisir un genre")
    else:
        f=open("avis.dat","ab")
        l=ff.tw.rowCount()
        ff.tw.setRowCount(l+1)
        ff.tw.setItem(l,0,QTableWidgetItem(ff.let.text()))
        if ff.brf.isChecked() :
            ff.tw.setItem(l,1,QTableWidgetItem(ff.brf.text()))
        else:
            ff.tw.setItem(l,1,QTableWidgetItem(ff.brh.text()))
        ff.tw.setItem(l,2,QTableWidgetItem(ff.cb.currentText()))
        e=dict()
        e["tel"]=ff.let.text()
        if ff.brf.isChecked() :
            e["egn"]=ff.brf.text()
        else:
            e["egn"]=ff.brh.text()
        e["feu"]=ff.cb.currentText()
        dump(e,f)
        f.close()
def pourc(c,t,ch,n):
    if c=="h":
        s=0
        for i in range(n):
            if t[i]["egn"]=="Homme" and t[i]["feu"]==ch:
                s=s+1
        return (s*100)/n
    else:
        s=0
        for i in range(n):
            if t[i]["egn"]=="Femme" and t[i]["feu"]==ch:
                s=s+1
        return (s*100)/n

#calculer_le_nombre_de
def cal():
    f=open("avis.dat","rb")
    i=0
    te=True
    while te:
        try:
            x=load(f)
            i=i+1
        except:
            te=False
    f.close()
    return(i)
def remp():
    pass
#show_statistique

def stat():
    try:
        f=open("avis.dat","rb")
    except:
        return 0
    n=cal()
    t=array(n*[dict()])
    eof=False
    i=0
    while eof==False:
        try:
            t[i]=dict()
            t[i]=load(f)
            i+=1
        except:
            eof=True
    f.close()
    t1=remp()
    t1=["FALLUJAH","JEBAL LAHMER","SINDRELLA","SABEK EL KHIR"]
    for i in range(4):
        a="le feuilleton "+t1[i]+" suivi par "+str(pourc("h",t,t1[i],n))[:4]+"% homme "+str(pourc("f",t,t1[i],n))[:4]+"% femme"
        b="le feuilleton "+t1[i]+" suivi par "+str(int(n*((pourc("h",t,t1[i],n)+pourc("f",t,t1[i],n))/100)))+" telespectateur"
        print(a,"\n",b)
        ff.ls.addItem(str(a))
        ff.ls.addItem(str(b))
app=QApplication([])
ff=loadUi("mousalset.ui")
ff.show()
ff.bc.clicked.connect(confirmer)
ff.bs.clicked.connect(stat)
app.exec_()