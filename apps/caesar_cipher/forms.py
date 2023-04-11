from typing import ClassVar

from django import forms


class MessageForm(forms.Form):
    _ROWS_TEXTAREA: ClassVar[int] = 3

    message = forms.CharField(
        label="Message",
        max_length=250,
        widget=forms.Textarea(
            attrs={
                "rows": _ROWS_TEXTAREA,
            },
        ),
    )

    key_step = forms.IntegerField(
        label="Key Step",
    )

    is_encrypt = forms.BooleanField(
        label="Encrypt",
        required=False,
    )

    usage_count = forms.IntegerField(
        label="Usage Count",
        required=False,
        widget=forms.NumberInput(
            attrs={"readonly": "readonly"},
        ),
    )

    message_altered = forms.CharField(
        label="Message Altered",
        max_length=250,
        widget=forms.Textarea(
            attrs={
                "readonly": "readonly",
                "rows": _ROWS_TEXTAREA,
            },
        ),
        required=False,
    )
