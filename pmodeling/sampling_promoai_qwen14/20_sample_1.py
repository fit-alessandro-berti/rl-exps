import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

GuestCallsRoomService = Transition(label='Guest calls room service')
KitchenPreparesFood = Transition(label='Kitchen prepares food')
ManagerAssignsOrderToWaiter = Transition(label='Manager assigns order to waiter')
ManagerGivesOrderToSommelier = Transition(label='Manager gives order to sommelier')
ManagerSubmitsOrderTicketToKitchen = Transition(label='Manager submits order ticket to kitchen')
ManagerTakesDownTheOrder = Transition(label='Manager takes down the order')
SommelierFetchesWineAndPrepareAlcoholicBeverages = Transition(label='Sommelier fetches wine and prepare alcoholic beverages')
WaiterDebitsGuestsAccount = Transition(label='Waiter debits guest\'s account')
WaiterDeliversOrderToGuestsRoom = Transition(label='Waiter delivers order to guest\'s room')
WaiterPreparesNonalcoholicDrinks = Transition(label='Waiter prepares nonalcoholic drinks')
WaiterReadiesCart = Transition(label='Waiter readies cart')
WaiterReturnsToRoomServiceStation = Transition(label='Waiter returns to room-service station')
WaiterWaitsDelaysDebiting = Transition(label='Waiter waits/delays debiting')

loop = OperatorPOWL(operator=Operator.LOOP, children=[WaiterReadiesCart, WaiterDeliversOrderToGuestsRoom, WaiterReturnsToRoomServiceStation, WaiterWaitsDelaysDebiting, WaiterDebitsGuestsAccount])

root = StrictPartialOrder(nodes=[GuestCallsRoomService, ManagerTakesDownTheOrder, ManagerSubmitsOrderTicketToKitchen, ManagerAssignsOrderToWaiter, ManagerGivesOrderToSommelier, KitchenPreparesFood, SommelierFetchesWineAndPrepareAlcoholicBeverages, WaiterPreparesNonalcoholicDrinks, loop])

root.order.add_edge(GuestCallsRoomService, ManagerTakesDownTheOrder)
root.order.add_edge(ManagerTakesDownTheOrder, ManagerSubmitsOrderTicketToKitchen)
root.order.add_edge(ManagerSubmitsOrderTicketToKitchen, ManagerAssignsOrderToWaiter)
root.order.add_edge(ManagerAssignsOrderToWaiter, ManagerGivesOrderToSommelier)
root.order.add_edge(ManagerGivesOrderToSommelier, KitchenPreparesFood)
root.order.add_edge(ManagerGivesOrderToSommelier, SommelierFetchesWineAndPrepareAlcoholicBeverages)
root.order.add_edge(KitchenPreparesFood, WaiterPreparesNonalcoholicDrinks)
root.order.add_edge(WaiterPreparesNonalcoholicDrinks, WaiterReadiesCart)
root.order.add_edge(WaiterReadiesCart, WaiterDeliversOrderToGuestsRoom)
root.order.add_edge(WaiterDeliversOrderToGuestsRoom, WaiterReturnsToRoomServiceStation)
root.order.add_edge(WaiterReturnsToRoomServiceStation, WaiterWaitsDelaysDebiting)
root.order.add_edge(WaiterWaitsDelaysDebiting, WaiterDebitsGuestsAccount)