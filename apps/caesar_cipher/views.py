# from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.caesar_cipher.forms import MessageForm

# from apps.caesar_cipher.models import MessageModel


class MessageView(FormView):
    # success_url = reverse_lazy("game:list")
    template_name = "caesar_cipher/messagemodel_form.html"
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # room_id = self.kwargs["pk"]

        # room = Room.objects.filter(pk=room_id).get()
        # word_form = WordForm
        # context["title"] = room.name
        # words = room.word_set.all()
        # # words = Word.objects.all()
        # context["words"] = words
        # context["word_form"] = word_form

        return context


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )
