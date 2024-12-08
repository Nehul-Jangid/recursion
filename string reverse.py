def reverse(x):
    if (x == ""):
        return ""
    else:
        return reverse(x[1:]) + x[0]

print(reverse("hello"))