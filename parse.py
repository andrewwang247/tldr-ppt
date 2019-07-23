from pptx import Presentation

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")
slide_list = []

for slide in prs.slides:
	elements = []
	for shape in slide.shapes:
		if shape.has_text_frame:
			for para in shape.text_frame.paragraphs:
				if shape.is_placeholder:
					elements.append( ( True, shape.placeholder_format.type, para.text ) )
				else:
					elements.append( ( False, shape.shape_type, para.text) )
	if len(elements) != 0:
		slide_list.append(elements)

print(slide_list)