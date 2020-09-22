def ground_shipping_cost(weight):
  cost = 0
  if weight <= 2:
    cost = (1.50 * weight) + 20
  elif (weight > 2) and (weight <= 6):
    cost = (3.00 * weight) + 20
  elif weight > 6 and weight <= 10:
    cost = (4 * weight) + 20
  else:
    cost = (4.75 * weight) + 20
  return cost

premium_ground_shipping = 125

def drone_shipping_cost(weight):
  cost = 0
  if weight <= 2:
    cost = 4.50 * weight
  elif weight > 2 and weight <= 6:
    cost = 9 * weight
  elif weight > 6 and weight <= 10:
    cost = 12 * weight
  else:
    cost = 14.25 * weight
  return cost

def best_shipping_method(weight):
  if drone_shipping_cost(weight) < ground_shipping_cost(weight) and drone_shipping_cost(weight) < 125:
    return "Drone shipping is cheaper"
  elif ground_shipping_cost(weight) < drone_shipping_cost(weight) and ground_shipping_cost(weight) < 125:
    return "Ground shipping is cheaper"
  elif 125 < drone_shipping_cost(weight) and 125 < ground_shipping_cost(weight):
    return "Premium shipping is cheaper"
  else:
    return "All solutions cost the same"

print((best_shipping_method(41.5)))
