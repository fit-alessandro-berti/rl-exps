import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
receive = Transition(label='Receive Artifact')
condition_log = Transition(label='Condition Log')
radiocarbon = Transition(label='Radiocarbon Test')
spectroscopy = Transition(label='Spectroscopy Scan')
expert_consult = Transition(label='Expert Consult')
provenance = Transition(label='Provenance Check')
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

# Build the analysis branch: Radiocarbon -> Spectroscopy -> Expert Consult -> Provenance Check -> Archive Search -> Risk Assess
analysis_branch = StrictPartialOrder(nodes=[
    radiocarbon, spectroscopy, expert_consult, provenance, archive_search, risk_assess
])
analysis_branch.order.add_edge(radiocarbon, spectroscopy)
analysis_branch.order.add_edge(spectroscopy, expert_consult)
analysis_branch.order.add_edge(expert_consult, provenance)
analysis_branch.order.add_edge(provenance, archive_search)
analysis_branch.order.add_edge(archive_search, risk_assess)

# Build the certificate issuance branch: Legal Review -> Insurance Setup -> Certificate Draft -> Certificate Approve
cert_branch = StrictPartialOrder(nodes=[
    legal_review, insurance_setup, certificate_draft, certificate_approve
])
cert_branch.order.add_edge(legal_review, insurance_setup)
cert_branch.order.add_edge(insurance_setup, certificate_draft)
cert_branch.order.add_edge(certificate_draft, certificate_approve)

# Build the packaging and monitoring branch: Climate Pack -> Conservation Plan -> Monitoring Schedule
pack_branch = StrictPartialOrder(nodes=[
    climate_pack, conservation_plan, monitoring_schedule
])
pack_branch.order.add_edge(climate_pack, conservation_plan)
pack_branch.order.add_edge(conservation_plan, monitoring_schedule)

# Assemble the overall workflow: Receive -> Condition Log -> Analysis -> Cert Issuance -> Pack
root = StrictPartialOrder(nodes=[
    receive, condition_log, analysis_branch, cert_branch, pack_branch
])
root.order.add_edge(receive, condition_log)
root.order.add_edge(condition_log, analysis_branch)
root.order.add_edge(condition_log, cert_branch)
root.order.add_edge(analysis_branch, cert_branch)
root.order.add_edge(cert_branch, pack_branch)
root.order.add_edge(cert_branch, monitoring_schedule)