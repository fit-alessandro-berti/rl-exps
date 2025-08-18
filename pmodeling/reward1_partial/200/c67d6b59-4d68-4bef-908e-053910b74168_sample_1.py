import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
client_meet = Transition(label='Client Meet')
design_draft = Transition(label='Design Draft')
vendor_select = Transition(label='Vendor Select')
component_order = Transition(label='Component Order')
parts_inspect = Transition(label='Parts Inspect')
frame_build = Transition(label='Frame Build')
wiring_setup = Transition(label='Wiring Setup')
software_load = Transition(label='Software Load')
flight_sim = Transition(label='Flight Sim')
quality_test = Transition(label='Quality Test')
feedback_review = Transition(label='Feedback Review')
adjust_design = Transition(label='Adjust Design')
compliance_check = Transition(label='Compliance Check')
packaging_prep = Transition(label='Packaging Prep')
final_demo = Transition(label='Final Demo')
ship_drone = Transition(label='Ship Drone')

# Define the silent transitions for the process
skip = SilentTransition()

# Define the process tree for the design, assembly, and delivery stages
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_draft, vendor_select, component_order, parts_inspect, frame_build, wiring_setup, software_load, flight_sim, quality_test, feedback_review, adjust_design, compliance_check, packaging_prep, final_demo, ship_drone])

# Define the root node of the process
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, final_demo)

# Print the root node
print(root)