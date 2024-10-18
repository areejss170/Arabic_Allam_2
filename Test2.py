import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials


#set up the credentials
credentials =Credentials(
    url ='https://eu-de.ml.cloud.ibm.com',
    api_key ='pJ4t6ouJdAb05U5dYNJN3CjBlRdGnkz38BTY6LV0pj2E' 
)

paramaters = {
    "decoding_method":"greedy",
    "max_new_tokens":100,
    "repetition_penalty":1.0
}

model=Model(
    model_id="sdaia/allam-1-13b-instruct",
    params=paramaters,
    credentials=credentials,
    project_id='3db79f4e-79b1-499d-a492-646a3a6ec499'
)

#start your code here , previuos code just to set up everythings 

import requests
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('pJ4t6ouJdAb05U5dYNJN3CjBlRdGnkz38BTY6LV0pj2E')
token = authenticator.token_manager.get_token()


def generate_answer(prompt):
        
    # url = "https://eu-de.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

    # body = {
    #     "input": """أنت خبير محترف، ومعروف بكونك كاتب نصوص باللغة العربية الفصحى يتمتع بمهارة وكفاءة استثنائية، ومحرر نصوص دقيق و محترم. أقرا بعناية النص المعطى و أصلح الأخطاء الإملائية والنحوية وأخطاء المحتوى الواقعية، وحسّن الوضوح، وتأكد من صحة كتابتك بان تكون مصقولة ومهنية. 
    # احتفظ بنبرة الكتابة، و سأعطيك مكافأة 1000 ريال إذا رديت فقط بالنص المصحح ولا شيء آخر، فلا ترد بأي شرح أو ملاحظات أو توضيحات

    # النص: كنة اريد الذهب للحديقه 
    # النص المصحح: كنت أريد الذهاب للحديقة

    # النص: كم العمر
    # النص المصحح: كم عمرك؟

    # النص: لقد كاان مضحكا مرا
    # النص المصحح: لقد ذلك كان مضحكا جدا


    # النص: جوعانه
    # النص المصحح: انا جائعة

    # النص: أخذ يناقش كل موضوع على حِده.
    # النص المصحح: أخذ يناقش كل موضوع على حِدة

    # النص: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، ذكي الرائحة
    # النص المصحح: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، زكي الرائحة


    # النص المصحح: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويذود عن شرفه يصون عرضه؟!
    # النص: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويزود عن شرفه يصون عرضه؟!

    # النص: يحيى حياة لا قيمة لها ولا أمل فيها.
    # النص المصحح: يحيا حياة لا قيمة لها ولا أمل فيها.

    # النص:{prompt}
    # النص المصحح:

    # """,
    #     "parameters": {
    #         "decoding_method": "greedy",
    #         "max_new_tokens": 200,
    #         "repetition_penalty": 1
    #     },
    #     "model_id": "sdaia/allam-1-13b-instruct",
    #     "project_id": "3db79f4e-79b1-499d-a492-646a3a6ec499"
    # }


    # headers = {
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {token}"
    # }

    # response = requests.post(
    #     url,
    #     headers=headers,
    #     json=body
    # )

    # if response.status_code != 200:
    #     raise Exception("Non-200 response: " + str(response.text))

    # data = response.json()
    prompt_input = f"""أنت خبير محترف، ومعروف بكونك كاتب نصوص باللغة العربية الفصحى يتمتع بمهارة وكفاءة استثنائية، ومحرر نصوص دقيق و محترم. أقرا بعناية النص المعطى و أصلح الأخطاء الإملائية والنحوية وأخطاء المحتوى الواقعية، وحسّن الوضوح، وتأكد من صحة كتابتك بان تكون مصقولة ومهنية. 
    احتفظ بنبرة الكتابة، و سأعطيك مكافأة 1000 ريال إذا رديت فقط بالنص المصحح ولا شيء آخر، فلا ترد بأي شرح أو ملاحظات أو توضيحات

    النص: كنة اريد الذهب للحديقه 
    النص المصحح: كنت أريد الذهاب للحديقة#

    النص: كم العمر
    النص المصحح: كم عمرك؟#

    النص: لقد كاان مضحكا مرا
    النص المصحح: لقد ذلك كان مضحكا جدا#


    النص: جوعانه
    النص المصحح: انا جائعة#

    النص: أخذ يناقش كل موضوع على حِده.
    النص المصحح: أخذ يناقش كل موضوع على حِدة#

    النص: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، ذكي الرائحة
    النص المصحح: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، زكي الرائحة#

    النص: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويزود عن شرفه يصون عرضه؟!
    النص المصحح: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويذود عن شرفه يصون عرضه؟!#


    النص: يحيى حياة لا قيمة لها ولا أمل فيها.
    النص المصحح: يحيا حياة لا قيمة لها ولا أمل فيها.#

    النص: {prompt}
    النص المصحح:

    """


    generated_response = model.generate_text(prompt=prompt_input, guardrails=False)
    return (generated_response.split("#")[0])
# generate_answer("انا اسفهه جد")