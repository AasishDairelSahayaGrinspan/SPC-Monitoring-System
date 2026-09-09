from spc.xbar_r import calculate_xbar_r


data = [
    [500.1, 500.3, 499.9, 500.2, 500.0],
    [500.4, 500.1, 500.2, 500.3, 500.0],
    [499.8, 500.0, 500.1, 499.9, 500.2],
    [500.2, 500.3, 500.1, 500.4, 500.0],
    [499.9, 500.1, 500.0, 500.2, 499.8]
]


result = calculate_xbar_r(data)


print("Subgroup Means:", result["subgroup_means"])
print("Subgroup Ranges:", result["subgroup_ranges"])
print("Overall X-bar:", result["xbar"])
print("Average Range:", result["rbar"])
print("X-bar UCL:", result["xbar_ucl"])
print("X-bar LCL:", result["xbar_lcl"])
print("R UCL:", result["r_ucl"])
print("R LCL:", result["r_lcl"])