from PIL import Image


import matplotlib.pyplot as plt
from PIL.Image import Image as PilImage
from resizeimage import resizeimage
import textwrap, os

def display_images(
    images: [PilImage],
    columns=5, width=30, height=30, max_images=8,
    label_wrap_length=25, label_font_size=8):

    if not images:
        print("No images to display.")
        return

    if len(images) > max_images:
        print(f"Showing {max_images} images of {len(images)}:")
        images=images[0:max_images]

    height = max(height, int(len(images)/columns) * height)
    plt.figure(figsize=(width*0.8, height*0.8))
    for i, image in enumerate(images):

        plt.subplot(int(len(images) / columns + 1), columns, i + 1)
        plt.imshow(image)

        if hasattr(image, 'filename'):
            title=image.filename
            if title.endswith("/"): title = title[0:-1]
            title=os.path.basename(title)
            title=textwrap.wrap(title, label_wrap_length)
            title="\n".join(title)
            plt.title(title, fontsize=label_font_size);
    plt.show()


TAILLE = [1000, 1000]
img_01 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDEG_DDM1_CvS.png"), TAILLE)
img_02 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDEG_KD_CvS.png"), TAILLE)
img_03 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDEG_OX_CvS.png"), TAILLE)
img_04 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDEG_Temoin_CvS.png"), TAILLE)

img_05 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDET_DDM1_CvS.png"), TAILLE)
img_06 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDET_KD_CvS.png"), TAILLE)
img_07 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDET_OX_CvS.png"), TAILLE)
img_08 = resizeimage.resize_cover(Image.open("/home/alexandre/Téléchargements/Venn ASxDEG-T/Contrôle vs Sècheresse/ASxDET_Temoin_CvS.png"), TAILLE)

list = [img_01, img_02, img_03, img_04,
        img_05, img_06, img_07, img_08
        ]

display_images(list,columns=4)

#new_im.save("merged_images.png", "PNG")
#new_im.show()
