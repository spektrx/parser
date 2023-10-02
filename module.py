from urllib.parse import urlparse
import re

def ping_url(url):
    
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
    



def pars_web(title, sourse, url, date="today"):
    if ping_url(url):


        if date == "today":
            from datetime import date

            today = date.today()
            date = today.strftime("%d.%m.%y")
        text = f"{title} [Электронный ресурс]//{sourse} URL: {url} (дата обращения: {date})"

        return text
    else:
        raise ValueError("Ссылка не работает")
        

def pars_book(authors, name, publisher, pages):
    if len(authors.split(", ")) < 4:
        text = f"{authors} {name}. {publisher}, C. {pages}."
    else:
        text = f"{name}/{authors}. {publisher}, C. {pages}."

    return text
    
def bookcheck(string):
    pattern = r'^([А-ЯЁ][а-яё]+\s[А-ЯЁ]\.[А-ЯЁ]\.,\s){2}[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.[А-ЯЁ]\.\s.+?\s:\s.+?\.\sМ\.\s:\s[А-ЯЁA-Z]+\,\s\d{4},\s[CС]\.\s\d+\.$'



    if re.match(pattern, string):
        return True
    else:
        return False

    
def webcheck(string):
    pattern = r"\{.*\} \[электронный ресурс\]\/\/\{.*\} URL:\{.*\} \(дата обращения: \{.*\}\)"

    if re.match(pattern, string):
        return True
    else:
        return False
