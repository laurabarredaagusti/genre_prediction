from utils.functions import *

# Correct directory
os.chdir('/Users/laurabarreda/Documents/The_Bridge/genre_prediction/SRC/utils') 

# Read train dataset
train_data = pd.read_csv(train_data)

# Divide features and target
X = train_data.drop('genre', axis=1)
y = train_data['genre']

# Train the Random Forest Classifier model with the chosen params
rfc = RandomForestClassifier(max_depth=25, min_samples_leaf=1, min_samples_split=5, n_estimators=1200)
rfc.fit(X, y)

# Set the name of the resulting model
date = str(datetime.today().strftime('%y%m%d%H%M%S'))
name = filename + date
path = model_path + name

# Save it as pickle
with open(path, 'wb') as archivo_salida:
    pickle.dump(rfc, archivo_salida)

