import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[receive_artifact, condition_log, radiocarbon_test, spectroscopy_scan, expert_consult, provenance_check, archive_search, risk_assess, three_d_scan, legal_review, insurance_setup, certificate_draft, certificate_approve, climate_pack, conservation_plan, monitoring_schedule])

# Define the order between transitions
root.order.add_edge(receive_artifact, condition_log)
root.order.add_edge(condition_log, radiocarbon_test)
root.order.add_edge(radiocarbon_test, spectroscopy_scan)
root.order.add_edge(spectroscopy_scan, expert_consult)
root.order.add_edge(expert_consult, provenance_check)
root.order.add_edge(provenance_check, archive_search)
root.order.add_edge(archive_search, risk_assess)
root.order.add_edge(risk_assess, three_d_scan)
root.order.add_edge(three_d_scan, legal_review)
root.order.add_edge(legal_review, insurance_setup)
root.order.add_edge(insurance_setup, certificate_draft)
root.order.add_edge(certificate_draft, certificate_approve)
root.order.add_edge(certificate_approve, climate_pack)
root.order.add_edge(climate_pack, conservation_plan)
root.order.add_edge(conservation_plan, monitoring_schedule)

print(root)