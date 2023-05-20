#GITHUB
#https://github.com/softwareNuggets
#/Python_Shorts/vid_2_**kwargs.py

# **kwargs = keyword-arguments
#         zero to many keyword-arguments
#         comma separated





##########  example 1 #######################

def keyword_args_v1(**kwargs):
 print(f"""
  Numbers:
    {kwargs['field1']}
    {kwargs['field2']}
    {kwargs['field3']}
    """)
    



keyword_args_v1( 
              field1  =   'one',
              field2  =   'two',
              field3  =   'three')
            
            
print("\n\n\n")
##########  example 2 #######################

def translate_v2(**kwargs):
    for values in kwargs.values():
        print(values, end=", ")


translate_v2(   field1  =   'one',
                field2  =   'two',
                field3  =   'three')
            
print("\n\n\n")
##########  example 3 #######################            

def translate_v3(**kwargs):
        for key in kwargs.keys():
            print(key)
            
translate_v3(   field1  =   'one',
                field2  =   'two',
                field3  =   'three')           
            
print("\n\n\n")
##########  example 4 #######################               
def translate_v4(**kwargs):
        for key,value in kwargs.items():
            print(f"{key}:{value}")
            
translate_v4(   field1  =   'one',
                field2  =   'two',
                field3  =   'three')
            