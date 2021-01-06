#!/usr/bin/env python
# coding: utf-8

# <b>
#     <p style = "text-align:center;">
#         <font size = "6" color = "black">Basalt "Tectonic Setting" Estimation</font>
#     </p>
# <b> 

# <p style = "text-align:center">
#     <font size = "4">
#         <a href = 'http://georoc.mpch-mainz.gwdg.de/georoc/'>Georoc Data Resource Link</a>
#     </font>
# </p>

# <h1>Table of Contents</h1>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#1">1. Foreword</a>    
#         </li>
#         <br>
#         <li>
#             <a href="#2">2. Meet with Data</a>    
#         </li>
#         <br>
#         <li>
#             <a href="#3">3. Data Cleaning</a>    
#         </li>
#         <br>
#         <li>
#             <a href="#4">4. Column Data Filling</a>
#             <ul>
#                 <li><a href="#41">4.1. Age Column Filling</a></li>
#                 <li><a href="#42">4.2. Geol. Column Filling</a></li>
#                 <li><a href="#43">4.3. Rock Texture Column Filling</a></li>
#                 <li><a href="#44">4.4. Alteration Column Filling</a></li>
#             </ul>
#         </li>
#         <br>
#         <li>
#             <a href="#5">5. Principal Component Analysis (PCA)</a> 
#             <ul>
#                 <li><a href="#51">5.1. Label Encoder Application </a></li>
#                 <li><a href="#52">5.2. Standard Scaler Application</a></li>
#                 <li><a href="#53">5.3. PCA Application </a></li>
#             </ul>
#         </li>
#         <br>
#         <li>
#             <a href="#6">6. M.L. Model Developing</a> 
#              <ul>
#                 <li><a href="#61">6.1. Model Competition</a></li>
#                 <li><a href="#62">6.2. Best KFold Selection</a></li>
#                  <li><a href="#63">6.3. Hyper Parameter Selection</a></li>
#                  <li><a href="#64">6.4. Estimator Model Applying</a></li>  
#             </ul>
#         </li>
#         <br>
#         <li>
#             <a href="#7">7. Try Other 7 Data with Model</a>
#             <ul>
#                 <li><a href="#71">7.1. Clean All Basalt Data</a></li>
#                 <li><a href="#72">7.2. Apply PCA Concat Data</a></li>
#                 <li><a href="#73">7.3. Prepare Target Column</a></li>
#             </ul>
#         </li>
#         <br>
#         <li>
#             <a href="#8">8. Conclusion</a>   
#         </li>
#     </ul>
# </div>

# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id="1">1. FOREWORD</a></h1>

# <div>
#     <font size = "4", color = "#1e5492">
#         I am a Mineral Processing engineer and I am training myself about Data Science. 
#         Unfortunately, there is not much data about mineral processing, so I turned my face into Geology data.
#         Geologist are much closer to new world from mineral processing engineers. :(
#         Thanks to Jack Maughan, he has nice writing in 
#         <a href = "https://medium.com/@jackmaughan_50251/machine-learning-with-orange-vol-2-a5a90f9f3461">here</a>,
#         I met <a href = "http://georoc.mpch-mainz.gwdg.de/georoc/"> GEOROC </a> data sets. These data are real
#         challenges. Hard projects mean good experience. Let's start.
#     </font> 
# </div>

# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "2">2. MEET WITH DATA</a></h1>

# In[1]:


#data import 
import pandas as pd 

basalt1 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part1.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt2 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part2.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt3 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part3.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt4 = pd.read_csv("C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part4.csv", engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt5 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part5.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt6 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part6.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt7 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part7.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)
basalt8 = pd.read_csv('C:/Users/aktar/Desktop/GEOROC verileri/BASALT_part8.csv', engine = 'python',
                      sep=',', quotechar='"', error_bad_lines=False)


# In[2]:


print("Basalt1 rows = %1.0f and Basat1 columns = %1.0f" %(basalt1.shape[0], basalt1.shape[1]))
print("Basalt2 rows = %1.0f and Basat1 columns = %1.0f" %(basalt2.shape[0], basalt1.shape[1]))
print("Basalt3 rows = %1.0f and Basat1 columns = %1.0f" %(basalt3.shape[0], basalt1.shape[1]))
print("Basalt4 rows = %1.0f and Basat1 columns = %1.0f" %(basalt4.shape[0], basalt1.shape[1]))
print("Basalt5 rows = %1.0f and Basat1 columns = %1.0f" %(basalt5.shape[0], basalt1.shape[1]))
print("Basalt6 rows = %1.0f and Basat1 columns = %1.0f" %(basalt6.shape[0], basalt1.shape[1]))
print("Basalt7 rows = %1.0f and Basat1 columns = %1.0f" %(basalt7.shape[0], basalt1.shape[1]))
print("Basalt8 rows = %1.0f and Basat1 columns = %1.0f" %(basalt8.shape[0], basalt1.shape[1]))


# <font size = 5, color = #1e5492>
#     There are 8 data in here. They all have 172 columns. I will try to identfy columns 
# </font>  

# <p style = text-align:left>
#     <font size = 5 color = #1e5492>
#         <b>
#             Columns Names:
#         </b>
#     </font>
# </p> 
# <br>
# <div>
#     <ul>
#         <li><font color = #1e5492><b>0 - CITATIONS: </b></font>I guess we do not need this column</li>
#         <li><font color = #1e5492><b>1 - TECTONIC SETTING :</b></font> This the target column. We will try to identfy Rock Tectonic Tectonic
#             type (I don't want to push you to the wall with Geology terms)
#         </li>
#         <li><font color = #1e5492><b>2 - LOCATION, 3 - LOCATION COMMENT:</b></font> Detailed location values
#         </li>
#         <li>
#             <font color = #1e5492>
#                 <b>4 - LATITUDE MIN, 5 - LATITUDE MAX ,6 -LONGITUDE MIN, 7 - LONGITUDE MAX:</b>
#             </font> Location of samples values
#         </li>
#         <li><font color = #1e5492><b>8 - LAND OR SEA: </b></font> Sample from Land or Sea
#         </li>
#         <li><font color = #1e5492><b>9 - ELEVATION MIN, 10 - ELEVATION MAX:</b></font>
#         </li>
#         <li><font color = #1e5492><b>11 - SAMPLE NAME, 12 - ROCK NAME:</b></font> Definition about samples
#         </li>
#         <li><font color = #1e5492><b>13 - MIN. AGE (YRS.), 14 - MAX. AGE (YRS.):</b></font> Sample Age
#         </li>
#         <li><font color = #1e5492><b>15 - GEOL., 16 - AGE:</b></font> Geological category about Age
#         </li>
#         <li><font color = #1e5492><b>17 - ERUPTION DAY, 18 - ERUPTION MONTH, 19 - ERUPTION YEAR:</b></font>
#         </li>
#         <li><font color = #1e5492><b>20 - ROCK TEXTURE,21 - ROCK TYPE:</b></font>
#         </li>
#         <li><font color = #1e5492><b>22 - DRILL DEPTH MIN , 23 - DRILL DEPTH MAX:</b></font></li>
#         <li><font color = #1e5492><b>24 - ALTERATION:</b></font></li>
#         <li><font color = #1e5492><b>25 - MINERAL:</b></font></li>
#         <li><font color = #1e5492><b>26 - MATERIAL:</b></font></li>
#         <li><font color = #1e5492><b>27 to 60:</b></font>Sample content by weight values</li>
#         <li><font color = #1e5492><b>61 to 69:</b></font>I do not know the means of (CCM/G), (CCMSTP/G),
#         (AT/G), (MOLE/G), (NCC/G) values. 
#         </li>
#         <li><font color = #1e5492><b>71 to 145</b></font> Sample grades by ppm unit
#         </li>
#         <li><font color = #1e5492><b>146 to 169</b></font> Some values about sample. I don't know
#         </li>
#         <li><font color = #1e5492><b>170 - UNIQUE_ID</b></font>
#         </li>
#         <li><font color = #1e5492><b>171 - Unnamed: 171</b></font>
#         </li>

# <font size = 5, color = #1e5492>
#     Look closer to data  
# </font>  

# In[3]:


#is there nan values 
basalt1.isna().sum().values


# In[4]:


#there are lots of nan values in basalt1. Look at other data: 

print("Basalt 2 nan value counts")
print(basalt1.isna().sum().values)
print()
print("Basalt 3 nan value counts")
print(basalt3.isna().sum().values)
print()
print("Basalt 4 nan value counts")
print(basalt4.isna().sum().values)
print()
print("Basalt 5 nan value counts")
print(basalt5.isna().sum().values)
print()
print("Basalt 6 nan value counts")
print(basalt6.isna().sum().values)
print()
print("Basalt 7 nan value counts")
print(basalt7.isna().sum().values)
print()
print("Basalt 8 nan value counts")
print(basalt8.isna().sum().values)


# <font size = 5, color = #1e5492>
#     The nan value situations are same for all basalt data. So I want to work with shortest data, in the name
#     "basalt 3"
# </font> 

# In[5]:


#train data 
train = basalt3.copy()


# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "3">3. DATA CLEANING</a></h1>
# 

# In[6]:


train.isna().sum().values


# In[7]:


#define a function for drop data according to nan values 
def drop_nan_columns(df, number):
    #create a columns list 
    columns = df.columns
    #define a list wtih the name of columns that should be dropped 
    will_drop = list()
    #loop in columns
    for i in range(len(columns)):
        # is nan values equal to number?
        if (df.iloc[:,i].isnull().sum() == number):
            #add the name 
            will_drop.append(columns[i])
    #drop columns
    df = df.drop(columns = will_drop, axis = 1)
    #print the dropped columns number
    print("%1.0f columns dropped" %(len(will_drop)))
    #record new df 
    return df 


# <font size = 5, color = #1e5492>
#     The length of the data is 8457. Some columns seems like empty. I want to drop them first
# </font> 

# In[10]:


train = drop_nan_columns(train, 8457)
train.isna().sum()


# <font size = 5, color = #1e5492>
#     TECTONIC SETTING columns is target column. NaN values as unacceptable. 
# </font> 

# In[9]:


train = train[train['TECTONIC SETTING'].notna()]
train.isna().sum().values


# <font size = 5, color = #1e5492>
#     I want to look closer to columns 
# </font> 

# In[11]:


#print all columns name
train.columns.values


# In[12]:


#what is the data types of columns
train.dtypes.values


# <font size = 5 color = 1e5492>
#     I want to focus on 'OBJECT' data types columns.
# </font>
# 

# In[13]:


#create a function for objecty dtypes columns seperation
def define_objects(df):
    #columns list 
    columns = df.columns
    #define the list with name of columns that data types is object 
    objects_list = list()
    #loop in columns list 
    for i in range(len(columns)):
        #if column data types is object 
        if df.iloc[:,i].dtypes == 'object':
            #add columns name into the list 
            objects_list.append(columns[i])
    #print number of object columns 
    print('%1.0f columns dtypes are object' % (len(objects_list)))
    #define new data
    object_data = df[objects_list]
    return object_data


# In[14]:


#new data with the object data 
object_data = define_objects(train)
object_data.dtypes


# In[15]:


#look the data 
object_data.head(20)


# <font size = 4 color = #1e5492>
#     Columns Examination 
# </font>
# <hr>
# <div>
#     <ul>
#         <li><b><font color = #1e5492>CITATIONS:</font></b> This columns tell nothing to me. DROP</li>
#         <li><b><font color = #1e5492>TECTONIC SETTING:</font></b> Target column. Looks like categorical</li>
#         <li><b><font color = #1e5492>LOCATION:</font></b>Long string. I can not use it Drop!!!</li>
#         <li><b><font color = #1e5492>LOCATION COMMENT:</font></b>Long string. I can not use it Drop!!!</li>
#         <li><b><font color = #1e5492>LAND OR SEA:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>SAMPLE NAME:</font></b>Special codes. Can't use it. Drop!!!</li>
#         <li><b><font color = #1e5492>ROCK NAME:</font></b>Categorical. Love it!></li>
#         <li><b><font color = #1e5492>MIN. AGE (YRS.):</font></b>Ages good but lots of data is nan. Drop!!!</li>
#         <li><b><font color = #1e5492>MAX. AGE (YRS.):</font></b>Ages good but lots of data is nan. Drop!!!</li>
#         <li><b><font color = #1e5492>GEOL.:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>AGE:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>ROCK TEXTURE:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>ROCK TYPE:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>ALTERATION:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>MINERAL:</font></b>Long string. I can not use it Drop!!!</li>
#         <li><b><font color = #1e5492>MATERIAL:</font></b>Categorical. Love it!</li>
#         <li><b><font color = #1e5492>UNIQUE_ID:</font></b>Nothing to tell me. Drop!!!</li>
#     </ul>
# </div>

# In[16]:


#drop examination results 
dropped_columns_from_object = ["CITATIONS", 
                              "LOCATION",
                             "LOCATION COMMENT",
                             "SAMPLE NAME",
                             "MIN. AGE (YRS.)",
                             "MAX. AGE (YRS.)",
                             "MINERAL",
                             "UNIQUE_ID"]
object_data = object_data.drop(columns = dropped_columns_from_object, axis = 1)


# In[17]:


#change the other columns to categorical 
columns = object_data.columns 
object_data[columns] = object_data[columns].astype('category')
print(object_data.dtypes)


# In[18]:


object_data.head(10)


# <font size = 5 color = #1e5492>
#     There are unwanted numbers inside rows. I want to clean them
# </font>

# In[19]:


#remove values inside square brackets

object_data['ROCK NAME'] = object_data['ROCK NAME'].str.replace(r"(\s*\[.*?\]\s*)", "")
object_data['AGE'] = object_data['AGE'].str.replace(r"(\s*\[.*?\]\s*)", "")
object_data['MATERIAL'] = object_data['MATERIAL'].str.replace(r"(\s*\[.*?\]\s*)", "")
object_data['GEOL.'] = object_data['GEOL.'].str.replace(r"(\s*\[.*?\]\s*)", "")
object_data['ROCK TEXTURE'] = object_data['ROCK TEXTURE'].str.replace(r"(\s*\[.*?\]\s*)", "")

object_data.head(20)


# In[20]:


#discahrge train data. I need to space for work 
#first drop object_data columns 
train = train.drop(columns = object_data.columns.values, axis = 1)

#after drop already dropped columns 
train = train.drop(columns = dropped_columns_from_object, axis = 1)

train.columns


# <font size = 5 color = #1e5492>
#     Go back to the "train" data."ppm" values and "wt" values are laboratory mesurement results. I will seperate
#     them from main data and fill the NaN values with 0. 
# </font>

# In[21]:


#function for find specific columns 
def find_column_names(df,name):
    #list for specific name
    specific_name = list()
    # df columns name list 
    columns = df.columns
    #loop in columns
    for column in columns: 
        #if sprecific name inside column name
        if name in column:
            #add column name in specific_name
            specific_name.append(column)
    #create new df with specific columns
    new_df = df[specific_name]
    #record new_df
    return new_df


# In[22]:


#create ppm data 
ppm_data = find_column_names(train, '(PPM)')
print('ppm_data columns:')
print()
print(ppm_data.columns.values)
print()
#create wt data 
wt_data = find_column_names(train, '(WT%)')
print('wt_data columns:')
print()
print(wt_data.columns.values)


# In[23]:


#fill ppm and wt data NaN values with 0 
ppm_data = ppm_data.fillna(0)
print('ppm_data NaN values count:')
print()
print(ppm_data.isna().sum().values)
print()
wt_data = wt_data.fillna(0)
print('wt_data NaN values count:')
print()
print(wt_data.isna().sum().values)


# In[24]:


#discahrge train data. I need to space for work

#drop ppm_data columns
train = train.drop(columns = ppm_data.columns.values, axis = 1)

#drop wt_data columns
train = train.drop(columns = wt_data.columns.values, axis = 1)

train.columns.values


# In[25]:


train.shape


# <font size = 5 color = #1e5492>
#     Go back to the "train" data. Let's count again NaN values
# </font>

# In[26]:


# train data NaN values count 
train.isna().sum()


# <font size = 5 color = #1e5492>
#     I will delete all columns except Latitude and Longitude columns. I do not know nothing about last 21
#     columns.Maybe they are also labaratory results and I can fill them wtih zero same like ppm and wt data but I
#     can not find reliable resource about definition of them. If this is a mistake, excuse me Geologists :(
# </font>

# In[27]:


#create a langitude and latitude data
lat_lon_data = train.iloc[:,0:4]
lat_lon_data.head()


# <font size = 5 color = #1e5492>
#     It is time to bring together main data
# </font>

# In[28]:


#first categoric data 
data = object_data
data = data.join(lat_lon_data)
data = data.join(wt_data)
data = data.join(ppm_data)
data.head()


# In[29]:


#look again for NaN values 
data.isna().sum().values


# In[30]:


# third, fourth, fifth and seventh columns have nan values 
print('NaN values content columns:')
print(data.columns[3],data.columns[4],data.columns[5], data.columns[7] )


# <font size = 5 color = #1e5492>
#     I know that these columns are categorical. Can I fill them with usign rest of the data? I want to start with
#     AGE column. It has the least NaN value.
# </font>

# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "4"> 4. COLUMN DATA FILLING</a></h1>

# <h3><a id = "41">4.1. AGE column filling</a></h3>

# In[31]:


#create a data from other categorical columns 
data_forAge = data[['ROCK NAME', 'ROCK TYPE', 'MATERIAL']]

#create a list for age 
list_for_ageRAW = [0] * len(data_forAge)

#concat data_for_age rows 
for i in range(len(data_forAge)):
    list_for_ageRAW[i] = (data_forAge.iloc[i,0] + data_forAge.iloc[i,1] + data_forAge.iloc[i,2])
    
#group columns according to age values 
group_for_age = data.groupby(['ROCK NAME', 'ROCK TYPE', 'MATERIAL'])['AGE'].value_counts()

#list for grouped 
list_for_ageGrouped = [0] * len(group_for_age)

#list for age grouped 2 
age_listGrouped = [0] * len(group_for_age)

#concat grouped list rows for comparison
for x in range(len(group_for_age)):
    list_for_ageGrouped[x] = group_for_age.index.values[x][0] + group_for_age.index.values[x][1] + group_for_age.index.values[x][2]
    age_listGrouped[x] = group_for_age.index.values[x][3]

#age darta 
age = data['AGE']

#record before NaN values counts
age_null_before = age.isnull().sum()
print('NaN values before filling:')
print(age_null_before)
print()

#make comparison between listes and fill the NaN values
for i in range(len(data)):
    for x in range(len(group_for_age)):
        if list_for_ageRAW[i] == list_for_ageGrouped[x]:
            age[i] = age_listGrouped[x]

#record NaN values after filling
age_null_after = age.isnull().sum()
print('NaN values after filling:')
print(age_null_after)
print()

#change age column with new values  
data['AGE'] = age

#record NaN values for Age 
isnull_old = data.isnull().sum()

#delete residual NaN values from main data
data = data[data['AGE'].notna()]

#reset index
data = data.reset_index(drop = True)

#check null values 
isnull = data.isnull().sum()
print('NaN values caunt for all data ')
print(isnull.values)
print()
print('%1.0f values has been filled' % (age_null_after - age_null_before))
print()
print('and %1.0f rows has been deleted' % (age_null_after))


# <h3><a id = "42">4.2. GEOL. column filling</a></h3>

# In[32]:


#create geol data
geol = data['GEOL.']

#list from data 
data_forGeol = data[['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE']]
list_for_geolRAW = []

#concat rows
for i in range(len(data)):
    list_for_geolRAW.append(data_forGeol['ROCK NAME'][i] + data_forGeol['ROCK TYPE'][i] + data_forGeol['MATERIAL'][i]+ data_forGeol['AGE'][i])

#list from group
group_forGeol = data.groupby(['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE'])['GEOL.'].value_counts()
list_for_geolGrouped = []
geol_listedGrouped = []

#concat group data rows
for i in range(len(group_forGeol)):
    list_for_geolGrouped.append(group_forGeol.index.values[i][0] + 
                                group_forGeol.index.values[i][1] +
                                group_forGeol.index.values[i][2] + 
                                group_forGeol.index.values[i][3])
    
    geol_listedGrouped.append(group_forGeol.index.values[i][4])

#record before NaN values
geol_null_before = geol.isnull().sum()
print('NaN values before filling:')
print(geol_null_before)
print()

#comparison and filling
for i in range(len(data)):
    for x in range(len(group_forGeol)):
        if list_for_geolRAW[i] == list_for_geolGrouped[x]:
            geol[i] = geol_listedGrouped[x]

#record after filling NaN values
geol_null_after = geol.isnull().sum()
print('NaN values after filling:')
print(geol_null_after)
print()

#delete residual nan values  
data['GEOL.'] = geol
data = data[data['GEOL.'].notna()]

#reset index 
data = data.reset_index(drop = True)

#record NaN values 
isnull = data.isnull().sum()

print('NaN values caunt for all data ')
print(isnull.values)
print()
print('%1.0f values has been filled' % (geol_null_after - geol_null_before))
print()
print('and %1.0f rows has been deleted' % (geol_null_after))


# <h3><a id = "43">4.3. ROCK TEXTURE column filling</a></h3>

# In[33]:


texture = data['ROCK TEXTURE']

data_forTexture = data[['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE', 'GEOL.']]
list_for_textureRAW = []

for i in range(len(data)):
     list_for_textureRAW.append(data_forTexture['ROCK NAME'][i] + 
                                data_forTexture['ROCK TYPE'][i] + 
                                data_forTexture['MATERIAL'][i] + 
                                data_forTexture['AGE'][i] +
                                data_forTexture['GEOL.'][i])

group_forTexture = data.groupby(['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE', 'GEOL.'])['ROCK TEXTURE'].value_counts()
list_for_textureGrouped = []
texture_listedGrouped = []

for i in range(len(group_forTexture)):
    list_for_textureGrouped.append(group_forTexture.index.values[i][0] + 
                                group_forTexture.index.values[i][1] +
                                group_forTexture.index.values[i][2] + 
                                group_forTexture.index.values[i][3] + 
                                group_forTexture.index.values[i][4])
    
    texture_listedGrouped.append(group_forTexture.index.values[i][5])

texture_null_before = texture.isnull().sum()
print('NaN values before filling:')
print(texture_null_before)
print()

for i in range(len(data)):
    for x in range(len(group_forTexture)):
        if list_for_textureRAW[i] == list_for_textureGrouped[x]:
            texture[i] = texture_listedGrouped[x]

texture_null_after = texture.isnull().sum()
print('NaN values after filling:')
print(texture_null_after)
print()


data['ROCK TEXTURE'] = texture
data = data[data['ROCK TEXTURE'].notna()]
data = data.reset_index(drop = True)
isnull = data.isnull().sum()

print('NaN values caunt for all data ')
print(isnull.values)
print()
print('%1.0f values has been filled' % (texture_null_after - texture_null_before))
print()
print('and %1.0f rows has been deleted' % (texture_null_after))


# <h3><a id = "44">4.4. ALTERATION column filling</a></h3>

# In[34]:


data_forAlteration = data[['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE', 'GEOL.', 'ROCK TEXTURE']]
list_for_alterationRAW = []

for i in range(len(data)):
      list_for_alterationRAW.append(data_forAlteration['ROCK NAME'][i] + 
                                data_forAlteration['ROCK TYPE'][i] + 
                                data_forAlteration['MATERIAL'][i] + 
                                data_forAlteration['AGE'][i] +
                                data_forAlteration['GEOL.'][i] +
                                data_forAlteration['ROCK TEXTURE'][i])


group_forAlteration = data.groupby(['ROCK NAME', 'ROCK TYPE', 'MATERIAL', 'AGE', 'GEOL.', 'ROCK TEXTURE'])['ALTERATION'].value_counts()
list_for_alterationGrouped = []
alteration_listedGrouped = []

for i in range(len(group_forAlteration)):
    list_for_alterationGrouped.append(group_forAlteration.index.values[i][0] + 
                                group_forAlteration.index.values[i][1] +
                                group_forAlteration.index.values[i][2] + 
                                group_forAlteration.index.values[i][3] + 
                                group_forAlteration.index.values[i][4] +
                                group_forAlteration.index.values[i][5])
    
    alteration_listedGrouped.append(group_forAlteration.index.values[i][6])

alteration = data['ALTERATION']

alteration_null_before = alteration.isnull().sum()
print('NaN values before filling:')
print(alteration_null_before)
print()


for i in range(len(data)):
    for x in range(len(group_forAlteration)):
        if list_for_alterationRAW[i] == list_for_alterationGrouped[x]:
            alteration[i] = alteration_listedGrouped[x]


alteration_null_after = alteration.isnull().sum()
print('NaN values after filling:')
print(alteration_null_after)
print()


data['ALTERATION'] = alteration
data = data[data['ALTERATION'].notna()]
data = data.reset_index(drop = True)
isnull = data.isnull().sum()

print('NaN values caunt for all data ')
print(isnull.values)
print()
print('%1.0f values has been filled' % (alteration_null_after - alteration_null_before))
print()
print('and %1.0f rows has been deleted' % (alteration_null_after))


# In[35]:


#check NaN values 
data.isna().sum().values


# <font size = 5 color = red>
#     <p style = "text-align:center">
#         There is no NaN values. Hooray!!!
#     </p>
# </font>

# In[36]:


print("Data Sahape After Cleaning =", (data.shape))


# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "5"> 5. PRINCIPAL COMPONENET ANALYSIS (PCA)</a></h1>

# <font size = 5 color = #1e5492>
#     There are 109 column in data. From my Mineral Processing experience some ppm and wt result might show same
#     behaviour.I examined how I can reduce this columns and met the PCA. This is my first time to apply PCA.
#     <hr>
#     I will separate data to "attributes", "lat_lon"(Longitudes and Latitudes), "ppm" and "wt" parts and apply PCA
#     in itself for every part. 
#     <hr>
# </font>
# <font size = 5 color = red>
#     <em>
#         If you see any problem or have any idea about this type of PCA application, please do not hesitate to
#         contact me.
#     </em>
# </font> 
# 

# In[235]:


#seperate parts 
target = data['TECTONIC SETTING']
print("Shape of target data =", target.shape)
print("Data Types of target data =", target.dtypes)
print()

attributes = data.iloc[:,1:9]
column_attributes = attributes.columns
attributes_shape_before_PCA = attributes.shape
print("Shape of attributes data before PCA =", attributes_shape_before_PCA)
print("Data Types of attributes data =")
print(attributes.dtypes)
print()

lat_lon = data.iloc[:,9:13]
column_lat_lon = lat_lon.columns
lat_lon_shape_before_PCA = lat_lon.shape
print("Shape of lat_lon data before PCA =", lat_lon_shape_before_PCA)
print("Data Types of lat_lon data =")
print(lat_lon.dtypes)
print()

ppm = find_column_names(data, '(PPM)')
column_ppm = ppm.columns
ppm_shape_before_PCA = ppm.shape
print("Shape of ppm data before PCA =", ppm_shape_before_PCA)
print("Data Types of ppm data =")
print(ppm.dtypes)
print()

wt = find_column_names(data, '(WT%)')
column_wt = wt.columns
wt_shape_before_PCA = wt.shape
print("Shape of wt data before PCA =", wt_shape_before_PCA)
print("Data Types of wt data =")
print(wt.dtypes)
print()


# In[40]:


#transform all attributes data type to categorical 
attributes = attributes.astype('category')
print("Data Types of attributes data =")
print(attributes.dtypes)


# <h3><a id = "51">5.1. Label Encoder Application</a></h3>

# In[41]:


from sklearn.preprocessing import LabelEncoder

le_attributes = LabelEncoder() #special name for inverse transofrm need in future
attributes = attributes.apply(le_attributes.fit_transform)

print("Attributes data after label encoder application")
print()
attributes.head(10)


# <h3><a id = "52">5.2. Standard Scaler Application</a></h3>

# In[42]:


#Standard Scaller import
from sklearn.preprocessing import StandardScaler

#Standard Scaler for ppm 
ppm = StandardScaler().fit_transform(ppm.values)

#Standard Scaler for wt 
wt = StandardScaler().fit_transform(wt.values)

#Standard Scaler for lat_lon 
lat_lon = StandardScaler().fit_transform(lat_lon.values)


# In[43]:


print("ppm after standard scaler")
print(ppm)
print()

print("wt after standard scaler")
print(wt)
print()

print("lat_lon after standard scaler")
print(lat_lon)
print()


# <h3><a id = "53">5.3. PCA Application</a></h3>

# In[44]:


#import pca 
from sklearn.decomposition import PCA
pca = PCA(0.95)

#PCA for attributes
attributes = pca.fit_transform(attributes)
attributes_shape_after_PCA = attributes.shape
print("attributes shape after PCA=",attributes_shape_after_PCA)
print('%1.0f columns has been decreased from attributes' 
      %(attributes_shape_before_PCA[1]-attributes_shape_after_PCA[1]))
print()

#PCA for lat_lon
lat_lon = pca.fit_transform(lat_lon)
lat_lon_shape_after_PCA = lat_lon.shape
print("lat_lon shape after PCA=",lat_lon_shape_after_PCA)
print("%1.0f columns has been decreased from lat_lon" 
      % (lat_lon_shape_before_PCA[1]-lat_lon_shape_after_PCA[1]))
print()

#PCA for ppm
ppm = pca.fit_transform(ppm)
ppm_shape_after_PCA = ppm.shape
print("ppm shape after PCA=",ppm_shape_after_PCA)
print("%1.0f columns has been decreased from ppm" 
      % (ppm_shape_before_PCA[1]-ppm_shape_after_PCA[1]))
print()

#PCA for wt
wt = pca.fit_transform(wt)
wt_shape_after_PCA = wt.shape
print("wt shape after PCA=",wt_shape_after_PCA)
print("%1.0f columns has been decreased from wt" 
      % (wt_shape_before_PCA[1]-wt_shape_after_PCA[1]))


# In[45]:


#Data Re-Group after PCA Application 

df_attributes = pd.DataFrame(data = attributes, 
                             columns = ["attribute_1", "attribute_2","attribte_3"])

df_lat_lon = pd.DataFrame(data = lat_lon, 
                          columns = ["lat_lon_1","lat_lon_2","lat_lon_3"])
                                       
df_wt = pd.DataFrame(data = wt, 
                     columns = ['wt_1','wt_2','wt_3','wt_4','wt_5','wt_6','wt_7',
                               'wt_8','wt_9','wt_10','wt_11','wt_12','wt_13','wt_14',
                               'wt_15','wt_16','wt_17','wt_18'])

df_ppm = pd.DataFrame(data = ppm) #I want to confess, I didn't want to write 46 columns name one by one

#Create united dataframe except target (Tectonic Settings) column
df = df_attributes
df = df.join([df_lat_lon,df_wt,df_ppm])

df.head(10)


# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "6"> 6. ML MODEL DEVELOPING</a></h1>

# In[325]:


#target column examination 
df_target = pd.DataFrame(data = data['TECTONIC SETTING'])

#df_target only left to did not transfer to numeric. I want to apply it labelEncoder
#First time I decided to transform target data to dummies, but multi dimensional operation is different and 
#I am tired. I came back here and changed dummies to label encoder. 
le_target = LabelEncoder()
target = df_target.apply(le_target.fit_transform)

target.head()


# In[209]:


#see the target values in a bar chart

import seaborn as sns 
import matplotlib.pyplot as plt 
target_dummies = pd.get_dummies(df_target['TECTONIC SETTING'])
sns.set(font_scale = 2)
plt.figure(figsize=(15,8))
categories = df_target['TECTONIC SETTING'].unique()
ax= sns.barplot(categories, target_dummies.sum().values)

plt.title("Tectonic Settings velue Counts", fontsize=24)
plt.ylabel('Number of values', fontsize=18)
plt.xlabel('Tectonic Setting Type', fontsize=18)
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)

#adding the text labels
rects = ax.patches
labels = target.sum().values
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom', fontsize=18)

plt.show()


# <h3><a id = "61">6.1. Model Competition</a></h3>

# In[47]:


#import models 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import KFold, cross_val_score
from numpy import mean


# In[188]:


# models 
def get_models():
    models = list()
    models.append(KNeighborsClassifier())
    models.append(ExtraTreeClassifier())
    models.append(RandomForestClassifier())
    models.append(ExtraTreesClassifier())
    return models

#model competition with k_fold = 10
def model_competition(X,y):
          
    cv = KFold(n_splits = 10, shuffle = True, random_state = 2020)
    models = get_models()
    model_means = list()
    for model in models:
        scores =  cross_val_score(model, X, y, scoring = 'accuracy', cv = cv, n_jobs = -1)
        model_means.append(mean(scores))
        
    return model_means


# In[220]:


#for improve my misarable lap-top I will cut data 
df_competition = pd.DataFrame(data = df.iloc[0:100,:], columns = df.columns)
target_competition = pd.DataFrame(data = target.iloc[0:100,:])


# In[211]:


#lets do the competition
model_means = model_competition(df_competition, target_competition)

#show the competiton results on chart
models = get_models()
models_name = list()

for model in models:
    
    models_name.append(type(model).__name__)

plt.rcParams["figure.figsize"] = (15,10)   
plt.scatter(models_name, model_means)
plt.title('Model Competiton')
plt.xlabel('Model Name')
plt.ylabel('Competiton Results')
plt.xticks(rotation=90)
for a,b in zip(models_name, model_means): 
    plt.text(a, b, str(b)[:5])
plt.show()


# <font size = 6 color = red>
#     <p style = text-align:center>
#         Winner is ExtraTreesClassifier with 0.985.
#     </p>
# </font>

# <h3><a id = "62">6.2. Best KFold Selection</a></h3>

# In[215]:


#fold range
folds = range(2,25)

#competition winner model
model = ExtraTreesClassifier()

#lists for means, minimum and maximum results 
bestK_means, bestK_mins, bestK_maxs = list(), list(), list()

#loop in folds
for k in folds: 
    #define test conditions 
    cv = KFold(n_splits = k, shuffle = True, random_state = 2020)
    #evaluate k value 
    scores =  cross_val_score(model, df_competition, target_competition, scoring = 'accuracy', cv = cv, n_jobs = -1)
    k_mean = mean(scores)
    k_max = scores.max()
    k_min = scores.min()
    print('> folds = %d, accuracy=%.3f (%.3f,%.3f)' % (k, k_mean, k_min, k_max))
            
    bestK_means.append(k_mean)
    bestK_mins.append(k_mean - k_min)
    bestK_maxs.append(k_max - k_mean)


# In[216]:


#show in chart k-fold results 
plt.rcParams['figure.figsize'] = (30,10)
plt.plot(folds, bestK_means)
plt.title('Best K-Fold selection')
plt.xlabel('K folds')
plt.ylabel('Accuracy Mean')
for a,b in zip(folds, bestK_means): 
    plt.text(a, b, str(b)[:5])
plt.show()


# <font size = 6 color = red>
#     <p style = text-align:center>
#         Winner is the 21 KFold with 0.989.
#     </p>
# </font>

# <h3><a id = "63">6.3. Hyper Parameter Selection</a></h3>

# In[249]:


#import Randomized Search 
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import RandomizedSearchCV

#define model 
model = ExtraTreesClassifier(n_jobs = -1, random_state=2020)

#define pipeline
pipeline = Pipeline(steps = [('model', model)])

#define Repeated KFold with 21 splits
cv = RepeatedStratifiedKFold(n_splits=21, n_repeats=3, random_state=2020)
#define extratreesclassifiers hyperparameters 
param_grid = {"model__random_state": [2020], 
              #"n_estimators" : [10,100],
              "model__max_depth": [25, 30, 32, 34, 38, 45],
              "model__criterion": ['gini', 'entropy'],
              "model__min_samples_split": [2,5,10,12,15,17,20],
              "model__min_samples_leaf":[1,2,3,4,5],
              "model__max_features":["auto", "sqrt", "log2"]}

#define RandomizedSearchCV
search = RandomizedSearchCV(pipeline, param_grid, n_iter=500, scoring='accuracy', n_jobs=-1, cv=cv, random_state=2020)

#fit RandomizedSearchCV
search.fit(df_competition, target_competition)

#print results and scores 
print("After RandomizedSearchCV")
print()
print("Best index results is:",search.best_index_)
print()
print("Best score is:",search.best_score_)
print()
print("Best hyperparameter values are:",search.best_params_)


# <h3><a id = "64">6.4. Estimator Model Applying</a></h3>

# In[48]:


#import train test split and apply 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(df, target, test_size = 0.25, random_state = 2020)

#apply searched hyper parameters in model
model = ExtraTreesClassifier(random_state = 2020, 
                            n_jobs = -1,
                            min_samples_split = 5,
                            min_samples_leaf = 1,
                            max_features = 'auto',
                            max_depth = 34,
                            criterion = 'gini')
#fit model
model.fit(X_train, y_train)
#prediction
y_pred = model.predict(X_test)
#score
score = accuracy_score(y_test, y_pred)

print("The score of the model is %0.3f" % (score))


# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "7"> 7. TRY OTHER 7 DATA</a></h1>

# <h3><a id = "71">7.1. Clean All Basalt Data</a></h3>

# In[268]:


def prepare_basalts(df):
    columns = basalt1.columns
    print("Data shape at the begining = ", df.shape)
    print()
    #first drop empty columns. I already defining this function in the name drop_nan_columns 
    print("Drop empty columns")
    print()
    df = drop_nan_columns(df,len(df))
    print("Columns left after drop=", len(df.columns))
    print()
    
    #clean Tectonic Settng  empty rows 
    print("Clean Tectonic Setting NaN values rows from whole data")
    print()
    df = df[df['TECTONIC SETTING'].notna()]
    print('Data shape after delete Tectonic Setting NaN values=', df.shape)
    print()
    
    #seperate object data 
    print("Object Data Seperation")
    objects = define_objects(df)
    #drop useless columns from object_data
    dropped_columns_from_object = ["CITATIONS", 
                              "LOCATION",
                             "LOCATION COMMENT",
                             "SAMPLE NAME",
                             "MIN. AGE (YRS.)",
                             "MAX. AGE (YRS.)",
                             "MINERAL",
                             "UNIQUE_ID"]
    objects = objects.drop(columns = dropped_columns_from_object, axis = 1)

    #change object_data columns to category
    objects[['TECTONIC SETTING', 'LAND OR SEA', 'ROCK NAME', 'GEOL.', 'AGE',
       'ROCK TEXTURE', 'ROCK TYPE', 'ALTERATION', 'MATERIAL']] = objects[['TECTONIC SETTING', 'LAND OR SEA', 'ROCK NAME', 'GEOL.', 'AGE',
       'ROCK TEXTURE', 'ROCK TYPE', 'ALTERATION', 'MATERIAL']].astype('category')


    #clean object data rows  
    objects['ROCK NAME'] = objects['ROCK NAME'].str.replace(r"(\s*\[.*?\]\s*)", "")
    objects['AGE'] = objects['AGE'].str.replace(r"(\s*\[.*?\]\s*)", "")
    objects['MATERIAL'] = objects['MATERIAL'].str.replace(r"(\s*\[.*?\]\s*)", "")
    objects['GEOL.'] = objects['GEOL.'].str.replace(r"(\s*\[.*?\]\s*)", "")
    objects['ROCK TEXTURE'] = objects['ROCK TEXTURE'].str.replace(r"(\s*\[.*?\]\s*)", "")
    print("Objects Data is ready")
    print()
    
    print("ppm, wt, lat_lon data preperation")
    print()
    #seperate ppm data
    ppm = find_column_names(df, ('PPM'))
    
    #fill ppm data NaN values with 0 
    ppm = ppm.fillna(0)
    
    #seperate wt data
    wt = find_column_names(df, ('WT%'))
    #fill wt data NaN values with 0 
    wt = wt.fillna(0)
    
    #seperate a langitude and latitude data
    lat_lon = df.iloc[:,4:8]
    
    print("ppm, wt, lat_lon data are ready")
    print()
    
    #columns counts 
    print("Columns Counts")
    print("object columns count", len(objects.columns))
    print("ppm columns count", len(ppm.columns))
    print("wt columns count", len(wt.columns))
    print("lat_lon columns count", len(lat_lon.columns))
    print()
          
    #join date together 
    print("data re-union")
    print()
    data = objects
    data = data.join(lat_lon)
    data = data.join(wt)
    data = data.join(ppm)
    print("data shape after re-union", data.shape)
    print()
    
    #this time o dont need to fill data. So, I will drop whole NaN rows from object data
    print("Drop all NaN rows")
    print()
   
    data = data[data['ROCK TEXTURE'].notna()] 
    data = data[data['GEOL.'].notna()] 
    data = data[data['AGE'].notna()]
    data = data[data['ALTERATION'].notna()]
    print("final data shape", data.shape)
    
    return data


# In[269]:


#clean basalt1
basalt1_clean = prepare_basalts(basalt1)


# In[270]:


#clean basat2 
basalt2_clean = prepare_basalts(basalt2)


# In[271]:


#clean basalt4
basalt4_clean = prepare_basalts(basalt4)


# In[272]:


#clean basalt 5
basalt5_clean = prepare_basalts(basalt5)


# In[273]:


#clean basalt6 
basalt6_clean = prepare_basalts(basalt6)


# In[274]:


#clean basalt7
basalt7_clean = prepare_basalts(basalt7)


# In[275]:


#clean basalt8 
basalt8_clean = prepare_basalts(basalt8)


# <font size = 5 color = #1e5492>
#     There is not a standard between data about columns. ppm and wt columns counts are different of them. I will
#     concat these data becouse we do not have much rows for ML. I want to see result of the PCA on concat data.
# </font>

# In[282]:


#concat data 
concat = pd.concat([basalt1_clean,
                   basalt2_clean,
                   basalt4_clean,
                   basalt5_clean,
                   basalt6_clean,
                   basalt7_clean,
                   basalt8_clean])

print("concat data shape", concat.shape)


# In[289]:


#check columns 
concat.columns.values


# In[293]:


#check NaN values 
concat.isna().sum().values


# <font size = 5 color = #1e5492>
#     Every NaN values belog to ppm and wt values. I will fill tham with 0
# </font>

# In[294]:


concat = concat.fillna(0)
#check NaN values 
concat.isna().sum().values


# <h3><a id = "72">7.2. Apply PCA Concat Data</a></h3>

# In[295]:


#deploy pca 
pca = PCA(0.95)

#PCA for objects
le_objects_concat = LabelEncoder() #label encoder application
objects_concat = concat.iloc[:,1:9]
objects_concat = objects_concat.apply(le_objects_concat.fit_transform)
objects_concat_shape_before_PCA = objects_concat.shape
objects_concat = pca.fit_transform(objects_concat)
objects_concat_shape_after_PCA = objects_concat.shape
print("objects_concat shape after PCA=",objects_concat_shape_after_PCA)
print('%1.0f columns has been decreased from objects_concat' 
      %(objects_concat_shape_before_PCA[1]-objects_concat_shape_after_PCA[1]))
print()

#PCA for lat_lon
lat_lon_concat = concat.iloc[:,9:13]
lat_lon_concat = StandardScaler().fit_transform(lat_lon_concat.values)
lat_lon_concat_shape_before_PCA = lat_lon_concat.shape
lat_lon_concat = pca.fit_transform(lat_lon_concat)
lat_lon_concat_shape_after_PCA = lat_lon_concat.shape
print("lat_lon_concat shape after PCA=",lat_lon_concat_shape_after_PCA)
print("%1.0f columns has been decreased from lat_lon" 
      % (lat_lon_concat_shape_before_PCA[1]-lat_lon_concat_shape_after_PCA[1]))
print()

#PCA for ppm
ppm_concat = find_column_names(concat, ('PPM'))
ppm_concat = StandardScaler().fit_transform(ppm_concat.values)
ppm_concat_shape_before_PCA = ppm_concat.shape
ppm_concat = pca.fit_transform(ppm_concat)
ppm_concat_shape_after_PCA = ppm_concat.shape
print("ppm shape after PCA=",ppm_concat_shape_after_PCA)
print("%1.0f columns has been decreased from ppm" 
      % (ppm_concat_shape_before_PCA[1]-ppm_concat_shape_after_PCA[1]))
print()

#PCA for wt
wt_concat = find_column_names(concat, ('WT%'))
wt_concat = StandardScaler().fit_transform(wt_concat.values)
wt_concat_shape_before_PCA = wt_concat.shape
wt_concat = pca.fit_transform(wt_concat)
wt_concat_shape_after_PCA = wt_concat.shape
print("wt shape after PCA=",wt_concat_shape_after_PCA)
print("%1.0f columns has been decreased from wt" 
      % (wt_concat_shape_before_PCA[1]-wt_concat_shape_after_PCA[1]))


# In[299]:


#transform PCA date to the data frame 
df_objects_concat = pd.DataFrame(data =objects_concat, columns = ['attribute_1', "attribute_2","attribute_3"])
df_lat_lon_concat = pd.DataFrame(data =lat_lon_concat, columns = ["lat_lot_1", "lat_lot_2"])
df_wt_concat = pd.DataFrame(data = wt_concat, columns = ["wt_1","wt_2","wt_3","wt_4","wt_5",
                                                        "wt_6","wt_7","wt_8","wt_9","wt_10","wt_11"])
df_ppm_concat = pd.DataFrame(data = ppm_concat)


# In[304]:


df_wt_concat.shape


# In[310]:


#back together concat data 
concat_pca = df_objects_concat
concat_pca = concat_pca.join(df_lat_lon_concat)
concat_pca = concat_pca.join(df_wt_concat)
concat_pca = concat_pca.join(df_ppm_concat)

print("shape of concat_pca", concat_pca.shape)
concat_pca.head()


# <h3><a id = "73">7.3. Prepare Target Column</a></h3>

# In[326]:


le_concat_target = LabelEncoder()
target_concat = le_concat_target.fit_transform(concat['TECTONIC SETTING'])


# <h3><a id = "74">7.4. Feed ML Method </a></h3>

# In[327]:



print("df shape", df.shape)
print("target shape", target.shape)

print("concat_pca shape", concat_pca.shape)
print("target_concat shape", target_concat.shape)


# In[324]:


#prediction
y_pred = model.predict(concat_pca)
#score
score = accuracy_score(target, y_pred)

print("The score of the model is %0.3f" % (score))


# <hr style="border: none; border-bottom: 2px solid lightblue;">

# <h1><a id = "8"> 8. CONCLUSION</a></h1>

# <font size = 5 color = #1e5492>
#     Don't panic!!! I know there is an error code in there. I let it to be there because, I wanted to think on it.
#     In training data there were 70 columns for training but after cleaning concat data had only 36 columns. Model
#     did not worked as you could see above. The golden question:
# </font>
# <br>
# <br>
# <font size = 5 color = red>
#     <p style = text-align:center>
#         What would you do,if you were me, at this point?
#     </p>
# </font>
# <br>
# <font size = 5 color = #1e5492>
#     The first thing I thought, PCA usage could be mistake. I checked the all basalt data again and I realized,
#     there is no standard between columns especially between ppm and wt% columns. 
# </font>
# <font size = 5 color = #1e5492>
#     Maybe if I concat whole data at the beginning, I have could use all of them. I wanted to train ML with 1 data
#     and test the ML performance with others. Simulation of real world... I failed :) 
# </font>
# <br>
# <br>
# <font size = 5 color = #1e5492>
#     I learned much and I felt more and more ignorant while create this project, I hope you spent nice time with me.
# </font>
# <br>
# <br>
# <font size = 5 color = black>
#     <p style = text-align:right>
#         <em>
#             thank you for your patience
#             <br>
#             <br>
#             Best Regards            
#         </em>
#     </p> 
# </font>
# <hr>
# <br>
# <font size = 5 color = #1e5492>
#     <p style = text-align:center>
#         Aydin Aktar 
#         <br>
#         <br>
#         Mineral Processing Engineer 
#         <br>
#         <br>
#         aktaraydin@gmail.com
#         <br>
#         <br>
#         See you on next project...
#     </p>
# </font>    

# In[ ]:




