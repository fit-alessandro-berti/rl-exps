import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start, temperature_control, pH_monitoring])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, whey_draining])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, salting_process, quality_check])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, label_design])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, retail_delivery])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection, milk_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)