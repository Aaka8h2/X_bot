
import traceback





def check_cc(numb,month,year,cvv):
    try:
        if '<Insufficient funds message>' in response:
            return {"status":"False","message":"Your card has insufficient funds"}
        elif '<charge message>' in response:
            return {"status":"True","message":"charge"}
        else:
            error_message = '<scrap error message from html or json>'
            return {"status":"Error","message":f"{error_message}"}

    except Exception as e:
        error_message = traceback.format_exc()
        with open('error.txt','a',encoding='utf-8') as f:
            f.write(f'{numb} {month} {year} {cvv}\n{error_message}\n\n\n')
        print(f"\033[33m {error_message} \033[0m ")
        return {"status":"Error","message":"Error request"}