import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define relationships
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, coagulation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, pressing_block])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[brining_bath, aging_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, packaging_design])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, retail_outreach])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, demand_forecast])

loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, loop)