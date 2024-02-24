from typing import Generator
from emojis import Emojis


def main() -> None:
    prompt = input('Input: ')
    
    for emoji in get_Emoji(prompt):
        if emoji in Emojis.catalogue:
            prompt = prompt.replace(emoji, Emojis.catalogue[emoji])
    else: 
        print(prompt)
    
    with open('em.txt', 'r', encoding='utf-8') as f:
        #NOTE: Implement the function above, but with the file
        print(f.read(100))

    
def get_Emoji(prompt: str) -> Generator[str]:
    i_0 = i_f = 0
    for i in range(prompt.count(':')):
        if not (i_0 := prompt.find(':', i_f)) == -1:
            if not (i_f:=prompt.find(':', i_0+1)) == -1:
                if ' ' not in (emo:=prompt[i_0 : i_f+1]):
                    yield emo
            
          
main()