from django.shortcuts import render

def login_view(request):
    error_full_name = ""
    error_email = ""
    error_password = ""
    message = ""

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        
        if not full_name:
            error_full_name = "Full name is required."
        elif len(full_name) < 2:
            error_full_name = "Full name must be at least 2 characters long."

        
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

        
        if not error_full_name and not error_email and not error_password:
            message = f"Thanks for registering, {full_name}!"

    return render(request, "login.html", {
        "error_full_name": error_full_name,
        "error_email": error_email,
        "error_password": error_password,
        "message": message
    })
