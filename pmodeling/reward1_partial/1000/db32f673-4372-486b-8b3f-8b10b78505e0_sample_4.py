import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
receive_artifact = Transition(label='Receive Artifact')
condition_log = Transition(label='Condition Log')
radiocarbon_test = Transition(label='Radiocarbon Test')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
risk_assess = Transition(label='Risk Assess')
three_d_scan = Transition(label='3D Scan')
legal_review = Transition(label='Legal Review')
insurance_setup = Transition(label='Insurance Setup')
certificate_draft = Transition(label='Certificate Draft')
certificate_approve = Transition(label='Certificate Approve')
climate_pack = Transition(label='Climate Pack')
conservation_plan = Transition(label='Conservation Plan')
monitoring_schedule = Transition(label='Monitoring Schedule')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, archive_search])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, insurance_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certificate_draft, certificate_approve])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[climate_pack, conservation_plan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[monitoring_schedule, None])

# Define the POWL root
root = StrictPartialOrder(nodes=[receive_artifact, condition_log, radiocarbon_test, spectroscopy_scan, xor, risk_assess, three_d_scan, xor2, xor3, xor4, xor5])
root.order.add_edge(receive_artifact, condition_log)
root.order.add_edge(condition_log, radiocarbon_test)
root.order.add_edge(radiocarbon_test, spectroscopy_scan)
root.order.add_edge(spectroscopy_scan, xor)
root.order.add_edge(xor, risk_assess)
root.order.add_edge(risk_assess, three_d_scan)
root.order.add_edge(three_d_scan, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, None)