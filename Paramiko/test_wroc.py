#!/usr/bin/env python

import unittest
import wroc
import mock
import paramiko

class WrocTest(unittest.TestCase):


	def test_f1(self):
		w=wroc.f1(0)
		self.assertEqual(w,0)

        def test_f2(self):
                w=wroc.f1(1)
                self.assertEqual(w,1)

        def test_f3(self):
                w=wroc.f1(2)
                self.assertEqual(w,4)

        def test_f4(self):
                w=wroc.f1(2,1)
                self.assertEqual(w,5)
        def test_f5(self):
                w=wroc.f1(2,3)
                self.assertEqual(w,7)
       
	def test_f6(self):
                w=wroc.f2('ala')
                self.assertEqual(w,'a')

        def test_f7(self):
                w=wroc.f2([1,2,3])
                self.assertEqual(w,1)
        def test_f8(self):
                w=wroc.f2([])
                self.assertEqual(w,'BUUUUM')
	def test_f9(self):
		w=wroc.f3(1)
		self.assertEqual(w,"jeden")
	def test_f10(self):
		w=wroc.ilosc()
		self.assertEqual(w,2)
	@mock.patch.object(paramiko.SSHClient,"connect")
	def test_f11(self,mock_connect):
		w=wroc.ilosc2()
		self.assertEqual(w,"OK")


if __name__ == '__main__' :
	unittest.main()
