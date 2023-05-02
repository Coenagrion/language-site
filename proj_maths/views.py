from django.shortcuts import render
from django.core.cache import cache
from . import terms_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def rules_list(request):
    rules = terms_work.get_rules_for_table()
    return render(request, "rules_list.html", context={"rules": rules})


def add_term(request):
    return render(request, "term_add.html")


def add_rule(request):
    return render(request, "rule_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить перевод..."
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить слово..."
        else:
            context["success"] = True
            context["comment"] = "Слово в списке!"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def send_rule(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_rule = request.POST.get("new_rule", "")
        new_exceptions = request.POST.get("new_exceptions", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_exceptions) == 0:
            context["success"] = False
            context["comment"] = "Вы уверены, что нет исключений? Если уверены, поставьте прочерк."
        elif len(new_rule) == 0:
            context["success"] = False
            context["comment"] = "Вы забыли добавить правило..."
        else:
            context["success"] = True
            context["comment"] = "Правило в списке!"
            terms_work.write_rule(new_rule, new_exceptions)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "rule_request.html", context)
    else:
        add_term(request)
