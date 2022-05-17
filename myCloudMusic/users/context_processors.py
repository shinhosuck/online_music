from users.forms import MessageForm


def message_form(request):
    user_message_form = MessageForm()
    return {"user_message_form": user_message_form}