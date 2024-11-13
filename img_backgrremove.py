import rembg

input_path = "indir.png"
output_pat = "output.png"

with open(input_path, "rb") as i:
    with open(output_pat, "wb") as o:
        input_file = i.read()
        output = remove(input_file)
        o.write(output)
