from PIL import Image, ImageFilter


class profileImageEditor:
# This is a general class for other editing classes so that
# editing an image for each profile on each website is simple inherited
# and the halfsidelength is the only thing that needs to change
    
    def __init__(self, img):
        self.image = img
        self.halfsidelength = 0

    def editImage(self, centerPt):

        left = centerPt[0] - self.halfsidelength
        right = centerPt[0] + self.halfsidelength
        up = centerPt[1] - self.halfsidelength
        lower = centerPt [1] + self.halfsidelength

        box = (left, up, right, lower)
        region = self.image.crop(box)
        
        return region
    
class facebookImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 90

class twitterImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 200

class youtubeImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 400

class tiktokImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 50

class instagramImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 55

class pinterestImageEditor(profileImageEditor):
# Note, pinterest images are 165x165 so the half way point
# will be one pixel larger than it needs to be.

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 83

class tumblrImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 64

class linkedinImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 200

class whatsappImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 250

class redditImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 128

class tumblrImageEditor(profileImageEditor):

    def __init__(self, img):
        super().__init__(img)
        self.halfsidelength = 400

        
