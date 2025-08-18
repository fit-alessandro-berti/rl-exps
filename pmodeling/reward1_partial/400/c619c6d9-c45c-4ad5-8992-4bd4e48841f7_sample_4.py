import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
design_consult = Transition(label='Design Consult')
component_sourcing = Transition(label='Component Sourcing')
sensor_calibrate = Transition(label='Sensor Calibrate')
firmware_integrate = Transition(label='Firmware Integrate')
payload_configure = Transition(label='Payload Configure')
assembly_setup = Transition(label='Assembly Setup')
wiring_connect = Transition(label='Wiring Connect')
chassis_build = Transition(label='Chassis Build')
software_load = Transition(label='Software Load')
flight_testing = Transition(label='Flight Testing')
data_analyze = Transition(label='Data Analyze')
regulation_check = Transition(label='Regulation Check')
quality_inspect = Transition(label='Quality Inspect')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_review = Transition(label='Client Review')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        design_consult,
        component_sourcing,
        sensor_calibrate,
        firmware_integrate,
        payload_configure,
        assembly_setup,
        wiring_connect,
        chassis_build,
        software_load,
        flight_testing,
        data_analyze,
        regulation_check,
        quality_inspect,
        packaging_prep,
        logistics_plan,
        client_review
    ],
    order={
        (design_consult, component_sourcing),
        (design_consult, sensor_calibrate),
        (design_consult, firmware_integrate),
        (design_consult, payload_configure),
        (design_consult, assembly_setup),
        (design_consult, wiring_connect),
        (design_consult, chassis_build),
        (design_consult, software_load),
        (design_consult, flight_testing),
        (design_consult, data_analyze),
        (design_consult, regulation_check),
        (design_consult, quality_inspect),
        (design_consult, packaging_prep),
        (design_consult, logistics_plan),
        (design_consult, client_review),
        (component_sourcing, sensor_calibrate),
        (component_sourcing, firmware_integrate),
        (component_sourcing, payload_configure),
        (component_sourcing, assembly_setup),
        (component_sourcing, wiring_connect),
        (component_sourcing, chassis_build),
        (component_sourcing, software_load),
        (component_sourcing, flight_testing),
        (component_sourcing, data_analyze),
        (component_sourcing, regulation_check),
        (component_sourcing, quality_inspect),
        (component_sourcing, packaging_prep),
        (component_sourcing, logistics_plan),
        (component_sourcing, client_review),
        (sensor_calibrate, firmware_integrate),
        (sensor_calibrate, payload_configure),
        (sensor_calibrate, assembly_setup),
        (sensor_calibrate, wiring_connect),
        (sensor_calibrate, chassis_build),
        (sensor_calibrate, software_load),
        (sensor_calibrate, flight_testing),
        (sensor_calibrate, data_analyze),
        (sensor_calibrate, regulation_check),
        (sensor_calibrate, quality_inspect),
        (sensor_calibrate, packaging_prep),
        (sensor_calibrate, logistics_plan),
        (sensor_calibrate, client_review),
        (firmware_integrate, payload_configure),
        (firmware_integrate, assembly_setup),
        (firmware_integrate, wiring_connect),
        (firmware_integrate, chassis_build),
        (firmware_integrate, software_load),
        (firmware_integrate, flight_testing),
        (firmware_integrate, data_analyze),
        (firmware_integrate, regulation_check),
        (firmware_integrate, quality_inspect),
        (firmware_integrate, packaging_prep),
        (firmware_integrate, logistics_plan),
        (firmware_integrate, client_review),
        (payload_configure, assembly_setup),
        (payload_configure, wiring_connect),
        (payload_configure, chassis_build),
        (payload_configure, software_load),
        (payload_configure, flight_testing),
        (payload_configure, data_analyze),
        (payload_configure, regulation_check),
        (payload_configure, quality_inspect),
        (payload_configure, packaging_prep),
        (payload_configure, logistics_plan),
        (payload_configure, client_review),
        (assembly_setup, wiring_connect),
        (assembly_setup, chassis_build),
        (assembly_setup, software_load),
        (assembly_setup, flight_testing),
        (assembly_setup, data_analyze),
        (assembly_setup, regulation_check),
        (assembly_setup, quality_inspect),
        (assembly_setup, packaging_prep),
        (assembly_setup, logistics_plan),
        (assembly_setup, client_review),
        (wiring_connect, chassis_build),
        (wiring_connect, software_load),
        (wiring_connect, flight_testing),
        (wiring_connect, data_analyze),
        (wiring_connect, regulation_check),
        (wiring_connect, quality_inspect),
        (wiring_connect, packaging_prep),
        (wiring_connect, logistics_plan),
        (wiring_connect, client_review),
        (chassis_build, software_load),
        (chassis_build, flight_testing),
        (chassis_build, data_analyze),
        (chassis_build, regulation_check),
        (chassis_build, quality_inspect),
        (chassis_build, packaging_prep),
        (chassis_build, logistics_plan),
        (chassis_build, client_review),
        (software_load, flight_testing),
        (software_load, data_analyze),
        (software_load, regulation_check),
        (software_load, quality_inspect),
        (software_load, packaging_prep),
        (software_load, logistics_plan),
        (software_load, client_review),
        (flight_testing, data_analyze),
        (flight_testing, regulation_check),
        (flight_testing, quality_inspect),
        (flight_testing, packaging_prep),
        (flight_testing, logistics_plan),
        (flight_testing, client_review),
        (data_analyze, regulation_check),
        (data_analyze, quality_inspect),
        (data_analyze, packaging_prep),
        (data_analyze, logistics_plan),
        (data_analyze, client_review),
        (regulation_check, quality_inspect),
        (regulation_check, packaging_prep),
        (regulation_check, logistics_plan),
        (regulation_check, client_review),
        (quality_inspect, packaging_prep),
        (quality_inspect, logistics_plan),
        (quality_inspect, client_review),
        (packaging_prep, logistics_plan),
        (packaging_prep, client_review),
        (logistics_plan, client_review)
    }
)

# Print the POWL model
print(root)