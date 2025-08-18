import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

artifact_research_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_research, ownership_verify, stakeholder_meet, legal_review, diplomatic_contact, condition_report, transport_plan, insurance_setup, customs_clear, secure_packaging, shipping_monitor, community_brief, arrival_inspect])
artifact_research_loop.order.add_edge(artifact_research, ownership_verify)
artifact_research_loop.order.add_edge(ownership_verify, stakeholder_meet)
artifact_research_loop.order.add_edge(stakeholder_meet, legal_review)
artifact_research_loop.order.add_edge(legal_review, diplomatic_contact)
artifact_research_loop.order.add_edge(diplomatic_contact, condition_report)
artifact_research_loop.order.add_edge(condition_report, transport_plan)
artifact_research_loop.order.add_edge(transport_plan, insurance_setup)
artifact_research_loop.order.add_edge(insurance_setup, customs_clear)
artifact_research_loop.order.add_edge(customs_clear, secure_packaging)
artifact_research_loop.order.add_edge(secure_packaging, shipping_monitor)
artifact_research_loop.order.add_edge(shipping_monitor, community_brief)
artifact_research_loop.order.add_edge(community_brief, arrival_inspect)

artifact_research_xor = OperatorPOWL(operator=Operator.XOR, children=[public_release, skip])
artifact_research_xor.order.add_edge(artifact_research_loop, public_release)

root = StrictPartialOrder(nodes=[artifact_research_loop, artifact_research_xor])