from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom
import xml.etree.cElementTree as ET

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# CLASSES = ('__background__', 'person', 'rider', 'car',
#            'truck', 'bus', 'motorcycle', 'bicycle', 
#                         'caravan', 'trailer', 'fence', 'guard rail',
#                         'tunnel', 'traffic sign', 'traffic light')
# CLASSES = ('__background__')

class object_cls:
	def __init__(self, classId, bbox, truncated):
		self.classId = classId
		self.bbox = bbox
        	self.truncated = truncated

def create_xml(filename, outname, im_size, CLASSES, objects=None, folder='VOC2007', database = 'The VOC2007 Database', annotation = 'PASCAL VOC2007'):
    """Create the xml file"""
    top = Element('annotation')
    child_folder = SubElement(top, 'folder')
    child_folder.text = folder
    
    child_filename = SubElement(top, 'filename')
    child_filename.text = filename
    
    
    child_source = SubElement(top, 'source')
    child_source_database = SubElement(child_source, 'database')
    child_source_database.text = database
    
    child_source_annotation = SubElement(child_source, 'annotation')
    child_source_annotation.text = annotation
    child_source_image = SubElement(child_source, 'image')
    child_source_image.text = 'flickr'
    child_source_flickrid = SubElement(child_source, 'flickrid')
    child_source_flickrid.text = '341912865'

    child_owner = SubElement(top, 'owner')
    child_owner_flickrid = SubElement(child_owner, 'flickrid')
    child_owner_flickrid.text = 'Fried Camels'
    child_owner_name = SubElement(child_owner, 'name')
    child_owner_name.text = 'Jinky the Fruit Bat'

    child_size = SubElement(top, 'size')
    child_size_width = SubElement(child_size, 'width')
    child_size_width.text = str(im_size[0])
    child_size_height = SubElement(child_size, 'height')
    child_size_height.text = str(im_size[1])
    child_size_depth = SubElement(child_size, 'depth')
    child_size_depth.text = str(im_size[2])

    child_segmented = SubElement(top, 'segmented')
    child_segmented.text = '0'
    
    for i in range(len(objects)):
	if i == 0:
		# print 'add one object'
		child_object0 = SubElement(top, 'object')
    		child_object0_name = SubElement(child_object0, 'name')
    		child_object0_name.text = CLASSES[objects[i].classId]
 		child_object0_pose = SubElement(child_object0, 'pose')
		child_object0_pose.text = 'Left'
		child_object0_truncated = SubElement(child_object0, 'truncated')
		child_object0_truncated.text = str(objects[i].truncated)
		child_object0_difficult = SubElement(child_object0, 'difficult')
		child_object0_difficult.text = '0'

		child_object0_bndbox = SubElement(child_object0, 'bndbox')
		child_object0_bndbox_xmin = SubElement(child_object0_bndbox, 'xmin')
		child_object0_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object0_bndbox_ymin = SubElement(child_object0_bndbox, 'ymin')
		child_object0_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object0_bndbox_xmax = SubElement(child_object0_bndbox, 'xmax')
		child_object0_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object0_bndbox_ymax = SubElement(child_object0_bndbox, 'ymax')
		child_object0_bndbox_ymax.text = str(objects[i].bbox[3])

	elif i == 1:
		# print 'add one object'
		child_object1 = SubElement(top, 'object')
    		child_object1_name = SubElement(child_object1, 'name')
    		child_object1_name.text = CLASSES[objects[i].classId]
 		child_object1_pose = SubElement(child_object1, 'pose')
		child_object1_pose.text = 'Left'
		child_object1_truncated = SubElement(child_object1, 'truncated')
		child_object1_truncated.text = str(objects[i].truncated)
		child_object1_difficult = SubElement(child_object1, 'difficult')
		child_object1_difficult.text = '0'

		child_object1_bndbox = SubElement(child_object1, 'bndbox')
		child_object1_bndbox_xmin = SubElement(child_object1_bndbox, 'xmin')
		child_object1_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object1_bndbox_ymin = SubElement(child_object1_bndbox, 'ymin')
		child_object1_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object1_bndbox_xmax = SubElement(child_object1_bndbox, 'xmax')
		child_object1_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object1_bndbox_ymax = SubElement(child_object1_bndbox, 'ymax')
		child_object1_bndbox_ymax.text = str(objects[i].bbox[3])
	
	elif i == 2:
		# print 'add one object'
		child_object2 = SubElement(top, 'object')
    		child_object2_name = SubElement(child_object2, 'name')
    		child_object2_name.text = CLASSES[objects[i].classId]
 		child_object2_pose = SubElement(child_object2, 'pose')
		child_object2_pose.text = 'Left'
		child_object2_truncated = SubElement(child_object2, 'truncated')
		child_object2_truncated.text = str(objects[i].truncated)
		child_object2_difficult = SubElement(child_object2, 'difficult')
		child_object2_difficult.text = '0'

		child_object2_bndbox = SubElement(child_object2, 'bndbox')
		child_object2_bndbox_xmin = SubElement(child_object2_bndbox, 'xmin')
		child_object2_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object2_bndbox_ymin = SubElement(child_object2_bndbox, 'ymin')
		child_object2_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object2_bndbox_xmax = SubElement(child_object2_bndbox, 'xmax')
		child_object2_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object2_bndbox_ymax = SubElement(child_object2_bndbox, 'ymax')
		child_object2_bndbox_ymax.text = str(objects[i].bbox[3])
	elif i == 3:
		# print 'add one object'
		child_object3 = SubElement(top, 'object')
    		child_object3_name = SubElement(child_object3, 'name')
    		child_object3_name.text = CLASSES[objects[i].classId]
 		child_object3_pose = SubElement(child_object3, 'pose')
		child_object3_pose.text = 'Left'
		child_object3_truncated = SubElement(child_object3, 'truncated')
		child_object3_truncated.text = str(objects[i].truncated)
		child_object3_difficult = SubElement(child_object3, 'difficult')
		child_object3_difficult.text = '0'

		child_object3_bndbox = SubElement(child_object3, 'bndbox')
		child_object3_bndbox_xmin = SubElement(child_object3_bndbox, 'xmin')
		child_object3_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object3_bndbox_ymin = SubElement(child_object3_bndbox, 'ymin')
		child_object3_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object3_bndbox_xmax = SubElement(child_object3_bndbox, 'xmax')
		child_object3_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object3_bndbox_ymax = SubElement(child_object3_bndbox, 'ymax')
		child_object3_bndbox_ymax.text = str(objects[i].bbox[3])	
	elif i == 4:
		# print 'add one object'
		child_object4 = SubElement(top, 'object')
    		child_object4_name = SubElement(child_object4, 'name')
    		child_object4_name.text = CLASSES[objects[i].classId]
 		child_object4_pose = SubElement(child_object4, 'pose')
		child_object4_pose.text = 'Left'
		child_object4_truncated = SubElement(child_object4, 'truncated')
		child_object4_truncated.text = str(objects[i].truncated)
		child_object4_difficult = SubElement(child_object4, 'difficult')
		child_object4_difficult.text = '0'

		child_object4_bndbox = SubElement(child_object4, 'bndbox')
		child_object4_bndbox_xmin = SubElement(child_object4_bndbox, 'xmin')
		child_object4_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object4_bndbox_ymin = SubElement(child_object4_bndbox, 'ymin')
		child_object4_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object4_bndbox_xmax = SubElement(child_object4_bndbox, 'xmax')
		child_object4_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object4_bndbox_ymax = SubElement(child_object4_bndbox, 'ymax')
		child_object4_bndbox_ymax.text = str(objects[i].bbox[3])	
	elif i == 5:
		# print 'add one object'
		child_object5 = SubElement(top, 'object')
    		child_object5_name = SubElement(child_object5, 'name')
    		child_object5_name.text = CLASSES[objects[i].classId]
 		child_object5_pose = SubElement(child_object5, 'pose')
		child_object5_pose.text = 'Left'
		child_object5_truncated = SubElement(child_object5, 'truncated')
		child_object5_truncated.text = str(objects[i].truncated)
		child_object5_difficult = SubElement(child_object5, 'difficult')
		child_object5_difficult.text = '0'

		child_object5_bndbox = SubElement(child_object5, 'bndbox')
		child_object5_bndbox_xmin = SubElement(child_object5_bndbox, 'xmin')
		child_object5_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object5_bndbox_ymin = SubElement(child_object5_bndbox, 'ymin')
		child_object5_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object5_bndbox_xmax = SubElement(child_object5_bndbox, 'xmax')
		child_object5_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object5_bndbox_ymax = SubElement(child_object5_bndbox, 'ymax')
		child_object5_bndbox_ymax.text = str(objects[i].bbox[3])	
	elif i == 6:
		# print 'add one object'
		child_object6 = SubElement(top, 'object')
    		child_object6_name = SubElement(child_object6, 'name')
    		child_object6_name.text = CLASSES[objects[i].classId]
 		child_object6_pose = SubElement(child_object6, 'pose')
		child_object6_pose.text = 'Left'
		child_object6_truncated = SubElement(child_object6, 'truncated')
		child_object6_truncated.text = str(objects[i].truncated)
		child_object6_difficult = SubElement(child_object6, 'difficult')
		child_object6_difficult.text = '0'

		child_object6_bndbox = SubElement(child_object6, 'bndbox')
		child_object6_bndbox_xmin = SubElement(child_object6_bndbox, 'xmin')
		child_object6_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object6_bndbox_ymin = SubElement(child_object6_bndbox, 'ymin')
		child_object6_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object6_bndbox_xmax = SubElement(child_object6_bndbox, 'xmax')
		child_object6_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object6_bndbox_ymax = SubElement(child_object6_bndbox, 'ymax')
		child_object6_bndbox_ymax.text = str(objects[i].bbox[3])

	elif i == 7:
		# print 'add one object'
		child_object7 = SubElement(top, 'object')
    		child_object7_name = SubElement(child_object7, 'name')
    		child_object7_name.text = CLASSES[objects[i].classId]
 		child_object7_pose = SubElement(child_object7, 'pose')
		child_object7_pose.text = 'Left'
		child_object7_truncated = SubElement(child_object7, 'truncated')
		child_object7_truncated.text = str(objects[i].truncated)
		child_object7_difficult = SubElement(child_object7, 'difficult')
		child_object7_difficult.text = '0'

		child_object7_bndbox = SubElement(child_object7, 'bndbox')
		child_object7_bndbox_xmin = SubElement(child_object7_bndbox, 'xmin')
		child_object7_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object7_bndbox_ymin = SubElement(child_object7_bndbox, 'ymin')
		child_object7_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object7_bndbox_xmax = SubElement(child_object7_bndbox, 'xmax')
		child_object7_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object7_bndbox_ymax = SubElement(child_object7_bndbox, 'ymax')
		child_object7_bndbox_ymax.text = str(objects[i].bbox[3])

	elif i == 8:
		# print 'add one object'
		child_object8 = SubElement(top, 'object')
    		child_object8_name = SubElement(child_object8, 'name')
    		child_object8_name.text = CLASSES[objects[i].classId]
 		child_object8_pose = SubElement(child_object8, 'pose')
		child_object8_pose.text = 'Left'
		child_object8_truncated = SubElement(child_object8, 'truncated')
		child_object8_truncated.text = str(objects[i].truncated)
		child_object8_difficult = SubElement(child_object8, 'difficult')
		child_object8_difficult.text = '0'

		child_object8_bndbox = SubElement(child_object8, 'bndbox')
		child_object8_bndbox_xmin = SubElement(child_object8_bndbox, 'xmin')
		child_object8_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object8_bndbox_ymin = SubElement(child_object8_bndbox, 'ymin')
		child_object8_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object8_bndbox_xmax = SubElement(child_object8_bndbox, 'xmax')
		child_object8_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object8_bndbox_ymax = SubElement(child_object8_bndbox, 'ymax')
		child_object8_bndbox_ymax.text = str(objects[i].bbox[3])

	elif i == 9:
		# print 'add one object'
		child_object9 = SubElement(top, 'object')
    		child_object9_name = SubElement(child_object9, 'name')
    		child_object9_name.text = CLASSES[objects[i].classId]
 		child_object9_pose = SubElement(child_object9, 'pose')
		child_object9_pose.text = 'Left'
		child_object9_truncated = SubElement(child_object9, 'truncated')
		child_object9_truncated.text = str(objects[i].truncated)
		child_object9_difficult = SubElement(child_object9, 'difficult')
		child_object9_difficult.text = '0'

		child_object9_bndbox = SubElement(child_object9, 'bndbox')
		child_object9_bndbox_xmin = SubElement(child_object9_bndbox, 'xmin')
		child_object9_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object9_bndbox_ymin = SubElement(child_object9_bndbox, 'ymin')
		child_object9_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object9_bndbox_xmax = SubElement(child_object9_bndbox, 'xmax')
		child_object9_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object9_bndbox_ymax = SubElement(child_object9_bndbox, 'ymax')
		child_object9_bndbox_ymax.text = str(objects[i].bbox[3])

	elif i == 10:
		# print 'add one object'
		child_object10 = SubElement(top, 'object')
    		child_object10_name = SubElement(child_object10, 'name')
    		child_object10_name.text = CLASSES[objects[i].classId]
 		child_object10_pose = SubElement(child_object10, 'pose')
		child_object10_pose.text = 'Left'
		child_object10_truncated = SubElement(child_object10, 'truncated')
		child_object10_truncated.text = str(objects[i].truncated)
		child_object10_difficult = SubElement(child_object10, 'difficult')
		child_object10_difficult.text = '0'

		child_object10_bndbox = SubElement(child_object10, 'bndbox')
		child_object10_bndbox_xmin = SubElement(child_object10_bndbox, 'xmin')
		child_object10_bndbox_xmin.text = str(objects[i].bbox[0])
		child_object10_bndbox_ymin = SubElement(child_object10_bndbox, 'ymin')
		child_object10_bndbox_ymin.text = str(objects[i].bbox[1])
		child_object10_bndbox_xmax = SubElement(child_object10_bndbox, 'xmax')
		child_object10_bndbox_xmax.text = str(objects[i].bbox[2])
		child_object10_bndbox_ymax = SubElement(child_object10_bndbox, 'ymax')
		child_object10_bndbox_ymax.text = str(objects[i].bbox[3])
    
    tree = ET.ElementTree(top)
    tree.write(outname)
    return top

