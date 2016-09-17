# All objects are included here.

from django import models

# ======= TRASH OBJECT
# name: type of object           e.g. Cell Phone
# desc: description of obj       e.g. Any mobile device that uses wifi
# img_src: link to img           e.g. ../images/cellphone.png
# html: html repr. of the tips   e.g. <b>don't!</b> do this, yes so u throw bla bla idk
#       to give to user
# category: type of trash        e.g. Electronic waste
class Trash(models.Model):
	name = models.CharField()
	desc = models.CharField()
	img_src = models.ImageField()
	html = models.CharField()
	category = models.CharField(max_length=1)

	def throw(self, nm, dsc, img, html, cat):
		name = nm
		desc = dsc
		img_src = img
		html = html
		category = cat

