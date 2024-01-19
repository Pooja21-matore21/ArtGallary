from django.shortcuts import render, redirect
from AdminApp.models import Category, Mehandi, Payment
from UserApp.models import UserInfo, MyCart, OrderMaster,UserAppoinment
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def home(request):
    cats = Category.objects.all()
    mehandi = Mehandi.objects.all()
    return render(request, 'master.html', {'cats': cats, 'mehandi': mehandi})


def ShowMehandi(request, id):
    cats = Category.objects.all()
    mehandi = Mehandi.objects.filter(category=id)
    return render(request, "category.html", {"cats": cats, "mehandi": mehandi})


def ViewDetails(request, id):
    cats = Category.objects.all()
    mehandis = Mehandi.objects.get(id=id)
    return render(request, "viewDetails.html", {"cats": cats, "mehandis": mehandis})


def addToCart(request):
    if ("uname" in request.session):
        user = UserInfo.objects.get(username=request.session["uname"])
        mehandi_id = request.POST["cid"]
        mehandi = Mehandi.objects.get(id=mehandi_id)
        qty = request.POST["qty"]
        try:
            item = MyCart.objects.get(user=user, mehandi=mehandi)
        except:
            cart = MyCart()
            cart.user = user
            cart.mehandi = mehandi
            cart.qty = qty
            cart.save()
            messages.info(request, 'Item added successfully..!!')
        else:
            messages.info(request, 'Item already exists..!!')
        return redirect(showCartItems)
    else:
        return redirect(Login)


def showCartItems(request):
    cats = Category.objects.all()
    # fetch those request which added by user
    if (request.method == "GET"):
        items = MyCart.objects.filter(user=request.session["uname"])
        total = 0
        for item in items:
            total += item.qty * item.mehandi.price
        request.session["total"] = total
        return render(request, "showCartItems.html", {"items": items, "cats": cats})
    else:
        cart_id = request.POST["cart_id"]
        item = MyCart.objects.get(id=cart_id)
        action = request.POST["action"]
        if (action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(showCartItems)


def proceedToPay(request):
    if (request.method == "GET"):
        return render(request, "proceedToPay.html", {})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry_date = request.POST["expiry_date"]
        try:
            buyer = Payment.objects.get(
                card_no=card_no, cvv=cvv, expiry_date=expiry_date)

        except:
            return redirect(proceedToPay)
        else:
            owner = Payment.objects.get(
                card_no="22222", cvv="222", expiry_date="12/26")
            buyer.balance -= float(request.session["total"])
            owner.balance += float(request.session["total"])
            owner.save()
            buyer.save()

            myorder = OrderMaster()
            user = UserInfo.objects.get(username=request.session["uname"])
            myorder.user = user
            myorder.amount = request.session["total"]
            items = MyCart.objects.filter(user=user)
            details = ""
            for item in items:
                details += item.mehandi.mehandi_name+" "
                item.delete()

            myorder.details = details
            myorder.save()
            # delete all cart items

            return redirect(home)


def SignOut(request):
    # delete the session
    request.session.clear()
    return redirect(home)


def Login(request):
    if (request.method == "GET"):
        return render(request, "Login.html", {})
    else:

        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            user = UserInfo.objects.get(username=uname, password=pwd)
        except:
            msg = "Invalid credentials..Please try again..!!"
            return render(request, "Login.html", {"msg": msg})
        else:
            request.session["uname"] = uname
            return redirect(home)


def SignUp(request):
    if (request.method == "GET"):
        return render(request, "SignUp.html", {})
    else:
        email = request.POST["email"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            user = UserInfo.objects.get(username=uname)
        except:
            user = UserInfo(uname, pwd, email)
            user.save()
            return redirect(home)
        else:
            msg = "This user already exist.!!"
            return render(request, "SignUp.html", {"msg": msg})

def bookappoinment(request):
    if (request.method == "GET"):
        return render(request, "book_appoinment.html", {})
    else:
        
        email = request.POST["email"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        message = request.POST["message"]

        try:
            users = UserAppoinment.objects.get(usernamee=name)
        except:
            users = UserAppoinment(email,name,phone,date,message)
            users.save()
        return redirect(home)
        