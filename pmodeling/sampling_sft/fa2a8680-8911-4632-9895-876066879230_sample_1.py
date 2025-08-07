import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
client_meet     = Transition(label='Client Meet')
requirement_g   = Transition(label='Requirement Gather')
module_design   = Transition(label='Module Design')
supplier_vet    = Transition(label='Supplier Vetting')
component_order = Transition(label='Component Order')
prototype_build = Transition(label='Prototype Build')
field_testing   = Transition(label='Field Testing')
test_analysis   = Transition(label='Test Analysis')
software_setup  = Transition(label='Software Setup')
data_integration= Transition(label='Data Integration')
pilot_train     = Transition(label='Pilot Train')
compliance_chk  = Transition(label='Compliance Check')
fleet_deploy    = Transition(label='Fleet Deploy')
remote_monitor  = Transition(label='Remote Monitor')
maintenance_pl  = Transition(label='Maintenance Plan')
performance_t   = Transition(label='Performance Tune')

# Define the maintenance loop: Maintenance Plan, then either exit or Performance Tune and back
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_pl, performance_t])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    client_meet,
    requirement_g,
    module_design,
    supplier_vet,
    component_order,
    prototype_build,
    field_testing,
    test_analysis,
    software_setup,
    data_integration,
    pilot_train,
    compliance_chk,
    fleet_deploy,
    remote_monitor,
    maintenance_loop
])

# Define the sequence and concurrent dependencies
root.order.add_edge(client_meet, requirement_g)
root.order.add_edge(requirement_g, module_design)
root.order.add_edge(module_design, supplier_vet)
root.order.add_edge(supplier_vet, component_order)
root.order.add_edge(component_order, prototype_build)
root.order.add_edge(prototype_build, field_testing)
root.order.add_edge(field_testing, test_analysis)
root.order.add_edge(test_analysis, software_setup)
root.order.add_edge(software_setup, data_integration)
root.order.add_edge(data_integration, pilot_train)
root.order.add_edge(pilot_train, compliance_chk)
root.order.add_edge(compliance_chk, fleet_deploy)
root.order.add_edge(fleet_deploy, remote_monitor)
root.order.add_edge(remote_monitor, maintenance_loop)