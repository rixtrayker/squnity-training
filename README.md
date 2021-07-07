# squnity-training
**Squnity training scripts** a repo containing my tasks code.


## Cloing :

```bash
git clone https://github.com/rixtrayker/squnity-training.git
```

## Scripts inside :
1. **`wordpress-checker.py`**
    
    ***Single URL***
    ```bash
    python wordpress-checker.py -u example.com -w wordpress-paths.txt
    ```
    ***URLs from input file***
    ```bash
    python wordpress-checker.py -i domains.txt -w wordpress-paths.txt
    ```
    ***Output file is optional***
    ```bash
    python wordpress-checker.py -i domains.txt -w wordpress-paths.txt -o out.txt
    ```