from PIL import Image, ImageOps
import glob
desired_size = 368
im_pth = "queenfireant.png"
for image in glob.glob("*.png"):
    im = Image.open(image)
    old_size = im.size  # old_size[0] is in (width, height) format
    
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # use thumbnail() or resize() method to resize the input image
    
    # thumbnail is a in-place operation
    
    # im.thumbnail(new_size, Image.ANTIALIAS)
    
    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it
    
    new_im = Image.new("RGBA", (desired_size, desired_size), (0,0,0,0))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))

    new_im.save(f"square/{image}")
