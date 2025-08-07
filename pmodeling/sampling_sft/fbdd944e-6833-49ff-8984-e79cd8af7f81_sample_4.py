import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_clientOnboard   = Transition(label='Client Onboard')
t_needsAssess     = Transition(label='Needs Assess')
t_droneConfig     = Transition(label='Drone Config')
t_routeProgram    = Transition(label='Route Program')
t_complianceCheck = Transition(label='Compliance Check')
t_insuranceVerify = Transition(label='Insurance Verify')
t_leaseContract   = Transition(label='Lease Contract')
t_fleetDeploy     = Transition(label='Fleet Deploy')
t_monitorSetup    = Transition(label='Monitor Setup')
t_usageTrack      = Transition(label='Usage Track')
t_maintenancePlan = Transition(label='Maintenance Plan')
t_incidentManage  = Transition(label='Incident Manage')
t_billingProcess  = Transition(label='Billing Process')
t_performanceRep  = Transition(label='Performance Report')
t_contractRenew   = Transition(label='Contract Renew')
t_priceAdjust     = Transition(label='Price Adjust')
t_feedbackCollect = Transition(label='Feedback Collect')

# Loop for dynamic pricing adjustment: do Price Adjust, then optionally repeat
loop_price = OperatorPOWL(operator=Operator.LOOP, children=[t_priceAdjust, t_priceAdjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t_clientOnboard, t_needsAssess,
    t_droneConfig, t_routeProgram,
    t_complianceCheck, t_insuranceVerify,
    t_leaseContract, t_fleetDeploy,
    t_monitorSetup, t_usageTrack,
    t_maintenancePlan, t_incidentManage,
    t_billingProcess, t_performanceRep,
    t_contractRenew, t_feedbackCollect,
    loop_price
])

# Define the control-flow dependencies
root.order.add_edge(t_clientOnboard,     t_needsAssess)
root.order.add_edge(t_needsAssess,       t_droneConfig)
root.order.add_edge(t_needsAssess,       t_routeProgram)
root.order.add_edge(t_droneConfig,       t_complianceCheck)
root.order.add_edge(t_routeProgram,      t_complianceCheck)
root.order.add_edge(t_complianceCheck,   t_insuranceVerify)
root.order.add_edge(t_insuranceVerify,   t_leaseContract)
root.order.add_edge(t_leaseContract,     t_fleetDeploy)
root.order.add_edge(t_fleetDeploy,       t_monitorSetup)
root.order.add_edge(t_fleetDeploy,       t_usageTrack)
root.order.add_edge(t_monitorSetup,      t_maintenancePlan)
root.order.add_edge(t_usageTrack,        t_maintenancePlan)
root.order.add_edge(t_maintenancePlan,   t_incidentManage)
root.order.add_edge(t_incidentManage,    t_billingProcess)
root.order.add_edge(t_billingProcess,    t_performanceRep)
root.order.add_edge(t_performanceRep,    t_contractRenew)
root.order.add_edge(t_contractRenew,     t_feedbackCollect)
root.order.add_edge(t_contractRenew,     loop_price)