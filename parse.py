from pptx import Presentation

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")
slide_list = []

for slide in prs.slides:
	elements = []
	for shape in slide.shapes:
		if shape.has_text_frame:
			for para in shape.text_frame.paragraphs:
				if para.text == "":
					continue
				elif shape.is_placeholder:
					elements.append( ( True, shape.placeholder_format.type, para.text ) )
				else:
					elements.append( ( False, shape.shape_type, para.text) )
	if len(elements) != 0:
		slide_list.append(elements)
print(slide_list)
            
# for slide in prs.slides:
#     for shape in slide.shapes:
#         if 'Picture' in shape.name:
#             picture = shape
#             image = picture.image
#             image_file_bytes = image.blob
#             file_extension = image.ext
#             file_path=image.filename
#             print(file_path)


# for shape in slide.shapes:
#     if shape.shape_type != MSO_SHAPE_TYPE:
#         continue
#     picture = shape
#     print(picture._pic.nvPicPr.cNvPr.get('descr'))
