import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
pest_scan = Transition(label='Pest Scan')
light_control = Transition(label='Light Control')
growth_monitor = Transition(label='Growth Monitor')
water_cycle = Transition(label='Water Cycle')
air_quality = Transition(label='Air Quality')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
data_logging = Transition(label='Data Logging')
packaging = Transition(label='Packaging')
waste_sort = Transition(label='Waste Sort')
energy_audit = Transition(label='Energy Audit')
retail_sync = Transition(label='Retail Sync')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
sub_process1 = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, skip])
sub_process2 = OperatorPOWL(operator=Operator.XOR, children=[light_control, skip])
sub_process3 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, skip])
sub_process4 = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, skip])
sub_process5 = OperatorPOWL(operator=Operator.XOR, children=[air_quality, skip])
sub_process6 = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, skip])
sub_process7 = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, skip])
sub_process8 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
sub_process9 = OperatorPOWL(operator=Operator.XOR, children=[data_logging, skip])
sub_process10 = OperatorPOWL(operator=Operator.XOR, children=[packaging, skip])
sub_process11 = OperatorPOWL(operator=Operator.XOR, children=[waste_sort, skip])
sub_process12 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
sub_process13 = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip])

# Define the main process
root = StrictPartialOrder(nodes=[
    sub_process1, sub_process2, sub_process3, sub_process4, sub_process5, sub_process6, sub_process7, sub_process8, sub_process9, sub_process10, sub_process11, sub_process12, sub_process13
])

# Define dependencies
root.order.add_edge(sub_process1, sub_process2)
root.order.add_edge(sub_process2, sub_process3)
root.order.add_edge(sub_process3, sub_process4)
root.order.add_edge(sub_process4, sub_process5)
root.order.add_edge(sub_process5, sub_process6)
root.order.add_edge(sub_process6, sub_process7)
root.order.add_edge(sub_process7, sub_process8)
root.order.add_edge(sub_process8, sub_process9)
root.order.add_edge(sub_process9, sub_process10)
root.order.add_edge(sub_process10, sub_process11)
root.order.add_edge(sub_process11, sub_process12)
root.order.add_edge(sub_process12, sub_process13)