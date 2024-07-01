# Leiaute dos arquivos

### `pessoas.gz.parquet`
| Atributo      | Tipo      | Obs                                               | 
| ---           | ---       | ---                                               |
| ID_PESSOA     | long      | O identificador da pessoa                         | 
| CPF           | string    | O cadastro de pessoa física da pessoa no Brasil   | 
| NOME          | string    | O nome da pessoa                                  | 
| MUNICIPIO     | string    | O município (cidade) onde a pessoa reside         | 
| UF            | string    | O estado onde a pessoa reside                     | 

### `valores.gz.parquet`

| Atributo          | Tipo      | Obs                                               | 
| ---               | ---       | ---                                               |
| ID_PAGAMENTO      | string    | O identificador do pagamento (uuid4)              | 
| ID_PESSOA         | long      | O identificador da pessoa                         | 
| VALOR             | float     | O valor pago pela pessoa ("." como ponto decimal) | 
| MES_COMPETENCIA   | integer   | O mês de competência do pagamento                 | 

