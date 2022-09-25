from django.http import HttpResponse


class Webhook_Handler:
    """Handles Stripe Webhook"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a webhook event.
        that can be generic/unexpected/unknown
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status=200)

    def payment_intent_succeded(self, event):
        """Handles payment intent succeded webhook (stripe)"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status=200)

    def payment_intent_payment_failed(self, event):
        """Handles payment_intent.payment_failed webhook (stripe)"""
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}', status=200)
