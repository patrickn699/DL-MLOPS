import os
import numpy as np
import shutil
import random
import yaml

dir = 'E:\MlOPS-DeepLearning\Data Set'
imgs = os.listdir(dir)
root_dir = 'Data Set'
p = 'E:\MlOPS-DeepLearning\Data Set' #\Bulbasaur'
classes_dir = ['Bulbasaur', 'Charmander','Squirtle']
per = len(os.listdir('Data Set/Bulbasaur'))
#print(per)
split_ratio = round((80/100)*per)

cld_dir = [i for i in os.listdir(dir)]
print(cld_dir)


def create_fold(imgs):
    os.mkdir('train')
    os.mkdir('test')
    for i in range(len(imgs)):
        
        os.makedirs(os.path.join('train','class_'+str(i)))
        os.makedirs(os.path.join('test','class_'+str(i)))

#create_fold(imgs)  





for k in range(len(classes_dir)):
    print(classes_dir[k])
    cnt = 0
    for j in os.listdir(os.path.join(root_dir,classes_dir[k])):
        pat = os.path.join(p+'/'+classes_dir[k],j)
        if cnt != split_ratio:
            #print(cnt)
            shutil.copy(pat,'train/class_'+str(k))
            cnt = cnt+1

        else:
            shutil.copy(pat,'test/class_'+str(k))

print('done')
