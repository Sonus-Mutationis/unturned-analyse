import sys
import os
from xml.etree import ElementTree as ET
from pathlib import Path

def merge_xml_comments(target_file, source_folder):
    # Read the target XML file
    try:
        tree = ET.parse(target_file)
        root = tree.getroot()
        members = root.find('members')
        
        if members is None:
            members = ET.SubElement(root, 'members')
    except ET.ParseError as e:
        print(f"Error: Unable to parse target file {target_file}")
        print(e)
        return
    
    # Iterate through all XML files in the source folder
    for xml_file in Path(source_folder).glob('*.xml'):
        try:
            # Add file source comments
            
            # Parse the source XML file
            source_tree = ET.parse(xml_file)
            source_root = source_tree.getroot()
            
            members_to_add = list(source_root.iter('member'))
            
            if members_to_add:
                insert_position = len(members)
                comment = ET.Comment(f' From file: {xml_file.name} ')
                members.insert(insert_position, comment)
                
                for member in members_to_add:
                    members.append(member)
                
        except ET.ParseError as e:
            print(f"Warning: Unable to parse file {xml_file}")
            print(e)
            continue
    
    # Save the merged file
    ET.indent(tree)
    tree.write(target_file, encoding='utf-8', xml_declaration=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <target XML file> <source XML folder>")
        return
    
    target_file = sys.argv[1]
    source_folder = sys.argv[2]
    
    if not os.path.exists(target_file):
        print(f"Error: Target file {target_file} does not exist")
        return
        
    if not os.path.isdir(source_folder):
        print(f"Error: Source folder {source_folder} does not exist")
        return
    
    merge_xml_comments(target_file, source_folder)
    print("XML files merged successfully!")

if __name__ == "__main__":
    main()