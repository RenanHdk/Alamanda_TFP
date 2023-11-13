import os 
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def h_cortina_explicacao(cortina):
    return json.dumps({"processo": "A higienização começa com uma avaliação detalhada do tecido da cortina para determinar o método de limpeza mais apropriado. Geralmente, utilizamos uma combinação de limpeza a seco e a vapor, que remove sujeiras, poeiras e manchas sem danificar o tecido. Após a limpeza, as cortinas são cuidadosamente secas e passadas, garantindo que mantenham sua forma e aparência original.", "tempo do processo": "O tempo de higienização varia de acordo com o tamanho e o tipo de tecido da cortina. Normalmente, o processo leva entre 2 a 4 horas. No entanto, cortinas maiores ou mais delicadas podem exigir mais tempo para garantir uma limpeza eficaz e cuidadosa."})



def h_cortina_orcamento(cortina):
    return json.dumps({"Entrega e retirada": "R$ 5,00 por kilometro", "Valor fixo": "R$ 20,00", "Valor adicional por metro quadrado de cortina": "R$ 5,00"})



def h_persiana_explicacao(persiana):
    return json.dumps({"processo": "O processo de higienização de persianas começa com uma inspeção cuidadosa para identificar o material e o tipo de sujidade presente. Utilizamos um método de limpeza a seco ou úmido, dependendo do material da persiana. A limpeza inclui a remoção de poeira, manchas e possíveis acúmulos de sujeira entre as lâminas. Em seguida, as persianas são cuidadosamente secas e realinhadas para manter sua funcionalidade e aparência.", "tempo de processo": "O tempo necessário para a higienização varia conforme o tamanho e o tipo de persiana. Geralmente, o processo leva entre 1 a 3 horas. Persianas maiores ou com níveis mais altos de sujeira podem exigir mais tempo para uma limpeza completa e minuciosa."})



def h_persiana_orcamento(persiana):
    return json.dumps({"Entrega e retirada": "R$ 5,00 por kilometro", "Valor fixo": "R$ 25,00", "Valor adicional por metro quadrado de persiana": "R$ 7,00"})



def produtos_cortina(cortina=None, poeira_odor=None, sujeira_mancha=None):
    if poeira_odor!=None and sujeira_mancha==None:
        return json.dumps({"produto": "Spray Revitalizante para Cortinas: Esta solução de limpeza em spray é ideal para a higienização rápida de cortinas, removendo eficazmente poeira e odores, enquanto revitaliza o tecido, mantendo sua cor e textura originais."})
    elif poeira_odor==None and sujeira_mancha!=None:
        return json.dumps({"produto": "Espuma de Limpeza Profunda para Cortinas: Especialmente formulada para cortinas, esta espuma de limpeza penetra profundamente nas fibras, eliminando sujeiras e manchas, e deixando um aroma fresco e suave, sem necessidade de enxágue."})
    else:
        return json.dumps({"produtos": "Os produtos são: Spray Revitalizante para Cortinas: Esta solução de limpeza em spray é ideal para a higienização rápida de cortinas, removendo eficazmente poeira e odores, enquanto revitaliza o tecido, mantendo sua cor e textura originais.Espuma de Limpeza Profunda para Cortinas: Especialmente formulada para cortinas, esta espuma de limpeza penetra profundamente nas fibras, eliminando sujeiras e manchas, e deixando um aroma fresco e suave, sem necessidade de enxágue."})



def produtos_persiana(persiana=None, poeira_odor=None, sujeira_mancha=None):
    if poeira_odor!=None and sujeira_mancha==None:
        return json.dumps({"produto": "Spray Revitalizante para Persianas: Esta solução de limpeza em spray é ideal para a higienização rápida de persianas, removendo eficazmente poeira e odores, enquanto revitaliza o tecido, mantendo sua cor e textura originais."})
    elif poeira_odor==None and sujeira_mancha!=None:
        return json.dumps({"produto": "Espuma de Limpeza Profunda para Persianas: Especialmente formulada para persianas, esta espuma de limpeza penetra profundamente nas fibras, eliminando sujeiras e manchas, e deixando um aroma fresco e suave, sem necessidade de enxágue."})
    else:
        return json.dumps({"produtos": "Os produtos são: Spray Revitalizante para Persianas: Esta solução de limpeza em spray é ideal para a higienização rápida de persianas, removendo eficazmente poeira e odores, enquanto revitaliza o tecido, mantendo sua cor e textura originais.Espuma de Limpeza Profunda para Persianas: Especialmente formulada para persianas, esta espuma de limpeza penetra profundamente nas fibras, eliminando sujeiras e manchas, e deixando um aroma fresco e suave, sem necessidade de enxágue."})


def get_result(prompt):
    tools = [
        {
            "type": "function",
            "function": {
                "name": "h_cortina_explicacao",
                "description": "Dar uma explicação sobre o processo de higienização da cortina caso demonstre interesse no processo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cortina": {
                            "type": "string",
                            "description": "Cortina relacionada ao processo de higienização"
                        }
                    },
                    "required": ["cortina"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "h_cortina_orcamento",
                "description": "Dar o orçamento da higienização da cortina caso demonstre interesse no orçamento",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cortina": {
                            "type": "string",
                            "description": "Cortina relacionada ao processo de higienização"
                        }
                    },
                    "required": ["cortina"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "h_persiana_explicacao",
                "description": "Dar uma explicação sobre o processo de higienização da persiana caso demonstre interesse no processo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "persiana": {
                            "type": "string",
                            "description": "Persiana relacionada ao processo de higienização"
                        }
                    },
                    "required": ["persiana"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "h_persiana_orcamento",
                "description": "Dar o orçamento da higienização da persiana caso demonstre interesse no orçamento",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "persiana": {
                            "type": "string",
                            "description": "Persiana relacionada ao processo de higienização"
                        }
                    },
                    "required": ["persiana"]
                }
            }
        
        
        
        
        
        
        },
            {
            "type": "function",
            "function": {
                "name": "produtos_cortina",
                "description": "Fornecer uma explicação dos(s) produto(s) utilizado(s) na higienização das cortinas",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cortina": {
                            "type": "string",
                            "description": "Cortina relacionada ao processo de higienização"
                        },
                        "poeira_odor":{
                            "type": "string",
                            "description": "caso seja citado que a cortina tenha muita poeira e/ou odor"
                        },
                        "sujeira_mancha":{
                            "type": "string",
                            "description": "caso seja citado que a cortina tenha muita sujeira e/ou mancha"
                        }
                    },
                    "required": ["cortina"]
                }
            }
        },
            {
            "type": "function",
            "function": {
                "name": "produtos_persiana",
                "description": "Fornecer uma explicação dos(s) produto(s) utilizado(s) na higienização das persianas",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "persiana": {
                            "type": "string",
                            "description": "Persiana relacionada ao processo de higienização"
                        },
                        "poeira_odor":{
                            "type": "string",
                            "description": "caso seja citado que a cortina tenha muita poeira e/ou odor"
                        },
                        "sujeira_mancha":{
                            "type": "string",
                            "description": "caso seja citado que a cortina tenha muita sujeira e/ou mancha"
                        }
                    },
                    "required": ["persiana"]
                }
            }
        }
    ]


    message = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=message,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        available_functions = {
            "h_cortina_explicacao": h_cortina_explicacao,
            "h_cortina_orcamento": h_cortina_orcamento,
            "h_persiana_explicacao": h_persiana_explicacao,
            "h_persiana_orcamento": h_persiana_orcamento,
            "produtos_cortina": produtos_cortina,
            "produtos_persiana": produtos_persiana
        }
        message.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)

            function_response = None

            if "h_cortina_explicacao" in function_name or "h_cortina_orcamento" in function_name:
                function_response = function_to_call(
                    cortina = function_args.get("cortina")
                )
            elif "h_persiana_explicacao" in function_name or "h_persiana_orcamento" in function_name:
                function_response = function_to_call(
                    persiana = function_args.get("persiana")
                )
            elif "produtos_cortina" in function_name:
                function_response = function_to_call(
                    cortina = function_args.get("cortina"),
                    poeira_odor = function_args.get("poeira_odor"),
                    sujeira_mancha = function_args.get("sujeira_mancha")
                )
            elif "produtos_persiana" in function_name:
                function_response = function_to_call(
                    persiana = function_args.get("persiana"),
                    poeira_odor = function_args.get("poeira_odor"),
                    sujeira_mancha = function_args.get("sujeira_mancha")            
                )
            
            if function_response:
                message.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response
                })
        
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=message
        )    

        return second_response.choices[0].message.content     
    else:
        return response.choices[0].message.content
