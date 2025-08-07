import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
receive = Transition(label='Receive Artifact')
condition = Transition(label='Condition Log')
radiocarbon = Transition(label='Radiocarbon Test')
spectroscopy = Transition(label='Spectroscopy Scan')
expert = Transition(label='Expert Consult')
provenance = Transition(label='Provenance Check')
archive = Transition(label='Archive Search')
risk = Transition(label='Risk Assess')
three_d = Transition(label='3D Scan')
legal = Transition(label='Legal Review')
insurance = Transition(label='Insurance Setup')
certificate = Transition(label='Certificate Draft')
approve = Transition(label='Certificate Approve')
climate = Transition(label='Climate Pack')
conservation = Transition(label='Conservation Plan')
monitoring = Transition(label='Monitoring Schedule')

# Build the analysis and provenance sub‐workflow
analysis = StrictPartialOrder(nodes=[
    radiocarbon, spectroscopy, expert, provenance, archive, risk
])
analysis.order.add_edge(radiocarbon, expert)
analysis.order.add_edge(spectroscopy, expert)
analysis.order.add_edge(expert, provenance)
analysis.order.add_edge(provenance, archive)
analysis.order.add_edge(provenance, risk)

# Build the compliance and insurance sub‐workflow
compliance = StrictPartialOrder(nodes=[
    legal, insurance
])
compliance.order.add_edge(legal, insurance)

# Build the certificate and packaging sub‐workflow
cert_pack = StrictPartialOrder(nodes=[
    certificate, approve, climate, conservation, monitoring
])
cert_pack.order.add_edge(certificate, approve)
cert_pack.order.add_edge(approve, climate)
cert_pack.order.add_edge(climate, conservation)
cert_pack.order.add_edge(conservation, monitoring)

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    receive, condition, analysis, compliance, cert_pack
])
root.order.add_edge(receive, condition)
root.order.add_edge(condition, analysis)
root.order.add_edge(condition, compliance)
root.order.add_edge(analysis, cert_pack)
root.order.add_edge(compliance, cert_pack)