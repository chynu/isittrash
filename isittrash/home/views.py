#importing the html template 
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'index.html'

	def howtodealwiththistrash(self, request, model):
		context= {
			self.name = model.name
			self.desc = model.desc
			self.img_src = model.img_src
			self.html = model.html
			self.category = model.category
		}
		
		return self.render()
 