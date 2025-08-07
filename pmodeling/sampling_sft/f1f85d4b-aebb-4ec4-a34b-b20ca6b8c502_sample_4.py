import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
initial = Transition(label='Initial Review')
prov = Transition(label='Provenance Check')
material = Transition(label='Material Testing')
expert = Transition(label='Expert Survey')
digital = Transition(label='Digital Scan')
condition = Transition(label='Condition Report')
legal = Transition(label='Legal Review')
risk = Transition(label='Risk Analysis')
negotiation = Transition(label='Seller Negotiation')
doc = Transition(label='Documentation')
archive = Transition(label='Archival Entry')
committee = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')
acquisition_setup = Transition(label='Acquisition Setup')
exhibit_planning = Transition(label='Exhibit Planning')

# Define the loop for repeated expert survey and condition reporting
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert, condition]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial, prov, material, expert_loop, digital,
    legal, risk, negotiation, doc, archive,
    committee, final_approval, acquisition_setup, exhibit_planning
])

# Define the control-flow dependencies
root.order.add_edge(initial, prov)
root.order.add_edge(prov, material)
root.order.add_edge(material, expert_loop)
root.order.add_edge(expert_loop, digital)
root.order.add_edge(digital, legal)
root.order.add_edge(legal, risk)
root.order.add_edge(risk, negotiation)
root.order.add_edge(negotiation, doc)
root.order.add_edge(doc, archive)
root.order.add_edge(archive, committee)
root.order.add_edge(committee, final_approval)
root.order.add_edge(final_approval, acquisition_setup)
root.order.add_edge(acquisition_setup, exhibit_planning)