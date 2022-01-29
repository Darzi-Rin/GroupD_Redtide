from asyncio.windows_events import NULL
from datetime import date
from glob import glob
from pickle import FALSE
from re import A
from tkinter import image_names
from django.shortcuts import render
from django.template import context
from django.views import View
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from keras.models import load_model

import glob

from config.settings import MODEL_FILE_PATH
from config.settings import AI_IMG

# def hantei(self, request, *args, **kwargs): 
    #     context={
    #         'date':request.POST['date'],
    #         'area':request.POST['area'],
    #         'akasio':akasio,
    #     }


def hantei(request):

    model = load_model(MODEL_FILE_PATH)

    
    date=request.POST['date']
    area=request.POST['area']

    if date== '':
        #日付が選択されなかった時
        return render (request,'basic/redtide_observe_ans.html',{'akasio':"日付を選択してください。"})
    else:
        #formで受け取ったareaとdateでファイル名検索
        search_img=glob.glob('{}/{}/{}.jpg'.format(AI_IMG,area,date))
        if search_img == []:
            #画像がなかった場合
            return render (request,'basic/redtide_observe_ans.html',{'akasio':"画像がありません。"})
        else:
            #リストから抽出
            img_name=search_img[0]


    categories = ["None", "True"]
    
    img_path = img_name

    img = image.load_img(img_path, target_size=(60, 60, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    features = model.predict(x)

    for i in range(0,2):
        if features[0,i] == 1:
            cat = categories[i]
    message = "それは" + cat
    print(message)
    if features[0,0] == 1:
        akasio='赤潮はありません。'
        # return render (request,'basic/redtide_observe_ans.html',{'akasio':"赤潮はありません。"})

    elif features[0,1] == 1:
        akasio='赤潮が発生しています。'
        # return render (request,'basic/redtide_observe_ans.html',{'akasio':"赤潮が発生しています。"})
        # print("赤潮が発生しています。")

    else:
        akasio='わかりません。'
        # return render (request,'basic/redtide_observe_ans.html',{'akasio':"わかりません。"})
        # print("わかりません。")


    return render (request,'basic/redtide_observe_ans.html',{'akasio':akasio})
