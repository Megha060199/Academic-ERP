from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Enroll Student"),
			"items": [
				{
					"type": "doctype",
					"name": "Enroll Student",
					"onboard": 1,
				},
			]
		},
	
	]
