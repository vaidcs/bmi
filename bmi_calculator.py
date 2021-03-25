import logging


logger = logging.getLogger(__name__)


def bmi_calculator(data_list):
	final_data_list = []
	for data in data_list:
		try:
			height_cm = data["HeightCm"]
			weight_kg = data["WeightKg"]
			gender = data["Gender"]

			heiht_m = height_cm/100
			bmi_range = round(weight_kg/(heiht_m**2), 1)

			if bmi_range <= 18.4:
				bmi_cateory = "Underweight"
				health_risk = "Malnutrition risk"

			elif (bmi_range >= 18.5 and bmi_range <= 24.9):
				bmi_cateory = "Normal weight"
				health_risk = "Low risk"

			elif (bmi_range >= 25 and bmi_range <= 29.9):
				bmi_cateory = "Overweight"
				health_risk = "Enhanced risk"

			elif (bmi_range >= 30 and bmi_range <= 34.9):
				bmi_cateory = "Moderately obese"
				health_risk = "Medium risk"

			elif (bmi_range >= 35 and bmi_range <= 39.9):
				bmi_cateory = "Severely obese"
				health_risk = "High risk"

			else:
				bmi_cateory = "Very severely obese"
				health_risk = "Very high risk"

			logger.info(f"Gender:{gender} BMI Range (kg/m2): {bmi_range} BMI Category: {bmi_cateory} Health Risk: {health_risk}")
			final_data_list.append({"gender": gender, "bmi_range": bmi_range, "bmi_cateory": bmi_cateory, "health_risk": health_risk})
		
		except KeyError:
			# invlid data format
			logger.error(f"invalid key format, please correct the keys: {data}")
			pass

	return final_data_list


data_list = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


# function calling
bmi_calculator(data_list)
