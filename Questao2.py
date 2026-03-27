
class televisao:
    def __init__(self,ligar,canal,volume):
        self.canal =canal
        self.volume = volume
        self.ligar = ligar
        print(f"tv ligou!")

  
    def volumeAlterar (self,volumeDireto = 0,clique:bool = False):
      
       volumeclique = 0
       while(clique != False):
            pergunta = input('deseja apertar aumentar volume ? ')
            
            if(pergunta == "sim"):
                self.volume = self.volume + 1
                print(f"o volume da tv esta no volume {self.volume}")

            if(pergunta == "nao"):
                perguntaDiminuirVolume = input('deseja diminuir o volume ? ')
                
                if(perguntaDiminuirVolume == "sim"):
                    self.volume = self.volume - 1
                    print(f'o volume da tv esta no volume {self.volume}')
                
               
                if(perguntaDiminuirVolume == "nao"):
                    print(f"o volume da tv final esta no volume {self.volume}")
                    clique = False
                    volumeclique = self.volume
                    break


       if(volumeDireto > 0):
          print(f"o volume da tv esta no volume {self.volume}")    
        
          volumeAlteradoDireto = self.volume = volumeDireto
          print(f"volume alterado para {volumeAlteradoDireto}")

       if(volumeDireto > 0 and volumeclique > 0):
              volumeSomado = volumeDireto + volumeclique 
              self.volume = volumeSomado

        








    def volumeMudo (self):
        mudo = self.volume - self.volume
        print(f"o volume da tv esta {mudo} no modo mudo ")

    def alterarCanal (self,NumCanal,clique:bool = False):
 
        while(clique!=False):
            pergunta2 = input("deseja clicar pra mudar de canal ?")
            while(pergunta2 !='nao'):
           
             if(pergunta2 == 'sim'):
              self.canal =self.canal + 1
              print(f"canal foi alterado para o canal{self.canal}")
              pergunta2 = input("deseja clicar pra mudar de canal ?")
        
            perguntaMudançaCanal = input("deseja mudar para o canal diretamente ?")
            if(perguntaMudançaCanal =="sim"):
              
              self.canal = NumCanal
              print(f"o canal foi mudou para {self.canal}")
              clique = False 
            elif(perguntaMudançaCanal =='nao'):
              clique = False 
                  
       

    def visualizarDetalhes(self):
     print(f"a tv esta no canal {self.canal} no volume {self.volume}")    




    


televisaoCanais = televisao("ligar",12,12)   
televisaoCanais.alterarCanal(22)
televisaoCanais.alterarCanal(22,clique=True)
televisaoCanais.visualizarDetalhes()
televisaoCanais.volumeAlterar(clique=True)
televisaoCanais.visualizarDetalhes()