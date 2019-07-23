from pptx import python-pptx
from pptx.enum.shapes import MSO_SHAPE_TYPE

prs = Presentation("C:/Users/siwei/Downloads/test.pptx")

text_runs = []
image_runs = []
slide_list = []
for slide in prs.slides:
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        #paras=shape.text_frame.paragraphs
        #for paragraph in shape.text_frame.paragraphs:
         #   for run in paragraph.runs:
          #      text_runs.append(run.text)
        len_1=len(shape.text_frame.paragraphs)
        runs=''
        for i in range(0,len_1):
            for run in shape.text_frame.paragraphs[i].runs:
                text_runs.append(run.text)
        slide_list.append(text_runs)
        text_runs=[]
            
for slide in prs.slides:
    for shape in slide.shapes:
        if 'Picture' in shape.name:
            picture = shape
            image = picture.image
            image_file_bytes = image.blob
            file_extension = image.ext
            file_path=image.filename
            #print(file_path)

 

for shape in slide.shapes:
    if shape.shape_type != MSO_SHAPE_TYPE.PICTURE:
        continue
    picture = shape
    print(picture._pic.nvPicPr.cNvPr.get('descr'))
print(slide_list)