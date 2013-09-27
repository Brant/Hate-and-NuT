"""
Custom forms
"""
from noodles.forms import ContactForm


class HancomContactForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super(HancomContactForm, self).__init__(*args, **kwargs)
        self.fields["email"].help_text = "So I can get back to you"
        self.fields["name"].help_text = "So I know what to call you"
        self.fields["message"].help_text = "What's on your mind?"
