import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

intake = Transition(label='Intake Review')
visual = Transition(label='Visual Inspect')
test = Transition(label='Material Test')
provenance = Transition(label='Provenance Check')
archive = Transition(label='Archival Search')
expert = Transition(label='Expert Consult')
digital = Transition(label='Digital Scan')
condition = Transition(label='Condition Report')
forgery = Transition(label='Forgery Assess')
legal = Transition(label='Legal Review')
risk = Transition(label='Risk Analysis')
vote = Transition(label='Acquisition Vote')
catalog = Transition(label='Catalog Entry')
storage = Transition(label='Storage Prep')
final = Transition(label='Final Approval')

skip = SilentTransition()

intake_to_test = OperatorPOWL(operator=Operator.XOR, children=[intake, test])
test_to_provenance = OperatorPOWL(operator=Operator.XOR, children=[test, provenance])
provenance_to_archive = OperatorPOWL(operator=Operator.XOR, children=[provenance, archive])
archive_to_expert = OperatorPOWL(operator=Operator.XOR, children=[archive, expert])
expert_to_digital = OperatorPOWL(operator=Operator.XOR, children=[expert, digital])
digital_to_condition = OperatorPOWL(operator=Operator.XOR, children=[digital, condition])
condition_to_forgery = OperatorPOWL(operator=Operator.XOR, children=[condition, forgery])
forgery_to_legal = OperatorPOWL(operator=Operator.XOR, children=[forgery, legal])
legal_to_risk = OperatorPOWL(operator=Operator.XOR, children=[legal, risk])
risk_to_vote = OperatorPOWL(operator=Operator.XOR, children=[risk, vote])
vote_to_catalog = OperatorPOWL(operator=Operator.XOR, children=[vote, catalog])
catalog_to_storage = OperatorPOWL(operator=Operator.XOR, children=[catalog, storage])
storage_to_final = OperatorPOWL(operator=Operator.XOR, children=[storage, final])

root = StrictPartialOrder(nodes=[
    intake_to_test,
    test_to_provenance,
    provenance_to_archive,
    archive_to_expert,
    expert_to_digital,
    digital_to_condition,
    condition_to_forgery,
    forgery_to_legal,
    legal_to_risk,
    risk_to_vote,
    vote_to_catalog,
    catalog_to_storage,
    storage_to_final
])

root.order.add_edge(intake_to_test, test_to_provenance)
root.order.add_edge(test_to_provenance, provenance_to_archive)
root.order.add_edge(provenance_to_archive, archive_to_expert)
root.order.add_edge(archive_to_expert, expert_to_digital)
root.order.add_edge(expert_to_digital, digital_to_condition)
root.order.add_edge(digital_to_condition, condition_to_forgery)
root.order.add_edge(condition_to_forgery, forgery_to_legal)
root.order.add_edge(forgery_to_legal, legal_to_risk)
root.order.add_edge(legal_to_risk, risk_to_vote)
root.order.add_edge(risk_to_vote, vote_to_catalog)
root.order.add_edge(vote_to_catalog, catalog_to_storage)
root.order.add_edge(catalog_to_storage, storage_to_final)