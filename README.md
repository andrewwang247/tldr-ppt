The returned array is two dimensional. The first dimension indexes into the slide deck. The second dimension accesses individual elements. Each element consists of 3 objects. f elem[0] is true, then the object is a placeholder and elem[1] s the placeholder_format enum type of the object. If elem[0] is alse, then the object is not a placeholder and elem[1] just returns the general shape_type enum. In either case enum[2] is the string containing the text in that element.
