s ="""# PropertySet

## Properties

- **`Name`** *(string)*: Name of the PropertySet.
- **`Definition`** *(string)*: Definition of the PropertySet. Default: ``.
  
## Definitions

- **`UseTypeEnum`** *(string)*: An enumeration. Must be one of: `['Room Data Template', 'Product Data Template', 'IFC Property Set', 'Max Fordham Property Set', 'Undefined']`.
- **`StatusEnum`** *(string)*: An enumeration. Must be one of: `['Active', 'Inactive']`.
"""
# import pathlib
# lines = pathlib.Path('eg.txt').read_text().split('\n')
#  ^ if reading text from file

lines = s.split('\n')
lines = lines[0:lines.index('## Definitions')]  # remove definitions onwards
lines = [l for l in lines if "#" not in l]  # remove titles
lines = [l for l in lines if l != ''] # remove blank lines
lines = [l for l in lines if l.replace(' ', '') != '']  # remove strings 
lines