BLUE = (0,0,255)
ROYALBLUE = (106,90,205)
PURPLE = (180,0,255)
DARKBLUE = (0,0,139)


while True :
  np.brightness = 0.2
  np[0]=RED
  np[1]=ORANGERED
  np[2]=YELLOW
  np[3]=GREENYELLOW 
  np[4]=CHARTREUSE 
  np[5]=LIMEGREEN
  np[6]=GREEN
  np[7]=MEDIUMSEAGREEN
  np[8]=CYAN
  np[9]=BLUE
  np[10]=ROYALBLUE
  np[11]=PURPLE
  np.write()
  time.sleep(2)
  
  #np.clear()
