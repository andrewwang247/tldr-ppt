from pptx import Presentation

# The returned array is two dimensional. The first dimension
# indexes into the slide deck. The second dimension accesses
# individual elements. Each element consists of 3 objects.
# If elem[0] is true, then the object is a placeholder and elem[1]
# is the placeholder_format enum type of the object. If elem[0] is
# false, then the object is not a placeholder and elem[1] just
# returns the general shape_type enum. In either case enum[2] is the
# string containing the text in that element.
def returnText(fileName):

	prs = Presentation(fileName)
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
	return slide_list
            
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
