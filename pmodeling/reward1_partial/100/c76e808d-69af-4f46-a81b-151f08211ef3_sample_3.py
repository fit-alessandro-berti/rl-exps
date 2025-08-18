import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
env_monitoring = Transition(label='Env Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
blockchain_entry = Transition(label='Blockchain Entry')
quality_audit = Transition(label='Quality Audit')
retail_sync = Transition(label='Retail Sync')
transport_prep = Transition(label='Transport Prep')
delivery_tracking = Transition(label='Delivery Tracking')
customer_feedback = Transition(label='Customer Feedback')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define exclusive choices
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, curd_formation])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, molding_cheese])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[salting_process, aging_setup])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[env_monitoring, flavor_profiling])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, blockchain_entry])
exclusive_choice7 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, retail_sync])
exclusive_choice8 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, delivery_tracking])
exclusive_choice9 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip1])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice1, skip2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice2, skip3])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, exclusive_choice3, exclusive_choice4, exclusive_choice5, exclusive_choice6, exclusive_choice7, exclusive_choice8, exclusive_choice9])
root.order.add_edge(loop1, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, exclusive_choice5)
root.order.add_edge(exclusive_choice5, exclusive_choice6)
root.order.add_edge(exclusive_choice6, exclusive_choice7)
root.order.add_edge(exclusive_choice7, exclusive_choice8)
root.order.add_edge(exclusive_choice8, exclusive_choice9)