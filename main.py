import numpy as np

# EMRAX 228 Motor
motor_continuous_power = 109000  # Continuous power in Watts
motor_efficiency = 0.96  # Motor efficiency
motor_coolant_flow_rate = 7 / 60  # Coolant flow rate in kg/s (from 7 L/min)

# Rinehart PM100DZ Motor Controller
controller_continuous_power = 78200  # Assuming the controller's power is the same as motor's continuous power for this calculation
controller_efficiency = 0.97  # Controller efficiency
controller_coolant_flow_rate = 12 / 60  # Coolant flow rate in kg/s (from 10 L/min to kg/s)

# Combined cooling requirements
combined_coolant_flow_rate = motor_coolant_flow_rate + controller_coolant_flow_rate  # Combined flow rate for coolant

# Specific heat capacity of coolant water
Cp_coolant = 4200  # Specific heat capacity in J/(kg*K) 

# Heat dissipation calculations
heat_dissipated_motor = (1 - motor_efficiency) * motor_continuous_power  # Heat to be dissipated by motor
heat_dissipated_controller = (1 - controller_efficiency) * controller_continuous_power  # Heat to be dissipated by controller

# Total heat to be dissipated by the cooling system
total_heat_dissipation = heat_dissipated_motor + heat_dissipated_controller

# Print the results
print(f"Heat to be dissipated by the motor: {heat_dissipated_motor} W")
print(f"Heat to be dissipated by the controller: {heat_dissipated_controller} W")
print(f"Total heat to be dissipated by the system: {total_heat_dissipation} W")

# Assuming an ambient temperature of 30 degrees Celsius for the cooling system design
T_ambient = 30  # Ambient temperature in degrees Celsius

# Assuming inlet temperature for coolant is the max coolant temperature for both motor and controller
T_motor_inlet = 50  # Inlet coolant temperature for the motor in degrees Celsius
T_controller_inlet = 80  # Inlet coolant temperature for the controller in degrees Celsius

# Assuming the cooling system can maintain the inlet temperature at the maximum temperature specs
T_motor_outlet = T_ambient  # Outlet coolant temperature for the motor in degrees Celsius
T_controller_outlet = T_ambient  # Outlet coolant temperature for the controller in degrees Celsius

# Calculate the thermal capacity rates for coolant in the motor and controller
C_motor_coolant = motor_coolant_flow_rate * Cp_coolant
C_controller_coolant = controller_coolant_flow_rate * Cp_coolant

# Total thermal capacity rate for the combined coolant
C_total_coolant = combined_coolant_flow_rate * Cp_coolant

# TODO: UPDATE U: Values with calculation using equation 4 and values from data sheet
# approximating an overall heat transfer coefficient (U) and heat transfer surface area (A)
U = 0.82  # Overall heat transfer coefficient in W/(m^2*K)
A = 0.89  # Heat transfer surface area in m^2

# Calculate the NTU (Number of Transfer Units)
NTU = U * A / C_total_coolant

# Calculate the heat capacity ratio
Cr = C_total_coolant / max(C_motor_coolant, C_controller_coolant)

# Estimate the effectiveness based on the NTU and Cr for a parallel flow heat exchanger
effectiveness = 1 - np.exp(-NTU * (1 + Cr)) / (1 + Cr)

# Calculate the maximum possible heat transfer rate
Q_max = C_total_coolant * (max(T_motor_inlet, T_controller_inlet) - T_ambient)

# Calculate the actual heat transfer rate using the effectiveness
Q_actual = effectiveness * Q_max

# Display results
print(f'Effectiveness: {effectiveness}')
print(f'Maximum possible heat transfer rate: {Q_max} W')
print(f'Actual heat transfer rate: {Q_actual} W')

# # Check if the cooling system meets the requirements
# if Q_actual >= total_heat_dissipation:
#     print('The cooling system is sufficient.')
# else:
#     print('The cooling system is NOT sufficient.')