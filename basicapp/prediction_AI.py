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
from keras.preprocessing import image
import numpy as np
from keras.models import load_model

import glob
import os
#import pandas as pd
#from config.settings import BASE_DIR

#from config.settings import BASE_DIR
from config.settings import MODEL_PATH
from config.settings import AI_IMG
from config.settings import TOKYO_IMG

# def hantei(self, request, *args, **kwargs): 
    #     context={
    #         'date':request.POST['date'],
    #         'area':request.POST['area'],
    #         'akasio':akasio,
    #     }


def yosoku(request):

    model = load_model(MODEL_PATH, compile=False)

    
    #date=request.POST['date']
    area=request.POST['area']

    #if date== '':
        #日付が選択されなかった時
    #    return render (request,'basic/redtide_prediction_ans.html',{'yosoku':"日付を選択してください。"})
    #else:
        #formで受け取ったareaとdateでファイル名検索
    
    # for f in glob.glob('{}/{}/*.png'.format(AI_IMG,area)):
    #     imgs_date = os.path.splitext(os.path.basename(f))[0]
    # df = pd.imgs_date
    # latest_date = imgs_date.sort_values("datatime").tail(1)

    # list_of_files = glob.glob('{}/{}/*'.format(AI_IMG,area))
    # latest_date = max(list_of_files, key=os.path.getctime)

    

    search_img=glob.glob('{}/{}/{}.png'.format(AI_IMG,area,latest_date))
    search_img2=glob.glob('{}/{}/{}.png'.format(TOKYO_IMG,area,latest_date))
    if search_img == []:
        #画像がなかった場合
        return render (request,'basic/redtide_prediction_result.html',{'yosoku':"画像がありません。"})
    else:
        #リストから抽出
        img_name=search_img[0]

        imgs1=search_img2[0]
        imgs_change=imgs1[41:]


    categories = ["None", "True"]
    
    img_path = img_name

    img = image.load_img(img_path, target_size=(60, 60, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    features = model.predict(x)

    # for i in range(0,2):
    #     if features[0,i] == 1:
    #         cat = categories[i]
    # message = "それは" + cat
    # print(message)
    if features[0,0] == 1:
        yosoku='赤潮は発生しません。'
        # return render (request,'basic/redtide_prediction_result.html',{'akasio':"赤潮はありません。"})
        # print("赤潮が発生しています。")

    elif features[0,1] == 1:
        yosoku='赤潮が発生します。'
        # return render (request,'basic/redtide_prediction_result.html',{'akasio':"赤潮が発生しています。"})
        # print("赤潮が発生しています。")

    else:
        yosoku='わかりません。'
        # return render (request,'basic/redtide_prediction_result.html',{'akasio':"わかりません。"})
        # print("わかりません。")

    all = {
        'yosoku': yosoku,
        'imgs1': imgs_change,
    }

    return render (request,'basic/redtide_prediction_ans.html',all)

# def image(img):

#     date=img.POST['date']
#     area=img.POST['area']

#     if date== '':
#             #日付が選択されなかった時
#             return render (img,'basic/redtide_observe_ans.html',{'imgs':""})
#     else:
#         #formで受け取ったareaとdateでファイル名検索
#         search_img=glob.glob('{}/{}/{}.png'.format(TOKYO_IMG,area,date))
#         if search_img == []:
#             #画像がなかった場合
#             return render (img,'basic/redtide_observe_ans.html',{'imgs':""})
#         else:
#             #リストから抽出
#             imgs=search_img[0]
#             imgs_change=imgs[39:]
#             return render (img,'basic/redtide_observe_ans.html',{'imgs':imgs_change} )