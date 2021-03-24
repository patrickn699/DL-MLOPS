import os
import shutil

dir = 'E:\MlOPS-DeepLearning\Data Set'
dir = os.chdir(dir)
imgs = os.listdir(dir)
#print(imgs)
cnt = 0

def create_fold(imgs):
    os.mkdir('train')
    os.mkdir('test')
    for i in range(len(imgs)):
        
        os.makedirs(os.path.join('train','class_'+str(i)))
        os.makedirs(os.path.join('test','class_'+str(i)))

#create_fold(imgs)  


def train_test_split(imgs):

    

        

    for i in os.listdir(os.path.join(imgs,k)):

        print(i)

    for j in os.listdir(i):
        #print(j)
        '''
        
        if i.startswith('te') or i.startswith('tr'):
            pass
        else:
            pat = os.path.join(i,j)
            shutil.copy(pat,str(p)+'/train_'+str(p))
    
    #print("DONE!")
    '''


train_test_split(dir)