from django.shortcuts import render

def login_view(request):
    error_email = ""
    error_password = ""
    message = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        
        if not email:
            error_email = "Email is required."
        elif "@" not in email or "." not in email:
            error_email = "Invalid email format."
        elif email.endswith("@gmail.com"):
            error_email = "Gmail addresses are not allowed."

        
        if not password:
            error_password = "Password is required."
        elif len(password) < 6:
            error_password = "Password must be at least 6 characters long."

    
        if not error_email and not error_password:
            message = f"Thanks for registering, {email}!"

    return render(request, "login.html", {
        "error_email": error_email,
        "error_password": error_password,
        "message": message
    })
