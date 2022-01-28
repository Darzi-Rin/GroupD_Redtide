from django.shortcuts import render
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from keras.models import load_model

from config.settings import MODEL_FILE_PATH
from config.settings import AI_IMG


def hantei(request):

    model = load_model(MODEL_FILE_PATH)

    categories = ["None", "True"]
    #image_pathは判定したい画像のパス
    #なし
    # img_path = ("{}/2020-01-06-00_00_2020-01-06-23_59_Sentinel-2_L2A_True_color.jpg".format(AI_IMG))
    #img_path = ("{}/2021-01-20-00_00_2021-01-20-23_59_Sentinel-2_L2A_True_colorA.jpg".format(AI_IMG))
    #あり
    img_path = ("{}/2021-07-22-00_00_2021-07-22-23_59_Sentinel-2_L2A_True_color.jpg".format(AI_IMG))
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
        return render (request,'basic/redtide_observe_ans.html',{'akasio':"赤潮はありません。"})

    elif features[0,1] == 1:
        return render (request,'basic/redtide_observe_ans.html',{'akasio':"赤潮が発生しています。"})
        # print("赤潮が発生しています。")

    else:
        return render (request,'basic/redtide_observe_ans.html',{'akasio':"わかりません。"})
        # print("わかりません。")