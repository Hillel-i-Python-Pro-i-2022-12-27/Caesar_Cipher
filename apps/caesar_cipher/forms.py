from django.forms import ModelForm

from apps.caesar_cipher.models import MessageModel


class MessageForm(ModelForm):
    class Meta:
        model = MessageModel
        fields = ["text ", "key_step"]
