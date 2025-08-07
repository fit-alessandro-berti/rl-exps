from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define each activity as a Transition object with the given label
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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    client_meet,
    design_draft,
    vendor_select,
    component_order,
    parts_inspect,
    frame_build,
    wiring_setup,
    software_load,
    flight_sim,
    quality_test,
    feedback_review,
    adjust_design,
    compliance_check,
    packaging_prep,
    final_demo,
    ship_drone
])