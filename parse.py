from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")
slide_list = []

for slide in prs.slides:
	elements = []
	for shape in slide.placeholders:
		if not shape.has_text_frame:
			continue
		if not shape.is_placeholder:
			continue
		for para in shape.text_frame.paragraphs:
			elements.append( (shape.placeholder_format.type, para.text) )
	if len(elements) != 0:
		slide_list.append(elements)