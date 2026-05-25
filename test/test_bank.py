import unittest
from app.bank import verification

class TestLoanApproval(unittest.TestCase):

    # Nhóm 1 : Kiểm tra ngoại lệ
    def test_invalid_input(self):
        # Biên tuổi
        self.assertEqual(verification(17, 50.0, 700, "C"), "Invalid Input")  # TC_01
        self.assertEqual(verification(66, 50.0, 700, "C"), "Invalid Input")  # TC_02
        # Biên thu nhập
        self.assertEqual(verification(30, 4.9, 700, "C"), "Invalid Input")   # TC_03
        self.assertEqual(verification(30, 500.1, 700, "C"), "Invalid Input") # TC_04
        # Biên điểm tín dụng
        self.assertEqual(verification(30, 50.0, 299, "C"), "Invalid Input")  # TC_05
        self.assertEqual(verification(30, 50.0, 851, "C"), "Invalid Input")  # TC_06
        # Sai định dạng công việc
        self.assertEqual(verification(30, 50.0, 700, "X"), "Invalid Input")  # TC_07

	# Nhóm 2 : test logic nghiệp vụ 
    # test reject case
    def test_reject_cases(self):
        # Rule 1: High Risk (300-500) luôn bị REJECT
        self.assertEqual(verification(30, 5.0, 300, "C"), "REJECT")    # TC_08
        self.assertEqual(verification(65, 5.0, 500, "F"), "REJECT")    # TC_09
        self.assertEqual(verification(30, 500.0, 400, "C"), "REJECT")  # TC_10
        
        # Rule 2: Thu nhập thấp (<15.0) + Medium Risk
        self.assertEqual(verification(19, 5.0, 501, "C"), "REJECT")    # TC_11
        self.assertEqual(verification(30, 14.9, 600, "C"), "REJECT")   # TC_12
        
        # Rule 2: Thu nhập thấp (<15.0) + Freelance
        self.assertEqual(verification(64, 5.0, 701, "F"), "REJECT")    # TC_13
        self.assertEqual(verification(30, 14.9, 850, "F"), "REJECT")   # TC_14

    # test APPROVED
    def test_APPROVED_cases(self):
        # Thu nhập >= 15.0 + (Low/Medium Risk) + Contract
        self.assertEqual(verification(30, 15.0, 501, "C"), "APPROVED")  # TC_17
        self.assertEqual(verification(30, 500.0, 700, "C"), "APPROVED") # TC_18
        self.assertEqual(verification(18, 15.0, 701, "C"), "APPROVED")  # TC_19
        self.assertEqual(verification(65, 500.0, 850, "C"), "APPROVED") # TC_20


    # test manual review
    def test_manual_review_cases(self):
        # Thu nhập < 15.0 + Low Risk + Contract
        self.assertEqual(verification(18, 5.0, 701, "C"), "MANUAL REVIEW")    # TC_15
        self.assertEqual(verification(65, 14.9, 850, "C"), "MANUAL REVIEW")   # TC_16
        
        
        # Thu nhập >= 15.0 + (Low/Medium Risk) + Freelance
        self.assertEqual(verification(30, 15.0, 501, "F"), "MANUAL REVIEW")   # TC_21
        self.assertEqual(verification(30, 500.0, 700, "F"), "MANUAL REVIEW")  # TC_22
        self.assertEqual(verification(30, 15.0, 701, "F"), "MANUAL REVIEW")   # TC_23
        self.assertEqual(verification(30, 500.0, 850, "F"), "MANUAL REVIEW")  # TC_24

    # test at interface
    def test_at_interface(self):
        self.assertEqual(verification(44, 100.0, 500, "C"), "REJECT")  # TC_25
        self.assertEqual(verification(44, 100.0, 501, "C"), "APPROVED") # TC_26
        self.assertEqual(verification(44, 14.9, 750, "C"), "MANUAL REVIEW")   # TC_27
        self.assertEqual(verification(44, 15.0, 750, "C"), "APPROVED")  # TC_28

    # just test for some one that 
    def test_invalid_input_types(self):
        self.assertEqual(verification("30", 50.0, 700, "C"), "Invalid Input")  # TC_29
        self.assertEqual(verification(30, "50.0", 700, "C"), "Invalid Input")  # TC_30
        self.assertEqual(verification(30, 50.0, "700", "C"), "Invalid Input")  # TC_31
        self.assertEqual(verification(30, 50.0, 700, 1), "Invalid Input")      # TC_32

if __name__ == "__main__":
    unittest.main()