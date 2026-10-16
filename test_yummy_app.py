import unittest
from yummy_app import YummyApp
import gps_service
# ================================================================
# CAP DO 1: Bo test co ban cho san ( Moi chi dat ~35% Coverage )
# ================================================================
class TestEasyLevel ( unittest . TestCase ) :
    """ Kiem thu chuc nang co ban tinh tien don hang """
    def setUp ( self ):
        self.app = YummyApp ()

    def test_calculate_total_for_single_item ( self ):
        cart = { "pho" : 2}
        self.assertEqual(self.app.calculate_order_total(cart), 100000)

    def test_calculate_total_for_multiple_items ( self ):
        cart = { "pho" : 1, "bun" : 1}
        self.assertEqual(self.app.calculate_order_total(cart), 95000)

    def test_calculate_total_for_empty_cart ( self ):
        self.assertEqual(self.app.calculate_order_total({}), 0.0)

    def test_calculate_total_with_zero_quantity ( self ):
        cart = { "pho" : 0}
        self.assertEqual(self.app.calculate_order_total(cart), 0.0)

class TestMediumLevel(unittest.TestCase):
    """Lớp kiểm thử các kịch bản liên quan đến áp dụng mã giảm giá"""

    def test_tc01_apply_promo_online_valid(self):
        """TC01: Áp dụng mã giảm giá khi Online hợp lệ"""
        result = apply_promo_code(promo_code="NORMAL_CODE", os_version=15, network_status="online")
        self.assertTrue(result)

    def test_tc02_apply_promo_offline_raise_connection_error(self):
        """TC02: Áp dụng mã giảm giá khi Offline ném ConnectionError"""
        with self.assertRaises(ConnectionError):
            apply_promo_code(promo_code="NORMAL_CODE", os_version=15, network_status="offline")

    def test_tc03_apply_special_code_on_os15(self):
        """TC03: Áp dụng mã đặc biệt trên hệ điều hành OS 15"""
        result = apply_promo_code(promo_code="SPECIAL_CODE", os_version=15, network_status="online")
        self.assertTrue(result)

    def test_tc04_apply_special_code_on_os14_raise_value_error(self):
        """TC04: Áp dụng mã đặc biệt trên OS 14 ném ValueError"""
        with self.assertRaises(ValueError):
            apply_promo_code(promo_code="SPECIAL_CODE", os_version=14, network_status="online")
        
# ================================================================
# CAP DO 2 ( TIET 3) : SINH VIEN TU TAY LAP TRINH TEST CASE DUOI DAY
# ( Sau khi da hoan thanh Ban thiet ke test case viet tay tren giay )
# ================================================================
# Sinh vien tu viet class TestMediumLevel o day (4 test case cho apply_promo_code )
# ...
# Sinh vien tu viet class TestHardLevel o day ( @patch cho get_nearby_restaurants )
# ...
if __name__ == '__main__':
    unittest.main ()