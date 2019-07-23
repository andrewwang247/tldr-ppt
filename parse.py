from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")



i = 1
for slide in prs.slides:
	print(i)
	i = i + 1
	for shape in slide.placeholders:
		if not shape.has_text_frame:
			continue
		if not shape.is_placeholder:
			continue
		for para in shape.text_frame.paragraphs:
			print(shape.placeholder_format.type)
			print(para.text)