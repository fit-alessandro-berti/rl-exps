import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
stylistic_review = Transition(label='Stylistic Review')
expert_panel = Transition(label='Expert Panel')
legal_clearance = Transition(label='Legal Clearance')
ethics_audit = Transition(label='Ethics Audit')
insurance_quote = Transition(label='Insurance Quote')
risk_assess = Transition(label='Risk Assess')
digital_archive = Transition(label='Digital Archive')
replica_build = Transition(label='Replica Build')
transport_prep = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog_entry = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition_report = Transition(label='Condition Report')

# Define the silent transitions (if any)
skip = SilentTransition()

# Define the loop and choice nodes
# Loop for the initial provenance research and material analysis
loop_provenance_material = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_testing])
# Choice for expert panel and legal clearance
choice_expert_clearance = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, legal_clearance])
# Choice for insurance quote and ethics audit
choice_insurance_ethics = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, ethics_audit])
# Choice for risk assess and digital archive
choice_risk_archive = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, digital_archive])
# Choice for replica build and transport prep
choice_replica_transport = OperatorPOWL(operator=Operator.XOR, children=[replica_build, transport_prep])
# Choice for final review and catalog entry
choice_final_catalog = OperatorPOWL(operator=Operator.XOR, children=[final_review, catalog_entry])
# Choice for public notice and condition report
choice_public_condition = OperatorPOWL(operator=Operator.XOR, children=[public_notice, condition_report])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_provenance_material, choice_expert_clearance, choice_insurance_ethics, choice_risk_archive, choice_replica_transport, choice_final_catalog, choice_public_condition])
root.order.add_edge(loop_provenance_material, choice_expert_clearance)
root.order.add_edge(loop_provenance_material, choice_insurance_ethics)
root.order.add_edge(choice_expert_clearance, choice_risk_archive)
root.order.add_edge(choice_expert_clearance, choice_replica_transport)
root.order.add_edge(choice_insurance_ethics, choice_risk_archive)
root.order.add_edge(choice_insurance_ethics, choice_replica_transport)
root.order.add_edge(choice_risk_archive, choice_final_catalog)
root.order.add_edge(choice_replica_transport, choice_final_catalog)
root.order.add_edge(choice_final_catalog, choice_public_condition)
root.order.add_edge(choice_public_condition, final_review)
root.order.add_edge(choice_public_condition, catalog_entry)
root.order.add_edge(final_review, condition_report)
root.order.add_edge(catalog_entry, public_notice)
root.order.add_edge(condition_report, public_notice)