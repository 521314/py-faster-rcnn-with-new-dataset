### TRAIN FASTER-RCNN ON A NEW DATASET

To train this faster rcnn model on a new dataset, follow the instructions below. 

#### Step 1: Download Faster-RCNN:

(1) git clone --recursive https://github.com/rbgirshick/py-faster-rcnn.git

(2) cd into $Faster-RCNN-Root/lib and "make"

(3) cd into $Faster-RCNN-Root/caffe-fast-rcnn and "cp Makefile.config.example Makefile.config"

(4) change "Makefile.config" : first, uncomment "WITH_PYTHON_LAYER := 1" then uncomment "USE_CUDNN := 1" if you'd like to use GPU (recommended), I assume you've already installed GPU, CUDA, cuDNN. 

(5) "$make -j8"

(6) "$make pycaffe"


#### Step 2: Download models and run a demo

(1) "$cd .."

(2) "$./data/scripts/fetch_faster_rcnn_models.sh"

(3) run demo.py "python ./tools/demo.py --gpu 0 --net vgg16"

Make sure you've successfully finished all parts mentioned above without error message. Then you can proceed.

#### Step 3: Train your own model. 

My strategy is to prepare the data as the same format as the pascal_voc data. After you have prepare the data. 

(1) Download the pascal voc data in a directory $data: "$cd $data";

(2) Then download them: 

wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar

wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar

wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCdevkit_08-Jun-2007.tar

tar xvf VOCtrainval_06-Nov-2007.tar

tar xvf VOCtest_06-Nov-2007.tar

tar xvf VOCdevkit_08-Jun-2007.tar

Then you should linke this dataset with py-faster-rcnn: 

cd $Faster-RCNN-Root/data

ln -s $VOCdevkit $YOUR/DATA/DIRECTORY/VOCdevkit

(3) Prepare your own dataset: this is the most important step, and you should modify multiple files in side $Faster-RCNN-Root/lib



