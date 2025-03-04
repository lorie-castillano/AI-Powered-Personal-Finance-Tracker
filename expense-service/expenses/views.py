from rest_framework import viewsets

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expense to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
