import math,random,json,os

# veja o video apartir dos 13 minutos
from .axonio import math_axonio_start
def math_nucleo_celular_start():
 
    print('math_:line:07,nucleo_celular. em start  ---------> Receptor 1 aqui aguarndando procedimentos de inicialização em listing acesso ao axios')
    print(math_axonio_start())
    progress = 'math_:line:09,nucleo_celular. em start  iA rede Neural !@@ -1 para controle ok confirmo Nucleo_celular atividade !:  controlle.py(copy@)'
    return progress

class math_Activation_nucleo_neural():   


    def math_single_mode():
        #OVER FITHING 
        #UNDER FITHING 

        bias=1
        bias_weight=0.1 
        artifical_bias=bias*bias_weight



        input=0
        output_desire=0
        learng_rate=0.01
       

        outher_neuronos=0

        input_weight=0.05

        sum=(input*input_weight)+(outher_neuronos)+(artifical_bias)

        def math_activation(sum):
            if sum >=0:
                return 1
            else:
                return 0

        output=activation(sum)
        print('math_:line:91,nucleo_celular. em?+line:41',output)
        interator=0
        
        print("math_:line:46,nucleo_celular. em single_mode  entrada",input,"desejado",output_desire)
        

        print('math_:line:91,nucleo_celular. em?+math_:line:49,nucleo_celular. em single_mode saida',output)

        error=output_desire-output
        print("erro",error)


    def math_percipton_mode():
        #OVER FITHING 
        #UNDER FITHING 

        bias=1
        
        bias_weight=0.1 
        
        artifical_bias=bias*bias_weight

        interator=0

        input=1
        
        output_desire=0
        
        outher_neuronos=0

        input_weight=0.01

        learng_rate=0.01



        def math_activation(sum):
            if sum >=0:
                return 1
            else:
                return 0

        #print("entrada",input,"desejado",output_desire)
        
        error=math.inf
        
        while not error == 0:
            interator += 1
            print("math_:line:91,nucleo_celular. em perceptio_mode ## bias_sum",artifical_bias)
            print("math_:line:91,nucleo_celular. em perceptio_mode##Interator",interator)
            print("math_:line:91,nucleo_celular. em perceptio_modePeso",input_weight)

            sum=(input*input_weight)+(outher_neuronos)+(artifical_bias)

            output=activation(sum)

            print("-perceptio_mode saida",output)
                     
            error=output_desire-output
            
            print("-perceptio_mode erro",error)

            if not error == 0:
                input_weight= input_weight + learng_rate * input * error

                print("math_:line:91,nucleo_celular. em perceptio_modeinput_weight-perceptio_mode :",input_weight)
        print('math_:line:91,nucleo_celular. em?+math_:line:91,nucleo_celular. em perceptio_mode-perceptio_mode -----Aprendizado concluido!')

    print('math_:line:91,nucleo_celular. em?+ Formula base de aprendizado NUCLEO NEURONIO PERCIPTON CALIBRADO !!')


    def math_teste_un_neural(x,w,b,ta,Ÿ):
        #OVER FITHING 
        #UNDER FITHING 

        
        artifical_bias=b

        interator=0

        input=x
        
        output_desire=Ÿ
        
        outher_neuronos=0

        input_weight=w

        learng_rate=ta



        def math_activation(sum):
            if sum >=0:
                return 1
            else:
                return 0

        #print("entrada",input,"desejado",output_desire)
        
        error=math.inf
        
        while not error == 0:
            interator += 1
            print("_outText-line:142-mode interator:",interator)
            print("_outText-line:146-w1:",input_weight)

            sum=(input*input_weight)+(outher_neuronos)+(artifical_bias)

            output=activation(sum)

            print("_outText-line:152-mode saida:",output)
                     
            error=(output_desire-output)
            
            print("_outText_-line:156-mode erro:",error)

            if not error == 0:
                input_weight= input_weight + learng_rate * input * error

                print("-_outText-line:161-Text_mode input_weight:",input_weight)
                print('math_:line:91,nucleo_celular. em?+-----  TEsTE > Aprendizado concluido!')
        print("________________________________")
        print(" ")
        print('math_:line:91,nucleo_celular. em?+ -_OUTTEXT-Text_mode NUCLEO NEURONIO PERCIPTON CALIBRADO !!')
        print(" ")
        print("________________________________")
    

    def math_percipton_x2():
        



        #active deactive function teste()

        #active_teste=True
        active_teste=False
        #$mode
        i=3
        
        #as nick_name
        #$mode
        nick=['00','01','02','03']
        
        #bias
        #alert - atention! caution
        #OVER FITHING 
        #UNDER FITHING 
        ba=-0.50
        bb=1.0
        rb=random.uniform(ba,bb)
   
        #$mode
        b=[1,0.56,1.5,1]
        #$mode
        wb=[rb,rb,rb,0.1]
        
        sum_b=(b[i]*wb[i])


        interator=0
        #input

        xa=-0.50
        xb=1.0
        rx=random.uniform(xa,xb)
        #$mode
        x1=[0,1,1,1]
        #$mode
        w1=[rx,rx,rx,0.01]

        sum_x1=(x1[i]*w1[i])
        
        #x1=[input[0],input[1],input[2]]

        #w1=[-0.10999999999999999,0.5,-0.45000]

        #$mode
        limt=[980,900,900,900]
        #$mode
        
        #output_desire=0
        Ÿ=[1,1,0,0]
        
        learng_rate=0.01





        if active_teste==True:
            #$mode
            w1m=-707034037809.6578

            print("")
            print("________________________________")
            print('math_:line:91,nucleo_celular. em?+line:196 teste activation!')
            print('math_:line:91,nucleo_celular. em?+inTest_x1 :',x1[i])
            print('math_:line:91,nucleo_celular. em?+inTest_w1 :',w1[i])
            print('math_:line:91,nucleo_celular. em?+inTest_sum_b :',sum_b)
            print('math_:line:91,nucleo_celular. em?+inTest_ta :',learng_rate)
            print('math_:line:91,nucleo_celular. em?+inTest_Ÿ :',Ÿ)

            Activation_nucleo_neural.teste_un_neural(x1[i],w1m,sum_b,learng_rate,Ÿ[i])

        else:
            print("________________________________")
            print(" ")
            print("line:246 Nivel Neural **********!")
            

            def math_activation(sum):
                #print('math_:line:91,nucleo_celular. em?+line:240:-out_sum:',f"{sum:.20f}")


                if sum >=0:
                    return 1
                else:
                    return 0

      
        
            error=math.inf

                                                        #$mode
            while not error == 0 and interator<limt[i]+2000:
            
                interator += 1


                print('math_:line:91,nucleo_celular. em?+NcL:',nick[i],'_interator',interator)
                print('math_:line:91,nucleo_celular. em?+line:269_sum_b',sum_b)
                print('math_:line:91,nucleo_celular. em?+line:270:-in_wb:',wb[i])
                print('math_:line:91,nucleo_celular. em?+line:271:-in_w1:',w1[i])

               

  


                sum=(x1[i]*w1[i])+(b[i]*wb[i])

                y=activation(sum)

                print('math_:line:91,nucleo_celular. em?+line:249:-out_y_activate:',y)
                     
                error=Ÿ[i]-y
                print('math_:line:91,nucleo_celular. em?+line:249:-out_error:',y)
            
                
                print('math_:line:91,nucleo_celular. em?+line:276:-in_Ÿ:',Ÿ[i])


                if not error == 0:
                    
                    print("________________________________")
                    print('math_:line:91,nucleo_celular. em?+line:280:-in_erro:x1',x1[i])
                    print('math_:line:91,nucleo_celular. em?+line:280:-in_erro:w1',w1[i])
                    print('math_:line:91,nucleo_celular. em?+line:280:-in_erro:sum',sum)
                    print('math_:line:91,nucleo_celular. em?+line:280:-out_erro:Ÿ',Ÿ)
                    print('math_:line:91,nucleo_celular. em?+line:280:-out_erro:y',y)
                    print('math_:line:91,nucleo_celular. em?+line:280:-out_erro:',error)

                    if interator>limt[i]and x1[i]==0 and w1[i]==0:
                        sum_b =wb[i] -wb[i]
                        print('math_:line:91,nucleo_celular. em?+line:281:-sum_b:',sum_b)
                    #input_weight= input_weight + learng_rate * input * error
                    w1[i] = w1[i] + learng_rate * x1[i] * error
                    #sum_x1=(x1[i]*w1[i])
                    print('math_:line:91,nucleo_celular. em?+line:284:-in_w1:',w1[i])
                    print("________________________________")
                                        #$mode
                if interator==limt[i]+2000:
                    print('math_:line:91,nucleo_celular. em?+interator limited:',limt[i])
                    print('math_:line:91,nucleo_celular. em?+NcL:',nick[i],'_interator',interator)
                    print('math_:line:91,nucleo_celular. em?+line:307:-in_w1:',w1[i])
                    print('math_:line:91,nucleo_celular. em?+line:308:-sum_b',sum_b)
                    print('math_:line:91,nucleo_celular. em?+line:309:-out_sum:',sum)
                    print('math_:line:91,nucleo_celular. em?+line:310:-out_erro:',error)

            print('math_:line:91,nucleo_celular. em?+-----Aprendizado concluido!')
            print("________________________________")
            print(" ")

    



    def math_perceptron_train(dataset):
        threshold=1e-3
        eta=0.1
        dataset=[[0,0,0],
                 [0,1,0],
                 [1,0,0],
                 [1,1,1]]     
        matriz=dataset        

        Y=[linha[-1] for linha in matriz]
        print('math_:line:91,nucleo_celular. em?+ultima_coluna',Y)

        X=[]
        for linha in matriz:
            X.append(linha[:-1])
        print('math_:line:91,nucleo_celular. em?+classes',X)

        #Equacoes do adaptacao peso w-1 w-2 e theta
        #w_1(t+1)=w_1(t)-eta *dE2/dw_1
        #w_2(t+1)=w_2(t)-eta *dE2/dw_2
        #theta_1(t+1)=theta(t)-eta *dE2/dtheta

        #weights =[ w_1 w_2 theta ]
        ba=-0.50

        def math_activation(sum):
        #print('math_:line:91,nucleo_celular. em?+line:240:-out_sum:',f"{sum:.20f}")
            if sum >=0.5:
                return 1
            else:
                return 0
        
        #entao force criado a coluna bias mais os respectivos pessos randomicos respitando a extrutura abaixo
        #gerando o bios manual
        b=(1)
        bw=random.uniform(-0.5,0.5,)
        theta=(b*bw)
        sum_x=0

        error=math.inf
        sqerror=threshold*2

        #$mode
        while not sqerror>threshold:
            sqerror += 1

        for i in range(len(X)):
            weights = random.uniform(-0.5,0.5,)
            #set indice 4 como bias valor
            x=X[i]
            y=Y[i]
            w=weights
            print('math_:line:91,nucleo_celular. em?+meu_:i:',i,'x:',x,'y',y,'w',w,'b',b,'bw',bw)
            print(weights,'meu_:y:',i,'x:',x)
            #aplicação do modelo perseption
            for i in range(len(x)):

                print("net de x",x)
                print(x[i])
                sum_x=(x[i]*w)+sum_x

            sum=sum_x+(theta)

            y_o=activation(sum)
            #erro quadrado do perceptrons x2
            #error=Ÿ[i]-y
            error=y-y_o
            sqerror=sqerror+error**2
            
            #1implementar formula de caculo do desvio padrao do erro
            dE2_dw1=2*(error)*-x[0]
            dE2_dw2=2*(error)*-x[1]
            dE2_dtheta=2*(error)*-x[1]
            dE2_=dE2_dw1+dE2_dw2+dE2_dtheta
            weights=weights-eta*dE2_





            print('math_:line:91,nucleo_celular. em?+sqerror line:408',sqerror)



    def math_perceptron_bitrain(dataset):







        bios_ia_atualization=0
        learng_rate=0.01
        threshold=1e-3
        interator=0

        dataset=[[0,0,0],
                 [0,1,0],
                 [1,0,0],
                 [1,1,1]]   


        #as nick_name
        #$mode
        nick=['col_1','col_2','respŸ']  


        

        matriz=dataset        

        Y=[linha[-1] for linha in matriz]
        print('math_:line:91,nucleo_celular. em?+ultima_coluna',Y)

        X=[]
        for linha in matriz:
            X.append(linha[:-1])
        print('math_:line:91,nucleo_celular. em?+classes',X)

       

        def math_activation(sum):
            if sum >=0.5:
                return 1
            else:
                return 0
        
        #entao force criado a coluna bias mais os respectivos pessos randomicos respitando a extrutura abaixo
        #gerando o bios manual
        b=(1.0)
        bw=random.uniform(-0.5,0.5,)
        theta=(b*bw)
        sum_x=0

        error=math.inf
        sqerror=threshold*2

        weights = random.uniform(-0.5,0.5,)
        iASet=[['weights'],['interations']]

        def math_f_read_Ias():
            loading_rate=[]
            with open("arquivo_Artificial1.json","r") as arquivo:
                datareload=json.load(arquivo)
        
            titulo=datareload["titulo"]
            learng_rate=datareload["learng_rate"]
            iaset_interaction=datareload["interactions"]
            b=datareload["b"]
            bw=datareload["bw"]
            
            weights=datareload["weights"]
            print('math_:line:91,nucleo_celular. em?+my_information is:',datareload["aprendizado"])
            print("________________________________")
            print("sendo 'as:",titulo)
            print('math_:line:91,nucleo_celular. em?+learng_rate:',learng_rate)
            print('math_:line:91,nucleo_celular. em?+weights:',weights)
            print('math_:line:91,nucleo_celular. em?+bias:',b)
            print('math_:line:91,nucleo_celular. em?+bias_weight:',bw)
            print('math_:line:91,nucleo_celular. em?+iaset_interaction:',iaset_interaction)

            iASet[0].append(weights)
            loading_rate=[titulo,learng_rate,iaset_interaction,b,bw,datareload,weights]
            print("________________________________")
            load_Ia=input("\033[1m'verifique eas informações :gostaria de usar?\033[Om")            
            if load_Ia=='y':
                loading_rate=[titulo,learng_rate,iaset_interaction,b,bw,datareload,weights]
                return(loading_rate)



        if os.path.exists("arquivo_Artificial1.json"):


            f_read_Ia=input('Existe um aquivo para esse treinamento gostaria de usar?')            
            if f_read_Ia=='y':
                f_read_Ias()
        
        
        if f_read_Ias():

            loading_conf=f_read_Ias()
            print('math_:line:91,nucleo_celular. em?+line:514- l',loading_conf[0])
            titulo=loading_conf[0]
            learng_rate=loading_conf[1]
            iaset_interaction=loading_conf[2]
            b=loading_conf[3]
            bw=loading_conf[4]
            datareload=loading_conf[5]
            weights=loading_conf[6]






        #$mode
        while not error == 0:
            
            sqerror += 1
            interator+=1
            print('math_:line:91,nucleo_celular. em?+interator aqui!@')
            print('math_:line:91,nucleo_celular. em?+nº:',interator)
            iASet[1].append(interator)

            for i in range(len(X)):
                
                #set indice 4 como bias valor
                x=X[i]
                y=Y[i]
                w=weights
                print("________________________________")
                print("sendo 'as")
                print('math_:line:91,nucleo_celular. em?+i:',i)
                print('math_:line:91,nucleo_celular. em?+x:',x)
                print('math_:line:91,nucleo_celular. em?+y',y)
                print('math_:line:91,nucleo_celular. em?+w',w)
                print('math_:line:91,nucleo_celular. em?+b',b)
                print('math_:line:91,nucleo_celular. em?+bw',bw)
                print(weights,'weights:')
                iASet[0].append(weights)
                print("________________________________")
                #aplicação do modelo perseption

                for i in range(len(x)):
                    print("legitimo de x",[i])
                    print(x[i])

                    sum_x=(x[i]*w)+sum_x

                sum=sum_x+(theta)
                print('math_:line:91,nucleo_celular. em?+line:494-activation sum',sum)
                y_o=activation(sum)
                #erro quadrado do perceptrons x2
                #error=Ÿ[i]-y
                error=y-y_o

                if not error == 0:
                    print("________________________________")
                    print('math_:line:91,nucleo_celular. em?+interator=',interator)
                    print('math_:line:91,nucleo_celular. em?+line:499:-in_erro:x_index[',x[i])
                    print('math_:line:91,nucleo_celular. em?+line:499:-in_erro:weights',w)
                    print('math_:line:91,nucleo_celular. em?+line:499:-in_erro:sum',sum)
                    print('math_:line:91,nucleo_celular. em?+line:499:-out_erro:Ÿ',y)
                    print('math_:line:91,nucleo_celular. em?+line:499:-out_erro:y',y_o)
                    print('math_:line:91,nucleo_celular. em?+line:499:-out_erro:',error)
                    #input_weight= input_weight + learng_rate * input * error
                    weights = w + learng_rate * x[i] * error

               
                print("________________________________")
                                        #$mode
                if interator==threshold:
                    print('math_:line:91,nucleo_celular. em?+interator limited:',limt[i])
                    print('math_:line:91,nucleo_celular. em?+NcL:',nick[i],'_interator',interator)
                    print('math_:line:91,nucleo_celular. em?+line:508:-in_w1:',w1[i])
                    print('math_:line:91,nucleo_celular. em?+line:508:-sum_b',sum_b)
                    print('math_:line:91,nucleo_celular. em?+line:508:-out_sum:',sum)
                    print('math_:line:91,nucleo_celular. em?+line:508:-out_erro:',error)

                    print('math_:line:91,nucleo_celular. em?+----Em aprendizado aguarndando....')
                    print("________________________________")
                    print(" ")
                else:

                    print('math_:line:91,nucleo_celular. em?+-----Aprendizado concluido!')
                    print('math_:line:91,nucleo_celular. em?+SETWEIGTHS in:',weights)
                    print("________________________________")
                    print(" ")

            



            print('math_:line:91,nucleo_celular. em?+sqerror line:408',sqerror)
        print("________________________________")
        print(" ")
        iASetread=[0]
      
        bios_ia_atualization+= 1

        print("weights aprendizado ",iASet[0][-1])
        iaset_weights=iASet[0][-1] 

        print("interator_aprendizado ",iASet[1][-1])
        iaset_interaction=iASet[1][-1] 
        print('math_:line:91,nucleo_celular. em?+ultima_coluna',iaset_interaction)

        
        dados={
        "aprendizado":bios_ia_atualization,
        "titulo":"teste_0",
        'learng_rate':learng_rate,
        "interactions":iaset_interaction,
        "b":b,
        "bw":b,
        "weights":iaset_weights
        }


        def math_save(dados):
            with open("arquivo_Artificial1.json","w") as arquivo:
                json.dump(dados,arquivo)

        f_save=input('Salvar? [sim]=y [nao]=n')
        if f_save=='y':
            save(dados)

    

    def math_execult_ia():


        def math_f_read_Ias():

            loading_rate=[]
            with open("arquivo_Artificial1.json","r") as arquivo:
                datareload=json.load(arquivo)
        
            titulo=datareload["titulo"]
            learng_rate=datareload["learng_rate"]
            iaset_interaction=datareload["interactions"]
            b=datareload["b"]
            bw=datareload["bw"]
            weights=datareload["weights"]
            print('math_:line:91,nucleo_celular. em?+my_information is:',datareload["aprendizado"])
            print("________________________________")
            print("sendo 'as:",titulo)
            print('math_:line:91,nucleo_celular. em?+learng_rate:',learng_rate)
            print('math_:line:91,nucleo_celular. em?+weights:',weights)
            print('math_:line:91,nucleo_celular. em?+bias:',b)
            print('math_:line:91,nucleo_celular. em?+bias_weight:',bw)
            print('math_:line:91,nucleo_celular. em?+iaset_interaction:',iaset_interaction)

            loading_rate=[titulo,learng_rate,iaset_interaction,b,bw,datareload,weights]
            return(loading_rate)



         
        
        
        if math_f_read_Ias():

            loading_conf=math_f_read_Ias()
            print('math_:line:91,nucleo_celular. em?+line:514- l',loading_conf[0])
            titulo=loading_conf[0]
            learng_rate=loading_conf[1]
            iaset_interaction=loading_conf[2]
            b=loading_conf[3]
            bw=loading_conf[4]
            datareload=loading_conf[5]
            weights=loading_conf[6]



      
        

        calibrate=weights*2
        def math_activation(sum):
            print('math_:line:91,nucleo_celular. em?+acesso a o activation,y',float(sum))
            
            if float(sum)>=calibrate:
                return 1
            else:
                return 0


        error=math.inf
        print(float(weights))
        var1=input('var_1?')
        var2=input('var_2?')

        sum=(float(var1)*float(weights))+(float(var2)*float(weights))*(float(b)*float(bw))
        Ÿ=math_activation(sum)
        print('math_:line:91,nucleo_celular. em?+soma=',sum,'Sistema encontra',Ÿ)
        


       
     


 
















    def math_proportion(array_l, all_=None,objective_=None,titulo=None):
          




        proportion=[]
        for valor,alcance in zip(array_l,all_):
            if alcance>valor:
                print("________________________________")
                print("")
                print('line:738',alcance)
                print('line:738 pode ser dividido em:',alcance/valor,'de tamanhos/pedaços de:',valor)
                porc_Proporcao=(100/(alcance/valor))
                print('line:738 porcentagem:/',titulo,':-',porc_Proporcao,'%')
                porc_Proporcao=(100/(alcance/valor))
                print("")
                print("________________________________")
                proportion.append(100/(alcance/valor))
            else:
                print("________________________________")
                print("")
                print('line:738',valor)
                print('line:738 pode ser dividido em:',valor/alcance,'de tamanhos/pedaços de:',alcance)
                porc_Proporcao=(100/(valor/alcance))
                print('line:738 porcentagem:/',titulo,':-',porc_Proporcao,'%')
                porc_Proporcao=(100/(valor/alcance))
                print("")
                print("________________________________")
                proportion.append(100/(valor/alcance))
        
        return proportion

    def estimated(array_l, all_=None,objective_=None,titulo=None):
        #BASE EM REGRA DE 3 ACUMULATIVA     caderno Avin
        estimable=[]
            #for linha in matriz:
            #X.append(linha[:-1])

        if len(array_l)>len(all_):
            numero_dif_len=len(array_l)-len(all_)
            for i in range(numero_dif_len):
                print('line:767:-all menor')
                soma_all=0
                soma_array_l=0
                estimable_is_all_=[]
                for i in range(len(all_)):
                    soma_all+=all_[i]
                    soma_array_l+= array_l[i]

                    prop_soma_all=[soma_all]
                    prop_soma_array_l=[soma_array_l]

                    prop_taxa=math_Activation_nucleo_neural.math_proportion(prop_soma_array_l,prop_soma_all)

            for i in range(len(array_l)):
                print("________________________________")
                print(titulo)
                print('line 781:taxa obtitda p_%:',prop_taxa[0])       
                estimable_is_all_.append(array_l[i]*prop_taxa[0]/100+array_l[i])
                print("")
                print("________________________________")
            return estimable_is_all_
                


        elif len(array_l)<len(all_):
            numero_dif_len=len(all_)-len(array_l)
            for i in range(numero_dif_len):
                print('line:795:-all menor')
                soma_all_=0
                soma_array_l=0
                estimable_is_array_l=[]
                for i in range(len(array_l)):
                    soma_array_l+=array_l[i]
                    soma_all_+= all_[i]

                    prop_soma_all_=[soma_all_]
                    prop_soma_array_l=[soma_array_l]

                    prop_taxa=math_Activation_nucleo_neural.math_proportion(prop_soma_all_,prop_soma_array_l)

            for i in range(len(all_)):
                print("________________________________")
                print(titulo)
                print('line 781:taxa obtitda p_%:',prop_taxa[0])       
                estimable_is_array_l.append(all_[i]*prop_taxa[0]/100+all_[i])
                print("")
                print("________________________________")
            return estimable_is_array_l

        else: 
            soma_all_=0
            soma_array_l=0
            estimable_is_all_=[]
            estimable_is_array_l=[]
            for valor,alcance in zip(array_l,all_):
                    soma_array_l+=valor
                    soma_all_+= alcance

                    prop_soma_all_=[soma_all_]
                    prop_soma_array_l=[soma_array_l]


                    prop_taxa=math_Activation_nucleo_neural.math_proportion(prop_soma_all_,prop_soma_array_l)
            
            for i in range(len(all_)):
                print("________________________________")
                print(titulo)
                print('line 781:taxa obtitda tip_%:',prop_taxa[0])       
                estimable_is_all_.append(all_[i]*prop_taxa[0]/100)

                print("")
                print("________________________________")
            
            for i in range(len(array_l)):
                print("________________________________")
                print(titulo)
                print('line 781:taxa obtitda tip_%:',prop_taxa[0])       
                estimable_is_array_l.append(array_l[i]*prop_taxa[0]/100)
                print("")
                print("________________________________")

            estimable=math_Activation_nucleo_neural.math_proportion(estimable_is_array_l,estimable_is_all_)
            #estimable=[estimable_is_array_l,estimable_is_all_]

        
        return estimable


   

        

    def arithmetic_progression(a1,n,r):
        soma =(n*(2*a1+(n-1)*r))//2

        

      
        return soma


   

        