from rest_framework.exceptions import ValidationError
from django.conf import settings
from rest_framework import serializers


class APIDeprecationMixin(serializers.Serializer):
    class Meta:
        abstract = True

    def is_valid(self, raise_exception=False):
        message = "Temporarily unavailable, please update your app."
        if self.context["request"].version.replace("v", "") != settings.CURRENT_API_VERSION:
            raise ValidationError(message)
        return super().is_valid(raise_exception)







    def is_valid(self, raise_exception=False):
        is_valid = super().is_valid(raise_exception)
        if is_valid:
            message = "Payment online is temporarily unavailable, card on delivery available"
            if all(
                [
                    self.validated_data["payment_method"] == Order.PAY_ON_DELIVERY.online,
                    any(
                        [
                            self.context["request"].version.replace("v", "")
                            not in ("1.3", settings.CURRENT_API_VERSION),
                            not self.context["request"].user.can_use_tokenization,
                        ]
                    ),
                ]
            ):
                raise ValidationError(message)
        return is_valid