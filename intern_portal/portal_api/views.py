from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def intern_data(request):
    # """
    # Yeh API endpoint intern dashboard ke liye dummy data deta hai.
    # """
    data = {
        "internName": "Aman Gupta",
        "referralCode": "AMANGUPTA123",
        "totalDonations": 15750
    }
    return Response(data)



@api_view(['GET'])
def leaderboard_data(request):
    data = [
        {"rank": 1, "name": "Riya Sharma", "donations": 25500},
        {"rank": 2, "name": "Karan Singh", "donations": 22100},
        {"rank": 3, "name": "Priya Patel", "donations": 19850},
        {"rank": 4, "name": "Aman Gupta", "donations": 15750}, 
        {"rank": 5, "name": "John Smith", "donations": 12300},
        {"rank": 6, "name": "Anjali Gupta", "donations": 11000},
        {"rank": 7, "name": "Mohammed Ali", "donations": 9500},
        {"rank": 8, "name": "Sophia Chen", "donations": 8200},
        {"rank": 9, "name": "Vikram Rathore", "donations": 7800},
        {"rank": 10, "name": "Emily White", "donations": 7500},
        {"rank": 11, "name": "Arjun Reddy", "donations": 6900},
        {"rank": 12, "name": "Fatima Khan", "donations": 6100},
    ]
    return Response(data)