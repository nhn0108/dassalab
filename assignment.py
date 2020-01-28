#!/usr/bin/env python
# coding: utf-8

# ### 16진수 변환

# In[6]:


print('1'+'2')


# In[15]:


def ex3(num):
    my_num='0123456789ABCDEF'
    a,b=divmod(num,16)
    if a==0:
        return my_num[b]
    else:
        #이러면 계속 16을 나눠주니까 16의 거듭제곱을 나눠주는 거랑 똑같다
        return ex3(a)+my_num[b]
    

        


# In[18]:


ex3(2015)


# 아직 멀었다...따흑<br>
# 저걸 string 구조로 만들어서 인덱싱해서 데려올 생각도 못했고<br>
# string 끼리 더하면  **'1' + '2' = '12'** 가 되는 지도 몰랐고<br>
# 재귀함수를 생각하긴 했지만 조금 어설펐다

# ### 계단 별모양 출력

# In[23]:


def ex4(num):
    count=0
    for i in range(2*num-1,0,-2):
        if count%2==0:
            print(' '*count+'-'*i+' '*count)
        else:
            print(' '*count+'+'*i+' '*count)
        count+=1


# In[25]:


ex4(20)


# 제가 드디어 이걸 해냈습니다...엉어어어엉<br>
# 감격의 순간~~ ****^O^**** <br>
# 심지어 지현 언니 코드 보다 조금 비효율적 일 뿐 나쁘지 않았오ㅜㅜ<br>
# 1년 전 만 해도 꿈도 못 꿨을 일,,,

# In[ ]:




