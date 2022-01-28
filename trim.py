#東京湾のみ　トリミング
import sys
from PIL import Image

import os
from glob import glob

import shutil

def trim(left,top,right,bottom):
    #最新のファイルのフルパスを取得
    def image_name(dirname):
        target = os.path.join(dirname, '*')
        files = [(f, os.path.getmtime(f)) for f in glob(target)]
        latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
        return latest_modified_file_path[0]
    if __name__ == '__main__':
        dirname = "C:/Users/student/Documents/sotuken/auto_save_trim/image"
        full_path=image_name(dirname)

    #フルパスからファイル名だけ取得
    im_name=os.path.basename(full_path)


    im = Image.open('{}'.format(full_path))
    #トリミングする座標の指定
    im_crop = im.crop((left,top,right,bottom))
    im_crop.save("C:/Users/student/Documents/sotuken/auto_save_trim/trimming/"+im_name,quality=95)

    #フォルダの中身ごと削除
    # shutil.rmtree('C:/Users/student/Documents/sotuken/auto_save_trim/image')

    # #フォルダの作り直し
    # os.mkdir('C:/Users/student/Documents/sotuken/auto_save_trim/image')


# trim(496, 208, 646, 358)

def path_cut():
    #最新のファイルのフルパスを取得
    def image_name(dirname):
        target = os.path.join(dirname, '*')
        files = [(f, os.path.getmtime(f)) for f in glob(target)]
        latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
        return latest_modified_file_path[0]
    if __name__ == '__main__':
        #最新のファイル場所
        dirname = "C:/Users/student/Documents/sotuken/auto_save_trim/image"
        full_path=image_name(dirname)

    #フルパスからファイル名だけ取得
    im_name=os.path.basename(full_path)
    im_name_cut=im_name.replace('-23_59_Sentinel-2_L2A_Highlight_Optimized_Natural_Color', '')
    # im_name_cut=im_name.rstrip(49)
    return im_name_cut
    #2020-07-02-00_00_2020-07-02-23_59_Sentinel-2_L2A_True_color

print(path_cut())