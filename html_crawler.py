import argparse
from lxml import etree


parser = argparse.ArgumentParser(description=
        'locate sligtly different html elements. It returns path of the element_id in the diff file')
parser.add_argument('-s', '--source_file',required=True, type=str,help='source file where locate element')
parser.add_argument('-d', '--diff_file',required=True, type=str,help='diff file where element should be found')
parser.add_argument('-e', '--element',required=True, type=str,help='html element id to be found on source file')

args = parser.parse_args()

# calculates diff between attributes between elments
def get_element_diff_count(source_element, target_element):
	result = sum(map(lambda e: 1, filter(lambda i : target_element.get(i[0], None) != i[1] , source_element.items())))
	return result

# Looks for the html element on target_list with less differences compared to source_element. If there is more than 1 element with less differences returns the first.
def get_most_similar_element(source_element, target_list):
	element_to_return=(None,None)
	for target_element in target_list:
		diff_count = get_element_diff_count(source_element, target_element)
		if element_to_return[1] is None or element_to_return[1] > diff_count:
			element_to_return = (target_element, diff_count)
		if diff_count <=1:
			break
	return element_to_return[0]


## Parse bot html files
html_parser = etree.HTMLParser()
origin_html = etree.parse(args.source_file, html_parser)
target_html = etree.parse(args.diff_file, html_parser)


find_element_on_origin = origin_html.xpath("//*[@id='{}']".format(args.element))
source_element = find_element_on_origin[0]

# Once I get element on source look for elements on target with the same html tag
find_element_on_target = target_html.xpath("//*/{}".format(source_element.tag))
element_list = find_element_on_target

found_element = get_most_similar_element(source_element,element_list)

print(target_html.getpath(found_element))


#for i in found_element.items():
#	print("key: {} - value:{} ".format(i[0],i[1]))
#print(found_element.text)

