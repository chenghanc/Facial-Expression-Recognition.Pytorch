import os

for i in range(10):
    #cmd = 'python mainpro_CK+.py --model VGG19 --bs 32 --lr 0.01 --fold %d' %(i+1)
    #cmd = 'python mainpro_CK+.py --model VGG19 --bs 64 --lr 0.01 --fold %d' %(i+1)
    #cmd = 'python mainpro_CK+.py --model Resnet18 --bs 64 --lr 0.01 --fold %d' %(i+1)
    #cmd = 'python mainpro_CK+.py --model Resnet34 --bs 64 --lr 0.01 --fold %d' %(i+1)
    cmd = 'python mainpro_CK+.py --model Resnet50 --bs 64 --lr 0.01 --fold %d' %(i+1)
    os.system(cmd)
print("Train VGG19 ok!")

