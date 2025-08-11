import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
provenance_check = Transition(label='Provenance Check')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
disassembly = Transition(label='Disassembly')
surface_clean = Transition(label='Surface Clean')
structural_repair = Transition(label='Structural Repair')
reconstruction = Transition(label='Reconstruction')
finish_match = Transition(label='Finish Match')
stabilize_parts = Transition(label='Stabilize Parts')
documentation = Transition(label='Documentation')
quality_audit = Transition(label='Quality Audit')
valuation = Transition(label='Valuation')
market_analysis = Transition(label='Market Analysis')
target_outreach = Transition(label='Target Outreach')
delivery_prep = Transition(label='Delivery Prep')
client_feedback = Transition(label='Client Feedback')

# Define the silent transitions
skip = SilentTransition()

# Define the loop for material test
loop_material_test = OperatorPOWL(operator=Operator.LOOP, children=[material_test, skip])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_outreach = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, target_outreach])

# Define the xor for delivery prep and client feedback
xor_delivery_prep_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[delivery_prep, client_feedback])

# Define the xor for valuation and client feedback
xor_valuation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[valuation, client_feedback])

# Define the xor for reconstruction and client feedback
xor_reconstruction_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[reconstruction, client_feedback])

# Define the xor for finish match and client feedback
xor_finish_match_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[finish_match, client_feedback])

# Define the xor for stabilization and client feedback
xor_stabilize_parts_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[stabilize_parts, client_feedback])

# Define the xor for documentation and client feedback
xor_documentation_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[documentation, client_feedback])

# Define the xor for quality audit and client feedback
xor_quality_audit_client_feedback = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, client_feedback])

# Define the xor for market analysis and target outreach
xor_market_analysis_target_out