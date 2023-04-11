from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import FormView

from apps.caesar_cipher import models
from apps.caesar_cipher.forms import MessageForm
from apps.caesar_cipher.services.caesar_password import crypto, decrypto


class MessageView(LoginRequiredMixin, FormView):
    template_name = "caesar_cipher/messagemodel_form.html"
    form_class = MessageForm

    def get_success_url(self):
        return self.request.path

    def get_initial(self):
        initial = super().get_initial()

        owner = self.request.user
        if (
            latest_message := models.Message.objects.filter(
                owner=owner,
            )
            .order_by("-modified_at")
            .first()
        ):
            is_show_encrypted = latest_message.is_latest_mode_encrypted

            if is_show_encrypted:
                message = latest_message.message_encrypted
                message_altered = decrypto(
                    text=latest_message.message_encrypted,
                    key=latest_message.key.key_step,
                )
            else:
                message = decrypto(
                    text=latest_message.message_encrypted,
                    key=latest_message.key.key_step,
                )
                message_altered = latest_message.message_encrypted

            initial["message"] = message
            initial["key_step"] = latest_message.key.key_step
            initial["is_encrypt"] = not is_show_encrypted
            initial["usage_count"] = latest_message.usage_count
            initial["message_altered"] = message_altered
        else:
            initial["message"] = ""
            initial["key_step"] = 0
            initial["is_encrypt"] = True
            initial["usage_count"] = 0

        return initial

    def form_valid(self, form):
        message = form.cleaned_data["message"]
        key_step = form.cleaned_data["key_step"]
        is_encrypt = form.cleaned_data["is_encrypt"]

        action = crypto if is_encrypt else decrypto
        new_message = action(text=message, key=key_step)

        message_encrypted = new_message if is_encrypt else message

        try:
            message_obj = models.Message.objects.filter(
                message_encrypted=message_encrypted,
                owner=self.request.user,
                key__key_step=key_step,
            ).get()
        except models.Message.DoesNotExist:
            key_obj = models.Key.objects.create(
                key_step=key_step,
            )
            message_obj = models.Message.objects.create(
                message_encrypted=message_encrypted,
                owner=self.request.user,
                key=key_obj,
            )

        message_obj.usage_count += 1
        message_obj.is_latest_mode_encrypted = is_encrypt
        message_obj.save()

        return super().form_valid(form)


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )
