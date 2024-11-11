import matplotlib.pyplot as plt
# ----- INDICATEUR RSI -----
# Faisant partie des indicateurs les plus utilisés dans l'analyse financière, le RSI permet d'indiquer si le titre est sur acheté ou sur vendu
# Pour cela il n'a besoin que d'une seule courbe, ici sous forme d'une liste de valeurs, et d'une fonction d'interpretation de celle-ci
# La formule est: RSI=100-100/(1+RS) 
# avec RS=m_G/m_L  m_G=Moyenne des gains  m_L=moyenne des pertes
# A noter que la complexité de la fonction est directement liée à l'utilisation renouvelée d'EMA (voir les commentaires du fichier : MACD.py)

def f_RSI(prix):
  list_RSI=[]
  sum_G,sum_L=0.000001,0.000001 # La valeur exacte 0 causerait une erreur dans certains cas, que l'on cherche à éviter

  # Initialisation : Calcul de la 1ere valeur de list_RSI
  # On utilise pour ça les formules : 
  # --> Moyenne des gains (m_G)= Somme des gains sur 14 périodes (sum_G) / 14
  # --> Moyenne des pertes (m_L) = somme des pertes sur 14 périodes (sum_L) / 14
 
  for i in range(14,0,-1):
    if prix[-i-14][0]>prix[-i-15][0]:
      sum_G+=(prix[-i-14][0]/prix[-i-15][0]-1)*100
    else:
      sum_L+=(prix[-i-14][0]/prix[-i-15][0]-1)*100
  m_G=sum_G/14
  m_L=sum_L/14
  RS=m_G/m_L
  RSI_0=100-(100/(1+RS))
  list_RSI.append(RSI_0) 

  # : Calcul des 14 valeurs suivantes de list_RSI
  for i in range(14,0,-1):
    if prix[-i][0]>prix[-i-1][0]:
      c_G=(prix[-i][0]/prix[-i-1][0]-1)*100
      m_G=(m_G*13+c_G)/14
      m_L*=13/14
    else:
      c_L=(prix[-i][0]-prix[-i-1][0]-1)*100
      m_L=(m_L*13+c_L)/14
      m_G*=13/14
    RS=m_G/m_L
    iRSI=100-(100/(1+RS))
    list_RSI.append(iRSI)
  return list_RSI

# Fonction d'affichage du RSI, mais inutilisable car indépendante de la courbe de prix
"""def f_afficher_RSI(prix):
  RSI=f_RSI(prix)

  plt.xlabel('Temps')
  plt.ylabel('RSI')
  plt.title('Courbe du RSI')

  x = range(len(prix[:][0]))
  y = prix[:][0]
  plt.plot(x, y,'r.-')
  plt.plot(x, RSI,'b.-')
  plt.grid()
  plt.show()
  return"""