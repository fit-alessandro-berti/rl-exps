import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

GuestCallsRoomService = Transition(label='Guest calls room service')
ManagerTakesDownTheOrder = Transition(label='Manager takes down the order')
ManagerSubmitsOrderTicketToKitchen = Transition(label='Manager submits order ticket to kitchen')
KitchenPreparesFood = Transition(label='Kitchen prepares food')
ManagerGivesOrderToSommelier = Transition(label='Manager gives order to sommelier')
SommelierFetchesWineAndPrepareAlcoholicBeverages = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
ManagerAssignsOrderToWaiter = Transition(label='Manager assigns order to waiter')
WaiterReadiesCart = Transition(label='Waiter readies cart')
WaiterPreparesNonalcoholicDrinks = Transition(label='Waiter prepares nonalcoholic drinks')
WaiterDeliversOrderToGuestsRoom = Transition(label='Waiter delivers order to guest\'s room')
WaiterReturnsToRoomServiceStation = Transition(label='Waiter returns to room-service station')
WaiterDebitsGuestsAccount = Transition(label='Waiter debits guest\'s account')
WaiterWaitsDelaysDebiting = Transition(label='Waiter waits/delays debiting')

loop = OperatorPOWL(operator=Operator.LOOP, children=[WaiterWaitsDelaysDebiting])
xor = OperatorPOWL(operator=Operator.XOR, children=[WaiterDebitsGuestsAccount, loop])
root = StrictPartialOrder(nodes=[GuestCallsRoomService, ManagerTakesDownTheOrder, ManagerSubmitsOrderTicketToKitchen, KitchenPreparesFood, ManagerGivesOrderToSommelier, SommelierFetchesWineAndPrepareAlcoholicBeverages, ManagerAssignsOrderToWaiter, WaiterReadiesCart, WaiterPreparesNonalcoholicDrinks, WaiterDeliversOrderToGuestsRoom, WaiterReturnsToRoomServiceStation, xor])

root.order.add_edge(GuestCallsRoomService, ManagerTakesDownTheOrder)
root.order.add_edge(ManagerTakesDownTheOrder, ManagerSubmitsOrderTicketToKitchen)
root.order.add_edge(ManagerSubmitsOrderTicketToKitchen, KitchenPreparesFood)
root.order.add_edge(ManagerTakesDownTheOrder, ManagerGivesOrderToSommelier)
root.order.add_edge(ManagerGivesOrderToSommelier, SommelierFetchesWineAndPrepareAlcoholicBeverages)
root.order.add_edge(ManagerTakesDownTheOrder, ManagerAssignsOrderToWaiter)
root.order.add_edge(ManagerAssignsOrderToWaiter, WaiterReadiesCart)
root.order.add_edge(ManagerAssignsOrderToWaiter, WaiterPreparesNonalcoholicDrinks)
root.order.add_edge(WaiterReadiesCart, WaiterDeliversOrderToGuestsRoom)
root.order.add_edge(WaiterPreparesNonalcoholicDrinks, WaiterDeliversOrderToGuestsRoom)
root.order.add_edge(WaiterDeliversOrderToGuestsRoom, WaiterReturnsToRoomServiceStation)
root.order.add_edge(WaiterReturnsToRoomServiceStation, xor)