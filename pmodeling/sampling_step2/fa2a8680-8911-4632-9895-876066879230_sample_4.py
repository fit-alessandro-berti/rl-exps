import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
client_meet = Transition(label='Client Meet')
req_gather = Transition(label='Requirement Gather')
module_design = Transition(label='Module Design')
supp_vet = Transition(label='Supplier Vetting')
comp_order = Transition(label='Component Order')
proto_build = Transition(label='Prototype Build')
field_test = Transition(label='Field Testing')
test_analysis = Transition(label='Test Analysis')
sw_setup = Transition(label='Software Setup')
data_int = Transition(label='Data Integration')
pilot_train = Transition(label='Pilot Train')
compliance_check = Transition(label='Compliance Check')
fleet_deploy = Transition(label='Fleet Deploy')
remote_monitor = Transition(label='Remote Monitor')
maint_plan = Transition(label='Maintenance Plan')
perf_tune = Transition(label='Performance Tune')

# Define partial order
root = StrictPartialOrder(nodes=[client_meet, req_gather, module_design, supp_vet, comp_order, proto_build, field_test, test_analysis, sw_setup, data_int, pilot_train, compliance_check, fleet_deploy, remote_monitor, maint_plan, perf_tune])

# Define order dependencies
root.order.add_edge(client_meet, req_gather)
root.order.add_edge(req_gather, module_design)
root.order.add_edge(module_design, supp_vet)
root.order.add_edge(supp_vet, comp_order)
root.order.add_edge(comp_order, proto_build)
root.order.add_edge(proto_build, field_test)
root.order.add_edge(field_test, test_analysis)
root.order.add_edge(test_analysis, sw_setup)
root.order.add_edge(sw_setup, data_int)
root.order.add_edge(data_int, pilot_train)
root.order.add_edge(pilot_train, compliance_check)
root.order.add_edge(compliance_check, fleet_deploy)
root.order.add_edge(fleet_deploy, remote_monitor)
root.order.add_edge(remote_monitor, maint_plan)
root.order.add_edge(maint_plan, perf_tune)

# Print the root model
print(root)