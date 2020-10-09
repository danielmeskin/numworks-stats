def outliers(q1,q3):
  iqr=q3-q1
  low=q1-(1.5*iqr)
  high=q3+(1.5*iqr)
  print("Low: "+str(low))
  print("High: "+str(high))
