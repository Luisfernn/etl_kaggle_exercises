def validate_data(df: pd.DataFrame) -> pd.DataFrame:

    expected_cols = ["expected_total", "diff", "suspect_transictions"]
    for col in expected_cols:
        if col not in df.colmuns:
            logger.waring(f"⚠️ Coluna ausente: {col}")

    numeric_cols = ["total_spent", "price_per_unit," "quantity"] 
    for col in numeric_cols:
        if df[col].isna().any:
            logger.waring(f"⚠️ Valores ausentes em {col}")

    inconsistents = (df["expected_total"] - (df["price_per_unit"] * df["quantity"])).abs() > 0.01
    if inconsistents.any():
        logger.waring(f"⚠️ {inconsistents.sum()} inconsistências detectadas entre o esperado e o calculado.")

    logger.info("✅ Validação concluída com sucesso.")    
    return df