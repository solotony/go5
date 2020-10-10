from .models.customers import Customer, AnonimousCustomer

class CustomerLoader:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated:
            request.customer = AnonimousCustomer()

        request.customer = Customer.objects.filter(id=request.user.id).first()
        if not request.customer:
            request.customer = AnonimousCustomer()

        return self.get_response(request)
