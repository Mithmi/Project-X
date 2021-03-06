import math
import re, time
import os, sys

def main():
	Test()
	#Value = Checkvalue(re.compile(r"^[0-9\ ]+$"), " Input Value ") #Do not forget this function
	Value = Checkvalue(re.compile(r"^[-+]?[0-9]*\.?[0-9]+$"), " Input Value ") # La Finale
	Value_list = Value.split(' ')
	os.system('clear')
	print " Current Value:", Value_list
	Category(Value_list)

def Test():
	print "|=========================================================================| \n| Hello, you are using a program developed by Three Six Group:            |\n|-Development by Alexandr Aleshkevich                                     |\n|-Design by Romah Thir                                                    |\n|-Documentation by Egor Ganyshkin                                         | \n|                                                                         |\n|             All right reserved since 01.07.2012 - 31.08.2012            |\n|=========================================================================| \n"
	Done = False
	while not Done:
		question = raw_input('Enable Test Drive? Yes/No ')
		if question == "Yes":
			time.sleep(1)
			print "\nFunction Lenght - Done"
			time.sleep(0.01)
			print "Function Weight - Done"
			time.sleep(0.03)
			print "Function Time - Done"
			time.sleep(0.1)
			print "Function Temperature - Done"
			time.sleep(0.001)
			print "Function Speed - Done"
			time.sleep(0.12)
			print "Function Capacity - Done"
			time.sleep(0.2)
			print "Function Power - Done"
			time.sleep(0.123)
			print "Function Area - Done"
			time.sleep(0.333)
			print "Function Radiation - Done"
			time.sleep(0.125)
			print "Function Sound - Done \n"
			time.sleep(0.23)
			print "System Prepared... \n"
			time.sleep(1.5)
			print "Prepared Complete \n" 
			Done = True
		if question == "No":
			print "Good day, Enjoy our Software"
			Done = True
	
def Category(Value_list):
	point = Checkpoint(re.compile(r"^[0-9\ ]+$")," Choose  category: \n Lenght - 0 \n Temperature - 1 \n Time - 2 \n Speed - 3 \n Weight - 4 \n Capacity - 5 \n Area - 6 \n Sound - 7 \n Power - 8 \n Radiation - 9 \n Reset Value - 10 \n Exit - 11	")
	os.system('clear')
	
	if point == '0':
		Lenght(Value_list)
	elif point == '1':
		Temp(Value_list)
	elif point == '2':
		Time(Value_list)
	elif point == '3':
		Speed(Value_list)
	elif point == '4': 
		Weight(Value_list)
	elif point == '5':
		Capacity(Value_list)
	elif point == '6':
		Area(Value_list)
	elif point == '7':
		Sound(Value_list)
	elif point == '8':
		Power(Value_list)
	elif point == '9':
		Radiation(Value_list)
	elif point == '10':
		Value = Checkvalue(re.compile(r"^[-+]?[0-9]*\.?[0-9]+$"), " Input Value ") # La Finale
		Value_list = Value.split(' ')
		os.system('clear')
		print " Current Value:", Value_list
		Category(Value_list)	
	elif point == '11':
		sys.exit()
	
def Checkvalue(regex, checkvalue_str):
	FLAG = False
	Value = ""
	while not FLAG:
		Value = raw_input(checkvalue_str).strip()
		if regex.match(Value):
			FLAG = True
			print FLAG
		else:
			print 'Try to Input Number Value \n For Example : 120 or 11.1 or -1 or 0 or 1e+01'
	return Value
 
def Checkpoint(regex, checkpoint_str):
	FLAG = False
	point = ""
	while not FLAG:
		point = raw_input(checkpoint_str).strip()
		if regex.match(point):
			FLAG = True
	return point

def Checknewpoint(regex, checknewpoint_str):
	FLAG = False
	newpoint = ""
	while not FLAG:
		newpoint = raw_input(checknewpoint_str).strip()
		if regex.match(newpoint):
			FLAG = True
	return newpoint

def Lenght(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4	 \n Exit - 5	')
			os.system('clear')
			
			if newpoint == '0': ## defun Millimeters
					inch = val/25.4 # Millimeters to Inch 
					cm = val/10 # Millimeters to Centimeters
					m = cm/100 # Millimeters to Meters
					km = m/1000 # Millimeters to Kilometers
					print 	'millimeters' , val,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km, '\n'
					newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4 \n Exit - 5 \n Back to Unit List - 6	')
					os.system('clear')
			
			if newpoint == '1': ## defun Inch
					mm = val*25.4 # Inch to Millimeters
					cm = mm/10 # Inch to Centimeters
					m = cm/100 # Inch to Meters
					km = m/1000 # Inch to Kilometers
					print 	'millimeters' , mm,'\n' 'inch' ,	val,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km, '\n'
					newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4	 \n Exit - 5 \n Back to Unit List - 6	')
					os.system('clear')
				
			if newpoint == '2': ## defun centimeters
					mm = val*10 # Centimeters to Millimeters
					inch = mm/25.4 # Centimeters to Inch
					m = val/100 # Centimeters to Meters
					km = m/1000 # Centimeters to Kilometers
					print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,val ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km, '\n'
					newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4 \n Exit - 5 \n Back to Unit List - 6	')
					os.system('clear')

			if newpoint == '3': ## defun meters
					cm = val*100 # Meters to Millimeters
					mm = cm*10 # Meters to Inch
					inch = mm/25.4 # Meters to Centimeters
					km = val/1000 # Meters to Kilometers
					print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	val,'\n' 'kilometers' ,	km, '\n'
					newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4 \n Exit - 5 \n Back to Unit List - 6	')
					os.system('clear')

			if newpoint == '4': ## defun kilometers
					m = val*1000 # Kilometers to Meters
					cm = m*100 # Kilometers to Centimeters
					mm = cm*10 # Kilometers to Millimeters
					inch = mm/25.4 # Kilometers to Inch
					print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	val, '\n'
					newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4	 \n Exit - 5 \n Back to Unit List - 6	')
					os.system('clear')
					
			if newpoint == '5': ## Exit
				Done = True
				break
					
			if newpoint == '6':
				os.system('clear')
				Lenght(Value_list)
				os.system('clear')
					
			i =i +1
	Category(Value_list)		
           
def Temp(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n Celsius - 1 \n Fahrenheit - 2 \n Kelvin - 3 \n Exit - 4	')
			os.system('clear')
			
			if newpoint == '1': #defun Celsius
				CK = val + 273.15 # Celsius to Kelvin 
				CF = val*33.8 # Celsius to Fahrenheit
				print	'Celsius' , val ,'\n','Kelvin' , CK,'\n','Fahrenheit' , CF, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n Celsius - 1 \n Fahrenheit - 2 \n Kelvin - 3 \n Exit - 4 \n Back to Unit List - 5	')
				os.system('clear')
				
			if newpoint == '2': #defun Fahrenheit	
				FC = val/33.8 # Fahrenheit to Celsius 
				FK = FC + 273.15 # Fahrenheit to Kelvin
				print	'Celsius' , FC ,'\n','Kelvin' , FK,'\n','Fahrenheit' , val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n Celsius - 1 \n Fahrenheit - 2 \n Kelvin - 3 \n Exit - 4 \n Back to Unit List - 5	')
				os.system('clear')
				
			if newpoint == '3': #defun Kelvin   
				KC = val - 273.15 # Kelvin to Celsius 
				KF = KC*33.8 # Kelvin to Fahrenheit
				print	'Celsius' , KC ,'\n','Kelvin' , val,'\n','Fahrenheit' , KF, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n Celsius - 1 \n Fahrenheit - 2 \n Kelvin - 3 \n Exit - 4 \n Back to Unit List - 5	')
				os.system('clear')
				
			if newpoint == '4': ## Exit
				Done = True
				break
				
			if newpoint == '5':
				os.system('clear')
				Temp(Value_list)
				os.system('clear')
				
			i =i +1
	Category(Value_list)

def Time(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6	')
			os.system('clear')
			
			if newpoint == '1': #defun milliseconds
				sec = val/1000 # Milliseconds to Seconds
				mints = sec/60 # Milliseconds to Minutes
				hour = mints/60 # Milliseconds to Hour
				day = hour/24 # Milliseconds to Day
				print	'milliseconds' , val, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , day, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6 \n Back to Unit List - 7	')
				os.system('clear')
				
			if newpoint == '2': #defun seconds
				ms = val*1000 # Seconds to Milliseconds
				mints = val/60 # Seconds to Minutes
				hour = mints/60 # Seconds to Hour
				day = hour/24 # Seconds to Day
				print	'milliseconds' , ms, '\n' , 'seconds' , val, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , day, '\n'	
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6 \n Back to Unit List - 7	')
				os.system('clear')
				
			if newpoint == '3': #defun minutes 
				sec = val*60 # Minutes to Seconds
				ms = sec*1000 # Minutes to Milliseconds
				hour = val/60 # Minutes to Hour
				day = hour/24 # Minutes to Day
				print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , val, '\n', 'hour' , hour, '\n', 'day' , day, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6 \n Back to Unit List - 7	')
				os.system('clear')
				
			if newpoint == '4': #defun hour 
				mints = val*60 # Hour to Minutes
				sec = mints*60 # Hour to Seconds
				ms = sec*1000 # Hour to Milliseconds
				day = val/24 # Hour to Day
				print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , val, '\n', 'day' , day, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6 \n Back to Unit List - 7 	')
				os.system('clear')
				
			if newpoint == '5': #defun day 
				hour = val*24 # Day to Hour
				mints = hour*60 # Day to Minutes
				sec = mints*60 # Day to Seconds
				ms = sec*1000 # Day to Milliseconds
				print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5 \n Exit - 6 \n Back to Unit List - 7	')
				os.system('clear')
				
			if newpoint == '6': ## Exit
				Done = True
				break
				
			if newpoint == '7':
				os.system('clear')
				Time(Value_list)
				os.system('clear')
				
			i =i +1
	Category(Value_list)

def Speed(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4 \n Exit - 5	')
			os.system('clear')
			
			if newpoint == '1': #defun meters per second
				km = val*3.6 # Meters per Second to Kilometers per Hour
				knot = km/1.852 # Meters per Second to Knot
				miles = km/1.6093 # Meters per Second to Miles per Hour
				print	'm/s' , val, '\n', 'km/h' ,	km, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	miles, '\n'			
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
				
			if newpoint == '2': #defun kilometers per hour
				mes = val/3.6 # Kilometers per Hour to Meters per Second
				knot = val/1.852 # Kilometers per Hour to Knot
				miles = val/1.6093 # Kilometers per Hour to Miles per Hour
				print	'm/s' , mes, '\n', 'km/h' ,	val, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	miles, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '3': #defun knot 
				km = val*1.852 # Knot to Kilometers per Hour
				mes = km/3.6 # Knot to Meters per Second
				miles = km/1.6093 # Knot to Miles per Hour
				print	'm/s' , mes, '\n', 'km/h' ,	km, '\n', 'knot' ,	val, '\n', 'miles/h' ,	miles, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '4': #defun miles per hour
				km = val*1.6093 # Miles per Hour to Kilometers per Hour
				mes = km/3.6 # Miles per Hour to Meters per Second
				knot = km/1.852 # Miles per Hour to Knot
				print	'm/s' , mes, '\n', 'km/h' ,	km, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
				
			if newpoint == '5': ## Exit
				Done = True
				break
				
			if newpoint == '6':
				os.system('clear')
				Speed(Value_list)
				os.system('clear')
				
			i =i +1
	Category(Value_list)

def Weight(Value_list):
	weight = 453.59237
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4 \n Exit - 5 \n ')
			os.system('clear')
			
			if newpoint == '1': #defun Gram
				kg = val/1000 # Gram to Kilogram
				pound = val/weight # Gram to Pound
				tonne = kg/1000 # Gram to Tonne
				print	'gram',	val, '\n', 'kilogram',	kg, '\n', 'pound',	pound , '\n', 'tonne',	tonne, '\n'	
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')

			if newpoint == '2': #defun Kilogram
				gram = val*1000 # Kilogram to Gram
				pound = gram/weight # Kilogram to Pound
				tonne = val/1000 # Kilogram to Tonne
				print	'gram',	gram, '\n', 'kilogram',	val, '\n', 'pound',	pound , '\n', 'tonne',	tonne, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '3': #defun pound 
				gram = val*weight # Pound to Gram
				kg = gram/1000 # Pound to Kilogram
				tonne = kg/1000 # Pound to Tonne
				print	'gram',	gram, '\n', 'kilogram',	kg, '\n', 'pound',	val , '\n', 'tonne',	tonne, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '4': #defun tonne
				kg = val*1000 # Tonne to Kilogram
				gram = kg*1000 # Tonne to Gram
				pound = gram/weight # Tonne to Pound
				print	'gram',	gram, '\n', 'kilogram',	kg, '\n', 'pound',	pound , '\n', 'tonne',	val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
				
			if newpoint == '5':## Exit
				Done = True
				break
			
			if newpoint == '6':
				os.system('clear')
				Weight(Value_list)
				os.system('clear')
				
			i =i +1
	Category(Value_list)
		
def Capacity(Value_list):
	Done = False
	i = 0
	GCS = 2.6417205e-07 # Gallon Const US
	GCK = 2.1996925e-07 # Gallon Const UK
	BCK = 6.1102569e-09 # Barrel Const UK
	BCS = 8.3864144e-09 # Barrel Const US
	val = float(Value_list[i])
	while not Done:
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6 \n Exit - 7 ')
			os.system('clear')
			if newpoint == '1': #defun cubic millimeters
				ccm = val/1000 #cubic millimeters to cubic centimeters
				cm = val*1.0e-09 #cubic millimeters to cubic meters
				lit = val*1.0e-06 #cubic millimeters to liter
				gUK = val*GCK #cubic millimeters to Gallon UK
				gUS = val*GCS #cubic millimeters to Gallon US
				bUK = val*BCK #cubic millimeters to Barrel UK
				bUS = val*BCS #cubic millimeters to Barrel US
				print 'cubic millimeters', val,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS, '\n' 
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6 \n Exit -7 \n Back to Unit List - 8	')
				os.system('clear')
			
			
			if newpoint == '2': #defun cubic centimeters
				cmm = val*1000 # cubic centimeters to cubic millimeters
				cm = val*1.0e-06 # cubic centimeters to cubic meters
				lit = val/1000 # cubic centimeters to liters
				gUK = cmm*GCK # cubic centimeters to Gallon UK
				gUS = cmm*GCS # cubic centimeters to Gallon US
				bUK = cmm*BCK # cubic centimeters to Barrel UK
				bUS = cmm*BCS # cubic centimeters to Barrel US
				print 'cubic millimeters', cmm,'\n','cubic centimeters', val,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6 \n Exit -7 \n Back to Unit List - 8	')
				os.system('clear')
			
			if newpoint == '3': #defun cubic meters
				lit = val*1000 # cubic meters to liters
				ccm = lit*1000 # cubic meters to cubic centimeters
				cmm = ccm*1000 # cubic meters to cubic millimeters
				gUK = cmm*GCK # cubic meters to Gallon UK
				gUS = cmm*GCS # cubic meters to Gallon US
				bUK = cmm*BCK # cubic meters to Barrel UK
				bUS = cmm*BCS # cubic meters to Barrel US 
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', val,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6 \n Exit -7 \n Back to Unit List - 8	')
				os.system('clear')
		
			if newpoint == '4': #defun liter
				ccm = val*1000 # liter to cubic centimeters
				cmm = ccm*1000 # liter to cubic millimeters
				cm = val/1000 # liter to cubic meters
				gUK = cmm*GCK # liter to Gallon UK
				gUS = cmm*GCS # liter to Gallon US
				bUK = cmm*BCK # liter to Barrel UK
				bUS = cmm*BCS # liter to Barrel US
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', val,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6 \n Exit -7 \n Back to Unit List - 8	')
				os.system('clear')
			
			if newpoint == '5': #defun Gallon
				midpoint = raw_input(' UK or US ')
				os.system('clear')
				FLAG = False
				while not FLAG:

					if midpoint == 'UK':
						lit = val*4.54609 # Gallon UK to Liter
						ccm = lit*1000 # Gallon UK to cubic centimeter
						cmm = ccm*1000 # Gallon UK to cubic millimeters
						cm = lit/1000 # Gallon UK to cubic meters
						gUS = cmm*GCS # Gallon UK to Gallon US
						bUK = cmm*BCK # Gallon UK to Barrel UK
						bUS = cmm*BCS # Gallon UK to Barrel US
						print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', val,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS	, '\n'	
						midpoint = raw_input(' Choose: \n UK - United Kingdom Standart \n US - United States Standart \n Back to Unit List - 0 ')
						os.system('clear')
				
					if midpoint == 'US':
						lit = val*3.7854118 # Gallon US to Liter
						ccm = lit*1000 # Gallon US to cubic centimeters
						cmm = ccm*1000 # Gallon US to cubic millimeters
						cm = lit/1000 # Gallon US to cubic meters
						gUK = cmm*GCK # Gallon US to Gallon UK
						bUK = cmm*BCK # Gallon US to Barrel UK
						bUS = cmm*BCS # Gallon US to Barrel US
						print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', val,'\n','Barrel UK', bUK,'\n','Barrel US', bUS, '\n'
						midpoint =  raw_input(' Choose: \n UK - United Kingdom Standart \n US - United States Standart \n Back to Unit List - 0 ' )
						os.system('clear')
						
					if midpoint == '0':
						FLAG = True
						break
									
			if newpoint == '6': #defun Barrel
				midpoint = raw_input(' Choose: \n UK - United Kingdom Standart \n US - United States Standart \n Back to Unit List - 0 ')
				os.system('clear')
				FLAG = False
				while not FLAG:
			
					if midpoint == 'UK':
						lit = val*163.65924 # Barrel UK to Liter
						ccm = lit*1000 # Barrel UK to cubic centimeters
						cm = lit/1000 # Barrel UK to cubic meters
						cmm = ccm*1000 # Barrel UK to cubic millimeters
						gUS = cmm*GCS # Barrel UK to Gallon US
						gUK = cmm*GCK # Barrel UK to Gallon UK
						bUS = cmm*BCS # Barrel UK to Barrel US
						print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', val,'\n','Barrel US', bUS, '\n'
						midpoint =  raw_input(' Choose: \n UK - United Kingdom Standart \n US - United States Standart \n Back to Unit List - 0 ')
						os.system('clear')
				
					if midpoint == 'US':
						lit = val*119.2404712 # Barrel US to Liter
						ccm = lit*1000 # Barrel US to cubic centimeters
						cm = lit/1000 # Barrel US to cubic meters
						cmm = ccm*1000 # Barrel US to cubic millimeters
						gUS = cmm*GCS # Barrel US to Gallon US
						gUK = cmm*GCK # Barrel US to Gallon UK
						bUK = cmm*BCK # Barrel US to Barrel UK
						print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', val, '\n'
						midpoint =  raw_input(' Choose: \n UK - United Kingdom Standart \n US - United States Standart \n Back to Unit List - 0 ')
						os.system('clear')
					
					if midpoint == '0':
						FLAG = True
						break
				
			if newpoint == '7':
				Done = True
				break
				
			if newpoint == '8':
				os.system('clear')
				Capacity(Value_list)
				os.system('clear')
				
			i = i+1
	Category(Value_list)
		
def Area(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6 \n ')
			os.system('clear')
		
			if newpoint =='1': #defun Square Centimeter
				sqm = val*0.0001 # Square Centimeter to Square Meter
				sqkm = val*1.0e-10 # Square Centimeter to Square Kilometer
				hec = val*1.0e-08 # Square Centimeter to Hectare
				are = val*1.0e-06 # Square Centimeter to Are
				print 'Square Centimeter',	val,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	are, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6 \n Back to Unit List - 7		')
				os.system('clear')
				
			if newpoint =='2': #defun Square Meter
				sqcm = val*10000 # Square Meter to Square Centimeter
				sqkm = val*1.0e-06 # Square Meter to Square Kilometer
				hec = val*0.0001 # Square Meter to Hectar
				are = val*0.01 # Square Meter to Are
				print 'Square Centimeter',	sqcm,'\n','Square Meter',	val,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	are, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6	\n Back to Unit List - 7	')
				os.system('clear')
				
			if newpoint =='3': #defun Square Kilometer
				sqcm = val*1.0e+10 # Square Kilometer to Square Centimeter 
				sqm = val*1000000 # Square Kilometer to Square Meter
				hec = val*100 # Square Kilometer to Hectar
				are = val*10000 # Square Kilometer to Are
				print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	val,'\n','Hectare',	hec,'\n','Are',	are , '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6 \n Back to Unit List - 7		')
				os.system('clear')
				
			if newpoint == '4': #defun Hectare
				sqcm = val*1.0e+08 # Hectare to Square Centimeter
				sqm = val*10000 # Hectare to Square Meter
				sqkm = val*0.01 # Hectare to Square Kilometer
				are = val*100 # Hectare to Are
				print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	val,'\n','Are',	are, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6 \n Back to Unit List - 7		')
				os.system('clear')
				
			if newpoint =='5': #defun Are
				sqcm = val*1000000 # Are to Square Centimeter
				sqm = val*100 # Are to Square Meter
				sqkm = val*0.0001 # Are to Square Kilometer
				hec = val*0.01 # Are to Hectare
				print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5 \n Exit - 6 \n Back to Unit List - 7		')
				os.system('clear')
				
			if newpoint == '6':
				Done = True
				break
				
			if newpoint == '7':
				os.system('clear')
				Area(Value_list)
				os.system('clear')
				
			i = i+1
	Category(Value_list)
		
def Sound(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Bel - 1 \n Decibel - 2 \n Neper - 3 \n Exit - 4 ')
			os.system('clear')
		
			if newpoint == '1': #defun Bel
				decibel = val*10 # Bel to Decibel
				neper = val*1.1512779 # Bel to Neper
				print 'Bel', val,'\n','Decibel', decibel,'\n','Neper', neper, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Bel - 1 \n Decibel - 2 \n Neper - 3 \n Exit - 4 \n Back to Unit List - 5	')
				os.system('clear')
			
			if newpoint == '2': #defun Decibel
				bel = val/10 # Decibel to Bel
				neper = val*0.1151278 # Decibel to Neper
				print 'Bel', bel,'\n','Decibel', val,'\n','Neper', neper, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Bel - 1 \n Decibel - 2 \n Neper - 3 \n Exit - 4 \n	Back to Unit List - 5')
				os.system('clear')
			
			if newpoint == '3': # defun Neper
				bel = val*0.8686 # Neper to Bel
				decibel = val*8.686 # Neper to Decibel
				print 'Bel', bel,'\n','Decibel', decibel,'\n','Neper', val , '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Bel - 1 \n Decibel - 2 \n Neper - 3 \n Exit - 4 \n Back to Unit List - 5	')
				os.system('clear')
				
			if newpoint == '4':
				Done = True
				break
				
			if newpoint == '5':
				os.system('clear')
				Sound(Value_list)
				os.system('clear')
				
			i = i+1
	Category(Value_list)
		
def Power(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Watt - 1 \n Kilowatt - 2 \n Megawatt - 3 \n Horsepower - 4 \n Exit - 5 \n ')
			os.system('clear')
		
			if newpoint == '1': #Watt
				Kw = val*0.001 # Watt to Kilowatt
				Mw = val*1.0e-06 # Watt to Megawatt
				Hp = val*0.0013596 # Watt to Horsepower
				print 'Watt',	val,'\n','Kilowatt',	Kw,'\n','Megawatt',	Mw,'\n','Horsepower',	Hp, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Watt - 1 \n Kilowatt - 2 \n Megawatt - 3 \n Horsepower - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '2': #Kilowatt
				w = val*1000 # Kilowatt to Watt
				Mw = val*1.0e-03 # Kilowatt to Megawatt
				Hp = val*1.3596216 # Kilowatt to Horsepower
				print 'Watt',	w,'\n','Kilowatt',	val,'\n','Megawatt',	Mw,'\n','Horsepower',	Hp, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Watt - 1 \n Kilowatt - 2 \n Megawatt - 3 \n Horsepower - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '3': #Megawatt
				w = val*1.0e+06 # Megawatt to Watt
				Kw = val*1000 # Megawatt to Kilowatt
				Hp = val*1359.6216173 # Megawatt to Horsepower
				print 'Watt',	w,'\n','Kilowatt',	Kw,'\n','Megawatt', val,'\n','Horsepower',	Hp, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Watt - 1 \n Kilowatt - 2 \n Megawatt - 3 \n Horsepower - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
			
			if newpoint == '4': #Horsepower
				w = val*745.6998716 # Watt to Kilowatt
				Kw = val*0.7456999 # Watt to Megawatt
				Mw = val*0.0007457 # Watt to Horsepower
				print 'Watt',	w,'\n','Kilowatt',	Kw,'\n','Megawatt',	Mw,'\n','Horsepower',	val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n Watt - 1 \n Kilowatt - 2 \n Megawatt - 3 \n Horsepower - 4 \n Exit - 5 \n Back to Unit List - 6	')
				os.system('clear')
				
			if newpoint == '5':
				Done = True
				break
				
			if newpoint == '6':
				os.system('clear')
				Power(Value_list)
				os.system('clear')
				
			i = i+1
	Category(Value_list)
			
def Radiation(Value_list):
	i = 0
	Done = False
	val = float(Value_list[i])
	while not Done:
		
		while i < len(Value_list)*16000:
			newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),' Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4 \n Exit - 5 \n ')
			os.system('clear')
		
			if newpoint == '1': # Gray/sec
				rad = val*100 # Gray per sec to Rad per sec
				watt = val # Gray per sec to Watt per Kilogram
				rem = val*100 # Gray per sec to Rem per sec
				print 'Gray/sec',	val,'\n','Rem/sec', rem,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	rad, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'\n Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4 \n Exit - 5 \n Back to Union List - 6	')
				os.system('clear')
			
			if newpoint == '2': # Rad/sec
				gray = val*0.01 # Rad per sec to Gray per sec
				watt = val*0.01 # Rad per sec to Watt per Kilogram
				rem = val # Rad per sec to Rem per sec
				print 'Gray/sec',	gray,'\n','Rem/sec', rem,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	val, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'\n Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4 \n Exit - 5 \n Back to Union List - 6	')
				os.system('clear')
		
			if newpoint == '3': # Watt/Kilogram
				rad = val*100 # Watt per Kilogram to Rad per sec
				gray = val # Watt per Kilogram to Gray per sec 
				rem = val*100 # Watt per Kilogram to Rem per sec
				print 'Gray/sec',	gray,'\n','Rem/sec', rem,'\n','Watt/Kilogram', val,'\n','Rad/sec',	rad, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'\n Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4 \n Exit - 5 \n Back to Union List - 6	')
				os.system('clear')
		
			if newpoint == '4': # Rem/sec
				rad = val # Rem per sec to Rad per sec
				watt = val*0.01 # Rem per sec to Watt per Kilogram
				gray = val*0.01 # Rem per sec to Gray per sec 
				print 'Gray/sec',	gray,'\n','Rem/sec', val,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	rad, '\n'
				newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'\n Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4 \n Exit - 5 \n Back to Union List - 6	')
				os.system('clear')
				
			if newpoint =='5':
				Done = True	
				break
				
			if newpoint == '6':
				os.system('clear')
				Radiation(Value_list)
				os.system('clear')
				
			i = i +1
			
	Category(Value_list)
	
		
main()
