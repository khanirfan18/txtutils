from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    dj_text = request.POST.get("text", "")

    rem_punc = request.POST.get("remove_punctuations", "off")
    full_caps = request.POST.get("full_caps", "off")
    newline_rem = request.POST.get("newline_rem", "off")
    space_rem = request.POST.get("space_rem", "off")
    char_count = request.POST.get("char_count", "off")

    if len(dj_text) == 0:
        return render(request, "404.html")

    analyzed = dj_text
    purpose = []

    if rem_punc == "on":
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        analyzed_text = ""

        for char in analyzed:
            if char not in punctuations:
                analyzed_text += char

        analyzed = analyzed_text
        purpose.append("Removed Punctuations")

    if full_caps == "on":
        analyzed = analyzed.upper()
        purpose.append("Capitalized")

    if newline_rem == "on":
        analyzed_text = ""

        for char in analyzed:
            if char != "\n" and char != "\r":
                analyzed_text += char

        analyzed = analyzed_text
        purpose.append("Removed New Lines")

    if space_rem == "on":
        analyzed_text = ""

        for index, char in enumerate(analyzed):
            if (
                char == " "
                and index != len(analyzed) - 1
                and analyzed[index + 1] == " "
            ):
                continue
            analyzed_text += char

        analyzed = analyzed_text
        purpose.append("Removed Extra Spaces")

    if char_count == "on":
        space_count = 0

        for char in analyzed:
            if char == " ":
                space_count += 1

        analyzed += (
            f"\n\nTotal Characters: {len(analyzed)}"
            f"\nTotal Spaces: {space_count}"
        )
        purpose.append("Character Count")

    if len(purpose) == 0:
        return render(request, "404.html")

    params = {
        "purpose": ", ".join(purpose),
        "analyzed_text": analyzed
    }

    return render(request, "analyze.html", params)