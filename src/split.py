import os
import numpy as np
import shutil
import random
import yaml
import argparse
from getdata import get_data



'''
dir = 'E:\MlOPS-DeepLearning\Data_Set'
imgs = os.listdir(dir)
root_dir = 'Data Set'
p = 'E:\MlOPS-DeepLearning\Data_Set' #\Bulbasaur'
classes_dir = ['Bulbasaur', 'Charmander','Squirtle']
per = len(os.listdir('Data Set/Bulbasaur'))
#print(per)
split_ratio = round((80/100)*per)

cld_dir = [i for i in os.listdir(dir)]
print(cld_dir)
'''

####################method for creating folder#####################

def create_fold(config,img = None):
    config = get_data(config)
    dirr = config['load_data']['preprocessed_data']
    cla = config['load_data']['num_classes']
    print(dirr)
    print(cla)

    if os.path.exists(dirr+'/'+'train'+'/'+'class_0') and os.path.exists(dirr+'/'+'test'+'/'+'class_0'):
        print('train and test folders already exist...')
        print('skipping it!')

    else:
        os.mkdir(dirr+'/'+'train')
        os.mkdir(dirr+'/'+'test')
        for i in range(cla):
            
            os.makedirs(os.path.join(dirr+'/'+'train','class_'+str(i)))
            os.makedirs(os.path.join(dirr+'/'+'test','class_'+str(i)))

#create_fold(imgs)  


###########method for splitting the images for train and test###########

def train_test_split(config):
    config =  get_data(config)
    root_dir = config['data_source']['data_src'] 
    dest = config['load_data']['preprocessed_data']
    p = config['load_data']['full_p']
    cla = config['data_source']['data_src']
    cla = os.listdir(cla)
    cla = [i for i in cla if not i.endswith('.dvc') and cla if not i.startswith('.git')]
    print(cla)
    splitr = config['train_split']['split_ratio']
    print(splitr)
    

    for k in range(len(cla)):
        print(cla[k])
        per = len(os.listdir((os.path.join(root_dir,cla[k]))))
        cnt = 0
        for j in os.listdir(os.path.join(root_dir,cla[k])):
            #per = len(os.path.join(root_dir,cla[k]))
            #print(per)
            pat = os.path.join(p+'/'+cla[k],j)
            split_ratio = round((splitr/100)*per)
            print(split_ratio)
            if cnt != split_ratio:
                #print(cnt)
                shutil.copy(pat,dest+'/'+'train/class_'+str(k))
                cnt = cnt+1

            else:
                shutil.copy(pat,dest+'/'+'test/class_'+str(k))

    print('done')



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = 'parameters.yaml')
    passed_args = args.parse_args()
    
    create_fold(config=passed_args.config)
    train_test_split(config = passed_args.config)

    

