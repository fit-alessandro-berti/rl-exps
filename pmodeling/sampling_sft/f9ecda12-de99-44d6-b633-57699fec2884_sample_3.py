import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
concept_approve = Transition(label='Concept Approve')
budget_align   = Transition(label='Budget Align')
design_review  = Transition(label='Design Review')
structure_sim  = Transition(label='Structure Simulate')
material_proc  = Transition(label='Material Procure')
vendor_select  = Transition(label='Vendor Select')
permit_apply   = Transition(label='Permit Apply')
safety_check   = Transition(label='Safety Check')
site_prep      = Transition(label='Site Prep')
logistics_plan = Transition(label='Logistics Plan')
fabricate      = Transition(label='Fabricate Parts')
assemble       = Transition(label='Assemble Onsite')
quality_inspect= Transition(label='Quality Inspect')
weather_monitor= Transition(label='Weather Monitor')
public_unveil  = Transition(label='Public Unveil')
maintenance_plan= Transition(label='Maintenance Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')

# Loop for iterative design reviews
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_review, structure_sim])

# Build the partial order
root = StrictPartialOrder(nodes=[
    concept_approve,
    budget_align,
    loop_design,
    material_proc,
    vendor_select,
    permit_apply,
    safety_check,
    site_prep,
    logistics_plan,
    fabricate,
    assemble,
    quality_inspect,
    weather_monitor,
    public_unveil,
    maintenance_plan,
    stakeholder_meet
])

# Sequence: Concept Approve -> Budget Align
root.order.add_edge(concept_approve, budget_align)

# Sequence: Budget Align -> Design Review
root.order.add_edge(budget_align, loop_design)

# Loop: Design Review -> Structure Simulate
root.order.add_edge(loop_design, structure_sim)

# Parallel: Material Procure -> Vendor Select
root.order.add_edge(material_proc, vendor_select)

# Parallel: Permit Apply -> Safety Check
root.order.add_edge(permit_apply, safety_check)

# Parallel: Site Prep -> Logistics Plan
root.order.add_edge(site_prep, logistics_plan)

# Parallel: Fabricate Parts -> Assemble Onsite
root.order.add_edge(fabricate, assemble)

# Concurrency: Quality Inspect -> Weather Monitor
root.order.add_edge(quality_inspect, weather_monitor)

# Sequence: Quality Inspect -> Public Unveil
root.order.add_edge(quality_inspect, public_unveil)

# Sequence: Weather Monitor -> Public Unveil
root.order.add_edge(weather_monitor, public_unveil)

# Sequence: Public Unveil -> Maintenance Plan
root.order.add_edge(public_unveil, maintenance_plan)

# Sequence: Maintenance Plan -> Stakeholder Meet
root.order.add_edge(maintenance_plan, stakeholder_meet)