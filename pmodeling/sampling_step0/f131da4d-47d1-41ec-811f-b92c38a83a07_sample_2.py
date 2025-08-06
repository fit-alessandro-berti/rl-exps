import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define transitions
skip = SilentTransition()

# Define POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing, fermentation_start])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[temperature_control, pH_monitoring])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[curd_cutting, whey_draining])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, salting_process])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, quality_check])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, label_design])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, retail_delivery])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip])

# Define root
root = StrictPartialOrder(nodes=[xor, loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, xor)