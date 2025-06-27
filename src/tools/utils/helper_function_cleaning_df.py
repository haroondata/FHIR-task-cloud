def clean_fhir_column_names(df):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    df.columns = (
        df.columns
        .str.replace(r'\.', '_', regex=True)          # replace dots with underscores
        .str.replace(r'\W+', '_', regex=True)         # remove weird characters
        .str.strip('_')                               # trim leading/trailing underscores
        .str.lower()                                  # lowercase for uniformity
       )


    return df