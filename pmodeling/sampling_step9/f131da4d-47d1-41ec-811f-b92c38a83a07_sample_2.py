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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_selection, milk_testing, fermentation_start, temperature_control, pH_monitoring, curd_cutting, whey_draining, molding_cheese, salting_process, aging_setup, quality_check, packaging_prep, label_design, distribution_plan, retail_delivery, customer_feedback])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)