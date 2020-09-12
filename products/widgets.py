from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy

class FileInput(ClearableFileInput):
    clear_checkbox_label = gettext_lazy('Remove')
    initial_text = gettext_lazy('Current Image')
    input_text = gettext_lazy('')
