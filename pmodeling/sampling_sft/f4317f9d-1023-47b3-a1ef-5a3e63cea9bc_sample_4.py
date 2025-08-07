import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Scan')
style = Transition(label='Style Compare')
ai = Transition(label='AI Imaging')
chemical = Transition(label='Chemical Test')
aging = Transition(label='Aging Verify')
record_match = Transition(label='Record Match')
database = Transition(label='Database Query')
panel = Transition(label='Panel Review')
market = Transition(label='Market Value')
report = Transition(label='Report Draft')
certification = Transition(label='Certification')
approval = Transition(label='Approval Stage')
packing = Transition(label='Secure Packing')
transport = Transition(label='Transport Prep')

# Define the choice for forgery risk (either Forgery Risk or a silent skip)
skip = SilentTransition()
forgery_choice = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Forgery Risk'), skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    provenance, material, style, ai,
    chemical, aging,
    record_match, database,
    panel, market, forgery_choice,
    report, certification, approval,
    packing, transport
])

# Sequence of activities after provenance check
root.order.add_edge(provenance, material)
root.order.add_edge(provenance, style)
root.order.add_edge(material, ai)
root.order.add_edge(style, ai)
root.order.add_edge(ai, chemical)
root.order.add_edge(chemical, aging)
root.order.add_edge(aging, record_match)
root.order.add_edge(aging, database)
root.order.add_edge(record_match, panel)
root.order.add_edge(database, panel)
root.order.add_edge(panel, market)
root.order.add_edge(market, forgery_choice)

# Loop for risk assessment and market value update
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_choice, market])

# Final sequence including risk loop and report/draft
root.order.add_edge(risk_loop, report)
root.order.add_edge(risk_loop, certification)
root.order.add_edge(report, approval)
root.order.add_edge(certification, approval)
root.order.add_edge(approval, packing)
root.order.add_edge(packing, transport)