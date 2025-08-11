import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
preflight_check = Transition(label='Preflight Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
battery_test = Transition(label='Battery Test')
route_update = Transition(label='Route Update')
firmware_patch = Transition(label='Firmware Patch')
flight_launch = Transition(label='Flight Launch')
telemetry_monitor = Transition(label='Telemetry Monitor')
anomaly_detect = Transition(label='Anomaly Detect')
collision_assess = Transition(label='Collision Assess')
data_upload = Transition(label='Data Upload')
postflight_review = Transition(label='Postflight Review')
battery_optimize = Transition(label='Battery Optimize')
damage_repair = Transition(label='Damage Repair')
compliance_report = Transition(label='Compliance Report')
performance_log = Transition(label='Performance Log')
mission_debrief = Transition(label='Mission Debrief')

# Define silent transitions for empty labels
skip = SilentTransition()

# Define loops for Battery Optimize and Performance Log
battery_optimize_loop = OperatorPOWL(operator=Operator.LOOP, children=[battery_test, telemetry_monitor, anomaly_detect, collision_assess, data_upload, postflight_review, battery_optimize, damage_repair, compliance_report, performance_log])
performance_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[mission_debrief])

# Define XOR for preflight check and sensor calibrate
preflight_check_sensor_calibrate = OperatorPOWL(operator=Operator.XOR, children=[preflight_check, sensor_calibrate])

# Define XOR for flight launch and telemetry monitor
flight_launch_telemetry_monitor = OperatorPOWL(operator=Operator.XOR, children=[flight_launch, telemetry_monitor])

# Define XOR for battery test and battery optimize
battery_test_battery_optimize = OperatorPOWL(operator=Operator.XOR, children=[battery_test, battery_optimize_loop])

# Define XOR for anomaly detect and performance log
anomaly_detect_performance_log = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, performance_log_loop])

# Define XOR for collision assess and mission debrief
collision_assess_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[collision_assess, mission_debrief])

# Define XOR for data upload and compliance report
data_upload_compliance_report = OperatorPOWL(operator=Operator.XOR, children=[data_upload, compliance_report])

# Define XOR for postflight review and damage repair
postflight_review_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[postflight_review, damage_repair])

# Define XOR for firmware patch and route update
firmware_patch_route_update = OperatorPOWL(operator=Operator.XOR, children=[firmware_patch, route_update])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator=Operator.XOR, children=[mission_debrief, damage_repair])

# Define XOR for battery optimize and performance log
battery_optimize_performance_log = OperatorPOWL(operator=Operator.XOR, children=[battery_optimize_loop, performance_log_loop])

# Define XOR for performance log and mission debrief
performance_log_mission_debrief = OperatorPOWL(operator=Operator.XOR, children=[performance_log_loop, mission_debrief])

# Define XOR for mission debrief and damage repair
mission_debrief_damage_repair = OperatorPOWL(operator