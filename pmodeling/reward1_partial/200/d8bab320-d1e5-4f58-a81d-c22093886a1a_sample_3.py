import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
mold_inoculate = Transition(label='Mold Inoculate')
cheese_pressing = Transition(label='Cheese Pressing')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_forecast = Transition(label='Order Forecast')
regulation_audit = Transition(label='Regulation Audit')
waste_recycling = Transition(label='Waste Recycling')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the control flow operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, curd_formation])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, mold_inoculate])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[cheese_pressing, aging_setup])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, flavor_testing])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[order_forecast, regulation_audit])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, market_delivery])
choice9 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, waste_recycling])

# Define the partial order
root = StrictPartialOrder(nodes=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9])
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)
root.order.add_edge(choice8, choice9)

# Print the root
print(root)