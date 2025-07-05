from langchain_community.llms  import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from  dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type,pet_color):
    llm=OpenAI(temperature=0.7)
    prompt=PromptTemplate(
        input_variables=["animal_type","pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it,it is {pet_color} in color .Suggest me six cool names for my pet ",
    )
    chain=LLMChain(llm=llm,prompt=prompt)
    name_chain=chain.run(animal_type=animal_type, pet_color=pet_color)
    return name_chain
if __name__=="__main__":
    print (generate_pet_name("dog","orange brown"))