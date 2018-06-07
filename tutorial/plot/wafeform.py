import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(50, 5), dpi=100)
#x1=np.arange(0, 96, 96/len(y))
#print(x1)
x=[2232.8667,-462.06668,-17319.4,19984.467,13651.533,-6348.2666,-18561.334,-15277.8,-4411.933,12312.667,19456.467,13810.333,5231.1333,-4658.3335,-13333.267,-16137.533,-12196.8,-3150.6667,8466.134,16479.066,14731.6,6908.4,-2981.6667,-11316.134,-14776.934,-11481.667,-3784.4,6412.3335,14203.8,14452.667,8022.2666,-1435.8,-9968.333,-14155.8,-12005.467,-4873.3335,4350.6665,12350.6,14481.0,9192.467,359.73334,-8120.8667,-12972.333,-11990.134,-5830.933,2581.0667,9733.533,12939.333,9852.467,2276.2,-5841.7334,-11030.533,-11303.467,-6474.8667,907.6667,7747.1333,10950.667,9306.0,3389.0,-3532.6667,-8709.134,-9883.333,-6740.4,-778.4,5259.533,8633.6,8129.3335,4213.533,-1114.8667,-5094.467,-6862.6665,-6276.467,-3773.9333,-200.4,3423.6,6425.1333,7352.2666,4932.0,-24.466667,-4318.6,-6383.933,-6121.933,-3901.6667,-575.06665,2743.2666,5002.2666,5522.067,4041.0,1130.8,-2107.5334,-4431.467,-4957.2,-3522.8667,-706.3333,2274.0,4288.3335,4563.067,2954.4,143.46666,-2684.1333,-4369.7334,-4251.2,-2385.2666,401.06668,2986.0,4279.533,3748.2666,1664.7333,-1034.6,-3209.7334,-4006.3333,-3065.2666,-883.8,1620.6666,3348.0667,3626.4,2352.0,128.46666,-2102.7334,-3369.4666,-3185.2,-1668.5333,515.0,2472.5334,3409.8,2856.1333,1092.2,-1144.3334,-2893.2,-3322.6,-2411.1333,-355.8,1657.4667,3042.9333,3089.6,1737.4,-223.6,-2015.8,-2961.2,-2628.1333,-1152.6,585.0,2323.9333,2906.3333,2488.4,800.8,-1234.6666,-2622.6,-2938.0,-1965.8667,-202.86667,1476.6,2337.4666,2342.3333,1530.4,305.13333,-777.0,-1507.8667,-1713.8,-1366.0,-613.0,282.53333,984.3333,1280.4667,1080.6666,470.93332,-269.6,-863.8,-1083.4,-863.4,-318.86667,427.4,979.06665,1143.4667,858.4,134.0,-646.26666,-1121.4,-1087.0,-674.2,-24.866667,625.3333,980.6,939.4667,538.4,-25.0,-539.0,-774.73334,-693.06665,-328.4,138.6,540.13336,725.5333,601.6667,176.86667,-339.0,-665.2,-706.0,-430.53333,2.0666666,417.8,665.3333,605.6,331.4,-95.333336,-445.8,-581.6,-482.4,-198.06667,151.2,409.8,479.0,353.2,98.73333,-190.26666,-375.2,-383.6,-235.93333,-2.0,212.73334,345.2,354.26666,188.86667,-59.0,-284.53333,-368.8,-287.66666,-97.0,138.0,284.33334,317.13333,209.26666,33.266666,-152.13333,-256.06668,-255.13333,-145.6,1.3333334,154.8,253.73334,248.8,127.73333,-64.53333,-216.06667,-261.8,-195.6,-28.2,219.86667,143.06667,45.666668,-3.8,-56.0,12.6,126.8,131.93333,-148.46666,2251.9333,-889.26666,-17583.934,16429.934,11691.733,-6282.2666,-15783.6,-12848.267,-4030.8667,10830.8,17367.867,12674.8,4471.8667,-3819.6,-11834.934,-13972.066,-11135.6,-2746.0,7611.6665,14297.667,12732.2,5906.3335,-2629.2,-9591.066,-12545.6,-9878.0,-3342.8667,5475.2,12330.066,12598.4,6993.6,-1253.7333,-8604.533,-12378.134,-10361.4,-4026.0667,3924.0667,10732.267,12444.4,7910.6,228.26666,-6952.067,-10967.467,-10178.667,-4969.2666,2206.2666,8341.267,11184.0,8468.6,1943.1333,-5020.8667,-9507.267,-9713.733,-5611.067,852.6,6678.467,9389.333,7911.8,2866.9333,-3166.8,-7481.6,-8372.467,-5650.3335,-602.0,4481.2666,7412.067,6971.4,3588.5334,-997.2,-4375.6,-5867.933,-5344.933,-3219.9333,-168.33333,2931.1333,5493.0,6290.4,4225.1333,-25.133333,-3718.4,-5477.0,-5245.8,-3340.2,-517.3333,2325.9333,4269.933,4724.2,3468.6667,975.86664,-1818.8667,-3815.1333,-4280.2666,-3030.1333,-613.06665,1940.6666,3669.6,3899.2,2522.6667,118.2,-2285.6,-3733.8,-3636.6667,-2022.2667,344.4,2538.8667,3652.4,3186.6,1410.6,-885.2,-2736.0,-3402.7334,-2603.8,-748.26666,1373.2667,2838.5334,3081.0,1995.4667,107.13333,-1790.0667,-2853.0667,-2688.7334,-1407.2667,429.66666,2090.8,2878.8667,2429.1333,930.2,-1000.4,-2457.6667,-2806.1333,-2004.8667,-328.26666,1436.8667,2554.8667,2612.4666,1438.5333,-138.33333,-1687.3334,-2540.1333,-2244.4,-1029.9333,536.3333,1884.8667,2435.6667,1971.0,680.4667,-1035.3334,-2263.8,-2409.4,-1647.5333,-186.86667,1199.6666,1904.5333,1929.0,1252.3334,265.33334,-655.2,-1263.6,-1432.2667,-1131.6,-494.26666,243.2,794.4667,1032.2667,886.5333,384.0,-232.53334,-711.0,-880.73334,-706.4667,-267.8,353.93332,799.5333,951.26666,734.06665,151.6,-521.26666,-929.4,-893.6,-558.73334,-28.733334,495.73334,792.3333,760.86664,445.13333,-19.0,-449.0,-643.73334,-572.86664,-271.26666,114.13333,440.93332,605.8,495.73334,146.93333,-285.06668,-564.6667,-604.13336,-1.6,391.06668,-581.6,354.73334,214.33333,437.13333,967.8,-401.6,-1467.3334,-441.2,445.2,153.0,131.73334,610.3333,624.26666,-271.33334,-296.13333,-227.73334,-29.933332,-329.0,-170.2,538.6,504.46667,-140.06667,-41.933334,-191.53334,-147.73334,-313.33334,-53.266666,-4.6666665,289.73334,228.2,32.533333,-28.533333,154.93333,-86.53333,-192.2,-193.53334,-119.26667,-52.2,118.26667,263.86667,243.66667,86.73333,-83.73333,-176.8,-227.0,-184.13333,-44.266666,181.2,84.0,57.8,29.933332,-48.133335,29.466667,103.0,109.6,-145.4,2140.7334,-767.5333,-16918.934,19377.334,14020.8,-6696.1333,-17849.8,-15020.2,-4776.467,12155.667,19798.934,14008.533,4915.3335,-4841.7334,-13592.467,-16473.4,-12671.467,-3208.6,8711.8,16739.666,14891.533,6568.2666,-3142.7334,-11394.467,-14771.6,-11695.866,-4173.8,6068.6,14456.0,14983.533,8524.2,-1293.6666,-10143.533,-14681.467,-12254.733,-4711.8,4864.2666,12752.4,14442.267,8960.267,136.8,-8035.467,-12692.0,-11820.333,-5738.2,2610.5334,9788.4,13008.533,9865.934,2208.4666,-5826.2666,-11132.6,-11268.533,-6424.2666,1115.3334,7858.7334,10937.6,9146.733,3311.0,-3637.5334,-8671.533,-9722.066,-6598.0,-759.73334,5178.7334,8635.4,8162.3335,4218.1333,-1135.4667,-5125.3335,-6878.467,-6262.8,-3751.2,-185.0,3442.8,6434.4,7352.6665,4934.0,-55.2,-4308.4,-6361.067,-6116.8,-3903.4,-602.13336,2725.3333,5016.533,5534.4,4039.4,1123.4667,-2109.8667,-4424.6665,-4985.0,-3523.0667,-705.8,2284.3333,4287.6,4576.0,2962.6667,142.93333,-2699.2666,-4373.2666,-4249.067,-2380.6,407.53333,2991.4666,4296.1333,3738.7334,1656.9333,-1044.3334,-3216.8667,-3993.4,-3067.8667,-883.73334,1625.6666,3354.1333,3625.2,2346.4666,127.0,-2112.6667,-3375.6,-3187.0667,-1665.5333,512.4,2471.6,3407.5334,2885.4666,1093.2667,-1173.4667,-2925.8667,-3392.6,-2352.0,-436.73334,1762.8,3120.0,3059.4666,1904.5333,-246.8,-2092.8667,-2952.0,-2634.1333,-1242.4667,606.4,2116.0667,2939.3333,2489.2,803.06665,-1201.4,-2658.1333,-2950.0,-1944.3334,-209.73334,1441.2667,2421.6667,2319.1333,1488.8667,312.26666,-852.13336,-1574.6,-1705.4667,-1294.2667,-527.26666,347.06668,1029.1333,1298.2,1055.5333,415.86667,-320.4,-896.0,-1081.3334,-834.86664,-282.86667,459.6,985.93335,1155.6666,851.93335,94.8,-733.0,-1160.4,-1060.2667,-600.2,55.6,666.4,970.5333,889.86664,452.33334,-113.86667,-583.73334,-767.0,-644.13336,-268.33334,195.13333,573.13336,712.73334,542.13336,103.53333,-396.0,-692.3333,-700.4,-371.66666,86.8,486.86667,672.26666,570.4667,261.53333,-166.2,-478.73334,-583.06665,-449.53333,-146.93333,197.6,434.4,476.6,317.46667,53.733334,-225.6,-390.33334,-381.0,-221.13333,19.933332,232.0,361.6,355.93332,170.06667,-93.26667,-317.26666,-368.86667,-267.26666,-59.266666,170.13333,297.93332,313.86667,190.93333,8.666667,-166.53334,-255.66667,-240.33333,-128.53334,15.533334,174.26666,261.53333,238.2,107.46667,-100.13333,-231.33333,-250.53334,-155.46666,29.066668,271.8,28.6,3.8666666,-19.866667,-52.333332,41.2,158.86667,350.06668,-640.93335,7947.067,-11989.8,-5833.6665,19055.732,7570.467,-10056.4,-16762.4,-11715.134,270.46667,14128.733,17164.666,10334.066,2520.7334,-6904.533,-13256.0,-14513.934,-9667.2,-112.26667,10289.733,15496.267,12057.533,3885.7334,-4896.7334,-11619.467,-13184.733,-9014.934,-1240.8667,7950.2,13799.333,12164.2,5212.4,-3597.1333,-10618.667,-12999.866,-9531.866,-2188.2,6205.8,12443.2,12291.866,6288.8,-1923.9333,-8833.8,-11897.467,-9651.333,-3304.3333,4248.3335,10034.267,11573.533,7395.6665,86.4,-6763.467,-10484.0,-9412.667,-4215.933,2621.4666,8086.7334,9861.066,7134.3335,1298.9333,-4717.467,-8442.533,-8375.066,-4717.8667,855.2,5817.0,8022.067,6630.6665,2490.4666,-2173.1333,-5225.8,-6258.2666,-5212.6665,-2577.4666,739.13336,3908.0,6261.6,6346.2,3352.2666,-1205.8667,-4576.2,-5844.4,-5076.3335,-2732.1333,329.53333,3128.2666,4782.8,4788.067,3042.7334,251.13333,-2537.4,-4267.2666,-4260.2,-2561.4666,105.86667,2634.4,4080.4,3848.3333,2043.8667,-581.26666,-2935.2,-4054.9333,-3478.1333,-1501.8667,1038.6,3128.8667,3856.0,2953.3333,847.0,-1525.2,-3203.1333,-3495.3333,-2281.2,-169.73334,1954.4667,3188.2666,3042.1333,1610.0667,-558.6,-2375.8,-3084.9333,-2476.2666,-868.13336,1104.3334,2597.3333,3000.9333,2125.0667,305.0,-1645.4667,-2859.0667,-2849.2,-1498.5333,432.6,1957.1333,2902.3333,2423.5334,974.73334,-708.4,-2167.6,-2661.7334,-1790.2,-481.86667,1226.0667,2257.8667,2543.6667,1702.8,18.266666,-1572.0667,-2570.8,-2356.5334,-1221.8667,379.93332,1593.7333,2137.2,1923.6666,976.4667,-80.73333,-943.4,-1439.8,-1424.2,-998.93335,-237.2,507.26666,994.86664,1089.4,787.93335,193.33333,-434.46667,-853.4667,-925.86664,-625.2,-94.13333,555.26666,930.4667,985.06665,610.06665,-86.86667,-749.4,-1034.7333,-868.5333,-416.46667,175.46666,663.0,851.3333,723.6,310.86667,-179.33333,-571.4,-691.6667,-519.2,-160.86667,251.8,555.3333,631.73334,390.93332,-21.133333,-349.86667,-676.93335,-530.4,-282.73334,109.066666,544.26666,403.26666,571.06665,325.33334,-435.46667,-253.73334,-552.4667,-373.8,-286.93332,486.53333,355.4,289.06668,421.4,-177.8,-12.266666,-458.8,-294.4,-276.8,265.2,151.8,380.13333,339.6,96.0,-259.73334,-230.73334,-313.86667,-407.2,151.93333,241.0,115.13333,414.8,8.266666,72.333336,-214.33333,-299.46667,-193.93333,-43.6,-15.8,240.0,208.13333,240.06667,137.0,-104.13333,-241.4,-256.6,-159.26666,-25.2,298.0,88.933334,-21.2,-0.6666667,-30.6,-13.333333,201.8,139.73334,-85.6,8256.866,-14941.934,-4610.3335,21353.867,6715.933,-12284.733,-18432.934,-12447.533,564.26666,16236.733,18946.066,11087.667,2042.8667,-7766.467,-14689.333,-15132.8,-9892.533,609.86664,12124.934,16969.066,12578.866,3388.9333,-6119.6665,-13038.134,-14008.934,-9105.866,-592.4667,9325.8,15208.0,13078.934,5138.2666,-4566.6,-12027.2,-14390.533,-10238.066,-1862.1333,7528.3335,14201.4,13407.333,6351.8667,-2866.1333,-10156.4,-13137.2,-10323.733,-3129.6667,5231.4,11365.134,12578.533,7536.3335,-573.3333,-7995.4,-11682.0,-10135.8,-4082.3333,3459.4,9197.733,10892.667,7533.467,975.3333,-5632.7334,-9511.6,-9021.2,-4705.533,1481.6666,6740.0,8876.2,7141.6,2470.2,-2631.4666,-5972.2666,-6945.933,-5643.467,-2626.8,1076.6666,4585.533,7076.4,6967.6,3393.9333,-1681.6666,-5209.6,-6522.3335,-5523.6,-2846.0667,586.73334,3619.2666,5376.6665,5162.3335,3194.0,14.866667,-3006.4,-4809.2,-4639.1333,-2680.9333,350.86667,3069.4666,4596.6665,4183.0,2092.2,-856.06665,-3401.2,-4520.6665,-3769.1333,-1498.6,1341.0667,3585.9333,4285.7334,3165.5334,768.6667,-1861.0667,-3649.4,-3851.6,-2419.4,-27.333334,2319.0,3603.0667,3340.7334,1659.5333,-665.8,-2659.7334,-3459.5334,-2776.7334,-965.86664,1232.4,2915.2666,3366.9333,2385.3333,328.93332,-1855.6666,-3222.0,-3178.7334,-1762.4667,391.33334,2160.1333,3173.6667,2580.5334,992.2,-799.5333,-2333.6667,-2881.1333,-2018.1333,-577.26666,1371.1333,2536.0667,2901.4,2023.9333,116.13333,-1764.0,-2918.1333,-2681.1333,-1395.6666,406.0,1788.9333,2414.4666,2128.6,1065.8,-62.6,-1055.5333,-1632.4,-1619.4667,-1123.9333,-262.66666,580.06665,1133.3334,1243.3334,902.13336,225.4,-482.2,-981.73334,-1062.5333,-722.6667,-99.066666,653.3333,1076.8,1124.0667,689.93335,-98.86667,-848.8,-1157.4667,-973.93335,-471.2,197.46666,766.8,991.13336,824.6667,350.0,-217.33333,-647.6,-778.6667,-584.86664,-177.2,286.13333,632.8,718.5333,486.4,-16.8,-490.26666,-721.6,-634.73334,-259.8,180.26666,543.0,679.6667,514.26666,167.6,-259.06668,-521.86664,-574.06665,-388.13333,-57.8,277.73334,467.8,449.73334,263.6,-15.933333,-283.93332,-394.8,-342.86667,-150.13333,90.53333,272.26666,365.13333,304.8,89.6,-164.26666,-342.26666,-357.73334,-222.26666,4.6,222.86667,317.0,283.0,131.26666,-61.6,-216.53334,-265.93332,-218.26666,-73.53333,75.46667,211.06667,265.93332,204.53334,47.533333,-144.2,-250.66667,-246.46666,-121.26667,95.4,230.8,82.26667,14.533334,-41.4,-40.666668,87.066666,143.46666,87.86667,-3415.0667,12124.667,-14875.0,2950.6,16144.2,1824.2667,-11745.267,-13180.0,-7661.067,3168.9333,14108.533,12998.6,7139.067,23.2,-7210.2,-12001.0,-11622.533,-6287.1333,2151.0667,10589.134,12873.733,8434.2,1173.4667,-5936.467,-10585.333,-10430.267,-6002.2666,1128.2,8586.533,11898.934,9015.667,2381.4,-4816.067,-9971.4,-10631.8,-6532.1333,149.53334,7062.0,11164.4,9390.733,3562.0667,-3393.8,-8587.533,-10034.2,-6999.3335,-1067.3334,5112.2666,9285.6,9212.8,4562.0,-1841.1333,-7036.7334,-9113.533,-7127.8667,-2030.8667,3760.7334,7598.8,8077.8667,4918.067,-276.6,-5100.8667,-7509.8667,-6553.467,-2793.8,2011.3334,5744.933,6799.6665,4892.0,1032.2667,-2693.4666,-4846.1333,-5238.8,-3935.2,-1480.3334,1357.8667,3958.2666,5579.2,4991.6665,1842.7333,-1965.2,-4374.2,-4994.8,-3937.3333,-1677.1333,971.26666,3162.4,4224.8,3797.0667,2012.2,-484.13333,-2689.5334,-3803.0667,-3376.1333,-1625.2,730.3333,2703.3333,3576.8667,2994.4,1169.5333,-1107.8667,-2883.7334,-3481.8,-2625.0667,-717.5333,1436.8,2963.5334,3228.5334,2122.3333,168.53334,-1769.9333,-2932.6667,-2814.2666,-1527.9333,357.4,2055.5334,2803.3333,2356.9333,928.6667,-857.73334,-2235.2,-2620.6667,-1900.1333,-403.26666,1242.8667,2375.5334,2498.2,1555.0,-112.2,-1702.3334,-2520.4,-2231.1333,-1067.2667,586.73334,1839.8667,2454.2666,1868.1333,535.5333,-879.06665,-1970.9333,-2249.4666,-1463.2,-220.8,1123.0667,2031.3334,2101.1333,1319.0,-147.93333,-1558.5333,-2190.2,-1850.1333,-821.5333,564.13336,1522.7333,1810.8,1470.1333,655.8,-219.86667,-921.6,-1272.3334,-1164.0,-733.6667,-97.73333,501.6,883.86664,900.13336,575.93335,51.933334,-456.46667,-763.4667,-744.73334,-429.2,36.333332,549.4,802.4667,784.4667,393.13333,-201.2,-718.5333,-859.13336,-660.4667,-250.8,242.93333,629.06665,725.13336,554.6,189.53334,-225.0,-507.73334,-568.5333,-391.2,-65.86667,276.33334,499.86667,518.6,292.46667,-82.4,-406.53333,-557.2,-465.33334,-175.26666,635.4,207.6,556.8,337.8,-487.8,-114.13333,-315.2,-120.13333,-403.8,-32.4,312.73334,165.86667,249.26666,585.13336,139.4,-411.66666,-288.6,-303.0,-131.66667,-224.46666,24.666666,481.4,340.2,202.86667,-438.13333,-74.8,-78.066666,-458.73334,-191.06667,95.333336,460.4,476.73334,-7.4666667,-31.266666,-192.8,-246.4,-149.8,-34.533333,77.73333,170.0,231.4,161.73334,3.7333333,-109.4,-215.8,-188.66667,-79.933334,94.4,169.8,30.2,-10.0,-45.666668,-10.6,96.13333,110.6,111.46667,-3327.2666,11890.733,-19428.467,4578.4,20240.666,2241.5334,-14475.0,-17780.133,-10393.0,3827.0667,18120.6,17411.133,9072.467,303.26666,-9041.134,-15313.667,-14797.8,-8258.533,3105.4666,13817.0,16090.733,10700.6,1685.9333,-7489.8,-13674.667,-13673.6,-7967.8,1391.5333,11330.467,15482.2,11512.066,2747.6667,-6539.467,-13184.8,-13730.4,-8266.467,437.93332,9101.733,14235.733,11955.4,4508.2,-4353.1333,-10931.134,-12866.333,-9020.467,-1458.4667,6493.8667,11927.267,11951.6,5927.533,-2307.0,-9063.2,-11598.6,-9007.134,-2502.9333,4933.067,9868.934,10361.667,6166.6665,-478.46667,-6578.6,-9636.733,-8372.333,-3646.6667,2531.8,7382.2666,8790.6,6154.2,1219.8667,-3299.6667,-5646.3335,-7515.467,-5055.6665,-2186.4,1872.6666,5963.2666,7190.2,5605.467,2210.5334,-2436.6667,-5833.4,-6628.533,-4947.2666,-1750.4667,992.13336,3871.5334,5437.0,5052.3335,2389.6667,-789.8,-3153.2666,-4658.8667,-4652.8667,-2325.9333,730.0,3539.1333,4779.933,3866.5334,1622.5333,-1251.3334,-3688.0,-4657.2,-3651.6,-833.2,1851.1333,3840.4,4203.067,2795.2666,245.46666,-2244.0,-3747.9333,-3629.4,-1995.7333,467.13333,2646.7334,3642.4666,3075.0667,1218.9333,-1095.6666,-2904.1333,-3365.4666,-2430.4,-511.8,1635.0,3073.9333,3232.8667,2020.6666,-137.33333,-2168.6667,-3302.8,-3025.8,-1350.6666,925.2,2479.4,3240.2666,2296.0,604.4667,-1315.6,-2734.4666,-2821.6667,-1783.1333,-139.2,1622.9333,2715.6667,2799.4666,1707.0667,-353.13333,-2072.4666,-2886.2666,-2494.1333,-961.73334,837.93335,1982.2667,2396.6,1781.3334,701.06665,-372.33334,-1295.4,-1645.2,-1445.6666,-935.93335,-126.73333,678.4,1217.3334,1173.5333,730.6667,-14.133333,-709.4,-1030.2,-964.93335,-522.6,163.8,817.4,1119.7333,1037.5333,444.0,-375.33334,-1033.2667,-1143.9333,-827.06665,-238.06667,403.0,868.06665,960.06665,698.93335,166.6,-385.73334,-724.4,-747.86664,-457.93332,-24.0,411.8,679.13336,667.6,353.06668,-164.66667,-584.8,-738.6667,-572.26666,-142.6,298.2,620.06665,671.6,436.0,49.933334,-340.53333,-548.26666,-557.93335,-305.73334,21.066668,346.0,507.66666,416.13333,170.86667,-105.066666,-323.53333,-407.6,-303.4,-62.8,159.6,310.0,381.06668,260.73334,6.9333334,-244.33333,-365.06668,-322.66666,-158.73334,74.066666,254.73334,313.26666,254.66667,75.2,-94.666664,-245.13333,-265.06668,-182.46666,-43.466667,114.0,238.6,273.8,175.4,-10.733334,-189.53334,-258.13333,-220.86667,-81.86667,161.8,186.86667,70.13333,11.066667,-51.466667,-25.533333,135.53334,52.733334,-59.266666,-2338.6,7182.4,-14808.2,9079.4,14309.934,-1817.8,-13055.2,-13353.066,-6685.8,6299.7334,14813.0,12745.934,5644.2666,-1133.4,-8747.066,-12595.8,-11455.4,-5360.8667,4107.3335,12122.667,11912.6,7046.4,-94.666664,-7532.3335,-11332.333,-10458.2,-4690.067,2952.2,10208.2,12276.2,7361.6,973.26666,-6065.6,-11012.2,-10695.267,-5591.067,1706.6666,8348.533,11538.2,8989.4,2223.7334,-4643.8,-9580.066,-9862.066,-6227.1333,171.26666,6232.2,9858.6,9059.267,3587.8,-3032.4666,-8191.4,-9470.333,-6495.3335,-801.8,4905.933,8500.667,8223.333,3968.4,-1572.6,-6157.0,-8036.6665,-6452.0,-1994.2,3006.5334,6623.1333,6989.067,4380.1333,91.933334,-3311.6,-5301.0,-5299.4,-3821.7334,-855.06665,1811.4667,4687.2,5826.3335,4767.8,1191.7333,-2610.7334,-4717.6,-5204.0,-3654.0,-1196.3334,1551.2,3513.1333,4430.2,3704.6667,1492.7333,-986.3333,-3093.5334,-3992.7334,-3229.2,-1241.1333,1298.2667,3075.2,3764.8667,2769.6667,769.8,-1594.9333,-3211.7334,-3553.9333,-2342.4666,-322.6,1900.5333,3161.9333,3259.0,1860.6,-313.53333,-2132.0,-3127.0,-2697.1333,-1237.0,819.26666,2351.4666,2885.4666,2237.0667,585.5333,-1195.4,-2454.3333,-2633.9333,-1731.2,-41.6,1605.9333,2578.4,2471.2,1308.3334,-446.8,-2000.2,-2664.4666,-2055.4,-804.4667,886.0,2031.6666,2455.2,1930.6666,98.2,-1509.5333,-2290.6667,-2233.8667,-1309.8667,188.46666,1345.3334,2315.6,2073.7334,1049.6,-531.86664,-1981.1333,-2309.4,-1829.1333,-631.0,805.6,1742.4667,1779.7333,1238.4667,449.8,-403.33334,-1008.73334,-1298.4,-1116.5333,-614.6667,32.466667,616.13336,946.06665,885.2,517.73334,-60.266666,-543.5333,-818.2,-710.6667,-360.13333,171.06667,664.5333,864.4,773.8,304.66666,-333.0,-795.4667,-875.5333,-619.2,-173.53334,342.53333,700.06665,737.2,516.0,106.46667,-325.26666,-570.6667,-565.26666,-344.66666,9.4,341.46667,542.6667,563.2,186.06667,88.46667,-531.13336,-757.4667,-384.6,-118.333336,403.8,191.0,653.4667,380.8,-166.33333,-230.0,-361.2,-562.86664,-226.26666,295.0,92.066666,472.26666,345.53333,55.666668,-42.2,-387.33334,-244.2,-274.2,-98.73333,187.06667,190.66667,500.33334,104.73333,-167.6,-32.466667,-322.0,-269.26666,-141.2,181.2,210.86667,246.26666,110.6,35.0,-15.733334,-227.86667,-271.53333,-88.333336,-14.933333,134.06667,116.333336,271.8,129.66667,-1.7333333,-162.86667,-248.06667,-120.933334,-117.6,142.0,216.8,50.933334,0.46666667,-82.4,-46.2,112.933334,122.933334,93.2,-2915.0667,9370.134,-20920.467,12459.066,18690.268,-1556.8667,-16661.268,-17191.666,-8120.067,8272.4,18975.867,15996.333,7326.533,-1859.3334,-11397.533,-16444.6,-14069.866,-6084.6,5440.0,15411.733,16209.4,9410.2,-233.6,-9416.533,-14637.667,-13089.934,-6263.4,3729.6667,12990.733,15510.934,10364.2,1252.6666,-7987.6,-13860.8,-13391.4,-7241.0,1805.9333,10757.667,14842.134,11293.267,2972.5334,-6106.933,-12388.4,-13121.866,-7894.2666,364.93332,8208.533,12823.267,11295.333,4471.6,-3975.5334,-10210.333,-11991.733,-8357.2,-1131.8667,6189.4,10481.667,10207.467,5190.467,-1825.0,-7667.7334,-10070.733,-7962.2666,-2502.2,3884.6,8203.733,8759.2,5565.4,253.26666,-4313.0,-6728.6,-6749.4,-4703.3335,-1244.8667,2532.3333,5852.8,7515.067,6016.2666,1396.2667,-3407.1333,-6147.1333,-6489.533,-4687.0,-1492.6666,1946.9333,4602.0,5642.7334,4660.3335,2017.6666,-1302.8667,-3996.6667,-5084.2,-4120.8667,-1550.4667,1547.8,3942.6,4740.533,3590.0,959.86664,-2025.8667,-4133.3335,-4532.467,-3045.9333,-372.4,2410.8667,4156.3335,4114.2,2353.0,-335.06668,-2782.7334,-4012.9333,-3505.7334,-1557.4,990.26666,3058.5334,3757.8667,2852.7334,763.3333,-1585.2667,-3203.0,-3426.7334,-2199.1333,-90.26667,2044.8,3336.2,3206.9333,1680.4667,-583.4,-2603.0667,-3437.8,-2797.2666,-1000.8,1224.2667,2924.5334,3312.0667,2216.2666,352.73334,-1704.2,-2807.4,-2941.0667,-1599.3334,98.0,1940.0,2888.1333,2743.7334,1277.2667,-719.8,-2284.0,-3093.8667,-2356.6,-707.26666,1101.9333,2298.0667,2463.4,1859.5333,696.6667,-563.93335,-1412.6,-1762.7333,-1525.8667,-861.13336,84.666664,896.4667,1303.0667,1183.7333,627.73334,-119.53333,-762.8,-1076.5333,-945.3333,-460.06668,272.26666,908.93335,1161.5333,984.6667,318.86667,-547.06665,-1112.0667,-1146.2,-758.5333,-116.53333,546.5333,950.5333,961.4,608.86664,56.4,-483.13333,-760.8,-725.2,-393.06668,70.333336,490.0,718.13336,629.26666,230.73334,-285.93332,-646.4,-735.13336,-495.2,-55.066666,376.13333,655.0,635.0,374.8,-41.4,-414.33334,-578.13336,-513.73334,-237.93333,111.0,394.4,491.86667,376.06668,130.2,-178.53334,-368.26666,-399.26666,-264.8,-23.0,205.06667,338.66666,362.33334,202.8,-44.6,-276.73334,-373.53333,-301.13333,-113.333336,123.066666,277.13333,319.13333,223.66667,42.133335,-143.66667,-253.6,-259.6,-154.26666,-5.0666666,145.06667,253.53334,256.66666,139.33333,-48.8,-204.8,-249.93333,-184.26666,-7.0,218.0,35.666668,12.333333,-8.6,-40.266666,44.733334,148.8,133.46666,-403.26666,5502.4,-7030.1333,-12007.066,16872.334,8556.467,-7787.8667,-16151.467,-11860.6,-2266.6667,12416.333,17345.732,11473.934,3653.6667,-5284.2,-12514.533,-13941.667,-10159.8,-1374.1333,8660.733,14238.267,12019.8,4678.6,-3643.6667,-10362.134,-12560.467,-9186.0,-2197.8,6597.2,12819.8,12086.866,5984.6665,-2361.8667,-9422.2,-12480.4,-9758.934,-3057.4,4957.067,11375.2,12140.8,6992.467,-799.4,-7723.6665,-11263.2,-9780.467,-4071.1333,3146.6,8992.467,11144.934,7684.6665,877.93335,-5788.8667,-9724.733,-9358.467,-4795.467,1767.3334,7271.067,9414.267,7356.6665,2042.0667,-3851.7334,-7772.533,-8192.934,-5081.8,103.73333,5023.8667,7560.6665,6677.467,3022.1333,-1524.6666,-4689.2666,-5968.8,-5201.4,-2865.5334,245.0,3326.4,5742.0,6203.8,3730.4666,-609.6,-4076.8667,-5558.4,-5076.7334,-2978.1333,-89.26667,2676.4666,4415.2,4603.8,3150.2,571.06665,-2137.0667,-3946.0,-4160.0,-2726.8667,-244.6,2230.7334,3791.3333,3805.9333,2245.3333,-225.86667,-2556.3333,-3814.7334,-3489.4666,-1744.2667,675.2,2763.1333,3683.6667,3014.6667,1107.0,-1174.8,-2900.8667,-3376.2,-2404.9333,-466.6,1626.9333,2954.6667,3003.7334,1768.2667,-165.2,-1991.7333,-2906.2666,-2572.4666,-1182.9333,681.06665,2254.3333,2879.6,2280.2666,667.8,-1244.4667,-2588.0,-2768.9333,-1801.4,-141.33333,1681.6,2632.2,2463.6,1307.6,-413.0,-1841.3334,-2566.9333,-2161.2,-780.73334,746.0,1967.0,2498.8667,1889.8,407.66666,-1201.6,-2306.2666,-2371.6,-1411.4,27.533333,1375.5333,2007.6666,1806.0667,1154.8667,171.06667,-737.6667,-1299.4667,-1397.8,-1055.7333,-388.93332,311.6,840.93335,1045.9333,838.3333,298.6,-303.06668,-756.6,-876.3333,-660.26666,-199.6,425.53333,846.6,961.4667,683.93335,61.466667,-593.86664,-941.73334,-856.5333,-485.26666,45.2,549.6,804.3333,734.26666,391.66666,-84.46667,-497.06668,-657.5333,-541.3333,-222.86667,160.2,483.26666,601.06665,464.86667,85.6,-332.8,-580.2,-584.26666,329.66666,153.46666,-318.4,299.33334,159.13333,717.4,293.46667,-769.26666,-1168.1333,-140.93333,543.93335,131.93333,54.466667,560.26666,446.93332,16.4,-124.333336,-46.733334,-391.26666,-252.46666,58.066666,192.86667,163.66667,-30.8,57.733334,7.733333,-287.06668,-490.46667,348.53333,-227.8,1.9333333,82.8,186.13333,448.93332,-60.933334,-104.26667,-212.53334,-221.66667,-123.0,16.6,141.53334,239.4,245.6,85.333336,-98.333336,-177.53334,-235.73334,-172.8,-18.266666,204.26666,99.333336,65.066666,5.266667,-69.26667,21.533333,143.86667,119.066666,-456.93332,5516.067,-6890.6665,-12683.6,21129.8,11326.267,-8973.134,-17930.4,-14165.0,-2925.6667,14115.4,19648.268,12736.733,3859.4,-6231.0,-14428.866,-16187.0,-11801.0,-1611.0667,10198.134,16835.066,13937.934,5162.3335,-4456.933,-12188.066,-14619.866,-10611.066,-2484.5334,7718.2,15138.8,14349.866,7101.067,-2759.8,-11135.066,-14695.733,-11455.066,-3477.0667,6067.3335,13443.2,14036.333,7912.6665,-1072.6666,-8886.333,-12973.2,-11276.866,-4629.0,3665.7334,10538.267,13023.333,8973.6,1109.7333,-6824.467,-11439.4,-10893.467,-5509.1333,2143.9333,8496.8,10976.0,8571.0,2374.5334,-4470.0,-9048.2,-9464.866,-5882.467,124.4,5843.2666,8795.8,7770.6,3501.7334,-1792.7333,-5502.8667,-6982.4,-6082.933,-3353.6,298.53333,3907.9333,6728.2666,7249.2666,4347.067,-705.0,-4731.7334,-6501.7334,-5933.1333,-3490.9333,-114.066666,3116.7334,5184.8667,5433.6665,3714.9333,711.6,-2485.4666,-4632.933,-4875.2,-3192.0667,-291.0,2627.2,4463.6665,4458.533,2635.7334,-255.2,-3001.0]
#print(len(x))
#print(len(y))
plt.plot(x)
#plt.plot(y)
#plt.plot(x1, y)
plt.show()
#plt.savefig('foo.png', dpi=100)