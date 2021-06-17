import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def xml_to_csv2(path):
    xml_list = []
    file_name = []
    xml_list2 = []
    xml_list3 = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            if member[0].text == 'float':
                text_11 = 0
            elif member[0].text == 'WBC':
                text_11 = 1
            elif member[0].text == 'Platelets':
                text_11 = 2
            value = (text_11,
                     ((int(member[4][2].text) - int(member[4][0].text))/2 + int(member[4][0].text)) / int(root.find('size')[0].text),
                     ((int(member[4][3].text) - int(member[4][1].text))/2 + int(member[4][1].text)) / int(root.find('size')[1].text),
                     (int(member[4][2].text)-int(member[4][0].text))/int(root.find('size')[0].text),
                     (int(member[4][3].text)-int(member[4][1].text))/int(root.find('size')[1].text)
                     )
            xml_list.append(value)
            xml_list3.append(value)

        file_name.append(root.find('filename').text.replace(".jpg", ""))
        column_name2 = ['class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_list2.append(pd.DataFrame(xml_list, columns=column_name2))
        xml_list.clear()
    column_name = ['class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list3, columns=column_name)
    print(len(xml_list2))
    print(len(file_name))
    return xml_df, file_name, xml_list2


image_path = os.path.join(os.getcwd(), 'wow_fish/{}'.format('Annotations'))
xml_df, file_name_list, array_xml_list = xml_to_csv2(image_path)
print(xml_df)
print(array_xml_list[0])
print(xml_df.shape[0])
print(xml_df.loc[[0]])
# xml_df.to_csv('data/{}_labels2.csv'.format('Annotations'), index=None)
# xml_df.to_csv('BCCD/{}_labels2.txt'.format('Annotations'), index=None)
# np.savetxt('BCCD/{}_labels5.txt'.format('Annotations'), xml_df.loc[[0]].values[0], fmt='%1.6f')
xml_df.loc[[0]].to_csv('wow_fish/{}_labels5.txt'.format('Annotations'), index=None, header=None, sep=' ', float_format='%.6f')
num_list = 0
for xml_list in array_xml_list:
    xml_list.to_csv('wow_fish/{}.txt'.format(file_name_list[num_list]), index=None, header=None, sep=' ',
                           float_format='%.6f')
    num_list = num_list + 1

print('Successfully converted xml to csv.')

