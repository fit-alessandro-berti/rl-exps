from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

artifact_research = Transition(label='Artifact Research')
ownership_verify = Transition(label='Ownership Verify')
stakeholder_meet = Transition(label='Stakeholder Meet')
legal_review = Transition(label='Legal Review')
diplomatic_contact = Transition(label='Diplomatic Contact')
condition_report = Transition(label='Condition Report')
transport_plan = Transition(label='Transport Plan')
insurance_setup = Transition(label='Insurance Setup')
customs_clear = Transition(label='Customs Clear')
secure_packaging = Transition(label='Secure Packaging')
shipping_monitor = Transition(label='Shipping Monitor')
community_brief = Transition(label='Community Brief')
arrival_inspect = Transition(label='Arrival Inspect')
exhibit_prepare = Transition(label='Exhibit Prepare')
public_release = Transition(label='Public Release')

skip = SilentTransition()

artifact_research_xor = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, stakeholder_meet])
legal_review_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_report, diplomatic_contact])
insurance_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, insurance_setup])
customs_clear_xor = OperatorPOWL(operator=Operator.XOR, children=[secure_packaging, shipping_monitor])
community_brief_xor = OperatorPOWL(operator=Operator.XOR, children=[arrival_inspect, exhibit_prepare])
public_release_xor = OperatorPOWL(operator=Operator.XOR, children=[public_release])

root = StrictPartialOrder(nodes=[
    artifact_research,
    artifact_research_xor,
    legal_review_xor,
    insurance_setup_xor,
    customs_clear_xor,
    community_brief_xor,
    public_release_xor
])

root.order.add_edge(artifact_research, artifact_research_xor)
root.order.add_edge(artifact_research_xor, legal_review_xor)
root.order.add_edge(legal_review_xor, insurance_setup_xor)
root.order.add_edge(insurance_setup_xor, customs_clear_xor)
root.order.add_edge(customs_clear_xor, community_brief_xor)
root.order.add_edge(community_brief_xor, public_release_xor)