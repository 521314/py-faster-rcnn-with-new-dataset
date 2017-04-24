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
    
    child_object = {}
    child_object_name = {}
    child_object_pose = {}
    child_object_truncated = {}
    child_object_difficult = {}
    child_object_bndbox = {}
    child_object_bndbox_xmin = {}
    child_object_bndbox_ymin = {}
    child_object_bndbox_xmax = {}
    child_object_bndbox_ymax = {}

    for i in range(len(objects)):
        child_object[i] = SubElement(top, 'object')
        child_object_name[i] = SubElement(child_object[i], 'name')
        child_object_name[i].text = CLASSES[objects[i].classId].lower()
        child_object_pose[i] = SubElement(child_object[i], 'pose')
        child_object_pose[i].text = 'Left'
        child_object_truncated[i] = SubElement(child_object[i], 'truncated')
        child_object_truncated[i].text = str(objects[i].truncated)
        child_object_difficult[i] = SubElement(child_object[i], 'difficult')
        child_object_difficult[i].text = '0'

        child_object_bndbox[i] = SubElement(child_object[i], 'bndbox')
        child_object_bndbox_xmin[i] = SubElement(child_object_bndbox[i], 'xmin')
        child_object_bndbox_xmin[i].text = str(objects[i].bbox[0])
        child_object_bndbox_ymin[i] = SubElement(child_object_bndbox[i], 'ymin')
        child_object_bndbox_ymin[i].text = str(objects[i].bbox[1])
        child_object_bndbox_xmax[i] = SubElement(child_object_bndbox[i], 'xmax')
        child_object_bndbox_xmax[i].text = str(objects[i].bbox[2])
        child_object_bndbox_ymax[i] = SubElement(child_object_bndbox[i], 'ymax')
        child_object_bndbox_ymax[i].text = str(objects[i].bbox[3])
    
    tree = ET.ElementTree(top)
    tree.write(outname)
    return top

