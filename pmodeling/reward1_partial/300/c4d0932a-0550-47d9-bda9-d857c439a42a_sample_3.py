import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_block = Transition(label='Pressing Block')
brining_bath = Transition(label='Brining Bath')
aging_control = Transition(label='Aging Control')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
demand_forecast = Transition(label='Demand Forecast')
retail_outreach = Transition(label='Retail Outreach')
customer_feedback = Transition(label='Customer Feedback')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, starter_culture])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[coagulation, curd_cutting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, molding_cheese])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pressing_block, brining_bath])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[aging_control, flavor_profiling])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, demand_forecast])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[retail_outreach, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(milk_sourcing, xor1)
root.order.add_edge(milk_sourcing, xor2)
root.order.add_edge(milk_sourcing, xor3)
root.order.add_edge(milk_sourcing, xor4)
root.order.add_edge(milk_sourcing, xor5)
root.order.add_edge(milk_sourcing, xor6)
root.order.add_edge(milk_sourcing, xor7)

# Print the root model
print(root)