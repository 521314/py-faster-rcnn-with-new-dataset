### TRAIN FASTER-RCNN ON A NEW DATASET

To train this faster rcnn model on a new dataset, follow the instructions below. 

#### Step 1: Download Faster-RCNN:

    git clone --recursive https://github.com/rbgirshick/py-faster-rcnn.git
    cd $Faster-RCNN-Root/lib 
    make
    cd $Faster-RCNN-Root/caffe-fast-rcnn
    cp Makefile.config.example Makefile.config
Note: you may need to update your caffe through:

    cd caffe-fast-rcnn
    git remote add caffe https://github.com/BVLC/caffe.git
    git fetch caffe
    git merge -X theirs caffe/master

Then change "Makefile.config" : first, uncomment "WITH_PYTHON_LAYER := 1" then uncomment "USE_CUDNN := 1" if you'd like to use GPU (recommended), I assume you've already installed GPU, CUDA, cuDNN. You may also need to add hdf5 path to your Libraries directory.

    make -j8 && make pycaffe

#### Step 2: Download models and run a demo

    cd ..
    ./data/scripts/fetch_faster_rcnn_models.sh
    ./data/scripts/fetch_imagenet_models.sh

run demo.py "python ./tools/demo.py --gpu 0 --net vgg16"

Make sure you've successfully finished all parts mentioned above without error message. Then you can proceed.

#### Step 3: Prepare to train your model. 

My strategy is to prepare the data as the same format as the pascal_voc data. First, download pascal_voc data: 

	wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar

	wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar

	wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCdevkit_08-Jun-2007.tar

	tar xvf VOCtrainval_06-Nov-2007.tar

	tar xvf VOCtest_06-Nov-2007.tar

	tar xvf VOCdevkit_08-Jun-2007.tar

Then you should linke this dataset with py-faster-rcnn: 

	cd $Faster-RCNN-Root/data

	ln -s $YOUR/DATA/DIRECTORY/VOCdevkit VOCdevkit2007

#### Step 4: Prepare your own dataset

This is the most important step, and you should modify multiple files inside $Faster-RCNN-Root/lib.

(1) Transform your data into the format of VOC2007. The pascal voc 2007 dataset are composed of three folders: ImageSets, JPEGImages, Annotations. You should build your own dataset like this. The annotations file should be ".xml" format. Create the dataset using the script "tools/create_xml.py". Then you divide your dataset into trainval, val, train, test part. Then you delete the original "VOC2007" folder inside the "VOCdevkit" folder with the new dataset folder you just created. 

(2) change the file "$Faster-RCNN-Root/lib/datasets/pascal_voc.py" line 30 "self._classes" to the actuall classes of your datasets

Since you are using a different dataset, the number of classes might be different and the format of your picture might also be different from ".jpg", so you may also need to change "self._image_ext = '.jpg'" accordingly. 

(3) comment "$Faster-RCNN-Root/lib/datasets/imdb.py" line 111 "assert ..." and add these codes below:

    for iii in range(boxes.shape[0]):
	    if boxes[iii, 0] > boxes[iii, 2]:
    	          boxes[iii, 0] = 0

(4) File "$Faster-RCNN-Root/lib/rpn/proposal_target_layer.py" line 124 should be "cls = int(clss[ind])" and line 166 should be "...size=int(fg_rois_per_this_image),..." and line 184 should be "labels[int(fg_rois_per_this_image):] = 0"
and line 177 should be " ... size=int(bg_rois_per_this_image), ...". 

(5) change the number of classes in your "models/pascal_voc/faster_rcnn_end2end" prototxt file. The original 21 and 84 should be replaced with new numbers
(6) In lib/fast_rcnn/train.py import google.protobuf.text_format 

#### Step 5: Train your model!
	cd $Faster-RCNN-Root
	./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 pascal_voc
