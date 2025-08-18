from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
client_brief = Transition(label='Client Brief')
concept_sketch = Transition(label='Concept Sketch')
design_review = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
prototype_build = Transition(label='Prototype Build')
vendor_coordination = Transition(label='Vendor Coordination')
quality_check = Transition(label='Quality Check')
client_approval = Transition(label='Client Approval')
packaging_prep = Transition(label='Packaging Prep')
shipping_arrange = Transition(label='Shipping Arrange')
feedback_collect = Transition(label='Feedback Collect')
portfolio_update = Transition(label='Portfolio Update')
contract_sign = Transition(label='Contract Sign')
ip_management = Transition(label='IP Management')
future_schedule = Transition(label='Future Schedule')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        client_brief,
        concept_sketch,
        design_review,
        material_sourcing,
        prototype_build,
        vendor_coordination,
        quality_check,
        client_approval,
        packaging_prep,
        shipping_arrange,
        feedback_collect,
        portfolio_update,
        contract_sign,
        ip_management,
        future_schedule,
        maintenance_plan
    ],
    order=[
        (client_brief, concept_sketch),
        (concept_sketch, design_review),
        (design_review, material_sourcing),
        (material_sourcing, prototype_build),
        (prototype_build, vendor_coordination),
        (vendor_coordination, quality_check),
        (quality_check, client_approval),
        (client_approval, packaging_prep),
        (packaging_prep, shipping_arrange),
        (shipping_arrange, feedback_collect),
        (feedback_collect, portfolio_update),
        (portfolio_update, contract_sign),
        (contract_sign, ip_management),
        (ip_management, future_schedule),
        (future_schedule, maintenance_plan)
    ]
)

# Print the root
print(root)