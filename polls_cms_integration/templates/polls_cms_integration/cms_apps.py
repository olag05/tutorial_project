from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register  # register the application
class PollsApphook(CMSApp):
	app_name = "polls"
	name = _("Polls Application")
	
	def get_urls(self, page=None, language=None, **kwargs):
		return ["polls.urls"]
		
from django.conf.urls import url
from polls.views import PollListView, PollDetailView

class PollsApphook(CMSApp):
	# ...
	def get_urls(self, page=None, language=None, **kwargs):
		return [
			url(r'^$', PollListView.as_view()),
			url(r'^(?P<slug>[\w-]+)/?$', PollDetailView.as_view()),
		]