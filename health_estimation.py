import sys
import json

HEALTH_ESTIMATION_TABLE = [
  {"BMI Category": "Underweight", "BMI Range": (0, 18.4), "Health risk": "Malnutrition risk"},
  {"BMI Category": "Normal", "BMI Range": (18.5, 24.9), "Health risk": "Low risk"},
  {"BMI Category": "Overweight", "BMI Range": (25, 29.9), "Health risk": "Enhanced risk"},
  {"BMI Category": "Moderately obese", "BMI Range": (30, 34.9), "Health risk": "Medium risk"},
  {"BMI Category": "Severely obese", "BMI Range": (35, 39.9), "Health risk": "High risk"},
  {"BMI Category": "Very severely obese", "BMI Range": (40, 100), "Health risk": "Very high risk"}
]

def BMI_calc(weight, height):
  # BMI(kg/m2) = mass(kg) / height(m)2
  return round(weight/(height/100)**2, 1)

def get_BMICategory_healthRisk(BMI):
  for item in HEALTH_ESTIMATION_TABLE:
    if BMI >= item["BMI Range"][0] and  BMI <= item["BMI Range"][1]:
      return item["BMI Category"], item["Health risk"]

def main():
  f = open('data.json')
  input_data = json.load(f)
  BMI_Categories = [item["BMI Category"] for item in HEALTH_ESTIMATION_TABLE]
  print("*INFO: BMI Categories:", BMI_Categories)
  print("*INFO: Enter one BMI category name:")
  input_BMICategory = input()

  if input_BMICategory not in BMI_Categories:
    sys.exit("*ERROR: Enter correct BMI category name.")

  output = []
  total_number = 0
  for item in input_data:
    BMI = BMI_calc(item["WeightKg"], item["HeightCm"])
    BMICategory, HealthRisk = get_BMICategory_healthRisk(BMI)
    if BMICategory == input_BMICategory:
      total_number += 1
    item["BMI"] = BMI
    item["BMICategory"] = BMICategory
    item["HealthRisk"] = HealthRisk
    output.append(item)

  print("*INFO:", output)
  print(f"*INFO: Total number of {input_BMICategory}: {total_number}")

if __name__ == "__main__":
  main()