#
#Name: Peter Moe-Lange
#Student ID: 014335967
#Date (Last Modified): September 23th
#
#Lab 0
#Section 13
#Purpose of Lab: intro/warm up to python and github
#additional comments: in this program I prompt the user for an input which then format. after this I take the input and multiply it by the constant and the print it in a formatted string.
def weight_on_planets():
   e_weight = float(input("What do you weigh on earth? "))
   m_weight = e_weight * 0.38
   j_weight = e_weight * 2.34
   print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." % (m_weight, j_weight))
   
   
if __name__ == '__main__':
   weight_on_planets()
