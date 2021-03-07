'''
simple script to calculate AVB using the 2 'approved' methods
OG stands for Original Gravity and FG stands for Final Gravity
Traditional method
    ABV = (OG – FG) x 131.25
Improved method
    ABV = (76.08 x (OG – FG) / (1.775 – OG)) x (FG / 0.794)
'''
# enter OG here
OG = 1.082
# enter FG here
FG = 1.034

# Traditional
avb_trad = (OG - FG) * 131.25

# Improved
avb_imp = (76.08 * (OG - FG) / (1.775 - OG)) * (FG / 0.794)

print("AVB tradition method : {}".format(avb_trad))
print("AVB improved method : {}".format(avb_imp))
