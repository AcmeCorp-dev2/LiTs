import os

import numpy as np
import matplotlib.pyplot as plt

import nibabel as nib
from tifffile import imwrite, imread

DATA_ROOT = 'lits'

### loading images from folders ###

TRAIN_PATH = os.path.join(DATA_ROOT, 'train')
TEST_PATH = os.path.join(DATA_ROOT, 'test')

trainVNames = os.listdir(os.path.join(TRAIN_PATH, 'volume'))
testVNames = os.listdir(os.path.join(TEST_PATH, 'volume'))

print('No. of training volumes: ', len(trainVNames))
print('No. of testing volumes: ', len(testVNames))
print()

trainSNames = os.listdir(os.path.join(TRAIN_PATH, 'segmentation'))
testSNames = os.listdir(os.path.join(TEST_PATH, 'segmentation'))

try:
    assert(len(trainVNames)==len(trainSNames) and len(testVNames)==len(testSNames))
except AssertionError:
    print('The no. of patients and corresponding segmentations do not match!')
    print()

### extracting images from volumetric data and saving it as tiff file ###

def makedirs(path):
    '''
    Function to make necessary directories if not already present
    '''

    if(not os.path.isdir(path)):
        os.makedirs(path)

def npToTiff(array, pathName, train=True):
    '''
    Function to convert arrays extracted from image volume as images on disk

    Arguments:
    array: extracted array to be saved as image
    pathName: name of the image on disk
    train: if the extracted images belongs to training set or testing set
    '''
    # npToTiff(npdata[i], volPath.split('\\')[3][:-4]+'-'+str(i), train)
    
    makedirs('preprocessed\\train\\images')
    makedirs('preprocessed\\train\\masks')

    makedirs('preprocessed\\test\\images')
    makedirs('preprocessed\\test\\masks')

    print()
    print("This is the pathName inside npToTiff:",pathName)

    if train:
        if ('volume' in pathName):
            path = os.path.join('preprocessed\\train\\images',pathName)
            print("This is the path",path)
            imwrite(path+'.tif', array)
        else:
            imwrite(os.path.join('preprocessed\\train\\masks',pathName)+'.tif', array)
    else:
        if ('volume' in pathName):
            imwrite(os.path.join('preprocessed\\test\\images',pathName)+'.tif', array)
        else:
            imwrite(os.path.join('preprocessed\\test\\masks',pathName)+'.tif', array)

def imgFromVol(volPath, train=True):
    '''
    Function to read an image\\segmentation volume and write it as images on disk

    Arguments:
    vol_path: path to the CT scan volume
    train: if the extracted volume belongs to training set or testing set
    '''

    imgVol = nib.load(volPath)

    npdata = imgVol.get_fdata()
    npdata = npdata.transpose(2,1,0)
    # splits=volPath.split('\\')[-1]
    # split1 = splits.split('.')[0]
    # print("Volume path splits:\n",split1,"\n")
    # print("\n",npdata.shape[0],"\n")
    
    
    for i in range(npdata.shape[0]):
        splits = volPath.split("\\")[-1]
        # print("This is splits",splits)
        split1 = splits.split('.')[0]
        split2 = split1.split('-')[0]
        # print("This is split2: ",split2)
        # print("This is path being sent to nptotiff",split2+"-"+str(i))
        npToTiff(npdata[i], split2+"-"+str(i), train)

    return npdata.shape[0]


totalImages = 0

if(not os.path.isdir('preprocessed')):
    print('Extracting images from volume, on disk.')
    print()

    makedirs('preprocessed\\train')

    for i in range(len(trainVNames)):
        noImages = imgFromVol(os.path.join(os.path.join(TRAIN_PATH, 'volume'), 'volume-'+str(i)+'.nii'))
       
        #lits\\train\\volume\\volume-1.nii
        noMasks = imgFromVol(os.path.join(os.path.join(TRAIN_PATH, 'segmentation'), 'segmentation-'+str(i)+'.nii'))

        try:
            assert(noImages==noMasks)
        except AssertionError:
            print('[!] The no. of images and masks do not match!')
            print()

        print('Loaded {} images from volume-{}'.format(noImages, i))

        totalImages += noImages

    makedirs('preprocessed\\test')

    for i in range(len(testVNames)):
        noImages = imgFromVol(os.path.join(os.path.join(TEST_PATH, 'volume'), 'volume-'+str(10+i)+'.nii'), train=False)
        noMasks = imgFromVol(os.path.join(os.path.join(TEST_PATH, 'segmentation'), 'segmentation-'+str(10+i)+'.nii'), train=False)

        try:
            assert(noImages==noMasks)
        except AssertionError:
            print('[!] The no. of images and masks do not match!')
            print()

        print('Loaded {} images from volume-{}'.format(noImages, 110+i))

        totalImages += noImages

    print('Wrote {} images on disk.'.format(totalImages))

else:
    print('Extracted images already present on the disk.')