import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
curd_processing = Transition(label='Curd Processing')
salt_application = Transition(label='Salt Application')
mold_inoculation = Transition(label='Mold Inoculation')
press_molding = Transition(label='Press Molding')
brine_soaking = Transition(label='Brine Soaking')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
microbial_check = Transition(label='Microbial Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
trace_logging = Transition(label='Trace Logging')
distribution_plan = Transition(label='Distribution Plan')
customer_review = Transition(label='Customer Review')
inventory_audit = Transition(label='Inventory Audit')
sustainability_audit = Transition(label='Sustainability Audit')

# Define silent transitions for exclusive choices
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()
skip8 = SilentTransition()

# Define exclusive choices
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip1])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip2])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[curd_processing, skip3])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[salt_application, skip4])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, skip5])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[press_molding, skip6])
exclusive_choice7 = OperatorPOWL(operator=Operator.XOR, children=[brine_soaking, skip7])
exclusive_choice8 = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip8])

# Define loops for repeated activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[microbial_check, exclusive_choice1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, exclusive_choice2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, exclusive_choice3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, exclusive_choice4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[trace_logging, exclusive_choice5])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, exclusive_choice6])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[customer_review, exclusive_choice7])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, exclusive_choice8])
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit, exclusive_choice8])

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    exclusive_choice1,
    exclusive_choice2,
    exclusive_choice3,
    exclusive_choice4,
    exclusive_choice5,
    exclusive_choice6,
    exclusive_choice7,
    exclusive_choice8,
    loop1,
    loop2,
    loop3,
    loop4,
    loop5,
    loop6,
    loop7,
    loop8,
    loop9
])

# Define the dependencies between nodes
root.order.add_edge(exclusive_choice1, loop1)
root.order.add_edge(exclusive_choice2, loop2)
root.order.add_edge(exclusive_choice3, loop3)
root.order.add_edge(exclusive_choice4, loop4)
root.order.add_edge(exclusive_choice5, loop5)
root.order.add_edge(exclusive_choice6, loop6)
root.order.add_edge(exclusive_choice7, loop7)
root.order.add_edge(exclusive_choice8, loop8)
root.order.add_edge(exclusive_choice8, loop9)
root.order.add_edge(loop1, exclusive_choice1)
root.order.add_edge(loop2, exclusive_choice2)
root.order.add_edge(loop3, exclusive_choice3)
root.order.add_edge(loop4, exclusive_choice4)
root.order.add_edge(loop5, exclusive_choice5)
root.order.add_edge(loop6, exclusive_choice6)
root.order.add_edge(loop7, exclusive_choice7)
root.order.add_edge(loop8, exclusive_choice8)
root.order.add_edge(loop9, exclusive_choice8)

print(root)