from django.shortcuts import render
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import os


def index(request):
    if request.method != 'POST':
        return render(request,'index.html')
    datalist=request.POST['file1']
        # path=os.getcwd()+'/sampleexcelfile/datalist[0:].xls'
    data = pd.read_excel(datalist[:])
    data_df  = data.drop(columns=['from'], axis=1).set_index('student')
    plt.figure(figsize=(10,4))
    # cbar_kws = {"orientation":"horizontal",         
    #    }
    # annot_kws={'fontsize':10,'fontstyle':'italic','color':"k",'alpha':0.9,'backgroundcolor':'w'}
    dataplot = sns.heatmap(data_df, cmap="coolwarm", annot=True ,robust = True ,linewidths=4,fmt='g',vmin = 0, vmax = 100)
    dataplot.set(title="Student Heatmap",
                 xlabel="Column",
                 ylabel=" Student Name",)
    sns.set(font_scale=2)
    scatter_fig = dataplot.get_figure()
    scatter_fig.savefig(os.getcwd()+"/readexcel_app/static/images/"+'scatterplot.png')
    # plt.show()
    # removing_files = glob.glob(os.getcwd()+'/readexcel_app/static/images/'+'scatterplot.png')
    # for i in removing_files:
    #     os.remove(removing_files)
    return render(request,'index.html',{'columns': data.columns,'rows': data.to_dict('records')})

    

