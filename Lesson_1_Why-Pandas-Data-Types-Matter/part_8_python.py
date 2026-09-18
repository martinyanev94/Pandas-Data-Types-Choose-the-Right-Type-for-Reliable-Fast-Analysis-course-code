df = pd.DataFrame([

    ["foo", 1, 123.45],

    ["bar", 2, 333.33],

    ["baz", 3, 999.99],

], columns=list("abc"))

df.dtypes



df.astype({

    "a": pd.StringDtype(),

    "b": pd.Int64Dtype(),

    "c": pd.Float64Dtype(),

}).dtypes
