import unittest

class Calculator:
  
    

    def mod(self, sf_income,sp_income):
        join_income = int(sf_income)+int(sp_income)
        allowance = 132000
        allowance1= 132000
        allowance2= 264000
        mpf_mc = 0
        mpf_mc1 =0
        join_mc = 0
        net_char = 0
        result = ""
        #if sf_income > allowance:
        if sf_income / 12 < 7100:
            mpf_mc = 0
        elif sf_income / 12 <= 30000:
            mpf_mc = sf_income * 0.05
        else:
            mpf_mc = 18000
        sf_mpf= int(mpf_mc)
        net_char = sf_income-allowance-sf_mpf
                   # print(net_char)
        #else:
         #   net_char =0
                   # print(net_char)

        if net_char < 0:
            net_char =0
        #if sp_income > allowance:
        if sp_income / 12 < 7100:
            mpf_mc1 = 0
        elif sp_income / 12 <= 30000:
            mpf_mc1 = sp_income * 0.05
        else:
            mpf_mc1 = 18000

        sp_mpf = int(mpf_mc1)
        net_char1 = sp_income-allowance1-sp_mpf
                   # print(net_char1)
        #else:
         #   net_char1=0
               # print(net_char1)

        if net_char1 < 0:
            net_char1 = 0

        join_mc = mpf_mc+mpf_mc1
               # print(mpf_mc)
               # print(mpf_mc1)
               # print(join_mc)
        join_net_char = join_income - allowance2- join_mc
               # print(join_net_char)
        if join_net_char <0:
            join_net_char = 0
               # print(join_net_char)
               # return c

        def tax1():
            join_tax = 0
            sf_stat = ""
            sp_stat = ""
            stat = ""
            if net_char <= 50000:
                tax_val1 = net_char*0.02
            elif net_char <= 100000:
                tax_val1 = 1000 + (net_char-50000)*0.06
            elif net_char <= 150000:
                tax_val1 = 4000 + (net_char-100000)*0.1
            elif net_char <= 200000:
                tax_val1 = 9000 + (net_char-150000)*0.14
            else:
                tax_val1 = 16000 + (net_char-200000)*0.17

            tax_val1s = (net_char+allowance) *0.15
            if tax_val1s < tax_val1:
                tax_val1 = tax_val1s
                sf_stat = "*"


            if net_char1 <= 50000:
                tax_val2 = net_char1*0.02
            elif net_char1 <= 100000:
                tax_val2 = 1000 + (net_char1-50000)*0.06
            elif net_char1 <= 150000:
                tax_val2 = 4000 + (net_char1-100000)*0.1
            elif net_char1 <= 200000:
                tax_val2 = 9000 + (net_char1-150000)*0.14
            else:
                tax_val2 = 16000 + (net_char1-200000)*0.17

            tax_val2s = (net_char1 + allowance1)*0.15
            if tax_val2s < tax_val2:
                tax_val2 = tax_val2s
                sp_stat = "*"

            if join_net_char <= 50000:
                join_tax = join_net_char*0.02
            elif join_net_char <= 100000:
                join_tax = 1000 + (join_net_char-50000)*0.06
            elif join_net_char <= 150000:
                join_tax = 4000 + (join_net_char-100000)*0.1
            elif join_net_char <= 200000:
                join_tax = 9000 + (join_net_char-150000)*0.14
            else:
                join_tax = 16000 + (join_net_char-200000)*0.17

                       # print(join_net_char)
                       # print(join_tax)
            join_taxs = (join_net_char + allowance2) *0.15
            if join_taxs < join_tax:
                join_tax = join_taxs
                stat= "*"

            joint = int(join_tax)

                       # print(tax_val1)
                       # print(tax_val2)
                       # print(join_tax)

            totaltax =tax_val1+tax_val2
            if int(totaltax) < joint:
                tax = totaltax
            else :
                tax = joint
            print(tax)

            return tax

        return tax1()
        


  
       

class CalculatorTest(unittest.TestCase):                 

    def test_mod_with_remainder(self):                   
        cal = Calculator()
        self.assertEqual(cal.mod(500000, 20000),22460)
        #self.assertEqual(cal.mod(500000, 20000),0)
        self.assertEqual(cal.mod(120000, 120000),0)
        self.assertEqual(cal.mod(200000, 160000),1880)
        self.assertEqual(cal.mod(250000, 300000),13970)
        self.assertEqual(cal.mod(100000, 350000),10890)  

   

if __name__ == '__main__':
    unittest.main()                      
