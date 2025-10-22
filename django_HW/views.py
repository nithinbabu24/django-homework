from django.shortcuts import render

def login_view(request):
    context = {"errors": {}, "email": "", "password": ""}

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        context["email"] = email
        context["password"] = password

        errors = {}

        if not email:
            errors["email"] = "Email is required."
        elif "@" not in email or "." not in email.split("@")[-1]:
            errors["email"] = "Enter a valid email address."
        elif email.lower().endswith("@gmail.com"):
            errors["email"] = "Gmail addresses are not allowed."

        if not password:
            errors["password"] = "Password is required."
        elif len(password) < 6:
            errors["password"] = "Password must be at least 6 characters long."

        if not errors:
            return render(request, "index.html", {"success": True, "email": email})

        context["errors"] = errors

    return render(request, "index.html", context)
