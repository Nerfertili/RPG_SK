#https://dnd5spells.rpgist.net/pt-BR/spells
#<a href="https://dnd5spells.rpgist.net/pt-BR/">https://dnd5spells.rpgist.net/pt-BR/</a>spells?klass_name=patrulheiro
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

spells = []

driver.get('https://dnd5spells.rpgist.net/pt-BR/spells')
time.sleep(5)
for i in driver.find_elements(By.TAG_NAME,'input'):
    if i.get_attribute('ng-model')=='itemsPerPage':
        i.send_keys(Keys.BACK_SPACE)
        i.send_keys(Keys.BACK_SPACE)
        i.send_keys('319')
        i.send_keys(Keys.ENTER)
        break
time.sleep(5)

soup = bs(driver.page_source,"html.parser")

spell_html = soup.find_all('spell', {'model': 'spell'})

spells = []

for spell in spell_html:
    try:
        casters = ''
        if spell.find('a', {'ng-bind': '::caster.name'})!=None:
            for i in spell.find_all('a', {'ng-bind': '::caster.name'}):
                casters+= '-'+i.get_text()
        else:
            pass
        spells.append(
            {
                'Name': spell.find('span', {'ng-bind': 'spell.name'}).get_text() if spell.find('span', {'ng-bind': 'spell.name'})!=None else '',
                'OriginalName': spell.find('span', {'ng-bind': 'spell.originalName'}).get_text() if spell.find('span', {'ng-bind': 'spell.originalName'})!=None else '' ,
                'CasterName': casters,
                'CastingTime': spell.find('span', {'ng-bind': 'spell.castingTime'}).get_text() if spell.find('span', {'ng-bind': 'spell.castingTime'})!=None else '',
                'CastingTimeUnit': spell.find('span', {'ng-bind': 'spell.castingTimeUnit'}).get_text() if spell.find('span', {'ng-bind': 'spell.castingTimeUnit'})!=None else '',
                'Range': spell.find('span', {'ng-bind': 'spell.range'}).get_text() if spell.find('span', {'ng-bind': 'spell.range'})!=None else '',
                'RangeUnit': spell.find('span', {'ng-bind': 'spell.rangeUnit'}).get_text() if spell.find('span', {'ng-bind': 'spell.rangeUnit'})!=None else '',
                'Duration': spell.find('span', {'ng-bind': 'spell.duration'}).get_text() if spell.find('span', {'ng-bind': 'spell.duration'})!=None else '',
                'DurationUnit': spell.find('span', {'ng-bind': 'spell.durationUnit'}).get_text() if spell.find('span', {'ng-bind': 'spell.durationUnit'})!= None else '',
                'Description': spell.find('div', {'ng-bind-html': 'spell.description'}).get_text() if spell.find('div', {'ng-bind-html': 'spell.description'})!= None else '',
                'Page': spell.find('span', {'ng-bind': 'reference.page'}).get_text() if spell.find('span', {'ng-bind': 'reference.page'})!=None else '',

            }
        )
    except:
        exit(spell.find('span', {'ng-bind': 'spell.name'}).get_text()+f'------{traceback.format_exc()}')

print(len(spells))
print(spells[1]['CasterName'])