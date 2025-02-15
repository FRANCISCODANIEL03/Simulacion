from prepare_ds import prepare_dataset

x_train_prep, x_val_prep, x_test_prep = prepare_dataset()

def red_ds():
    # Reducir el DataSet para representarlo graficamente 
    x_train_reduced = x_train_prep[['Area', 'ConvexArea'].copy()]
    x_val_reduced = x_val_prep[['Area','ConvexArea'].copy()]

    return x_train_reduced, x_val_reduced