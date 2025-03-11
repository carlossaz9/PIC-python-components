def testAddTwoIntegers(self, a, b):
    MyClass mc = MyClass()
    
    # baseline test
    self.assertTrue(mc.addTwoIntegers(0, 0) == 0)
    self.assertTrue(mc.addTwoIntegers(1, 2) == 3)
    self.assertTrue(mc.addTwoIntegers(-1, 1) == 0)
    self.assertTrue(mc.addTwoIntegers(-1, -2) == -3)
    self.assertFalse(mc.addTwoIntegers(1, 2) == 4)
    self.assertFalse(mc.addTwoIntegers(-1, -2) == -4)