from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")
slide_list = []

for slide in prs.slides:
	elements = []
	for shape in slide.shapes:
		if not shape.has_text_frame:
			continue
		for para in shape.text_frame.paragraphs:
			elements.append( (shape.shape_type, para.text) )
	if len(elements) != 0:
		slide_list.append(elements)

print(slide_list)