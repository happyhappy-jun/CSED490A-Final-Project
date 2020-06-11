def get_catagorical(train):
    output = []
    for col in [x for x in train.columns]:
        if (type(train[col][0]) == str):
            output.append(col)
    return output