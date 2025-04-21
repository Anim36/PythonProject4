from django.http import JsonResponse

def get_response(request):
    user_message = request.GET.get('message', '').lower()

    responses = {
        "hi": "Hello! Welcome to the University Help Desk. How can I assist you today?",
        "location": "74/A Green Rd, Dhaka 1205.",
        "admission requirement?": "SSC: GPA 4.00, HSC: GPA 4.00, Diploma: GPA 3.5 ",
        "tuition fees": "8,13,200 Tk.",
        "contact": "You can reach us at +880123456789 or email us at support@example.com.",
        "bye": "Goodbye! Have a great day! 👋"
    }

    reply = responses.get(user_message, "Sorry, I didn't understand that.")
    return JsonResponse({"response": reply})
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
