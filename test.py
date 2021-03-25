import unittest
from bmi_calculator import bmi_calculator


class TestBMICodeTest(unittest.TestCase):
   def test_code_1(self):
      data_list = [
          {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }
      ]
      response = bmi_calculator(data_list)
      self.assertEqual(32.8, response[0]["bmi_range"])
      self.assertEqual('Moderately obese', response[0]["bmi_cateory"])

   def test_code_2(self):
      data_list = [
          { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }
      ]
      response = bmi_calculator(data_list)
      self.assertEqual(32.8, response[0]["bmi_range"])
      self.assertEqual('Moderately obese', response[0]["bmi_cateory"])

   def test_code_3(self):
      data_list = [
       { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }
   ]
      response = bmi_calculator(data_list)
      self.assertEqual(23.8, response[0]["bmi_range"])
      self.assertEqual('Normal weight', response[0]["bmi_cateory"])

   def test_code_4(self):
      data_list = [
         { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}
      ]
      response = bmi_calculator(data_list)
      self.assertEqual(22.5, response[0]["bmi_range"])
      self.assertEqual('Normal weight', response[0]["bmi_cateory"])

   def test_code_5(self):
      data_list = [
              {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}
      ]
      response = bmi_calculator(data_list)
      self.assertEqual(31.1, response[0]["bmi_range"])
      self.assertEqual('Moderately obese', response[0]["bmi_cateory"])

   def test_code_6(self):
      data_list = [
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
   ]
      response = bmi_calculator(data_list)
      self.assertEqual(29.4, response[0]["bmi_range"])
      self.assertEqual('Overweight', response[0]["bmi_cateory"])

            
if __name__ == '__main__':
    unittest.main()
