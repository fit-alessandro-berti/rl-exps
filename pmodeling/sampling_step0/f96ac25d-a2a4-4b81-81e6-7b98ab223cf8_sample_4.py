import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Client Brief', 'Concept Sketch', 'Design Review', 'Material Sourcing', 'Prototype Build', 'Vendor Coordination', 'Quality Check', 'Client Approval', 'Packaging Prep', 'Shipping Arrange', 'Feedback Collect', 'Portfolio Update', 'Contract Sign', 'IP Management', 'Future Schedule', 'Maintenance Plan']
transitions = {act: Transition(label=act) for act in activities}
skip = SilentTransition()

# Define the process
client_brief = transitions['Client Brief']
concept_sketch = transitions['Concept Sketch']
design_review = transitions['Design Review']
material_sourcing = transitions['Material Sourcing']
prototype_build = transitions['Prototype Build']
vendor_coordination = transitions['Vendor Coordination']
quality_check = transitions['Quality Check']
client_approval = transitions['Client Approval']
packaging_prep = transitions['Packaging Prep']
shipping_arrange = transitions['Shipping Arrange']
feedback_collect = transitions['Feedback Collect']
portfolio_update = transitions['Portfolio Update']
contract_sign = transitions['Contract Sign']
ip_management = transitions['IP Management']
future_schedule = transitions['Future Schedule']
maintenance_plan = transitions['Maintenance Plan']

# Define the loop for the main process
main_process = OperatorPOWL(operator=Operator.LOOP, children=[
    client_brief,
    concept_sketch,
    design_review,
    material_sourcing,
    prototype_build,
    vendor_coordination,
    quality_check,
    client_approval,
    packaging_prep,
    shipping_arrange
])

# Define the choices for post-delivery
post_delivery = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[
        feedback_collect,
        portfolio_update,
        contract_sign,
        ip_management
    ]),
    OperatorPOWL(operator=Operator.LOOP, children=[
        future_schedule,
        maintenance_plan
    ])
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[main_process, post_delivery])
root.order.add_edge(main_process, post_delivery)

# Print the root POWL model
print(root)