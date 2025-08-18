import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
legal_audit = Transition(label='Legal Audit')
condition_report = Transition(label='Condition Report')
carbon_dating = Transition(label='Carbon Dating')
ownership_verify = Transition(label='Ownership Verify')
historical_match = Transition(label='Historical Match')
customs_clearance = Transition(label='Customs Clearance')
risk_assessment = Transition(label='Risk Assessment')
ethics_approval = Transition(label='Ethics Approval')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
exhibit_prep = Transition(label='Exhibit Prep')

# Define a silent transition
skip = SilentTransition()

# Define loops and choices
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
loop_expert = OperatorPOWL(operator=Operator.LOOP, children=[expert_review])
loop_legal = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit])
loop_condition = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])
loop_carbon = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating])
loop_ownership = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify])
loop_historical = OperatorPOWL(operator=Operator.LOOP, children=[historical_match])
loop_customs = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance])
loop_risk = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment])
loop_ethics = OperatorPOWL(operator=Operator.LOOP, children=[ethics_approval])
loop_restoration = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])
loop_final = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])
loop_catalog = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry])
loop_exhibit = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_prep])

xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_scan, skip])
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_audit, skip])
xor_condition = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor_carbon = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
xor_ownership = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
xor_historical = OperatorPOWL(operator=Operator.XOR, children=[historical_match, skip])
xor_customs = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, skip])
xor_risk = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])
xor_ethics = OperatorPOWL(operator=Operator.XOR, children=[ethics_approval, skip])
xor_restoration = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])
xor_catalog = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, skip])
xor_exhibit = OperatorPOWL(operator=Operator.XOR, children=[exhibit_prep, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop_provenance, xor_provenance,
                                  loop_material, xor_material,
                                  loop_expert, xor_expert,
                                  loop_legal, xor_legal,
                                  loop_condition, xor_condition,
                                  loop_carbon, xor_carbon,
                                  loop_ownership, xor_ownership,
                                  loop_historical, xor_historical,
                                  loop_customs, xor_customs,
                                  loop_risk, xor_risk,
                                  loop_ethics, xor_ethics,
                                  loop_restoration, xor_restoration,
                                  loop_final, xor_final,
                                  loop_catalog, xor_catalog,
                                  loop_exhibit, xor_exhibit])

# Define dependencies
root.order.add_edge(loop_provenance, xor_provenance)
root.order.add_edge(loop_material, xor_material)
root.order.add_edge(loop_expert, xor_expert)
root.order.add_edge(loop_legal, xor_legal)
root.order.add_edge(loop_condition, xor_condition)
root.order.add_edge(loop_carbon, xor_carbon)
root.order.add_edge(loop_ownership, xor_ownership)
root.order.add_edge(loop_historical, xor_historical)
root.order.add_edge(loop_customs, xor_customs)
root.order.add_edge(loop_risk, xor_risk)
root.order.add_edge(loop_ethics, xor_ethics)
root.order.add_edge(loop_restoration, xor_restoration)
root.order.add_edge(loop_final, xor_final)
root.order.add_edge(loop_catalog, xor_catalog)
root.order.add_edge(loop_exhibit, xor_exhibit)

print(root)