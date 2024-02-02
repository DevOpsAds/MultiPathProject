import math,random,json,os

# veja o video apartir dos 13 minutos
from .axonio import axonio_start
def nucleo_celular_start():
 
    print('**Nucleo_celular em sinapst  ---------> Receptor 1 aqui aguarndando procedimentos de inicialização em listing acesso ao axios')
    print(axonio_start())
    progress = 'iA rede Neural !@@ -1 para controle ok confirmo Nucleo_celular atividade !:  controlle.py(copy@)'
    return progress

class Activation_nucleo_neural():   


    def single_mode():
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

        def activation(sum):
            if sum >=0:
                return 1
            else:
                return 0

        output=activation(sum)
        print('line:41',output)
        interator=0
        
        print("entrada",input,"desejado",output_desire)
        

        print('saida',output)

        error=output_desire-output
        print("erro",error)


    def percipton_mode():
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



        def activation(sum):
            if sum >=0:
                return 1
            else:
                return 0

        #print("entrada",input,"desejado",output_desire)
        
        error=math.inf
        
        while not error == 0:
            interator += 1
            print("##-perceptio_mode ## bias_sum",artifical_bias)
            print("##-perceptio_mode ##Interator",interator)
            print("#-perceptio_mode Peso",input_weight)

            sum=(input*input_weight)+(outher_neuronos)+(artifical_bias)

            output=activation(sum)

            print("-perceptio_mode saida",output)
                     
            error=output_desire-output
            
            print("-perceptio_mode erro",error)

            if not error == 0:
                input_weight= input_weight + learng_rate * input * error

                print("input_weight-perceptio_mode :",input_weight)
        print('-perceptio_mode -----Aprendizado concluido!')

    print(' Formula base de aprendizado NUCLEO NEURONIO PERCIPTON CALIBRADO !!')


    def teste_un_neural(x,w,b,ta,Ÿ):
        #OVER FITHING 
        #UNDER FITHING 

        
        artifical_bias=b

        interator=0

        input=x
        
        output_desire=Ÿ
        
        outher_neuronos=0

        input_weight=w

        learng_rate=ta



        def activation(sum):
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
                print('-----  TEsTE > Aprendizado concluido!')
        print("________________________________")
        print(" ")
        print(' -_OUTTEXT-Text_mode NUCLEO NEURONIO PERCIPTON CALIBRADO !!')
        print(" ")
        print("________________________________")
    

    def percipton_x2():
        



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
            print('line:196 teste activation!')
            print('inTest_x1 :',x1[i])
            print('inTest_w1 :',w1[i])
            print('inTest_sum_b :',sum_b)
            print('inTest_ta :',learng_rate)
            print('inTest_Ÿ :',Ÿ)

            Activation_nucleo_neural.teste_un_neural(x1[i],w1m,sum_b,learng_rate,Ÿ[i])

        else:
            print("________________________________")
            print(" ")
            print("line:246 Nivel Neural **********!")
            

            def activation(sum):
                #print('line:240:-out_sum:',f"{sum:.20f}")


                if sum >=0:
                    return 1
                else:
                    return 0

      
        
            error=math.inf

                                                        #$mode
            while not error == 0 and interator<limt[i]+2000:
            
                interator += 1


                print('NcL:',nick[i],'_interator',interator)
                print('line:269_sum_b',sum_b)
                print('line:270:-in_wb:',wb[i])
                print('line:271:-in_w1:',w1[i])

               

  


                sum=(x1[i]*w1[i])+(b[i]*wb[i])

                y=activation(sum)

                print('line:249:-out_y_activate:',y)
                     
                error=Ÿ[i]-y
                print('line:249:-out_error:',y)
            
                
                print('line:276:-in_Ÿ:',Ÿ[i])


                if not error == 0:
                    
                    print("________________________________")
                    print('line:280:-in_erro:x1',x1[i])
                    print('line:280:-in_erro:w1',w1[i])
                    print('line:280:-in_erro:sum',sum)
                    print('line:280:-out_erro:Ÿ',Ÿ)
                    print('line:280:-out_erro:y',y)
                    print('line:280:-out_erro:',error)

                    if interator>limt[i]and x1[i]==0 and w1[i]==0:
                        sum_b =wb[i] -wb[i]
                        print('line:281:-sum_b:',sum_b)
                    #input_weight= input_weight + learng_rate * input * error
                    w1[i] = w1[i] + learng_rate * x1[i] * error
                    #sum_x1=(x1[i]*w1[i])
                    print('line:284:-in_w1:',w1[i])
                    print("________________________________")
                                        #$mode
                if interator==limt[i]+2000:
                    print('interator limited:',limt[i])
                    print('NcL:',nick[i],'_interator',interator)
                    print('line:307:-in_w1:',w1[i])
                    print('line:308:-sum_b',sum_b)
                    print('line:309:-out_sum:',sum)
                    print('line:310:-out_erro:',error)

            print('-----Aprendizado concluido!')
            print("________________________________")
            print(" ")

    



    def perceptron_train(dataset):
        threshold=1e-3
        eta=0.1
        dataset=[[0,0,0],
                 [0,1,0],
                 [1,0,0],
                 [1,1,1]]     
        matriz=dataset        

        Y=[linha[-1] for linha in matriz]
        print('ultima_coluna',Y)

        X=[]
        for linha in matriz:
            X.append(linha[:-1])
        print('classes',X)

        #Equacoes do adaptacao peso w-1 w-2 e theta
        #w_1(t+1)=w_1(t)-eta *dE2/dw_1
        #w_2(t+1)=w_2(t)-eta *dE2/dw_2
        #theta_1(t+1)=theta(t)-eta *dE2/dtheta

        #weights =[ w_1 w_2 theta ]
        ba=-0.50

        def activation(sum):
        #print('line:240:-out_sum:',f"{sum:.20f}")
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
            print('meu_:i:',i,'x:',x,'y',y,'w',w,'b',b,'bw',bw)
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





            print('sqerror line:408',sqerror)



    def perceptron_bitrain(dataset):







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
        print('ultima_coluna',Y)

        X=[]
        for linha in matriz:
            X.append(linha[:-1])
        print('classes',X)

       

        def activation(sum):
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

        def f_read_Ias():
            loading_rate=[]
            with open("arquivo_Artificial1.json","r") as arquivo:
                datareload=json.load(arquivo)
        
            titulo=datareload["titulo"]
            learng_rate=datareload["learng_rate"]
            iaset_interaction=datareload["interactions"]
            b=datareload["b"]
            bw=datareload["bw"]
            
            weights=datareload["weights"]
            print('my_information is:',datareload["aprendizado"])
            print("________________________________")
            print("sendo 'as:",titulo)
            print('learng_rate:',learng_rate)
            print('weights:',weights)
            print('bias:',b)
            print('bias_weight:',bw)
            print('iaset_interaction:',iaset_interaction)

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
            print('line:514- l',loading_conf[0])
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
            print('interator aqui!@')
            print('nº:',interator)
            iASet[1].append(interator)

            for i in range(len(X)):
                
                #set indice 4 como bias valor
                x=X[i]
                y=Y[i]
                w=weights
                print("________________________________")
                print("sendo 'as")
                print('i:',i)
                print('x:',x)
                print('y',y)
                print('w',w)
                print('b',b)
                print('bw',bw)
                print(weights,'weights:')
                iASet[0].append(weights)
                print("________________________________")
                #aplicação do modelo perseption

                for i in range(len(x)):
                    print("legitimo de x",[i])
                    print(x[i])

                    sum_x=(x[i]*w)+sum_x

                sum=sum_x+(theta)
                print('line:494-activation sum',sum)
                y_o=activation(sum)
                #erro quadrado do perceptrons x2
                #error=Ÿ[i]-y
                error=y-y_o

                if not error == 0:
                    print("________________________________")
                    print('interator=',interator)
                    print('line:499:-in_erro:x_index[',x[i])
                    print('line:499:-in_erro:weights',w)
                    print('line:499:-in_erro:sum',sum)
                    print('line:499:-out_erro:Ÿ',y)
                    print('line:499:-out_erro:y',y_o)
                    print('line:499:-out_erro:',error)
                    #input_weight= input_weight + learng_rate * input * error
                    weights = w + learng_rate * x[i] * error

               
                print("________________________________")
                                        #$mode
                if interator==threshold:
                    print('interator limited:',limt[i])
                    print('NcL:',nick[i],'_interator',interator)
                    print('line:508:-in_w1:',w1[i])
                    print('line:508:-sum_b',sum_b)
                    print('line:508:-out_sum:',sum)
                    print('line:508:-out_erro:',error)

                    print('----Em aprendizado aguarndando....')
                    print("________________________________")
                    print(" ")
                else:

                    print('-----Aprendizado concluido!')
                    print('SETWEIGTHS in:',weights)
                    print("________________________________")
                    print(" ")

            



            print('sqerror line:408',sqerror)
        print("________________________________")
        print(" ")
        iASetread=[0]
      
        bios_ia_atualization+= 1

        print("weights aprendizado ",iASet[0][-1])
        iaset_weights=iASet[0][-1] 

        print("interator_aprendizado ",iASet[1][-1])
        iaset_interaction=iASet[1][-1] 
        print('ultima_coluna',iaset_interaction)

        
        dados={
        "aprendizado":bios_ia_atualization,
        "titulo":"teste_0",
        'learng_rate':learng_rate,
        "interactions":iaset_interaction,
        "b":b,
        "bw":b,
        "weights":iaset_weights
        }


        def save(dados):
            with open("arquivo_Artificial1.json","w") as arquivo:
                json.dump(dados,arquivo)

        f_save=input('Salvar? [sim]=y [nao]=n')
        if f_save=='y':
            save(dados)

    

    def execult_ia():


        def f_read_Ias():

            loading_rate=[]
            with open("arquivo_Artificial1.json","r") as arquivo:
                datareload=json.load(arquivo)
        
            titulo=datareload["titulo"]
            learng_rate=datareload["learng_rate"]
            iaset_interaction=datareload["interactions"]
            b=datareload["b"]
            bw=datareload["bw"]
            weights=datareload["weights"]
            print('my_information is:',datareload["aprendizado"])
            print("________________________________")
            print("sendo 'as:",titulo)
            print('learng_rate:',learng_rate)
            print('weights:',weights)
            print('bias:',b)
            print('bias_weight:',bw)
            print('iaset_interaction:',iaset_interaction)

            loading_rate=[titulo,learng_rate,iaset_interaction,b,bw,datareload,weights]
            return(loading_rate)



         
        
        
        if f_read_Ias():

            loading_conf=f_read_Ias()
            print('line:514- l',loading_conf[0])
            titulo=loading_conf[0]
            learng_rate=loading_conf[1]
            iaset_interaction=loading_conf[2]
            b=loading_conf[3]
            bw=loading_conf[4]
            datareload=loading_conf[5]
            weights=loading_conf[6]



      
        

        calibrate=weights*2
        def activation(sum):
            print('acesso a o activation,y',float(sum))
            
            if float(sum)>=calibrate:
                return 1
            else:
                return 0


        error=math.inf
        print(float(weights))
        var1=input('var_1?')
        var2=input('var_2?')

        sum=(float(var1)*float(weights))+(float(var2)*float(weights))*(float(b)*float(bw))
        Ÿ=activation(sum)
        print('soma=',sum,'Sistema encontra',Ÿ)
        


       
     


 













