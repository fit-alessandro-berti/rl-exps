import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
temperature_control = Transition(label='Temperature Control')
pH_monitoring = Transition(label='pH Monitoring')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
label_design = Transition(label='Label Design')
distribution_plan = Transition(label='Distribution Plan')
retail_delivery = Transition(label='Retail Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, temperature_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pH_monitoring, milk_testing])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, label_design])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, customer_feedback])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[molded_cheese, curd_cutting])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, salting_process])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection, milk_testing, fermentation_start, temperature_control, pH_monitoring, curd_cutting, whey_draining, salting_process, aging_setup, quality_check, packaging_prep, label_design, distribution_plan, retail_delivery, customer_feedback])

# Create the root node
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

print(root)