# Example usage of profileImageEditor
from profile_image_editor import facebookImageEditor, twitterImageEditor, \
youtubeImageEditor, tiktokImageEditor, instagramImageEditor, \
pinterestImageEditor, tumblrImageEditor, linkedinImageEditor, \
whatsappImageEditor, redditImageEditor, tumblrImageEditor


def editImageAllPlatforms(img, centerPt):
    editors = []

    editors.append(facebookImageEditor(img))
    editors.append(twitterImageEditor(img))
    editors.append(youtubeImageEditor(img))
    editors.append(tiktokImageEditor(img))
    editors.append(instagramImageEditor(img))
    editors.append(pinterestImageEditor(img))
    editors.append(tumblrImageEditor(img))
    editors.append(linkedinImageEditor(img))
    editors.append(whatsappImageEditor(img))
    editors.append(redditImageEditor(img))
    editors.append(tumblrImageEditor(img))

    
    for item in editors:
        profileImg = item.editImage(centerPt)
        profileImg.show()

im = Image.open('mySelfie.jpeg')
editImageAllPlatforms(im, (321, 226))
