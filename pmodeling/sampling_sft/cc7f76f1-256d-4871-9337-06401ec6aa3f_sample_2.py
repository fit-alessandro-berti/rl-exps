import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intel_gathering = Transition(label='Intel Gathering')
risk_assess = Transition(label='Risk Assess')
behavior_scan = Transition(label='Behavior Scan')
network_monitor = Transition(label='Network Monitor')
audit_conduct = Transition(label='Audit Conduct')
flag_suspicion = Transition(label='Flag Suspicion')
legal_review = Transition(label='Legal Review')
compliance_check = Transition(label='Compliance Check')
employee_train = Transition(label='Employee Train')
threat_simulate = Transition(label='Threat Simulate')
incident_plan = Transition(label='Incident Plan')
response_drill = Transition(label='Response Drill')
data_encrypt = Transition(label='Data Encrypt')
partner_liaison = Transition(label='Partner Liaison')
report_generate = Transition(label='Report Generate')
feedback_loop = Transition(label='Feedback Loop')

# Build the monitoring and incident response sub‐process as a partial order
monitoring_po = StrictPartialOrder(
    nodes=[behavior_scan, network_monitor, audit_conduct, flag_suspicion]
)
monitoring_po.order.add_edge(behavior_scan, audit_conduct)
monitoring_po.order.add_edge(network_monitor, audit_conduct)
monitoring_po.order.add_edge(audit_conduct, flag_suspicion)

incident_response_po = StrictPartialOrder(
    nodes=[incident_plan, response_drill, data_encrypt, partner_liaison]
)
incident_response_po.order.add_edge(incident_plan, response_drill)
incident_response_po.order.add_edge(response_drill, data_encrypt)
incident_response_po.order.add_edge(data_encrypt, partner_liaison)

# Build the overall process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        intel_gathering,
        risk_assess,
        threat_simulate,
        monitoring_po,
        incident_response_po,
        legal_review,
        compliance_check,
        employee_train,
        feedback_loop,
        report_generate
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(intel_gathering, risk_assess)
root.order.add_edge(risk_assess, threat_simulate)
root.order.add_edge(threat_simulate, monitoring_po)
root.order.add_edge(monitoring_po, incident_response_po)
root.order.add_edge(incident_response_po, legal_review)
root.order.add_edge(incident_response_po, compliance_check)
root.order.add_edge(incident_response_po, employee_train)
root.order.add_edge(incident_response_po, feedback_loop)
root.order.add_edge(incident_response_po, report_generate)