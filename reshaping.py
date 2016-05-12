def unstack(df, i_col, p_col, v_col):
    cats = df.select(p_col).distinct().sort(p_col).toPandas()[p_col].tolist()
    for i in range(len(cats)):
        if i == 0:
            wide = df[(df[p_col] == cats[i])].select(i_col, v_col).withColumnRenamed(v_col, cats[i])
        else:
            wide = wide.join(df[(df[p_col] == cats[i])].select(i_col, v_col).withColumnRenamed(v_col, cats[i]), on=i_col, how='outer')
    return wide